import sys
import logging

# Log lỗi ra file
logging.basicConfig(level=logging.DEBUG)

try:
    import vxx
    print("[DEBUG] vxx.py imported successfully")
except Exception as e:
    print(f"[ERROR] Failed to import vxx: {e}")
    import traceback
    traceback.print_exc()
# app.py - Phiên bản chạy vxx.py thật
import os
import sys
import uuid
import subprocess
import tempfile
import shutil
import base64
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

def safe_obfuscate(source_code, python_version):
    """Chạy vxx.py thật để obfuscate code"""
    
    session_id = str(uuid.uuid4())
    temp_dir = os.path.join('/tmp', f'obf_{session_id}')
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        # Ghi file input
        input_path = os.path.join(temp_dir, 'source.py')
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write(source_code)
        
        # Copy vxx.py vào thư mục tạm
        vxx_path = os.path.join(os.path.dirname(__file__), 'vxx.py')
        if not os.path.exists(vxx_path):
            return False, None, "vxx.py not found"
        
        temp_vxx = os.path.join(temp_dir, 'vxx.py')
        shutil.copy2(vxx_path, temp_vxx)
        
        # Tạo script tự động trả lời input cho vxx.py
        runner_script = f'''import sys
import os

os.chdir(r"{temp_dir}")

# Mock input để tự động trả lời
original_input = __builtins__.input

def mock_input(prompt):
    if "Enter Your File Name" in prompt:
        return r"{input_path}"
    elif "More Obf" in prompt or "more obf" in prompt.lower():
        return "y"
    return ""

__builtins__.input = mock_input

# Chạy vxx.py
try:
    exec(open(r"{temp_vxx}", encoding="utf-8").read())
except Exception as e:
    print(f"VXX_ERROR: {{e}}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
'''
        
        runner_path = os.path.join(temp_dir, 'runner.py')
        with open(runner_path, 'w', encoding='utf-8') as f:
            f.write(runner_script)
        
        # Chạy script
        result = subprocess.run(
            [sys.executable, runner_path],
            capture_output=True,
            text=True,
            timeout=60,  # Tăng timeout vì vxx.py chạy lâu
            cwd=temp_dir
        )
        
        print(f"[DEBUG] stdout: {result.stdout}")
        print(f"[DEBUG] stderr: {result.stderr}")
        
        # Tìm file output (vxx.py tạo ra file obf-*.py)
        obf_file = None
        for f in os.listdir(temp_dir):
            if f.startswith('obf-') and f.endswith('.py'):
                obf_file = os.path.join(temp_dir, f)
                break
        
        # Thử tìm các dạng tên khác
        if not obf_file:
            for f in os.listdir(temp_dir):
                if 'obf' in f.lower() and f.endswith('.py'):
                    obf_file = os.path.join(temp_dir, f)
                    break
        
        if obf_file and os.path.exists(obf_file):
            with open(obf_file, 'r', encoding='utf-8') as f:
                obf_code = f.read()
            return True, obf_code, None
        else:
            # Log để debug
            files_list = os.listdir(temp_dir)
            return False, None, f"No obfuscated file found. Files in temp dir: {files_list}\nOutput: {result.stdout[:500]}\nError: {result.stderr[:500]}"
            
    except subprocess.TimeoutExpired:
        return False, None, "Timeout (60s) - vxx.py took too long"
    except Exception as e:
        return False, None, str(e)
    finally:
        try:
            shutil.rmtree(temp_dir)
        except:
            pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/obfuscate', methods=['POST'])
def obfuscate():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.py'):
            return jsonify({'error': 'Only .py files are allowed'}), 400
        
        python_version = request.form.get('version', '3.11')
        
        source_code = file.read().decode('utf-8')
        
        if len(source_code) > 5 * 1024 * 1024:
            return jsonify({'error': 'File too large (max 5MB)'}), 400
        
        success, obf_code, error = safe_obfuscate(source_code, python_version)
        
        if success:
            encoded_code = base64.b64encode(obf_code.encode('utf-8')).decode('ascii')
            return jsonify({
                'success': True,
                'code': encoded_code,
                'version': python_version,
                'message': 'Obfuscated successfully with vxx.py'
            })
        else:
            return jsonify({'success': False, 'error': error}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    vxx_path = os.path.join(os.path.dirname(__file__), 'vxx.py')
    return jsonify({
        'status': 'ok',
        'python': sys.version,
        'vxx_exists': os.path.exists(vxx_path),
        'vxx_path': vxx_path
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

# app.py - Phiên bản chạy vxx.py ĐÚNG cách
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
    """Chạy vxx.py bằng subprocess với stdin pipe"""
    
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
        
        # Tạo input để pipe vào vxx.py
        # vxx.py cần 2 lần input: (1) tên file, (2) more obf (y/n)
        input_data = f"{input_path}\nn\n"
        
        # Chạy vxx.py và pipe input vào
        result = subprocess.run(
            [sys.executable, temp_vxx],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=60,
            cwd=temp_dir
        )
        
        print(f"[DEBUG] Return code: {result.returncode}")
        print(f"[DEBUG] stdout: {result.stdout[:500] if result.stdout else 'empty'}")
        print(f"[DEBUG] stderr: {result.stderr[:500] if result.stderr else 'empty'}")
        
        # Tìm file output
        obf_file = None
        for f in os.listdir(temp_dir):
            if f.startswith('obf-') and f.endswith('.py'):
                obf_file = os.path.join(temp_dir, f)
                break
        
        if not obf_file:
            for f in os.listdir(temp_dir):
                if 'obf' in f.lower() and f.endswith('.py') and f not in ['runner.py', 'vxx.py']:
                    obf_file = os.path.join(temp_dir, f)
                    break
        
        if obf_file and os.path.exists(obf_file):
            with open(obf_file, 'r', encoding='utf-8') as f:
                obf_code = f.read()
            return True, obf_code, None
        else:
            files_list = os.listdir(temp_dir)
            return False, None, f"No output file. Files: {files_list}\nStdout: {result.stdout[:300]}\nStderr: {result.stderr[:300]}"
            
    except subprocess.TimeoutExpired:
        return False, None, "Timeout (60s)"
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
                'message': 'Obfuscated successfully'
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
        'vxx_exists': os.path.exists(vxx_path)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

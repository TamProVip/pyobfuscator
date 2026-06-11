# app.py - Gọi đúng Python version
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

# Map version -> lệnh Python (đã cài trong Docker)
PYTHON_CMDS = {
    '3.9': 'python3.9',
    '3.10': 'python3.10',
    '3.11': 'python3.11',
    '3.12': 'python3.12',
}

def get_python_cmd(version):
    """Lấy lệnh Python theo version"""
    cmd = PYTHON_CMDS.get(version, 'python3.11')
    
    # Kiểm tra lệnh có tồn tại không
    result = subprocess.run(['which', cmd], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    
    # Fallback
    return 'python3'

def safe_obfuscate(source_code, python_version):
    """Chạy vxx.py với đúng Python version"""
    
    session_id = str(uuid.uuid4())
    temp_dir = os.path.join('/tmp', f'obf_{session_id}')
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        # Ghi file input
        input_path = os.path.join(temp_dir, 'source.py')
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write(source_code)
        
        # Copy vxx.py
        vxx_path = os.path.join(os.path.dirname(__file__), 'vxx.py')
        if not os.path.exists(vxx_path):
            return False, None, "vxx.py not found"
        
        temp_vxx = os.path.join(temp_dir, 'vxx.py')
        shutil.copy2(vxx_path, temp_vxx)
        
        # Lấy đúng Python executable theo version người dùng chọn
        python_cmd = get_python_cmd(python_version)
        print(f"[INFO] Using: {python_cmd} for version {python_version}")
        
        # Input cho vxx.py
        input_data = f"{input_path}\nn\n"
        
        # Chạy với đúng Python version
        result = subprocess.run(
            [python_cmd, temp_vxx],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=90,
            cwd=temp_dir
        )
        
        # Tìm file output
        obf_file = None
        for f in os.listdir(temp_dir):
            if f.startswith('obf-') and f.endswith('.py'):
                obf_file = os.path.join(temp_dir, f)
                break
        
        if obf_file and os.path.exists(obf_file):
            with open(obf_file, 'r', encoding='utf-8') as f:
                obf_code = f.read()
            return True, obf_code, None
        else:
            return False, None, f"No output. Stderr: {result.stderr[:500]}"
            
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
        
        success, obf_code, error = safe_obfuscate(source_code, python_version)
        
        if success:
            encoded_code = base64.b64encode(obf_code.encode('utf-8')).decode('ascii')
            return jsonify({
                'success': True,
                'code': encoded_code,
                'version': python_version,
                'message': f'Obfuscated with Python {python_version}'
            })
        else:
            return jsonify({'success': False, 'error': error}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    # Kiểm tra các Python versions có sẵn
    available = {}
    for ver, cmd in PYTHON_CMDS.items():
        result = subprocess.run([cmd, '--version'], capture_output=True, text=True)
        available[ver] = result.returncode == 0
    
    return jsonify({
        'status': 'ok',
        'available_versions': available,
        'vxx_exists': os.path.exists(os.path.join(os.path.dirname(__file__), 'vxx.py'))
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

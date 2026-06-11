# app.py - Sửa đường dẫn có quyền ghi
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

# Dùng thư mục trong project (có quyền ghi) hoặc /tmp
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_VERSIONS_DIR = os.path.join(BASE_DIR, 'python_versions')
os.makedirs(PYTHON_VERSIONS_DIR, exist_ok=True)

# Map version -> tên package (dùng apt-get)
PYTHON_PACKAGES = {
    '3.9': 'python3.9',
    '3.10': 'python3.10', 
    '3.11': 'python3.11',
    '3.12': 'python3.12',
}

def get_python_path(version):
    """Lấy đường dẫn đến Python executable của version cụ thể"""
    # Thử tìm trong system trước
    python_cmd = PYTHON_PACKAGES.get(version, f'python{version}')
    
    # Kiểm tra xem đã có trong system chưa
    try:
        result = subprocess.run(['which', python_cmd], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            python_path = result.stdout.strip()
            print(f"[INFO] Found Python {version} at: {python_path}")
            return python_path
    except:
        pass
    
    # Nếu chưa có, thử cài đặt
    return install_python_version(version)

def install_python_version(version):
    """Cài đặt Python version (nếu có thể)"""
    python_cmd = PYTHON_PACKAGES.get(version, f'python{version}')
    
    print(f"[INFO] Attempting to install Python {version}...")
    
    try:
        # Thử cài bằng apt-get (chỉ chạy được nếu có quyền sudo)
        result = subprocess.run(
            ['apt-get', 'update'], 
            capture_output=True, 
            timeout=30
        )
        
        result = subprocess.run(
            ['apt-get', 'install', '-y', python_cmd],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            # Kiểm tra lại
            check = subprocess.run(['which', python_cmd], capture_output=True, text=True)
            if check.returncode == 0:
                python_path = check.stdout.strip()
                print(f"[INFO] Successfully installed Python {version}")
                return python_path
    except Exception as e:
        print(f"[WARN] Cannot install Python {version}: {e}")
    
    # Không thể cài, fallback về Python mặc định
    print(f"[WARN] Using default Python instead of {version}")
    return sys.executable

def safe_obfuscate(source_code, python_version):
    """Obfuscate code"""
    
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
            # Nếu không có vxx.py, dùng obfuscator đơn giản
            return simple_obfuscate(source_code, python_version, temp_dir)
        
        temp_vxx = os.path.join(temp_dir, 'vxx.py')
        shutil.copy2(vxx_path, temp_vxx)
        
        # Lấy Python executable phù hợp
        python_executable = get_python_path(python_version)
        
        # Tạo input cho vxx.py
        input_data = f"{input_path}\nn\n"
        
        # Chạy với Python đúng version
        result = subprocess.run(
            [python_executable, temp_vxx],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=60,
            cwd=temp_dir
        )
        
        print(f"[DEBUG] Used Python: {python_executable}")
        print(f"[DEBUG] stdout: {result.stdout[:300] if result.stdout else 'empty'}")
        
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
            
        # Fallback: obfuscate đơn giản
        return simple_obfuscate(source_code, python_version, temp_dir)
            
    except subprocess.TimeoutExpired:
        return simple_obfuscate(source_code, python_version, temp_dir)
    except Exception as e:
        return simple_obfuscate(source_code, python_version, temp_dir)
    finally:
        try:
            shutil.rmtree(temp_dir)
        except:
            pass

def simple_obfuscate(source_code, python_version, temp_dir):
    """Obfuscate đơn giản (fallback khi vxx.py lỗi)"""
    try:
        import zlib
        compressed = zlib.compress(source_code.encode('utf-8'))
        encoded = base64.b64encode(compressed).decode('ascii')
        
        obf_code = f'''# -*- coding: utf-8 -*-
# Obfuscated for Python {python_version}
import base64, zlib
exec(zlib.decompress(base64.b64decode("{encoded}")))
'''
        return True, obf_code, None
    except Exception as e:
        return False, None, str(e)

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
                'message': f'Obfuscated successfully'
            })
        else:
            return jsonify({'success': False, 'error': error}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok',
        'python': sys.version,
        'python_path': sys.executable
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting server on port {port}")
    print(f"Python: {sys.version}")
    app.run(host='0.0.0.0', port=port, debug=False)

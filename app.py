# app.py - Tự động cài và chạy đúng Python version
import os
import sys
import uuid
import subprocess
import tempfile
import shutil
import base64
import urllib.request
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# Đường dẫn lưu các phiên bản Python
PYTHON_VERSIONS_DIR = '/opt/python_versions'
os.makedirs(PYTHON_VERSIONS_DIR, exist_ok=True)

# Map version -> URL tải xuống (deadsnakes PPA cho Ubuntu)
PYTHON_URLS = {
    '3.9': 'https://www.python.org/ftp/python/3.9.18/Python-3.9.18.tgz',
    '3.10': 'https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tgz',
    '3.11': 'https://www.python.org/ftp/python/3.11.6/Python-3.11.6.tgz',
    '3.12': 'https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz',
}

def get_python_path(version):
    """Lấy đường dẫn đến Python executable của version cụ thể"""
    python_path = os.path.join(PYTHON_VERSIONS_DIR, f'python{version}', 'bin', 'python3')
    
    # Nếu đã có rồi thì trả về
    if os.path.exists(python_path):
        return python_path
    
    # Nếu chưa có, cài đặt
    return install_python_version(version)

def install_python_version(version):
    """Cài đặt Python version cụ thể từ source"""
    print(f"[INSTALL] Installing Python {version}...")
    
    version_dir = os.path.join(PYTHON_VERSIONS_DIR, f'python{version}')
    os.makedirs(version_dir, exist_ok=True)
    
    python_path = os.path.join(version_dir, 'bin', 'python3')
    
    # Kiểm tra lại sau khi tạo thư mục
    if os.path.exists(python_path):
        return python_path
    
    # Thử dùng apt-get trước (nhanh hơn)
    apt_python = f'python{version}'
    try:
        subprocess.run(['apt-get', 'update'], capture_output=True, timeout=30)
        result = subprocess.run(['apt-get', 'install', '-y', apt_python], 
                               capture_output=True, text=True, timeout=120)
        if result.returncode == 0:
            # Kiểm tra xem đã cài xong chưa
            check = subprocess.run(['which', apt_python], capture_output=True, text=True)
            if check.returncode == 0:
                python_path = check.stdout.strip()
                print(f"[INSTALL] Installed Python {version} via apt: {python_path}")
                return python_path
    except:
        pass
    
    # Nếu apt không được, compile từ source
    print(f"[INSTALL] Compiling Python {version} from source...")
    
    # Tải source
    url = PYTHON_URLS.get(version)
    if not url:
        return None
    
    tgz_file = os.path.join(PYTHON_VERSIONS_DIR, f'Python-{version}.tgz')
    extract_dir = os.path.join(PYTHON_VERSIONS_DIR, f'Python-{version}')
    
    try:
        # Tải file
        urllib.request.urlretrieve(url, tgz_file)
        
        # Giải nén
        subprocess.run(['tar', '-xzf', tgz_file, '-C', PYTHON_VERSIONS_DIR], 
                      capture_output=True, timeout=60)
        
        # Compile
        subprocess.run(['./configure', f'--prefix={version_dir}'], 
                      cwd=extract_dir, capture_output=True, timeout=30)
        subprocess.run(['make', '-j4'], cwd=extract_dir, capture_output=True, timeout=300)
        subprocess.run(['make', 'install'], cwd=extract_dir, capture_output=True, timeout=60)
        
        # Dọn dẹp
        os.remove(tgz_file)
        shutil.rmtree(extract_dir)
        
        print(f"[INSTALL] Successfully installed Python {version}")
        return python_path
        
    except Exception as e:
        print(f"[ERROR] Failed to install Python {version}: {e}")
        return None

def run_with_python_version(version, script_path, cwd, input_data=""):
    """Chạy script với Python version cụ thể"""
    python_path = get_python_path(version)
    
    if not python_path or not os.path.exists(python_path):
        # Fallback về Python mặc định
        python_path = sys.executable
        print(f"[WARN] Python {version} not available, using default: {sys.version}")
    
    result = subprocess.run(
        [python_path, script_path],
        input=input_data,
        capture_output=True,
        text=True,
        timeout=60,
        cwd=cwd
    )
    
    return result

def safe_obfuscate(source_code, python_version):
    """Obfuscate với đúng Python version người dùng chọn"""
    
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
        
        # Chuẩn bị input cho vxx.py
        input_data = f"{input_path}\nn\n"
        
        # Chạy với Python đúng version
        result = run_with_python_version(python_version, temp_vxx, temp_dir, input_data)
        
        print(f"[DEBUG] Python version used: {python_version}")
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
                if 'obf' in f.lower() and f.endswith('.py') and f != 'vxx.py':
                    obf_file = os.path.join(temp_dir, f)
                    break
        
        if obf_file and os.path.exists(obf_file):
            with open(obf_file, 'r', encoding='utf-8') as f:
                obf_code = f.read()
            return True, obf_code, None
        else:
            files_list = os.listdir(temp_dir)
            return False, None, f"No output. Files: {files_list}\nStdout: {result.stdout[:300]}\nStderr: {result.stderr[:300]}"
            
    except subprocess.TimeoutExpired:
        return False, None, f"Timeout (60s) for Python {python_version}"
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
                'message': f'Obfuscated successfully with Python {python_version}'
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
        'available_versions': list(PYTHON_URLS.keys())
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting server on port {port}")
    print(f"Default Python: {sys.version}")
    app.run(host='0.0.0.0', port=port, debug=False)

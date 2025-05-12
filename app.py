from flask import Flask, request, jsonify, render_template
import os
import pytesseract
from PIL import Image

app = Flask(__name__)

# 配置上传文件夹和允许的文件扩展名
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 确保上传文件夹存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        try:
            # 为了安全，使用安全的文件名
            # filename = secure_filename(file.filename) # secure_filename 需要 werkzeug 库
            # 简单起见，我们直接使用原始文件名，但在生产环境中应使用 secure_filename
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # 使用Pillow打开图像，然后用pytesseract进行OCR
            img = Image.open(filepath)
            text = pytesseract.image_to_string(img, lang='chi_sim+eng') # 假设需要识别中文简体和英文
            
            # 处理后可以删除临时文件
            # os.remove(filepath)

            return jsonify({'text': text})
        except Exception as e:
            # 在生产环境中，这里应该记录更详细的错误日志
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    # 在生产环境中，不要使用 Flask 自带的开发服务器
    # 可以考虑使用 Gunicorn 或 uWSGI
    app.run(debug=True) 
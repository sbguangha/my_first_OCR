# 图片文字识别 (OCR) Web 应用

这是一个简单的 Web 应用，允许用户上传图片，并通过 OCR 技术识别图片中的文字内容。

## 功能

- 用户通过网页上传图片 (支持 png, jpg, jpeg, gif格式)。
- 后端使用 Flask 处理图片上传。
- 使用 Tesseract OCR (通过 `pytesseract` 库) 识别图片中的文字。
- 前端实时显示识别结果。

## 技术栈

- **后端**: Python, Flask
- **OCR引擎**: Tesseract OCR
- **Python OCR库**: pytesseract
- **图像处理**: Pillow (PIL Fork)
- **前端**: HTML, CSS, JavaScript (Fetch API)

## 安装与运行

### 1. 先决条件

- **Python 3.x**: 请确保您的系统中安装了 Python 3。
- **Tesseract OCR引擎**: 这是本应用的核心依赖。您需要根据您的操作系统安装 Tesseract。
    - **Windows**:可以从 [UB Mannheim Tesseract releases](https://github.com/UB-Mannheim/tesseract/wiki) 下载安装程序。
        - **重要**: 安装时，请确保勾选 "Additional language data" (或类似选项) 并选择安装中文简体 (`chi_sim`) 和英文 (`eng`) 语言包。如果已安装，请确保这些语言包存在。
        - **重要**: 将 Tesseract 的安装路径添加到系统的 PATH 环境变量中。例如，如果安装在 `C:\Program Files\Tesseract-OCR`，则需要将此路径加入 PATH。或者，您需要在 `app.py` 中配置 `pytesseract.pytesseract.tesseract_cmd` 指向 `tesseract.exe` 的完整路径。
    - **macOS**: 可以使用 Homebrew: `brew install tesseract tesseract-lang` (这将安装所有语言包，包括中文简体)。
    - **Linux (Ubuntu/Debian)**: `sudo apt update && sudo apt install tesseract-ocr tesseract-ocr-chi-sim tesseract-ocr-eng`
    - **其他Linux发行版**: 请参考对应发行版的包管理器安装说明。

### 2. 克隆或下载项目 (如果您是通过版本控制获取)

```bash
git clone <repository_url>
cd <project_directory>
```

如果直接下载了文件，请解压并进入项目目录。

### 3. 创建并激活虚拟环境 (推荐)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS & Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

### 5. (可选) 配置 Tesseract 路径

如果在步骤1中没有将 Tesseract 添加到系统 PATH，或者 `pytesseract` 仍然找不到它，您可能需要在 `app.py` 文件的开头（在 `import pytesseract` 之后）明确指定 Tesseract 的可执行文件路径。例如：

```python
# 示例: Windows 下，如果 Tesseract 安装在 C:\Program Files\Tesseract-OCR
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 示例: Linux/macOS 下，如果 Tesseract 不在标准路径
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract' # 具体路径可能不同
```

### 6. 运行 Flask 应用

```bash
python app.py
```

应用默认会在 `http://127.0.0.1:5000/` 上运行。

### 7. 打开浏览器

在浏览器中访问 [http://127.0.0.1:5000/](http://127.0.0.1:5000/) 即可使用该应用。

## 项目结构

```
.
├── app.py                # Flask 后端应用
├── requirements.txt      # Python 依赖列表
├── templates/
│   └── index.html        # 前端 HTML 页面
├── uploads/              # (自动创建) 用于临时存储上传的图片
└── README.md             # 本文件
```

## 注意事项

- `uploads/` 文件夹用于临时存放图片，`app.py` 中当前版本的代码在处理完图片后并未删除它们。在生产环境中，您可能需要考虑图片的生命周期管理，例如处理后删除或定期清理。
- 错误处理相对简单，生产环境需要更健壮的日志和错误反馈机制。
- Flask 的开发服务器不适合生产环境，部署时请考虑使用 Gunicorn, uWSGI 等 WSGI 服务器，并结合 Nginx 等反向代理。
- Tesseract OCR 的识别准确率受图片质量、字体、语言、版面复杂程度等多种因素影响。 
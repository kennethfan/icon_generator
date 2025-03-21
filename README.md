# 文字图片生成工具

这个 Python 脚本可以根据你提供的文字、图片尺寸和输出路径，生成包含指定文字的图片。

## 安装环境

### 前提条件
确保你已经安装了 Python 3.x 版本。你可以通过以下命令检查 Python 版本：
```bash
python3 --version
```

### 安装依赖库
本脚本依赖于 `Pillow` 库，你可以使用 `pip` 进行安装：
```bash
pip3 install pillow
```

## 使用方法

### 运行脚本
脚本通过命令行参数接收文字、图片宽度、图片高度和输出路径。使用以下命令运行脚本：
```bash
# 修改处：将 generate_text_image 替换为 icon_generate
python3 /Users/kenneth/codes/python/icon_generator/icon_generate.py <文字内容> <图片宽度> <图片高度> <输出路径>
```

### 参数说明
- `<文字内容>`：要显示在图片中的文字，用字符串表示。
- `<图片宽度>`：生成图片的宽度，用整数表示。
- `<图片高度>`：生成图片的高度，用整数表示。
- `<输出路径>`：生成图片的保存路径，包括文件名和文件扩展名（如 `.png`）。

### 示例
假设你想生成一张宽度为 200 像素、高度为 100 像素，包含文字 “Hello, World!” 的图片，并将其保存为 `text_image.png`，可以使用以下命令：
```bash
python3 /Users/kenneth/codes/python/icon_generator/icon_generate.py "Hello, World!" 200 100 text_image.png
```

运行上述命令后，会在当前目录下生成一个名为 `text_image.png` 的图片，图片内容为 `Hello, World!`。

以上就是使用 `icon_generate.py` 脚本的详细步骤。如果你在使用过程中遇到任何问题，请随时联系我们。
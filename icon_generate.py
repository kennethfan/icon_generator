from PIL import Image, ImageDraw, ImageFont
import argparse

def generate_text_image(text, width, height, output_path):
    """
    Generate an image containing the specified text.

    :param text: The text to display in the image.
    :param width: The width of the image.
    :param height: The height of the image.
    :param output_path: The path to save the generated image.
    """
    # Create a new white image
    image = Image.new('RGB', (width, height), color='white')
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    # Select a font and font size
    font = ImageFont.load_default()
    # Calculate the bounding box of the text
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_width = right - left
    text_height = bottom - top
    # Calculate the position of the text to center it
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    # Draw the text on the image
    draw.text((x, y), text, fill='black', font=font)
    # Save the image
    image.save(output_path)

if __name__ == "__main__":
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='Generate an image with text.')
    # 添加命令行参数
    parser.add_argument('text', type=str, help='The text to display in the image.')
    parser.add_argument('width', type=int, help='The width of the image.')
    parser.add_argument('height', type=int, help='The height of the image.')
    parser.add_argument('output_path', type=str, help='The path to save the generated image.')
    # 解析命令行参数
    args = parser.parse_args()

    # 调用生成图片的函数
    generate_text_image(args.text, args.width, args.height, args.output_path)
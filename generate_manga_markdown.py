import os
import sys

def main(argv):
    image_folder = argv[1]

    folder_name = os.path.basename(image_folder)
    print(folder_name)

    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png'))]

    image_files.sort(key=lambda x: int(os.path.splitext(x)[0]))

    # 生成的 Markdown 文件路径
    markdown_file = os.path.join(os.path.dirname(image_folder), f"{folder_name}.md")

    # 生成 Markdown 内容
    markdown_content = f"# {folder_name}\n\n"  # 添加标题行
    for image_file in image_files:
        image_path = os.path.relpath(os.path.join(image_folder, image_file), os.path.dirname(markdown_file))
        image_path = os.path.normpath(image_path)  # 规范化路径
        image_path = image_path.replace("\\", "/")  # 将反斜杠替换为斜杠
        markdown_content += f"![image](./{image_path})\n"  # 使用斜杠表示相对路径

    # 写入 Markdown 文件
    with open(markdown_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Markdown file '{folder_name}' generated successfully.")

if __name__ == "__main__":
    main(sys.argv)
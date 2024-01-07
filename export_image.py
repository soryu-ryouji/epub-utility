import os
import shutil
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def process_html_file(file_path, output_folder):
    print(f"current file path: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    img_tags = soup.find_all('img')

    for index, img_tag in enumerate(img_tags, start=1):
        img_src = img_tag.get('src')
        img_name = os.path.basename(img_src)
        img_extension = os.path.splitext(img_name)[1]

        new_img_name = f"{str(index).zfill(5)}{img_extension}"

        img_src_abs = urljoin(file_path, img_src)
        print(f"img src: {img_src}\nabs img src: {img_src_abs}")

        new_img_path = os.path.join(output_folder, new_img_name)
        shutil.copy(img_src_abs, new_img_path)

def export_html_image(html_path, output_path):
    os.makedirs(output_path, exist_ok=True)

    html_files = [f for f in os.listdir(html_path) if f.endswith('.html')]

    for html_file in sorted(html_files):
        file_path = os.path.join(html_path, html_file)
        process_html_file(file_path, output_path)

if __name__ == "__main__":
    argv = sys.argv
    html_path = argv[1]
    output_path = argv[2]
    print(f"{html_path}\n{output_path}")
    export_html_image(html_path, output_path)

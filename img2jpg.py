from PIL import Image
import os

def convert_to_jpg(input_folder, output_folder):
    Image.MAX_IMAGE_PIXELS = None

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.png')):
            img = Image.open(os.path.join(input_folder, filename))
            new_filename = os.path.splitext(filename)[0] + '.jpg'
            img = img.convert("RGB")  # 将图像转换为RGB模式
            img.save(os.path.join(output_folder, new_filename), 'JPEG')

    print("Conversion complete.")

if __name__ == "__main__":
    input_path = input("input_folder_path : ")
    output_path = os.path.join( os.path.dirname(input_path), "output_jpg")
    
    convert_to_jpg(input_path, output_path)

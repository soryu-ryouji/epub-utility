import os

def generate_numbered_filenames(file_list):
    max_digits = len(str(len(file_list)))  # 最大的数字位数

    for i in range(1, len(file_list) + 1):
        padded_number = str(i).zfill(max_digits)  # 使用 zfill 补零
        new_filename = f"{padded_number}{os.path.splitext(file_list[i - 1])[1]}"
        yield new_filename

def main():
    folder_path = input("Input folder path: ")

    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    file_list.sort()

    new_filenames = list(generate_numbered_filenames(file_list))

    for old_filename, new_filename in zip(file_list, new_filenames):
        old_path = os.path.join(folder_path, old_filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)

    print("Files renamed successfully.")

if __name__ == "__main__":
    main()

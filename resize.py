from PIL import Image
import os

def main():
    path = "/home/xdt/disk/find_by_video/data/"
    new_path = "/home/xdt/disk/gitee/picture_paste/new/"
    files = os.listdir(path)

    error_list = []

    for file in files:
        try:
            image = Image.open(path + file)
            new_image = image.resize((500, 500))
            new_image.save(new_path + file)
            print("resize {} ---> {}".format(path + file, new_path + file))
        except Exception as e:
            error_list.append(path + file)
            pass
    
    print(error_list)

if __name__ == "__main__":
    main()
import os
from PIL import Image


def jpg_to_png(input_img_path, output_img_path):
    with Image.open(input_img_path) as img:
        img.save(output_img_path + ".png", "png")
        return 0


def op_file_path_wname(input_img_path):
    file_name = (input_img_path.split(sep='\\')[-1]).split(sep='.')[0]
    return file_name


if __name__ == "__main__":

    print("**********WELCOME TO JPG-PNG CONVERTER**********\n")
    input_img_path = str(input("Enter JPG File Path : "))

    if os.path.exists(input_img_path) == True:
        file_name = op_file_path_wname(input_img_path)
        output_img_path = str(input("Enter Desired PNG File Path : "))

        if os.path.exists(output_img_path) == True:
            flag = jpg_to_png(input_img_path, f"{output_img_path}\{file_name}")
            if flag == 0:
                print("SUCESS!!!")
            else:
                print("Somethin went wrong!!! Try Again Later")
        else:
            print("Path not exists")
            print("please try again with correct path")
    else:
        print("Path not exists")
        print("please try again with correct path")

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

List = []


def print_now():
    import os
    for root, dirs, files in os.walk(".", topdown=False):
        for each in files:
            print(os.path.join(root, each))
        for each in dirs:
            print(os.path.join(root, each))


def is_belong(str, fstr):
    f = 0
    # print(str, fstr)
    for s in str:
        for each in fstr:
            if s == each:
                f += 1
    # print(f, len(str))
    return f == len(str)


def file_display(filepath, name):
    for each in os.listdir(filepath):  # 得出文件的绝对路径
        absolute_path = os.path.join(filepath, each)
        is_file = os.path.isfile(absolute_path)  # 判断文件或目录得出布尔值
        if is_file:
            # print(each)
            if is_belong(name, each):
                print(absolute_path)
            # print(absolute_path)

        else:
            file_display(absolute_path, name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    t = int(input("请输入查找文件数量:\n"))
    while t:
        name = str(input("请输入查找的文件名:\n"))
        print("将为您查找存在文件名称的文件")
        file_display('C:\Program Files (x86)\MySQL', name)
        t -= 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

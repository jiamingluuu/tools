import os

import pdfplumber
import pyperclip
from PyQt5.QtWidgets import *


def get_clipboard():
    s = pyperclip.paste()
    pyperclip.copy(s)
    print("clip_board found:    " + s)
    return s


def search():
    os.system("cls")
    flag = False  # found?1:0
    data = clipboard.mimeData()
    if data.formats() == ["text/plain"] or data.formats() == [
        "text/html",
        "text/plain",
    ]:
        s = data.text().strip()
        print('Searching    "' + data.text() + '"    in file: ' + "RES.pdf\n")
        for page in pdf.pages:
            if s in page.extract_text():
                print(str(page) + ": \n")
                content = page.extract_text()
                print(content[: content.index(s)], end="")
                print("\033[1;37;41m" + s + "\033[0;37;40m", end="")
                print(content[content.index(s) + len(s) :], end="")
                print("\n___________________\n")
                flag = True
    if flag:
        print(">>SERACH FINISHED.\n\n\n")

    else:
        print('Searching    "' + data.text() + '"    in file: ' + "RES.pdf\n")
        print(">>NO CONTENT FOUND!\n\n\n")


def print_all(pdf):
    print("PDF.LEN = " + str(len(pdf.pages)) + "\n")
    for page in pdf.pages:
        print("\nPAGE = " + str(page) + ": ")
        print(page.extract_text())
        os.system("pause")


# initialize
app = QApplication([])
clipboard = app.clipboard()


# 当剪切板变动会执行该方法
def change_deal():
    data = clipboard.mimeData()

    # 获取剪切板内容格式
    # print(data.formats())
    # 如果是文本格式，把内容打印出来
    if data.formats() == ["text/plain"] or data.formats() == [
        "text/html",
        "text/plain",
    ]:
        print(data.text())


if __name__ == "__main__":
    file_path = "C:\RES.pdf"

    with pdfplumber.open(file_path) as pdf:
        page = pdf.pages[0]
        print("page[0]:\n\n")
        print(page.extract_text())
        print("\n\n")

        # 监听剪切板变动
        clipboard.dataChanged.connect(search)
        app.exec_()
        # print_all(pdf)

    # pdf.close()

# Pyinstaller -F setup.py 打包exe

# Pyinstaller -F -w setup.py 不带控制台的打包

# Pyinstaller -F -i xx.ico setup.py 打包指定exe图标打包

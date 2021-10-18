from tkinter import *

class Editor(Tk):
    def __init__(self):
        super().__init__()
        self.setWindow()
        self.createMenu()
        self.createBody()

    # 设置初始窗口的属性
    def setWindow(self):
        self.title("Editor")
        self.geometry('650x450')

    # 创建整个菜单栏
    def createMenu(self):
        menu_bar = Menu(self)
        # 创建文件的联级菜单
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='新建', accelerator='Ctrl+N')
        file_menu.add_command(label='打开', accelerator='Ctrl+O')
        file_menu.add_command(label='保存', accelerator='Ctrl+S')
        file_menu.add_command(label='另存为', accelerator='Shift+Ctrl+S')
        file_menu.add_separator()
        file_menu.add_command(label='退出', accelerator='Alt+F4')

        # 在菜单栏上添加菜单标签，并将该标签与相应的联级菜单关联起来
        menu_bar.add_cascade(label='文件', menu=file_menu)

        # 创建编辑的联级菜单
        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label='撤销', accelerator='Ctrl+Z')
        edit_menu.add_command(label='恢复', accelerator='Ctrl+Y')
        edit_menu.add_separator()
        edit_menu.add_command(label='剪切', accelerator='Ctrl+X')
        edit_menu.add_command(label='复制', accelerator='Ctrl+C')
        edit_menu.add_command(label='粘贴', accelerator='Ctrl+V')
        edit_menu.add_separator()
        edit_menu.add_command(label='查找', accelerator='Ctrl+F')
        edit_menu.add_separator()
        edit_menu.add_command(label='全选', accelerator='Ctrl+A')
        menu_bar.add_cascade(label='编辑', menu=edit_menu)

        self["menu"] = menu_bar

    # 创建程序主体
    def createBody(self):
        # 创建文本输入框
        content_text = Text(self, wrap='word')
        content_text.pack(expand='yes', fill='both')

if "__main__" == __name__:
    app = Editor()
    app.mainloop()

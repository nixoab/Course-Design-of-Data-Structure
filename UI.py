from tkinter import *    # 导入tkinter包
from tkinter.filedialog import *
from tkinter.ttk import *


def ret_filename():
    # 打开文件会话框，其返回值为一个元组形式的文件名
    file = askopenfilenames(title = "选择文件")
    # 遍历元组，将其添加到树形菜单中
    for i, ch in enumerate(file):
        tree.insert("", index = END, text = i, values = (ch))


window = Tk()                                   # 实例化object，建立窗口window
window.title("面向英文数据的编辑与信息检索系统")  # 给窗口的可视化起名字
window.geometry("1000x800")                      # 设定窗口的大小(长 * 宽)

Button(window, text = "选择", command = ret_filename).pack(pady = 5)  # 添加按钮
tree = Treeview(window, columns = ("path"))                           # 添加树形菜单
tree.heading("#0", text = "序号")
tree.heading("path", text = "路径")
tree.pack()

window.mainloop() # 进入消息循环
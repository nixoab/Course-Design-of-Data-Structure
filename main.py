from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter.ttk import *

class main(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        Frame.pack(self)
        self.grid()
        self.files = {}
        self.setupButton()
    
    def setupButton(self):
        bt1 = Button(self, text = "选择", command = self.ret_filename)
        bt1.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.setupTree()

    def setupTree(self):
        self.tree = Treeview(self, columns = ("#1"))
        self.tree.heading("#0", text = "序号")
        self.tree.column("#0", minwidth = 0, width = 50, stretch = NO)
        self.tree.heading("#1", text = "路径")
        self.tree.column("#1", minwidth = 0, width = 600, stretch = NO)
        self.tree.grid(row = 1, column = 0, padx = 5, pady = 5)
    
    def ret_filename(self):
        # 打开文件会话框，其返回值为一个元组形式的文件名
        self.files = askopenfilenames(title = "选择文件")
        # 遍历元组，将其添加到树形菜单中
        for i, ch in enumerate(self.files):
            self.tree.insert("", index = END, text = i + 1, values = (ch))
    
if __name__ == '__main__':
    root = Tk()
    root.geometry("600x700") 
    root.wm_title("面向英文数据的编辑与信息检索系统")
    main(root)
    root.mainloop()
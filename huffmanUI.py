import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter.filedialog import *
from huffmanTree import *

class MyApp(tk.Frame):
    
    def __init__(self):
        super().__init__()
        self.pack()
        self.content = ""
        self.setupButton()
    
    def setupButton(self):
        bt1 = tk.Button(self, text = '打开', command = self.get_file).pack()
        bt2 = tk.Button(self, text = '编码', command = self.get_huffmanCode).pack()
        bt3 = tk.Button(self, text = '译码', command = self.get_originCode).pack()
        self.text = tk.Text(self)
        self.text.pack()

    def get_file(self):
        # 打开文件
        file_path = askopenfilename(title="选择文件")  # 获取文件地址
        with open(file_path) as fr:
            # 打开文件
            self.content = fr.read()  #读取文件内容
            self.text.delete(0.0, tk.END)  # 清空文本框内容
            self.text.insert(tk.END, self.content)  # 在光标后插入内容
            self.tree = HuffmanTree(self.content)
    
    def get_huffmanCode(self):
        self.text.delete(0.0, tk.END)  # 清空文本框内容
        self.text.insert(tk.END, self.tree.huffmanStr)  # 在光标后插入内容

        self.top = Toplevel()
        self.top.title("编码表")
        columns = ("字母", "出现次数", "哈夫曼编码")
        treeview = ttk.Treeview(self.top, height = 18, show = "headings", columns = columns)  # 表格
        treeview.column("字母", width = 300, anchor = 'center') # 表示列,不显示
        treeview.column("出现次数", width = 300, anchor = 'center')
        treeview.column("哈夫曼编码", width = 300, anchor = 'center')
        treeview.heading("字母", text = "字母") # 显示表头
        treeview.heading("出现次数", text = "出现次数")
        treeview.heading("哈夫曼编码", text = "哈夫曼编码")
        treeview.pack()
        i = 0
        for item in self.tree.codes: # 写入数据
            treeview.insert('', i, values = (item[0], item[1], item[2]))
            i += 1

    def get_originCode(self):
        self.text.delete(0.0, tk.END)  # 清空文本框内容
        self.text.insert(tk.END, self.tree.originStr)  # 在光标后插入内容


if __name__ == '__main__': 
    MyApp().mainloop()
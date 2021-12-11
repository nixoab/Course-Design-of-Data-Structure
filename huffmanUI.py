import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter.filedialog import *
from huffmanTree import *

class MyApp(tk.Frame):
    def __init__(self, parent = None):
        tk.Frame.__init__(self, parent)
        tk.Frame.pack(self)
        self.grid()
        self.content = ""
        self.setupButton()
    
    def setupButton(self):
        bt1 = tk.Button(self, text = '打开', command = self.get_file)
        bt1.grid(row = 0, column = 0, padx = 5, pady = 5)
        bt2 = tk.Button(self, text = '编码', command = self.get_huffmanCode)
        bt2.grid(row = 0, column = 1, padx = 5, pady = 5)
        bt3 = tk.Button(self, text = '译码', command = self.get_originCode)
        bt3.grid(row = 0, column = 2, padx = 5, pady = 5)
        self.serEntry = tk.Entry(self)
        self.serEntry.grid(row = 2, column = 0, padx = 5, pady = 5)
        serBtn = tk.Button(self, text = "查找", command = self.search)
        serBtn.grid(row = 2, column = 1, padx = 5, pady = 5)
        self.repEntry = tk.Entry(self)
        self.repEntry.grid(row = 2, column = 2, padx = 5, pady = 5)
        repBtn = tk.Button(self, text = "替换全部", command = self.replace)
        repBtn.grid(row = 2, column = 3, padx = 5, pady = 5)
        self.text = tk.Text(self)
        self.text.grid(row = 4, column = 0, columnspan = 4, padx = 5, pady = 5)
        self.text.tag_configure("found", background = "yellow")

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
        treeview.grid()
        i = 0
        for item in self.tree.codes: # 写入数据
            treeview.insert('', i, values = (item[0], item[1], item[2]))
            i += 1

    def get_originCode(self):
        self.text.delete(0.0, tk.END)  # 清空文本框内容
        self.text.insert(tk.END, self.tree.originStr)  # 在光标后插入内容

    def search(self):
        self.text.tag_remove("found", "1.0", tk.END)
        start = "1.0"
        key = self.serEntry.get()
        if(len(key.strip()) == 0):
            return
        while True:
            pos = self.text.search(key, start, tk.END)
            if(pos == ""):
                break
            self.text.tag_add("found", pos, "%s + %dc" % (pos, len(key)))
            start = "%s + %dc" % (pos, len(key))

    def replace(self):
        serKey = self.serEntry.get()
        repKey = self.repEntry.get()
        self.text.delete(0.0, tk.END)
        self.text.insert(tk.END, self.content.replace(serKey, repKey))
        
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("600x400") 
    root.wm_title("文件")
    MyApp(root)
    root.mainloop()
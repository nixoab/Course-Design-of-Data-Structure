#节点类
class Node(object):
    def __init__(self,name = None, value = None):
        self.name  = name
        self.value = value
        self.left  = None
        self.right = None

#哈夫曼树类
class HuffmanTree(object):
    #初始化
    def __init__(self, text):
        self.text = text
        self.chars_freqs = [] #字频
        self.count_freq()
        self.Leav = [Node(part[0], part[1]) for part in self.chars_freqs]  #根据输入的字符及其频数生成节点
        self.creatTree()
        self.root = self.Leav[0]   #根节点
        self.curCode = [2] * 10000 #用于递归编码
        self.codes = []            #编码表
        self.huffmanStr = ""       #编码
        self.originStr = ""        #解码
        self.pre(self.root, 0)
        self.encodeStr()
        self.decodeStr()
    #字频统计
    def count_freq(self):
        dictionary = {c : self.text.count(c) for c in self.text}
        for key, value in dictionary.items():
            char_freq = (key, value)
            self.chars_freqs.append(char_freq)
        return self.chars_freqs
    #建树
    def creatTree(self):
        while len(self.Leav) != 1:
            self.Leav.sort(key = lambda node : node.value, reverse = True) #降序
            newNode = Node(value = (self.Leav[-1].value + self.Leav[-2].value))
            newNode.left = self.Leav.pop(-1)
            newNode.right = self.Leav.pop(-1)
            self.Leav.append(newNode)
    #生成编码表
    def pre(self, tree, length):
        node = tree
        s = ""
        if (not node):
            return
        elif node.name:
            for i in range(length):
                s += self.curCode[i]
            for item in self.chars_freqs:
                if node.name == item[0]:
                    code = (node.name, item[1], s)
                    self.codes.append(code)
            return
        self.curCode[length] = '0'
        self.pre(node.left, length + 1)
        self.curCode[length] = '1'
        self.pre(node.right, length + 1)
    #生成哈夫曼编码
    def encodeStr(self):
        for char in self.text:
            for item in self.codes:
                if char == item[0]:
                    self.huffmanStr += item[2]
                    break
        return self.huffmanStr
    #哈夫曼解码
    def decodeStr(self):
        self.originStr = ''
        temp = self.huffmanStr
        while temp != '':
            for item in self.codes:
                if item[2] in temp:
                    if temp.index(item[2]) == 0:
                        self.originStr += item[0]
                        temp = temp[len(item[2]):]
                        break
        return self.originStr
    def get_code(self):
        print(self.chars_freqs)
        print(self.codes)
        print(self.huffmanStr)
        print(self.originStr)

if __name__=='__main__':
    text = "     wwwwlllleeiiru"
    tree = HuffmanTree(text)
    tree.get_code()
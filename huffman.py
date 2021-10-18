def count_freq(text):
    dictionary = {x:text.count(x) for x in text}
    chars_freqs = []
    for key, value in dictionary.items():
        char_freq = (key, value)
        chars_freqs.append(char_freq)
    return chars_freqs

import heapq

class Node:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
    def isLeft(self):
        return self.father.left == self
    def __lt__(self,other):
        return self.freq < other.freq

# 创建叶子节点
def createNodes(freqs):
    return [Node(freq) for freq in freqs]

# 创建Huffman树
def createHuffmanTree(nodes):
    heap = []
    for item in nodes:
        heapq.heappush(heap, item)
    while len(heap) > 1:
        node_left = heapq.heappop(heap)
        node_right = heapq.heappop(heap)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        heap.append(node_father)
    heap[0].father = None
    return heap[0]


# Huffman编码
def huffmanEncoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes


# 编码整个字符串
def encodeStr(text, chars_freqs, codes):
    huffmanStr = ''
    for char in text:
        i = 0
        for item in chars_freqs:
            if char == item[0]:
                huffmanStr += codes[i]
                break
            i += 1
    return huffmanStr


# 解码整个字符串
def decodeStr(huffmanStr, chars_freqs, codes):
    orignStr = ''
    while huffmanStr != '':
        i = 0
        for item in codes:
            if item in huffmanStr:
                if huffmanStr.index(item) == 0:
                    orignStr += chars_freqs[i][0]
                    huffmanStr = huffmanStr[len(item):]
                    break
            i += 1
    return orignStr


if __name__ == '__main__':
    text = "asdf asdfg"
    chars_freqs = count_freq(text)
    nodes = createNodes([item[1] for item in chars_freqs])
    root = createHuffmanTree(nodes)
    codes = huffmanEncoding(nodes, root)
    huffmanStr = encodeStr(text, chars_freqs, codes)
    orignStr = decodeStr(huffmanStr, chars_freqs, codes)
    print(huffmanStr)
    print(orignStr)


#    https://www.92python.com/view/354.html
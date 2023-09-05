import heapq
from heapq import heappop, heappush
 
 
def isLeaf(root):
    return root.left is None and root.right is None
 
 
# ���� ������
class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right
 
    # �������������� ������� `__lt__()`, ����� ��������� ����� `Node` �������� � ������������ ��������.
    # ����� �������, ��� ������� � ��������� ����������� ����� ���������� �������
    def __lt__(self, other):
        return self.freq < other.freq
 
 
# ������ �� ������ �������� � ��������� ���� �������� � �������
def encode(root, s, huffman_code):
 
    if root is None:
        return
 
    # ��������� �������� ����
    if isLeaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'
 
    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '1', huffman_code)
 
 
# ������ �� ������ �������� � ������������ �������������� ������
def decode(root, index, s):
 
    if root is None:
        return index
 
    # ��������� �������� ����
    if isLeaf(root):
        print(root.ch, end='')
        return index
 
    index = index + 1
    root = root.left if s[index] == '0' else root.right
    return decode(root, index, s)
 
 
# ������ ������ �������� � ���������� �������� ������� �����
def buildHuffmanTree(text):
 
    # ������� ������: ������ ������
    if len(text) == 0:
        return
 
    # ������������ ������� ��������� ������� �������
    # � ��������� ��� � �������
    freq = {i: text.count(i) for i in set(text)}
 
    # �������� ������������ ������� ��� �������� �������� ����� ������ ��������.
    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)
 
    # ������ �� ��� ���, ���� � queue �� �������� ����� ������ ����
    while len(pq) != 1:
 
        # ������� ��� ���� � ��������� �����������
        # (����� ������ �������) �� queue
 
        left = heappop(pq)
        right = heappop(pq)
 
        # ������� ����� ���������� ���� � ����� ����� ������ � �������� �������� �
        # � ��������, ������ ����� ������ ���� �����.
        # �������� ����� ���� � ������������ �������.
 
        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))
 
    # `root` ������ ��������� �� ������ ������ ��������.
    root = pq[0]
 
    # �������� �� ������ �������� � ��������� ���� �������� � �������.
    huffmanCode = {}
    encode(root, '', huffmanCode)
 
    # ����������� ���� ��������
    print('Huffman Codes are:', huffmanCode)
    print('The original string is:', text)
 
    # ����������� �������������� ������
    s = ''
    for c in text:
        s += huffmanCode.get(c)
 
    print('The encoded string is:', s)
    print('The decoded string is:', end=' ')
 
    if isLeaf(root):
        # ������ ������: ��� ����� ���� a, aa, aaa � �. �.
        while root.freq > 0:
            print(root.ch, end='')
            root.freq = root.freq - 1
    else:
        # ����� ���������� ������ ��������, � �� ���� ���
        # ���������� �������������� ������
        index = -1
        while index < len(s) - 1:
            index = decode(root, index, s)
 
 
# ���������� ��������� ����������� # �������� �� Python
if __name__ == '__main__':
 
    text = 'Huffman coding is a data compression algorithm.'
    buildHuffmanTree(text)

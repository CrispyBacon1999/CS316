from queue import PriorityQueue

class HuffmanNode:
    data = 0
    c = ""
    left = None
    right = None

    def __repr__(self):
        return f"{c}:{data}"

    # Implements sorting of the elements by the data attribute
    def __gt__(self, other):
        return data > other
    def __lt__(self, other):
        return data < other
    def __eq__(self, other):
        return data == other

def split_chrs(data):
    chrs = []
    freq = []
    for c in data:
        if not c in chrs:
            chrs.append(c)
            freq.append(1)
        else:
            i = chrs.index(c)
            freq[i] += 1
    
    return chrs, freq

def gen_table(root, table={}, bytecode=""):
    if root.left == None and root.right == None and root.c != "∅":
        table[root.c] = bytecode
        return table
    if root.left != None:
        table = gen_table(root.left, table=table, bytecode=bytecode + "0")
    if root.right != None:
        table = gen_table(root.right, table=table, bytecode=bytecode + "1")
    return table

def pretty_table(table):
    out = ""
    for key, by in table.items():
        out += f"{key}: {by}\n"
    return out

def compress_string_gen(x, table):
    for let in x:
        yield table[let]

def compress_string(x, table):
    d = ""
    for bytestr in compress_string_gen(x, table):
        d += bytestr
    return d
input_val = input("Enter data to compress: ")
input_val = input_val.lower() # Ignore case

data = split_chrs(input_val)
q = PriorityQueue(len(data[0]))
table = {}
if len(data[0]) == 1:
    # Account for cases where there's only one letter to be compressed. Breaks this implementation. Gives 8x compression
    table[data[0][0]] = "1"
else:
    for char, freq in zip(data[0], data[1]):
        n = HuffmanNode()
        n.data = freq
        n.c = char
        q.put(n)

    root = None
    while(q.qsize() > 1):
        x = q.get()
        y = q.get()
        par = HuffmanNode()
        par.data = x.data + y.data
        par.c = "∅"
        par.left = x
        par.right = y
        root = par
        q.put(par)

    table = gen_table(root, table={})
print(pretty_table(table))
compressed = compress_string(input_val, table)
orig_size = 8 * len(input_val)
print(f"Output: {compressed}")
print(f"Compression Ratio: {len(compressed) / orig_size:.4f}")
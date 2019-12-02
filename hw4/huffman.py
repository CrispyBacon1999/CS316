class HuffmanNode:
    data = 0
    c = ""
    left = None
    right = None


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







x = input("Enter data to compress")
x = x.lower()

print(split_chrs(x))
# Recursive function to 
def syracuse(n, i, data=[]):
    if i == 0:
        return data
    else:
        data.append(n)
        if not n % 2: # x is even
            return syracuse(n/2, i-1, data=data)
        else:
            return syracuse(3 * n + 1, i-1, data=data)


if __name__ == "__main__":
    print(syracuse(7, 6))
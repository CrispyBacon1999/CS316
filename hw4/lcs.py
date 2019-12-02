from pprint import pprint

def lcs_tables(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for i in range(n+1)] for k in range(m+1)]
    b = [[" " for i in range(n+1)] for k in range(m+1)]
    for i in range(1, m+1):
        c[i][0] = 0
    for j in range(0, n+1):
        c[0][j] = 0
    for i in range(1, m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i - 1][j-1] + 1
                b[i][j] = "🡔"
            elif c[i - 1][j] >= c[i][j-1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "🡑"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "🠠"
    return (c,b)

def print_table(nums, arrs):
    for row, arrow in zip(nums, arrs):
        for n, a in zip(row, arrow):
            print(f'{a}{n}', end=" ")
        print("")



def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == "🡔":
        print_lcs(b, X, i - 1, j - 1)
        print(X[i - 1], end="")
    elif b[i][j] == "🡑":
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)

x = input("String 1: ")
y = input("String 2: ")
res = lcs_tables(x, y)
print_table(res[0], res[1])
print("LCS: ", end="")
print_lcs(res[1], x, len(x), len(y))
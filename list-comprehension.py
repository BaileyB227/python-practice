if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final = []
    for i in range(1+x):
        for j in range(y+1):
            for k in range(1+z):
                if i+j+k!=n:
                    temp=[i,j,k]
                    final.append(temp)
                else:
                    continue
    print(final)
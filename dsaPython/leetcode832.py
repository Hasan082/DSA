def flipAndInvertImage(image):
    lst = []
    for i in range(len(image)):
        seclist = []
        for j in range(len(image[i])):
            if image[i][j] == 0:
                seclist.append(1)
            else:
                seclist.append(0)
        seclist.reverse()
        lst.append(seclist)
    return lst


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(flipAndInvertImage(image))

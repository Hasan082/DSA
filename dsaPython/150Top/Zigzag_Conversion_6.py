def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    res = [''] * numRows
    index, step = 0, 1

    for char in s:
        res[index] += char

        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        
        index += step

    return "".join(res)


s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows)) # "PAHNAPLSIIGYIR"
numRows = 4
print(convert(s, numRows)) # "PINALSIGYAHRPI"
numRows = 5
print(convert(s, numRows)) # "PHASIYIRPLIGAN"
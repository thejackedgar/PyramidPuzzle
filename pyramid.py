
def descendingPyramid(rows, target, start=0, end=1, total=1, path=''):
    if not rows:
        return
    print(rows, 'start:', start, ', end:', end)
    # total = 0
    # level = 0
    row = rows[0]
    for i in range(start, end):
        thing = total*row[i]
        if path != '':
            if i%end == 0: 
                path = 'L' 
            else: 
                path = 'R'
        # print(i, 'spot:', row[i], ', total:', thing)
        print('spot:', row[i])
        if rows[1:]:
            # print('RECURSION')
            rtn = descendingPyramid(rows[1:], target, i, i+2, thing)
            # rtn2 = descendingPyramid(rows[1:], target, i, i+2, thing, 'R')
            # print(rows, i, "RTN IS", rtn, ", PATH IS", path)
            # path += rtn
            # print("rtn length:", len(rtn), "rows length:", len(rows))
            if rtn:
                path += rtn
                return path
        else:
            # print("reached end", thing, "i:", i, "end:", end)
            if thing == target:
                print('FOUND', path, row[i])
                # if i%end == 0:
                #     path += 'L'
                # else:
                #     path += 'R'
                # print("RETURNING PATH", path)
                return path
    return path
    

# rows = [[1], [2, 3], [4, 1, 1]]
# target = 2

# result = descendingPyramid(rows, target)
# print("RESULT IS", result)

rows2 = [[2], [4, 3], [3, 2, 6], [2, 9, 5, 2], [10, 5, 2, 15, 5]]
target2 = 720

result2 = descendingPyramid(rows2, target2)
print("RESULT_2 IS", result2)
# Solve the descending pyramid puzzle
#   rows is a list of lists, where each list is a row of the pyramid
#   target is the target product to be reached at the bottom of the pyramid
#   start, end, total, and path are used for recursion
#   start and end are the starting and ending indices of the current row
#   total is the product of the numbers in the path
#   path is the path taken to get to the current number
def descendingPyramid(rows, target, start=0, end=1, total=1, path=''):
    # if given an empty list, return nothing
    if not rows:
        return
    #starting at the first given row in the pyramid, iterate through each number in the row
    row = rows[0]
    for i in range(start, end):
        #keep track of the total product of the numbers in the path
        count = total*row[i]
        #if we are not on the first row of the pyramid, we need to check if the number is on the left or right side of the previous row's number
        if end != 1:
            if (i+1)%(end) != 0: 
                path = 'L' 
            else: 
                path = 'R'
        #if there are more rows in the pyramid, recursively call the function with the next row, giving the new start and end values, and the updated total
        if rows[1:]:
            rtn = descendingPyramid(rows[1:], target, i, i+2, count)
            #if the recursive call returns a path, add the current path and send it up the recursive chain
            if rtn:
                path += rtn
                return path
        #if we are on the last row of the pyramid, check if the total product is equal to the target
        else:
            if count == target:
                return path

# Helper function to print the pyramid puzzle for visualization
def printPyramid(rows):
    for row in rows:
        print(row)

rows = [[1], [2, 3], [4, 1, 1]]
target = 2
print("Puzzle 1 ( Target", target, "):")
printPyramid(rows)
result = descendingPyramid(rows, target)
print("Path:", result, end="\n\n")

rows2 = [[2], [4, 3], [3, 2, 6], [2, 9, 5, 2], [10, 5, 2, 15, 5]]
target2 = 720
print("Puzzle 2 ( Target", target2, "):")
printPyramid(rows2)
result2 = descendingPyramid(rows2, target2)
print("Path 2:", result2, end="\n\n")

rows3 = [[4], [1, 2], [3, 8, 2], [4, 5, 3, 9], [10, 1, 3, 8, 3]]
target3 = 1152
print("Puzzle 3 ( Target", target3, "):")
printPyramid(rows3)
result3 = descendingPyramid(rows3, target3)
print("Path 3:", result3, end="\n\n")

rows4 = [[1]]
target4 = 1
print("Puzzle 4 ( Target", target4, "):")
printPyramid(rows4)
result4 = descendingPyramid(rows4, target4)
print("Path 4:", result4, end="\n\n")

rows5 = [[2], [1, 9], [3, 4, 7], [5, 6, 4, 5], [8, 11, 3, 6, 10], [6, 2, 8, 1, 4, 2]]
target5 = 6912
print("Puzzle 5 ( Target", target5, "):")
printPyramid(rows5)
result5 = descendingPyramid(rows5, target5)
print("Path 5:", result5, end="\n\n")
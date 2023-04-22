# PyramidPuzzle

A Pyramid Descent Puzzle consists of a pyramid of positive integers. To solve the puzzle, you must find a path that traverses the pyramid from top to bottom visiting numbers whose product is a given target value. Each step in the path must go down one row, and go either one step to the left or one step to the right.

For example, suppose the pyramid below has a target value of 2:

<p>&nbsp&nbsp&nbsp&nbsp1<br>
&nbsp&nbsp2&nbsp&nbsp3<br>
4&nbsp&nbsp1&nbsp&nbsp1</p>

A solver for this puzzle should output LR, indicating that the correct path starts from the 1 on top, goes Left to the 2 on the second row, then goes Right to the 1 in the center of the bottom row.

The solver assumes that every input pyramid has a first row with one number and every row thereafter has one more number than the row above. Each row is aligned such that the center of the row aligns with the midline of the pyramid

Another example for a more complex pyramid with a target of 720 is:

<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 2 <br>
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 4 &nbsp&nbsp&nbsp&nbsp 3 <br>
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 3 &nbsp&nbsp&nbsp&nbsp&nbsp 2 &nbsp&nbsp&nbsp&nbsp 6 <br>
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 2 &nbsp&nbsp&nbsp&nbsp 9 &nbsp&nbsp&nbsp&nbsp  5 &nbsp&nbsp&nbsp 2 <br>
&nbsp&nbsp 10 &nbsp&nbsp 5 &nbsp&nbsp&nbsp&nbsp&nbsp 2 &nbsp&nbsp&nbsp 15 &nbsp&nbsp 5 <br>
</p>

A solver for this puzzle should output LRLL, or in other words 2\*4\*2\*9\*5=720. 

# PyramidPuzzle

A Pyramid Descent Puzzle consists of a pyramid of positive integers. To solve the puzzle, you must find a path that traverses the pyramid from top to bottom visiting numbers whose product is a given target value. Each step in the path must go down one row, and go either one step to the left or one step to the right.

For example, suppose the pyramid below has a target value of 2.

<p>&nbsp&nbsp&nbsp&nbsp1<br>
&nbsp&nbsp2&nbsp&nbsp3<br>
4&nbsp&nbsp1&nbsp&nbsp1</p>

A solver for this puzzle should output LR, indicating that the correct path starts from the 1 on top, goes Left to the 2 on the second row, then goes Right to the 1 in the center of the bottom row.

# Improved Break Point Reversal Sort

The program does the following steps:
1. Take input from a text file that contains a list of permuted numbers through the function load()
2. Add numbers at the start and end of the array inside the ibprs() function, which in turn changes the number of breakpoints
3. Add breakpoints to the list and categorize each adjacency into decreasing and increasing strips using the breakpoints() function
4. Sort the numbers by reducing the number of breakpoints on decreasing strips or if there are no decreasing strip, 1 increasing strip is reversed to reduce number of breakpoints after the next reversal. The Improved Breakpoints Reversal Sort algorithm is used to repetitively execute these sorts.
5. Output each step of sorting, including the number of breakpoints for the permutation of each step and new permutation after applying the reversal
6. Output the reversal distance to the identity permutation at the end

The output for the given example p0.txt file is out0.txt.
Other test cases used are respectively p1, p2, p3.txt with output files out1, out2, out3.txt.
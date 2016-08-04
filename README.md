A command line tool that is similar to "comm" in Linux. It support all the functionality of "comm" in Linux but it also supports an extra "-u" option to compare two unordered files.

Usage:
./comm.py [options] [file1] [file2]

options:
-1:suppress the first column
-2:suppress the second column
-3:suppress the third column
-u:compare unordered files

Note:
When used without -u option, two files must be sorted.
There will be 3 columns if none of -1, -2 and -3 options is specified. The first column is the lines that are unique to file1. The second column is the lines that are unique to file2 and the third column are lines that exist in both files.
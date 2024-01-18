HackerRank Home
HackerRank
|
Prepare
Certify
Compete
Apply
Search
|
Switch to..
marotishelke2000
PrepareData StructuresArraysSparse Arrays
Sparse Arrays
736.52 more points to get your next star!
Rank: 92086|Points: 1463.48/2200
Problem Solving
Problem
Submissions
Leaderboard
Discussions
Editorial
You made this submission a year ago.
Score:25.00Status:Accepted
People who solved Sparse Arrays attempted this next:

Array Manipulation
Perform m operations on an array and print the maximum of the values.
Submitted Code
Language: Python 3
Open in editor
1
#!/bin/python3
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
​
9
#
10
# Complete the 'matchingStrings' function below.
11
#
12
# The function is expected to return an INTEGER_ARRAY.
13
# The function accepts following parameters:
14
#  1. STRING_ARRAY strings
15
#  2. STRING_ARRAY queries
16
#
17
​
18
def matchingStrings(strings, queries):
19
    # Write your code here
20
    dic = {}
21
    for string in strings:
22
        if string in dic:
23
            dic[string] += 1
24
        else:
25
            dic[string] = 1
26
    res = []
27
    for i in queries:
28
        if i in dic:
29
            res.append(dic[i])
30
        else:
31
            res.append(0)
32
    return res
33
if __name__ == '__main__':
34
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
35
​
36
    strings_count = int(input().strip())
37
​
38
    strings = []
39
​
40
    for _ in range(strings_count):
41
        strings_item = input()
42
        strings.append(strings_item)
43
​
44
    queries_count = int(input().strip())
45
​
46
    queries = []
47
​
48
    for _ in range(queries_count):
49
        queries_item = input()
50
        queries.append(queries_item)
51
​
52
    res = matchingStrings(strings, queries)
53
​
54
    fptr.write('\n'.join(map(str, res)))
55
    fptr.write('\n')
56
​
57
    fptr.close()
58
​

Test case 0

Test case 1

Test case 2

Test case 3

Test case 4

Test case 5

Test case 6

Test case 7

Test case 8

Test case 9

Test case 10

Test case 11

Test case 12
Compiler Message
Success
Hidden Test Case
Unlock this testcase for 5 hackos.
NEED HELP?
View discussions
View editorial
View top submissions
BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy

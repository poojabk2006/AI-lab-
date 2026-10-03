Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
==== RESTART: C:/Users/BMSCECSE-SH/Desktop/1BM24CS203/8-puzzle using IDS.py ====
INITIAL STATE
-------------
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

GOAL STATE
----------
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]


DEPTH LIMIT = 0
====================
Depth: 0
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]


DEPTH LIMIT = 1
====================
Depth: 0
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Move: UP
  Depth: 1
  [1, 0, 3]
  [4, 2, 6]
  [7, 5, 8]

Move: DOWN
  Depth: 1
  [1, 2, 3]
  [4, 5, 6]
  [7, 0, 8]

Move: LEFT
  Depth: 1
  [1, 2, 3]
  [0, 4, 6]
  [7, 5, 8]

Move: RIGHT
  Depth: 1
  [1, 2, 3]
  [4, 6, 0]
  [7, 5, 8]


DEPTH LIMIT = 2
====================
Depth: 0
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Move: UP
  Depth: 1
  [1, 0, 3]
  [4, 2, 6]
  [7, 5, 8]

  Move: LEFT
    Depth: 2
    [0, 1, 3]
    [4, 2, 6]
    [7, 5, 8]

  Move: RIGHT
    Depth: 2
    [1, 3, 0]
    [4, 2, 6]
    [7, 5, 8]

Move: DOWN
  Depth: 1
  [1, 2, 3]
  [4, 5, 6]
  [7, 0, 8]

  Move: LEFT
    Depth: 2
    [1, 2, 3]
    [4, 5, 6]
    [0, 7, 8]

  Move: RIGHT
    Depth: 2
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 0]


GOAL STATE FOUND!

SOLUTION PATH
=============
Step 0
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Step 1
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Step 2
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]


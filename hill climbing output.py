Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
======= RESTART: C:/Users/BMSCECSE-SH/Desktop/1BM24CS203/hill climbing.py ======

Current State: [3, 1, 2, 0]
Current Cost: 2

Neighbor States:
Swap (0, 1) State: [1, 3, 2, 0] Cost: 1
Swap (0, 2) State: [2, 1, 3, 0] Cost: 1
Swap (0, 3) State: [0, 1, 2, 3] Cost: 6
Swap (1, 2) State: [3, 2, 1, 0] Cost: 6
Swap (1, 3) State: [3, 0, 2, 1] Cost: 1
Swap (2, 3) State: [3, 1, 0, 2] Cost: 1

Selected Swap: (0, 1)

Current State: [1, 3, 2, 0]
Current Cost: 1

Neighbor States:
Swap (0, 1) State: [3, 1, 2, 0] Cost: 2
Swap (0, 2) State: [2, 3, 1, 0] Cost: 2
Swap (0, 3) State: [0, 3, 2, 1] Cost: 4
Swap (1, 2) State: [1, 2, 3, 0] Cost: 4
Swap (1, 3) State: [1, 0, 2, 3] Cost: 2
Swap (2, 3) State: [1, 3, 0, 2] Cost: 0

Selected Swap: (2, 3)

Current State: [1, 3, 0, 2]
Current Cost: 0
Goal State Reached!

Final Configuration: [1, 3, 0, 2]
Final Cost: 0

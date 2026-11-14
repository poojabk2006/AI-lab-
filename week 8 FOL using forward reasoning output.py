Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/BMSCECSE-SH/Desktop/1BM24CS203/week 8 FOL using forward reasoning.py
========== CASE 1 ==========
Initial Facts:
('American', 'Robert')
('Enemy', 'A', 'America')
('Missile', 'T1')
('Owns', 'A', 'T1')

Forward Chaining:
Derived: ('Weapon', 'T1')
Derived: ('Sells', 'Robert', 'T1', 'A')
Derived: ('Hostile', 'A')
Derived: ('Criminal', 'Robert')

Final Knowledge Base:
('American', 'Robert')
('Criminal', 'Robert')
('Enemy', 'A', 'America')
('Hostile', 'A')
('Missile', 'T1')
('Owns', 'A', 'T1')
('Sells', 'Robert', 'T1', 'A')
('Weapon', 'T1')

Robert is a Criminal.

========== CASE 2 ==========
Initial Facts:
('American', 'Robert')
('Enemy', 'A', 'America')
('Missile', 'T1')
('Owns', 'A', 'T1')

Forward Chaining:
Derived: ('Weapon', 'T1')
Derived: ('Hostile', 'A')

Final Knowledge Base:
('American', 'Robert')
('Enemy', 'A', 'America')
('Hostile', 'A')
('Missile', 'T1')
('Owns', 'A', 'T1')
('Weapon', 'T1')

Robert is NOT a Criminal (under the modified facts).

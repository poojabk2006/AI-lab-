
# First Order Logic - Forward Chaining

def forward_chaining(KB, sell_rule=True):

    changed = True

    while changed:
        changed = False

        # Rule 1: Missiles are weapons
        for fact in list(KB):
            if fact[0] == "Missile":
                new_fact = ("Weapon", fact[1])

                if new_fact not in KB:
                    KB.add(new_fact)
                    print("Derived:", new_fact)
                    changed = True

        # Rule 2: Missiles owned by A were sold by Robert
        if sell_rule:
            for fact in list(KB):
                if fact[0] == "Missile":
                    x = fact[1]

                    if ("Owns", "A", x) in KB:
                        new_fact = ("Sells", "Robert", x, "A")

                        if new_fact not in KB:
                            KB.add(new_fact)
                            print("Derived:", new_fact)
                            changed = True

        # Rule 3: Enemies are hostile
        for fact in list(KB):
            if fact[0] == "Enemy":
                new_fact = ("Hostile", fact[1])

                if new_fact not in KB:
                    KB.add(new_fact)
                    print("Derived:", new_fact)
                    changed = True

        # Rule 4: Crime rule
        for fact in list(KB):
            if fact[0] == "Sells":
                p, q, r = fact[1], fact[2], fact[3]

                if (("American", p) in KB and
                    ("Weapon", q) in KB and
                    ("Hostile", r) in KB):

                    new_fact = ("Criminal", p)

                    if new_fact not in KB:
                        KB.add(new_fact)
                        print("Derived:", new_fact)
                        changed = True

    return KB


# CASE 1: Original Facts
KB1 = {
    ("Owns", "A", "T1"),
    ("Missile", "T1"),
    ("American", "Robert"),
    ("Enemy", "A", "America")
}

print("========== CASE 1 ==========")
print("Initial Facts:")

for fact in sorted(KB1):
    print(fact)

print("\nForward Chaining:")
result1 = forward_chaining(KB1)

print("\nFinal Knowledge Base:")
for fact in sorted(result1):
    print(fact)

if ("Criminal", "Robert") in result1:
    print("\nRobert is a Criminal.")


# CASE 2: Changed Facts
# Robert did not sell weapons to Country A

KB2 = {
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Missile", "T1"),
    ("Owns", "A", "T1")
}

print("\n========== CASE 2 ==========")
print("Initial Facts:")

for fact in sorted(KB2):
    print(fact)

print("\nForward Chaining:")
result2 = forward_chaining(KB2, sell_rule=False)

print("\nFinal Knowledge Base:")
for fact in sorted(result2):
    print(fact)

if ("Sells", "Robert", "T1", "A") not in result2:
    print("\nRobert is NOT a Criminal (under the modified facts).")

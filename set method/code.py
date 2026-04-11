# Starting sets
s = {1, 2, 3}
t = {3, 4, 5}

print("Original s:", s)
print("Original t:", t)

# 1. add()
s.add(6)
print("After add:", s)

# 2. update()
s.update([7, 8])
print("After update:", s)

# 3. remove()
s.remove(2)
print("After remove:", s)

# 4. discard()
s.discard(10)   # no error if not present
print("After discard:", s)

# 5. pop()
popped = s.pop()
print("After pop:", s, "| Popped:", popped)

# 6. clear()
temp = s.copy()
s.clear()
print("After clear:", s)

# Restore
s = temp.copy()

# 7. copy()
new_s = s.copy()
print("Copy:", new_s)

# 8. union()
print("Union:", s.union(t))

# 9. intersection()
print("Intersection:", s.intersection(t))

# 10. difference()
print("Difference:", s.difference(t))

# 11. symmetric_difference()
print("Symmetric Difference:", s.symmetric_difference(t))

# 12. issubset()
print("Is subset:", {3,4}.issubset(t))

# 13. issuperset()
print("Is superset:", t.issuperset({3}))

# 14. isdisjoint()
print("Is disjoint:", s.isdisjoint({9,10}))

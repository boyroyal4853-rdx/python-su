# Starting dictionary
d = {"a": 1, "b": 2, "c": 3}
print("Original:", d)

# 1. clear()
temp = d.copy()
d.clear()
print("After clear:", d)

# Restore
d = temp.copy()

# 2. copy()
new_d = d.copy()
print("Copy:", new_d)

# 3. fromkeys()
fk = dict.fromkeys(['x','y'], 0)
print("Fromkeys:", fk)

# 4. get()
print("Get 'a':", d.get("a"))

# 5. items()
print("Items:", d.items())

# 6. keys()
print("Keys:", d.keys())

# 7. values()
print("Values:", d.values())

# 8. pop()
val = d.pop("b")
print("After pop:", d, "| Popped:", val)

# 9. popitem()
pair = d.popitem()
print("After popitem:", d, "| Removed:", pair)

# 10. setdefault()
d.setdefault("z", 99)
print("After setdefault:", d)

# 11. update()
d.update({"a": 100, "x": 200})
print("After update:", d)

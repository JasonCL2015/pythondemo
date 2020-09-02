a = sorted([36, 5, -12, 9, -21], key=abs)
b = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
c = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

print(a)
print(b)
print(c)

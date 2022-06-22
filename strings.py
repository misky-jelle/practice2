# How to turn the first half into uppercase
x="childrenplayinginplayground"
y=len(x)//2
second=x[y:].upper()
first=x[:y].lower()
third=first+second
print(third)

x="childrenplayinginplayground"
y=len(x)//2
second=x[y:].lower()
first=x[:y].upper()
third=first+second
print(third)


# How to reverse and put y in upper case
n="childrenplayinginplayground"
k=len(n)//2
y=n[k:].upper()
j=n[:k].lower()
v=y+j
print(v)









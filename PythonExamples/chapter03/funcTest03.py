def myfunc(ga, na):
    result = ga * ga + na * na
    return result

a, b = 3, 4
y=myfunc(a, b)
print(y)

a, b = 2, 3
y=myfunc(a, b)
print(y)

for idx in range(3) :
    print(myfunc(idx, idx+1))

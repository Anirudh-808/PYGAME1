a = "hello"
print(a)

def f():
    global a
    a = "world"
    print(a)

f()
print(a)
def wish(name):
    print("hello good morning",name)

result = wish
wish('siva')
result('rama')
del wish
result('siva')


def outer():
    print('outer function started')
    def inner():
        print("inner function execution")
    print("outer function calling inner function")
    inner()
outer()#1
f1 = outer #2
f1()

def outer_1():
    print('outer function started...')
    def inner_1():
            print("inner function execution...")
    print("outer function calling inner function...")
    return inner_1

f1 = outer_1#function aliasing
f1()
f1()
f2=outer_1()#f2 is aliasing for inner function
f2()
f2()
f2()

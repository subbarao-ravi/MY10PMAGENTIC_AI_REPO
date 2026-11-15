import gc
import sys

print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

class Test:
    pass

t = Test()
t1=t
t2=t
t3=t
t4=t
print(sys.getrefcount(t))


from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableParallel

def add_ten(x):
    result=x+10
    return result

def multiply_ten(x):
     result= x*10
     return result

def sub_ten(x):
     result=x-5
     return result

parallel = RunnableParallel(
     add = add_ten,
     mul = multiply_ten,
     sub = sub_ten
)

result = parallel.invoke(10)
print(result)

print('-------------with lambda---------------')

add_ten = RunnableLambda(
     lambda x : x+10
)

mult_20 = RunnableLambda(
     lambda x : x *20
)

sub_20 = RunnableLambda(
     lambda x : x -20
)

parallel = RunnableParallel(
     add = add_ten,
     mul = mult_20,
     sub = sub_20
) 

result = parallel.invoke(100)
print(result)
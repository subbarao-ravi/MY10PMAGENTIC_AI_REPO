from dotenv import  load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableSequence, 
    RunnableParallel, 
    RunnableLambda,
    RunnablePassthrough,
    RunnableBranch
)

distinction = RunnableLambda(
    lambda x : f"{x['name']} : Distinction (Grade A)"
)
first_class = RunnableLambda(
    lambda x : f"{x['name']} : firstClass (Grade B)"
)

second_class = RunnableLambda(
    lambda x : f"{x['name']} : secondClass (Grade C)"
)

fail = RunnableLambda(
    lambda x : f"{x['name']} : Fail, needs to reappear"
)

gradeChain = RunnableBranch(
    (lambda x : x['marks'] >=75, distinction),
    (lambda x : x['marks'] >=60, first_class),
    (lambda x : x['marks'] >=40, second_class),
    fail
)

result = gradeChain.invoke({"name":"rama", "marks":80})
print(result)
# gradeChain.invoke({"name":"ravi", "marks":60})
# gradeChain.invoke({"name":"raja", "marks":50})
# gradeChain.invoke({"name":"roji", "marks":35})
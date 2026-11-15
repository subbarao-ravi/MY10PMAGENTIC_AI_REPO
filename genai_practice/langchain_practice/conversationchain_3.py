from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv, find_dotenv
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains.conversation.base import ConversationChain

load_dotenv(find_dotenv(), override=True)

llm = ChatOpenAI(
    model="gpt-4.1-mini"
)

memory = ConversationBufferMemory(
    return_messages=True,
    memory_key="history"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         '''
            You are a python teacher
            explain every thing in simple english
            assume the student is a beginner
            provide simple examples where ever possible
        '''
        ),
        (
            "human","{input}"
        ),
        MessagesPlaceholder(
            variable_name="history"
        )
    ]
)

conversation = ConversationChain(
    llm= llm,
    memory= memory,
    prompt= prompt
)
print()
print("LEGACY CHAT BOT")
print('type exit to stop')
print('----------------------')

while True:
    user_input = input('\nYou:')
    if user_input.lower() == 'exit':
        print('chat ended')
        break

    try:
        result = conversation.invoke({
             "input": user_input
         })
        print('history ', result['history'])
        print('response ', result['response'])
    except ConnectionError as e:
        print('error ', e)
    except Exception as e:
        print('error ', e)

    





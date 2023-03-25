from langchain import OpenAI 
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

load_dotenv('.env.txt')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)


conversation = ConversationChain(
memory= ConversationBufferMemory(),
verbose=True,
llm=OpenAI(temperature=0.9)
)

# output1 = conversation.predict(input = input("input here!"))
output2 = conversation.predict(input = input("input here!"))

print(output2)
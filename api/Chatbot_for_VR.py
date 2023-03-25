from langchain import OpenAI 
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

load_dotenv('.env.txt')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def chatGPT(input):
  conversation = ConversationChain(
  memory= ConversationBufferMemory(),
  verbose=True,
  llm=OpenAI(temperature=0.9)
  )
  return conversation.predict(input=input)
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate

llm = ChatOllama(model="gemma:2b")

difficulty = input("Enter your difficulty level: ")
topic = input("Enter topic: ")
promptTemplate = PromptTemplate(
    template="""
    You are a master of Java. 
    There are three different difficulty levels, Beginner, Intermediate and Expert, to check any individual's knowledge. 
    Generate 5 MCQs for {difficulty_level} difficulty on topic {topic}.
    """
)

if difficulty:
    if topic:
        response = llm.invoke(promptTemplate.format(difficulty_level=difficulty, topic = topic))
        print(response.content)
    else:
        print("Enter valid topic.")
else:
    print("Please give a valid difficulty level.")
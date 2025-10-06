from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm = OpenAI(temperature=0.7)
    name = llm(
        "I have a pet and i want a cool name for it. suggest five cool names for my pet"
    )

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def generate_pet_name():
    llm = OpenAI()
    
    response = llm.chat.completions.create( 
         model = "gpt-3.5-turbo",
         temperature=0.7,
        messages=[
        {"role": "system", "content":"you are a helpful pet naming assitant."},
        {"role": "user",  "content": "I have a dog pet and i want a cool name for it. suggest five cool names for my pet"},
        ]    
    )
       
    
   
    return response.choices[0].message.content

if __name__ == '__main__':
    print(generate_pet_name())



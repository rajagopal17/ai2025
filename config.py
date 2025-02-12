import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
###########################################################

from google import genai

client      = genai.Client(api_key=gemini_api_key)
response    = client.models.generate_content(
                        model    ="gemini-2.0-flash", 
                        contents ="Explain how combustion engine works in 10 sentences."
                      )


print('#####################\n')
print(response.model_dump())
print('#####################\n')
print(response.candidates[0].content)
print('#####################\n')    
#print(response.candidates[0].score)
print('#####################\n')
#print(response.candidates[0].metadata)
print('#####################\n')

print('#####################\n')
print(response.candidates[0].__dict__)
print('#####################\n')
#
print('#####################\n')
print(response.candidates[0].__dict__)
print('#####################\n')
print(response.candidates[0].content)
print('#####################\n')
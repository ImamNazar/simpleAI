API_KEY='Please put your generated secret API key from OpenAI API Keys in this field'
import openai
import os
os.environ['OPENAI_Key']=API_KEY
openai.api_key=os.environ['OPENAI_Key']

keep_prompting=True
while keep_prompting:
   prompt = input('What is your question? Type exit if done:)')
   if prompt=='exit':
    keep_prompting=False

   else:
      
      response=openai.Completion.create(engine='text-davinci-003', prompt=prompt, max_tokens=200)
      print(response['choices'][0]['text'])
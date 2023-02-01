API_KEY='Please put your generated secret API key from OpenAI API Keys in this field'
import openai

openai.api_key = API_KEY

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def chatbot():
    print("Hi, I am a chatbot powered by OpenAI. How can I help you today?")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
        response = generate_response(prompt)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()


      #Run the following command to install the official Python bindings: pip install openai

      #Run the following command in your Node.js project directory to install the official Node.js library: npm install openai
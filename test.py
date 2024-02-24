from openai import OpenAI
from dotenv import load_dotenv
import os
import gradio 

load_dotenv()

client = OpenAI(api_key=os.getenv('API_KEY'))

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)

messages =[{"role": "system", "content": "You are a data analyst"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response  = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Analytics Bot")

demo.launch()
import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nBossBot:"
restart_sequence = "\n\nUser:"
session_prompt = "BossBot is a chatbot that reluctantly answers questions.\n\n###\nUser: How many pounds are in a kilogram?\nBossBot: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\n###\nUser: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\n###\nBossBot: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\n###\nUser: Who was the first man in space?\nBossBot:"
chat_log = ""

def ask(question):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    answer = response['choices'][0]['text']
    append_interaction_to_chat_log(question, answer)
    return str(answer)

def append_interaction_to_chat_log(question, answer):
    global chat_log
    chat_log = f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

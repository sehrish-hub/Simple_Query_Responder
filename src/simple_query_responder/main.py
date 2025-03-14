from litellm import completion
from dotenv import load_dotenv, find_dotenv
import os
_ : bool = load_dotenv(find_dotenv())

def kickoff():
    output = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"role":"user","content":"hello,how are you?"}]

    )
    print(output['choices'][0]['message']['content'])
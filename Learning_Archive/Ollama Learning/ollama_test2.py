"""
import ollama

messages= [{"role":"system","content":"You are a loyal assistant who answers after analysing the question asked by user properly."}]

while True:
    
    userinput= input("Waiting for response\n")
    
    if userinput.lower() in {"bye","goodbye","see you","Take care"} or not userinput:
        break
    
    messages.append([{"role":"user","content":userinput}])
    
    response= ollama.chat(model="phi3",messages=messages)
    answer= response.message.content
    
    messages.append([{"role":"assitant","content":answer}])
    print(answer)
    """
#above one was giving lunatic answer
import ollama

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Answer clearly and concisely."
    }
]

while True:
    userinput = input("Waiting for response:\n> ")

    if ("command" in userinput.lower()) & ("function" in userinput.lower()) & ("override" in userinput.lower()):
        print("accepted")
        continue # Will add master control later
        
    if userinput.strip().lower() in ("bye", "goodbye", "see you", "take care", "quit", "exit"):
        print("Assistant: Bye! 👋")
        break

    messages.append({"role": "user", "content": userinput})

    response = ollama.chat(model="phi3", messages=messages)
    answer = response.message.content

    messages.append({"role": "assistant", "content": answer})
    print("Assistant:", answer)

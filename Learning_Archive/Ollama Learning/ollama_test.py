import ollama
print("Type /'BYE/' to exit chat")
while True:
    userinput=input("Waiting for response\n")
    if userinput.lower()=="bye":
        break
    
    response =ollama.chat(model="phi3",messages=[{"role":"user","content":userinput}])
    print(response["message"]["content"])

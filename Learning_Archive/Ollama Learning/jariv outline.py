import ollama

def simple_chat(prompt_text):
    try:
        # Ensure the Ollama service is running in the background
        # Ollama will automatically start if it's not running when you make a request.
        print(f"Sending prompt to phi3:mini...\n")
        response = ollama.chat(
            model='phi3:mini',
            messages=[{'role': 'user', 'content': prompt_text}],
            stream=False # We want the full response at once for now
        )
        return response['message']['content']
    except ollama.ResponseError as e:
        print(f"Ollama Error: {e}")
        print("Please ensure the Ollama desktop application is running.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    print("Jarvis Core Initiated. Type 'exit' or 'quit' to end the session.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Jarvis: Goodbye, sir.")
            break

        # Add a basic Jarvis persona prompt for initial interaction
        full_prompt = f"You are Jarvis, a helpful and sophisticated AI assistant. Respond concisely and professionally, like a butler. \n\nUser: {user_input}\nJarvis:"

        jarvis_response = simple_chat(full_prompt)
        if jarvis_response:
            print(f"Jarvis: {jarvis_response}")
        print("-" * 30) # Separator

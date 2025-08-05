import os
import requests
from ctransformers import AutoModelForCausalLM
import asyncio

# Configuration
MODEL_URL = "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q5_K_M.gguf"
MODEL_NAME = "mistral-7b-instruct-v0.1.Q5_K_M.gguf"
MODEL_PATH = os.path.join(os.getcwd(), MODEL_NAME)

async def download_model():
    if not os.path.exists(MODEL_PATH):
        print(f"Downloading model... (This may take several minutes)")
        response = requests.get(MODEL_URL, stream=True)
        response.raise_for_status()
        
        with open(MODEL_PATH, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Model downloaded successfully!")
    else:
        print("Model already exists, skipping download.")

async def initialize_model():
    await download_model()
    
    llm = AutoModelForCausalLM.from_pretrained(
        model_path_or_repo_id=MODEL_PATH,
        model_type="mistral",
        gpu_layers=1  # Adjust based on your GPU capability
    )
    return llm

async def generate_response(llm, prompt):
    response = llm(prompt, stream=True, max_new_tokens=1000)
    full_response = ""
    for token in response:
        full_response += token
    return full_response

async def chat_loop():
    llm = await initialize_model()
    print("\nModel loaded successfully!")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            break
        
        print("\nMistral: ", end='')
        response = await generate_response(llm, user_input)
        print(response + "\n")

if __name__ == "__main__":
    try:
        asyncio.run(chat_loop())
    except KeyboardInterrupt:
        print("\nExiting...")

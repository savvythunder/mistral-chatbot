---

# 🧠 Mistral-7B-Instruct Chatbot (Offline LLM with `ctransformers`)

This is a simple Python-based chatbot that uses the [Mistral-7B-Instruct-v0.1](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) model. It runs locally via the lightweight `ctransformers` library, and allows interactive conversations in your terminal using a quantized GGUF model.

---

## 🚀 Features

* ✅ Runs fully offline after the initial download
* ✅ Downloads a quantized version of Mistral 7B
* ✅ Loads efficiently via `ctransformers`
* ✅ Simple, async terminal-based chat interface
* ✅ Supports streaming token-by-token generation

---

## 📦 Requirements

* Python 3.8+
* Packages:

  ```bash
  pip install requests ctransformers
  ```

---

## ▶️ How to Use

1. **Save the code** to a file, e.g., `chatbot.py`.

2. **Run the script**:

   ```bash
   python chatbot.py
   ```

3. **Start chatting** with the model:

   ```plaintext
   You: Ai is going to
   ```

---

## 💬 Example Output

Here is what the model responded with for the prompt: `"Ai is going to"`

```plaintext
change
change the
change the world
change the world!
change the world! No
change the world! No doubt
change the world! No doubt about
change the world! No doubt about it.
change the world! No doubt about it. I
change the world! No doubt about it. I am
change the world! No doubt about it. I am writing
change the world! No doubt about it. I am writing this
change the world! No doubt about it. I am writing this while
change the world! No doubt about it. I am writing this while sipping
change the world! No doubt about it. I am writing this while sipping on
change the world! No doubt about it. I am writing this while sipping on a
change the world! No doubt about it. I am writing this while sipping on a cup
change the world! No doubt about it. I am writing this while sipping on a cup of
change the world! No doubt about it. I am writing this while sipping on a cup of coffee
change the world! No doubt about it. I am writing this while sipping on a cup of coffee (or
change the world! No doubt about it. I am writing this while sipping on a cup of coffee (or maybe
change the world! No doubt about it. I am writing this while sipping on a cup of coffee (or maybe it's
change the world! No doubt about it. I am writing this while sipping on a cup of coffee (or maybe it's tea,
change the world! No doubt about it. I am writing this while sipping on a cup of coffee (or maybe it's tea, who knows?)
```

---

## ⚙️ Configuration

You can tweak the following options in the script:

| Option         | Description                                                |
| -------------- | ---------------------------------------------------------- |
| `MODEL_URL`    | Hugging Face download URL for the GGUF model               |
| `MODEL_NAME`   | Filename to save the model as                              |
| `gpu_layers=1` | Number of layers to offload to GPU (set to 0 for CPU-only) |

---

## 📁 Files Downloaded

* **Model**: `mistral-7b-instruct-v0.1.Q5_K_M.gguf` (\~4–5 GB depending on quantization)

---

## 📄 License

* **Code**: MIT License
* **Model**: Provided by [TheBloke](https://huggingface.co/TheBloke) under their respective licenses via Hugging Face.

---

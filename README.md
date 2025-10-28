🧠 Rebuilding GPT-2 from Scratch

This project reconstructs the complete GPT-2 architecture from the ground up — including tokenization, embeddings, transformer layers, attention, and training — trained on The Verdict novel dataset. The goal was to deeply understand the internal mechanisms of large language models by manually re-implementing each component and extending it with controlled randomness and pretrained weight fine-tuning.

🚀 Features

🏗️ Full GPT-2 Architecture Rebuild:
Implemented every part of the model manually, including input embeddings, positional encoding, and transformer block logic.

🧩 Custom Tokenization & Vocabulary Creation:
Designed a lightweight tokenizer and vocabulary generator to process raw text efficiently.

🔁 Transformer Blocks (12-headed, 768-dim):
Built attention heads, feedforward networks, and layer normalization layers identical to GPT-2 small.

📉 Cross-Entropy Loss & Backpropagation:
Used manually computed gradients for loss optimization with temperature-scaled sampling for smoother text generation.

🔥 Temperature Scaling & Coherence Tuning:
Controlled randomness and creativity in text generation using temperature parameters for stable and diverse outputs.

🧠 Fine-Tuned with Pretrained GPT-2 Weights:
Loaded pretrained weights to enhance contextual understanding and fluency while preserving architectural customizations.

🧬 Architecture Overview
Input Text → Tokenizer → Embedding Layer + Positional Encoding
            ↓
      Multi-Head Attention (12 Heads)
            ↓
  Feedforward Neural Network + LayerNorm
            ↓
   Output Projection → Softmax → Text Generation

🧰 Tech Stack

Python

PyTorch

NumPy

Matplotlib / Seaborn (for training visualization)

Custom Tokenizer

Pretrained GPT-2 Weights (Hugging Face compatible)

📊 Training Details

Dataset: The Verdict novel text corpus

Batch Size: Variable (tuned for GPU/CPU memory)

Loss Function: Cross-Entropy

Optimizer: AdamW

Epochs: ~30

Temperature: 0.7–1.2 (for generation tuning)

🗣️ Example Usage
# Generate text from a trained GPT-2 model
prompt = "Justice is served when"
output = model.generate(prompt, max_length=100, temperature=0.8)
print(output)

🧩 Results

Generated text showed contextual coherence and semantic continuity across multi-sentence sequences.

Fine-tuning with pretrained GPT-2 weights boosted fluency, vocabulary diversity, and creative generation quality.

🧠 Learning Outcome

This project offered hands-on insight into:

The inner workings of transformer architectures

The relationship between attention heads and context depth

How temperature scaling and fine-tuning influence model creativity and factual consistency

📚 Future Work

Integrate LoRA for lightweight fine-tuning

Add visualization dashboards for attention maps

Extend model for domain-specific datasets

🧑‍💻 Author

Vanshika Arora
AI Engineer | LLMs | RAG | Transformer Architectures
📫 vanshikaa517@gmail.com

🔗 GitHub: @vanshikaarorax

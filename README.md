This Jupyter Notebook demonstrates the internal structure and functionality of a custom-built GPT-like Transformer model.

📌 About This Notebook
The notebook Model_Weights_Loaded.ipynb is part of a larger project in which I built a GPT-style model from scratch.

It includes:

Vocabulary tokenization

Positional encoding

Embedding layers

Multi-head self-attention mechanism

Transformer blocks

Final output decoding

The model dimensions are based on GPT architecture:

Embedding size: 768

Number of heads: 12

🔍 Why Open This Notebook?
If you want to:

Understand how a GPT-like model is constructed

See the structure and flow of a Transformer

View the trained weights loaded for inference

Explore how input is tokenized and passed through each layer

Then open this notebook and walk through each cell. This notebook reveals the internals of the architecture, making it educational and insightful for anyone interested in how large language models work.

🚀 How to Run
Make sure you have Python installed (preferably 3.8+).

Install the required libraries:

bash
Copy
Edit
pip install numpy torch matplotlib
Open the notebook using Jupyter:

bash
Copy
Edit
jupyter notebook Model_Weights_Loaded.ipynb
📁 Files Used
Model_Weights_Loaded.ipynb: Main notebook showcasing the model

the_verdict.txt: Text corpus used to build the vocabulary and train the model

model_weights.pth: Pretrained weights for the Transformer model


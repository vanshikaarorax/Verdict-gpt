import json


with open("Model_Weights_Loaded.ipynb", "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Filter out markdown cells
notebook['cells'] = [cell for cell in notebook['cells'] if cell['cell_type'] != 'markdown']

# Save the modified notebook
with open("Model-1.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

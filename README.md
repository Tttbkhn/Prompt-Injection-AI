# Prompt-Injection-AI
AI Services of Prompt Injection Project. Including Prompt Injection Training and pre-trained model of LLM

---

# BERT Classification Inference Model

This guide provides instructions on how to download and use the BERT Classification model for malicious prompt detection.

## Steps to Use the Inference Model

### 1. Download the Model

Download the pre-trained BERT Classification model from the following link:

**Download Model: [malicious-prompt-detector](<https://drive.google.com/drive/folders/1-8iXYXJG80IuPQ9O8fnrp8h8KEcjiHzX?usp=sharing>)**

### 2. Place Model in Folder `BERT`

After downloading, place the model files in the following directory structure:

```bash
Models/
│
└── BERT/
    └── malicious-prompt-detector
    └── inference.py
```

Make sure all required model files (such as `config.json`, `model.safetensors`, `special_tokens_maps.json`, `tokenizer_config.json`, and `vocab.txt`) are placed inside the `malicious-prompt-detector` folder.

### 3. Install Required Packages

Before running the inference, ensure that all necessary Python packages are installed. You can do this by running the following command:

```bash
pip install transformers torch
```
or
```bash
pip3 install transformers torch
```

Make sure you are using Python 3.10 or higher.

### 4. Run the Inference

To run the inference model, use the following command:

```bash
python inference.py
```
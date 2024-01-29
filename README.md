# Medical_chatbot_Llama2

STEPS TO RUN THE PROJECT:
```bash
conda create -n mchatbot python=3.8 -y

```
```bash
conda activate mchatbot
```
```bash
pip install -r requirements.txt
```

### create a '.env' file in the root directory and your Pinecone credential as follow

```ini
PINECONE_API_KEY=""
PINECONE_API_ENV=""
```

### Download the quantize model from the link given below

```ini
### Download the lamma2 model:

llama-2-7b-chat.ggmlv3.q4_0.bin

## From the following link
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```
from transformers import AutoTokenizer, AutoModel

MODEL_DIR = r'/path/to/model'

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModel.from_pretrained(MODEL_DIR)

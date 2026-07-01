import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

MODEL_PATH = os.path.join(ARTIFACTS_DIR, "chatbot_model.keras")
TOKENIZER_PATH = os.path.join(ARTIFACTS_DIR, "tokenizer.pkl")
LABEL_ENCODER_PATH = os.path.join(ARTIFACTS_DIR, "label_encoder.pkl")
RESPONSES_PATH = os.path.join(ARTIFACTS_DIR, "responses.pkl")
CONFIG_PATH = os.path.join(ARTIFACTS_DIR, "config.json")

CONFIDENCE_THRESHOLD = 0.6
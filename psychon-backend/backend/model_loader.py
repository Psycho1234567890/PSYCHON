import pickle
import json
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from config import ARTIFACTS_DIR, CONFIDENCE_THRESHOLD

# Custom Attention layer – must be defined before loading
class Attention(tf.keras.layers.Layer):
    def __init__(self, units, **kwargs):
        super(Attention, self).__init__(**kwargs)
        self.units = units
        self.W1 = tf.keras.layers.Dense(units)
        self.W2 = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, features):
        score = self.V(tf.nn.tanh(self.W1(features) + self.W2(features)))
        attention_weights = tf.nn.softmax(score, axis=1)
        context_vector = attention_weights * features
        context_vector = tf.reduce_sum(context_vector, axis=1)
        return context_vector

    def get_config(self):
        config = super().get_config()
        config.update({"units": self.units})
        return config

model = None
tokenizer = None
label_encoder = None
responses = None
max_len = None

def load_artifacts():
    global model, tokenizer, label_encoder, responses, max_len
    if model is None:
        model = tf.keras.models.load_model(
            os.path.join(ARTIFACTS_DIR, "chatbot_model.keras"),
            custom_objects={'Attention': Attention}
        )
        with open(os.path.join(ARTIFACTS_DIR, "tokenizer.pkl"), "rb") as f:
            tokenizer = pickle.load(f)
        with open(os.path.join(ARTIFACTS_DIR, "label_encoder.pkl"), "rb") as f:
            label_encoder = pickle.load(f)
        with open(os.path.join(ARTIFACTS_DIR, "responses.pkl"), "rb") as f:
            responses = pickle.load(f)
        with open(os.path.join(ARTIFACTS_DIR, "config.json"), "r") as f:
            config = json.load(f)
            max_len = config["max_len"]

def get_response(user_msg):
    load_artifacts()
    seq = tokenizer.texts_to_sequences([user_msg.lower()])
    padded = pad_sequences(seq, maxlen=max_len, padding="post")
    pred_probs = model.predict(padded, verbose=0)[0]
    confidence = float(np.max(pred_probs))
    if confidence < CONFIDENCE_THRESHOLD:
        return "Sorry, I didn't understand that."
    intent = label_encoder.inverse_transform([np.argmax(pred_probs)])[0]
    return np.random.choice(responses.get(intent, ["I don't have a response for that."]))
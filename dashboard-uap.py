from io import StringIO
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from transformers import TFBertForSequenceClassification, BertTokenizer
import joblib

@st.cache_resource
def load_resources():
    bilstm_model = tf.keras.models.load_model("./model/BiLSTM.h5")
    bilstm_tokenizer = joblib.load("./model/tokenizerbi.joblib")
    bert_model = TFBertForSequenceClassification.from_pretrained("dhafx/mybert")
    bert_tokenizer = BertTokenizer.from_pretrained("dhafx/mybert")

    return bilstm_model, bilstm_tokenizer, bert_model, bert_tokenizer

bilstm_model, bilstm_tokenizer, bert_model, bert_tokenizer = load_resources()

# Sidebar for viewing model information
selected_content = st.sidebar.selectbox(
    "Pilih", options=["Prediksi", "Informasi Model"]
)

if selected_content == "Prediksi":
    st.title("Klasifikasi Spesialisasi Medis Berdasarkan Transkripsi")
    st.write("Teks akan diprediksi menggunakan model Bi-LSTM dan BERT")
    user_input = st.text_area("Masukkan teks transkripsi:")
    labels = [
    "neurology",
    "neurosurgery",
    "obstetrics gynecology",
    "ophthalmology",
    "orthopedic",
    "pain management",
    "pediatrics neonatal",
    "radiology",
    "surgery",
]
    if st.button("Submit"):
        if user_input.strip():  # Ensure the input is not empty
            col1, col2 = st.columns(2)

            with col1:
                # BiLSTM 
                sequences = bilstm_tokenizer.texts_to_sequences([user_input])
                padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(
                    sequences, maxlen=500
                )
                bilstm_prediction = bilstm_model.predict(padded_sequences)
                bilstm_predicted_label = np.argmax(bilstm_prediction, axis=1)[0]
                bilstm_confidence = np.max(bilstm_prediction) * 100
                bilstm_label = labels[bilstm_predicted_label]  # Map index to label
                st.success(f"Predicted Label (BiLSTM): {bilstm_predicted_label}")
                st.success(f"Medical Specialist (BiLSTM): {bilstm_label}")
                st.write(f"Prediction Confidence (BiLSTM): {bilstm_confidence:.2f}%")
            
            with col2:
                # BERT 
                encoded_input = bert_tokenizer(
                    [user_input],
                    return_tensors="tf",
                    padding=True,
                    truncation=True,
                    max_length=512
                )
                bert_prediction = bert_model(encoded_input)
                bert_logits = bert_prediction.logits
                bert_predicted_label = tf.argmax(bert_logits, axis=1).numpy()[0]
                bert_confidence = tf.nn.softmax(bert_logits).numpy().max() * 100
                bert_label = labels[bert_predicted_label]  # Map index to label
                st.success(f"Predicted Label (BERT): {bert_predicted_label}")
                st.success(f"Medical Specialist (BERT): {bert_label}")
                st.write(f"Prediction Confidence (BERT): {bert_confidence:.2f}%")
        else:
            st.warning("Please enter a transcription before submitting.")    

elif selected_content == "Informasi Model":
    st.title("Informasi Model")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Model BiLSTM")
        string_io = StringIO()
        bilstm_model.summary(print_fn=lambda x: string_io.write(x + "\n"))
        model_summary = string_io.getvalue()
        st.text(model_summary)

        trainable_params_bilstm = np.sum([np.prod(var.shape) for var in bilstm_model.trainable_weights])
        non_trainable_params_bilstm = np.sum([np.prod(var.shape) for var in bilstm_model.non_trainable_weights])
        total_params_bilstm = trainable_params_bilstm + non_trainable_params_bilstm

        st.subheader("Jumlah Parameter BiLSTM")
        st.write(f"**Trainable Parameters:** {trainable_params_bilstm}")
        st.write(f"**Non-trainable Parameters:** {non_trainable_params_bilstm}")
        st.write(f"**Total Parameters:** {total_params_bilstm}")

    with col2:
        st.subheader("Model BERT")
        string_io = StringIO()
        bert_model.summary(print_fn=lambda x: string_io.write(x + "\n"))
        model_summary = string_io.getvalue()
        st.text(model_summary)

        trainable_params_bert = np.sum([np.prod(var.shape) for var in bert_model.trainable_weights])
        non_trainable_params_bert = np.sum([np.prod(var.shape) for var in bert_model.non_trainable_weights])
        total_params_bert = trainable_params_bert + non_trainable_params_bert

        st.subheader("Jumlah Parameter BERT")
        st.write(f"**Trainable Parameters:** {trainable_params_bert}")
        st.write(f"**Non-trainable Parameters:** {non_trainable_params_bert}")
        st.write(f"**Total Parameters:** {total_params_bert}")

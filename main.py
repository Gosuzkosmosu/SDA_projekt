import tkinter as tk
from tkinter import filedialog
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Funkcja do konwersji PDF na obrazy
def convert_pdf_to_image(pdf_path):
    return convert_from_path(pdf_path)

# Funkcja do ekstrakcji tekstu z obrazu
def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

# Funkcja do dzielenia tekstu na fragmenty
def split_into_chunks(text, max_chunk_length=510):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    for word in words:
        if current_length + len(word) + 1 > max_chunk_length:  # +1 for space
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
        else:
            current_chunk.append(word)
            current_length += len(word) + 1  # +1 for space
    chunks.append(" ".join(current_chunk))  # Add the last chunk
    return chunks

# Mapowanie numerów predykcji na etykiety tekstowe
id_to_label = {
    0: 'Lokalowa',
    1: 'Zabudowana',
    2: 'Gruntowa',
    # Dodaj więcej mapowań zgodnie z potrzebami
}

# Funkcja do przetwarzania tekstu i dokonywania predykcji dla każdego fragmentu
def classify_property(text, tokenizer, model):
    chunks = split_into_chunks(text)
    predictions = []
    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors="pt", padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            logits = model(**inputs).logits
        prediction = torch.argmax(logits, dim=-1).item()
        predictions.append(prediction)
    # Agregacja wyników
    final_prediction = max(set(predictions), key=predictions.count)
    # Zamiana numeru predykcji na etykietę tekstową
    final_label = id_to_label[final_prediction]
    return final_label

# Załadowanie tokentyzatora i modelu
tokenizer_name = "dkleczek/bert-base-polish-cased-v1"
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
model_dir = "D:\Miecho\SDAcademy\Projekt\model3\model"
model = AutoModelForSequenceClassification.from_pretrained(model_dir)

def process_file(filepath):
    if filepath.lower().endswith('.jpg'):
        image = Image.open(filepath)
        text = extract_text_from_image(image)
        label = classify_property(text, tokenizer, model)
        result_var.set(f"Predykcja dla obrazu: {label}")
    elif filepath.lower().endswith('.pdf'):
        images = convert_pdf_to_image(filepath)
        all_text = ""
        for image in images:
            text = extract_text_from_image(image)
            all_text += text + " "
        label = classify_property(all_text, tokenizer, model)
        result_var.set(f"Predykcja dla całego dokumentu PDF: {label}")
    else:
        result_var.set("Nieobsługiwany typ pliku.")

def open_file_dialog():
    filepath = filedialog.askopenfilename()
    if filepath:
        process_file(filepath)

# GUI setup
root = tk.Tk()
root.title("Klasyfikator Nieruchomości")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

open_file_btn = tk.Button(frame, text="Otwórz plik (PDF/JPG)", command=open_file_dialog)
open_file_btn.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var)
result_label.pack(pady=10)

root.mainloop()
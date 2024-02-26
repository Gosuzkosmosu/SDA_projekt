import os
import pytesseract
from PIL import Image

def ocr_dla_plikow_w_katalogu(katalog):
    for root, dirs, files in os.walk(katalog):
        for plik in files:
            if plik.endswith('.jpg') or plik.endswith('.pdf'):
                sciezka_do_pliku = os.path.join(root, plik)
                print("Przetwarzanie pliku:", sciezka_do_pliku)
                ocr_do_pliku_tekstowego(sciezka_do_pliku)

def ocr_do_pliku_tekstowego(sciezka_do_pliku):
    try:
        if sciezka_do_pliku.endswith('.pdf'):
            # Jeśli plik to PDF, użyj PIL do konwersji na obraz
            pages = convert_from_path(sciezka_do_pliku, 600)  # 600 to rozdzielczość DPI
            for page_num, image in enumerate(pages):
                parsed_text = pytesseract.image_to_string(image, lang='pol')
                output_file_path = f"{sciezka_do_pliku}_page_{page_num + 1}.txt"
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(parsed_text)
                print("Wynik został zapisany do pliku:", output_file_path)
        else:
            # Jeśli plik to obraz, użyj PIL do wczytania obrazu
            with Image.open(sciezka_do_pliku) as image:
                parsed_text = pytesseract.image_to_string(image, lang='pol')
                output_file_path = f"{sciezka_do_pliku}.txt"
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(parsed_text)
                print("Wynik został zapisany do pliku:", output_file_path)
    except Exception as e:
        print("Wystąpił błąd podczas przetwarzania pliku:", sciezka_do_pliku)
        print("Szczegóły błędu:", e)

# Wywołanie funkcji z podaną ścieżką do katalogu
katalog = r'D:\Miecho\SDAcademy\Projekt\DANE'
ocr_dla_plikow_w_katalogu(katalog)
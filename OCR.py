import os
import requests

def ocr_dla_plikow_w_katalogu(katalog, api_key):
    for plik in os.listdir(katalog):
        if plik.endswith('.jpg'):
            sciezka_do_pliku = os.path.join(katalog, plik)
            print("Przetwarzanie pliku:", sciezka_do_pliku)
            ocr_do_pliku_tekstowego(sciezka_do_pliku, api_key)

def ocr_do_pliku_tekstowego(sciezka_do_pliku, api_key):
    url = 'https://api.ocr.space/parse/image'
    with open(sciezka_do_pliku, 'rb') as file:
        response = requests.post(url,
                                 files={sciezka_do_pliku: file},
                                 data={'apikey': api_key})
        result = response.json()
        print("Odpowiedź z API OCR:", result)  # Dodatkowy komunikat diagnostyczny
        if result['IsErroredOnProcessing']:
            print('Błąd podczas przetwarzania pliku:', sciezka_do_pliku)
            print('Szczegóły błędu:', result.get('ErrorMessage', ''))
            return
        parsed_text = result['ParsedResults'][0]['ParsedText']
        output_file_path = sciezka_do_pliku + '.txt'
        with open(output_file_path, 'w', encoding='utf-8') as output_file:  # Ustawienie kodowania na UTF-8
            output_file.write(parsed_text)
        print("Wynik został zapisany do pliku:", output_file_path)

# Wywołanie funkcji z podaną ścieżką do katalogu oraz kluczem API
katalog = r'D:\Miecho\SDAcademy\Projekt\przyklad'
api_key = 'K89419461388957'
ocr_dla_plikow_w_katalogu(katalog, api_key)


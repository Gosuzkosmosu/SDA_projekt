import pandas as pd
import os

# Ścieżka do pliku CSV
sciezka_do_pliku = r'D:\Miecho\SDAcademy\Projekt\dane.csv'

# Wczytanie danych z pliku CSV do DataFrame
df = pd.read_csv(sciezka_do_pliku, sep=';')  # Ustawienie separatora na średnik

# Dodanie nowej kolumny 'tekst' z wartościami None
df['tekst'] = None

# Funkcja do odczytu zawartości pliku tekstowego
def odczytaj_zawartosc_pliku(sciezka, kodowanie='utf-8'):
    with open(sciezka, 'r', encoding=kodowanie) as plik:
        return plik.read()

# Iteracja po wierszach DataFrame'u
for indeks, wiersz in df.iterrows():
    # Odczytanie wartości z kolumny "Numer sieciowy"
    numer_sieciowy = wiersz['Numer sieciowy']

    # Podzielenie numeru sieciowego na nazwę folderu i nazwę pliku
    nazwa_folderu, nazwa_pliku = numer_sieciowy.split('/')

    # Konstrukcja ścieżki do pliku tekstowego
    sciezka_do_pliku = fr'D:\Miecho\SDAcademy\Projekt\DANE\{nazwa_folderu}\{nazwa_pliku}.txt'

    # Sprawdzenie, czy plik istnieje
    if os.path.exists(sciezka_do_pliku):
        # Odczytanie zawartości pliku tekstowego
        zawartosc = odczytaj_zawartosc_pliku(sciezka_do_pliku)

        # Przypisanie odczytanej zawartości do kolumny 'tekst' w DataFrame
        df.at[indeks, 'tekst'] = zawartosc

# Funkcja do dodania cudzysłowów do wartości w kolumnie 'tekst'
def dodaj_cudzyslowy(tekst):
    if tekst is not None:
        return f'"{tekst}"'
    else:
        return None

# Przypisanie odczytanej zawartości do kolumny 'tekst' w DataFrame
df['tekst'] = df['tekst'].apply(dodaj_cudzyslowy)

print(len(df))
print(df.iloc[0])

# Ścieżka do pliku, w którym chcesz zapisać DataFrame
sciezka_do_zapisu = "D:\Miecho\SDAcademy\Projekt\z_tekstem_cudzyslowy.csv"

# Zapisanie DataFrame do pliku CSV
df.to_csv(sciezka_do_zapisu, index=False)  # index=False zapobiega zapisywaniu indeksów wierszy do pliku CSV


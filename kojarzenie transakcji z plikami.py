import os
import shutil

# Ścieżka do pliku txt
file_path = r"D:\Miecho\SDAcademy\Projekt\numery.txt"
# Ścieżka do katalogu, gdzie mają być tworzone foldery
output_dir = r"D:\Miecho\SDAcademy\Projekt\DANE"
# Ścieżka do katalogu z plikami do skopiowania
source_dir = r"D:\ProNET\Walor\Album"

# Słownik przechowujący ścieżki katalogów dla różnych typów nieruchomości
types_directories = {}


# Funkcja do tworzenia folderów i kopiowania plików
def process_files(file_path, output_dir, source_dir):
    with open(file_path, "r") as file:
        next(file)  # Pominięcie nagłówka
        for line in file:
            typ_nieruchomosci, numer_sieciowy, nazwa_pliku, _ = line.strip().split("\t")
            source_file_path = os.path.join(source_dir, nazwa_pliku)

            if os.path.exists(source_file_path):
                folder_path = os.path.join(output_dir, typ_nieruchomosci, numer_sieciowy)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    print(f"Utworzono katalog dla typu nieruchomości {typ_nieruchomosci}: {folder_path}")

                destination_file_path = os.path.join(folder_path, nazwa_pliku)
                try:
                    shutil.copyfile(source_file_path, destination_file_path)
                    print(f"Plik {nazwa_pliku} skopiowany do {folder_path}")
                except Exception as e:
                    print(f"Wystąpił błąd podczas kopiowania pliku {nazwa_pliku}: {e}")
            else:
                print(f"Nie można odnaleźć pliku {nazwa_pliku} w katalogu źródłowym. Pomijanie...")


# Wywołanie funkcji
process_files(file_path, output_dir, source_dir)
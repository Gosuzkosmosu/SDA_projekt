import os
import shutil


def merge_txt_files(folder_path):
    # Przechodzenie przez wszystkie pliki i podfoldery w danym folderze
    for root, dirs, files in os.walk(folder_path):
        # Sprawdzanie czy istnieją pliki txt w bieżącym folderze
        txt_files = [file for file in files if file.endswith(".txt")]
        if txt_files:
            # Tworzenie nazwy nowego pliku na podstawie nazwy folderu i podfolderu
            new_file_name = os.path.join(root.split(os.sep)[-2], root.split(os.sep)[-1] + ".txt")
            # Ścieżka docelowa nowego pliku
            destination_path = os.path.join(folder_path, new_file_name)

            # Sprawdzenie czy folder docelowy istnieje, jeśli nie, utwórz go
            destination_folder = os.path.dirname(destination_path)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Łączenie zawartości plików txt w jeden plik
            with open(destination_path, "a", encoding="utf-8") as merged_file:
                for file_name in txt_files:
                    file_path = os.path.join(root, file_name)
                    with open(file_path, "r", encoding="utf-8") as file:
                        merged_file.write(file.read())
                        merged_file.write("\n")  # Dodanie nowej linii po każdym pliku


# Ścieżka folderu, który chcesz przeszukać
folder_path = r"D:\Miecho\SDAcademy\Projekt\DANE"

# Wywołanie funkcji łączącej pliki txt
merge_txt_files(folder_path)
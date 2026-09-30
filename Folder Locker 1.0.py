from pathlib import Path
import json
from datetime import datetime
import os
import time
import sys

# Wczytanie konfiguracji
config_path = Path("test/konfiguracja FLa.json")

config = json.loads(
    config_path.read_text(encoding="utf-8")
)

# Pobranie ustawień z konfiguracji
correct_code = config["ustawienia_ogólne"]["kod"]
folder_path = Path(config["ustawienia_ogólne"]["ścieżka"])
warning_file_name = config["ustawienia_logów"]["nazwa_pliku_z_ostrzeżeniem"]

print("-----FOLDER LOCKER 1.0-----")

if config["ustawienia_logów"].get("loguj_gdy_próba_dostępu") == "tak":
    # Zapisywanie daty
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Utworzenie pliku, jeśli nie istnieje
    folder_path.mkdir(parents=True, exist_ok=True)

    # Plik z informacją o próbie dostępu do zablokowanego folderu
    warning_file = folder_path / f"{warning_file_name}"

    # Zapisanie informacji o próbie dostępu do zablokowanego folderu do pliku
    with warning_file.open("a", encoding="utf-8") as file: file.write( f"[{timestamp}] Próba dostępu do zablokowanego folderu\n" )

# Pobranie kodu od użytkownika
code_attempt = input("Wpisz kod: ")

# Sprawdzenie kodu
if code_attempt == correct_code:
    print("Kod poprawny!")

    if config["ustawienia_logów"].get("loguj_gdy_prawidłowy_kod") == "tak":
        
        # Zapisywanie daty
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        # Utworzenie pliku, jeśli nie istnieje
        folder_path.mkdir(parents=True, exist_ok=True)
    
        # Plik z informacją o błędnym kodzie
        warning_file = folder_path / f"{warning_file_name}"
    
        # Zapisanie informacji o niepoprawnym kodzie do pliku
        with warning_file.open("a", encoding="utf-8") as file: file.write( f"[{timestamp}] Wpisano niepoprawny kod: {code_attempt}\n" )

    if config["ustawienia_logów"].get("pytaj_o_wyczyszczenie_logów") == "tak":

        time.sleep(1)  # Odczekaj 1 sekundę

        print("Czy wyczyścić zawartość pliku logów?")
        cleaning_choice = input("tak/nie: ").lower()
        if cleaning_choice == 'tak':
            warning_file.write_text("", encoding="utf-8")

            time.sleep(1)  # Odczekaj 1 sekundę

        print("Zawartość pliku logów została wyczyszczona.")

    time.sleep(1)  # Odczekaj 1 sekundę
    
    print("Otwieranie folderu...")

    time.sleep(1)  # Odczekaj 1 sekundę

    os.startfile(folder_path)

    sys.exit()  # Zakończenie programu po otwarciu folderu
else:
    print("Niepoprawny kod!")

    if config["ustawienia_logów"].get("loguj_gdy_zły_kod") == "tak":
        # Zapisywanie daty
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Utworzenie pliku, jeśli nie istnieje
        folder_path.mkdir(parents=True, exist_ok=True)

        # Plik z informacją o próbie dostępu do zablokowanego folderu
        warning_file = folder_path / f"{warning_file_name}"

        # Zapisanie informacji o niepoprawnym kodzie do pliku
        with warning_file.open("a", encoding="utf-8") as file: file.write( f"[{timestamp}] Wpisano niepoprawny kod: {code_attempt}\n" )
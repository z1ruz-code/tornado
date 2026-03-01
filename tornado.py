import sys
import time
import json
import os
from cryptography.fernet import Fernet
import art

class TornadoApp:
    def __init__(self):
        self.config_file = os.path.join('configuration', 'config.json')
        self.translations_file = os.path.join('configuration', 'translations.json')
        self.load_config()
        self.load_translations()
        self.show_banner()
        self.main_menu()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_terminal_width(self):
        try:
            return os.get_terminal_size().columns
        except OSError:
            return 80

    def center(self, text):
        width = self.get_terminal_width()
        if len(text) >= width:
            return text
        left_pad = (width - len(text)) // 2
        return ' ' * left_pad + text

    def center_input(self, prompt):
        print(self.center(prompt), end=' ')
        return input()

    def load_config(self):
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                self.lang = config.get('language', 'ru')
        except FileNotFoundError:
            self.lang = 'ru'
            self.save_config()

    def save_config(self):
        os.makedirs('configuration', exist_ok=True)
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump({'language': self.lang}, f, ensure_ascii=False, indent=4)

    def load_translations(self):
        try:
            with open(self.translations_file, 'r', encoding='utf-8') as f:
                self.translations = json.load(f)
        except FileNotFoundError:
            print("Error: translations.json file not found in configuration folder.")
            print("Please create it with the necessary translations.")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error: translations.json file contains invalid JSON.")
            sys.exit(1)

    def _(self, key):
        if self.lang in self.translations and key in self.translations[self.lang]:
            return self.translations[self.lang][key]
        if 'ru' in self.translations and key in self.translations['ru']:
            return self.translations['ru'][key]
        return key

    def show_banner(self):
        self.clear_screen()
        banner = art.text2art("TORNADO")
        for line in banner.splitlines():
            print(self.center(line))
        print() 
        print(self.center("by z1ruz-code"))

    def main_menu(self):
        while True:
            print("\n" + self.center("=" * 30))
            print(self.center(self._('main_menu_title')))
            print(self.center("=" * 30))
            print(self.center(f"1. {self._('decrypt')}"))
            print(self.center(f"2. {self._('encrypt')}"))
            print(self.center(f"3. {self._('settings')}"))
            print(self.center(f"4. {self._('exit')}"))

            print()
            choice = self.center_input(self._('choose_action'))

            if choice == "1":
                self.decrypt()
            elif choice == "2":
                self.encrypt()
            elif choice == "3":
                self.settings()
            elif choice == "4":
                self.clear_screen()
                print(self.center(self._('exiting')))
                time.sleep(1)
                sys.exit()
            else:
                print(self.center(self._('invalid_choice')))
                time.sleep(1)

    def decrypt(self):
        self.clear_screen()
        print("\n" + self.center("=" * 30))
        print(self.center(self._('decrypt_title')))
        print(self.center("=" * 30))

        try:
            key = self.center_input(self._('enter_key')).encode()
            token = self.center_input(self._('enter_token')).encode()

            f = Fernet(key)
            decrypted_text = f.decrypt(token)

            print(f"\n{self.center(self._('decrypt_result'))}")
            print("\n" + decrypted_text.decode())

        except Exception:
            print(f"\n{self.center(self._('decrypt_error'))}")
        print()
        self.center_input(self._('press_enter'))
        self.clear_screen()

    def encrypt(self):
        self.clear_screen()
        print("\n" + self.center("=" * 30))
        print(self.center(self._('encrypt_title')))
        print(self.center("=" * 30))

        try:
            text = self.center_input(self._('enter_text')).encode()

            key = Fernet.generate_key()
            f = Fernet(key)
            token = f.encrypt(text)

            print(f"\n{self.center(self._('your_key'))}")
            print("\n" + key.decode())
            print(f"\n{self.center(self._('your_token'))}")
            print("\n" + token.decode())
        except Exception:
            print(f"\n{self.center(self._('encrypt_error'))}")
        print()
        self.center_input(self._('press_enter'))
        self.clear_screen()

    def settings(self):
        while True:
            self.clear_screen()
            print("\n" + self.center("=" * 30))
            print(self.center(self._('settings_title')))
            print(self.center("=" * 30))
            print(self.center(f"1. {self._('change_language')}"))
            print(self.center(f"2. {self._('back')}"))

            print()
            choice = self.center_input(self._('choose_action'))

            if choice == "1":
                self.change_language()
            elif choice == "2":
                self.clear_screen()
                return
            else:
                print(self.center(self._('invalid_choice')))
                time.sleep(1)

    def change_language(self):
        self.load_translations()
        self.clear_screen()
        print("\n" + self.center("=" * 30))
        print(self.center(self._('choose_language')))
        print(self.center("=" * 30))

        languages = list(self.translations.keys())
        for i, lang in enumerate(languages, 1):
            name = self.translations[lang].get('language_name', lang)
            print(self.center(f"{i}. {name}"))
        print(self.center(f"{len(languages)+1}. {self._('back')}"))

        print()
        choice = self.center_input(self._('choose_action'))
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(languages):
                self.lang = languages[choice_num-1]
                self.save_config()
                print(self.center(self._('language_changed')))
                time.sleep(1)
            elif choice_num == len(languages)+1:
                return
            else:
                print(self.center(self._('invalid_language_choice')))
                time.sleep(1)
        except ValueError:
            print(self.center(self._('invalid_language_choice')))
            time.sleep(1)

if __name__ == "__main__":
    app = TornadoApp()

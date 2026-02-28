import sys
import time
import json
import os
from cryptography.fernet import Fernet
import art

class TornadoApp:
    def __init__(self):
        self.config_file = 'config.json'
        self.translations_file = 'translations.json'
        self.load_config()
        self.load_translations()
        self.show_banner()
        self.main_menu()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def load_config(self):
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                self.lang = config.get('language', 'ru')
        except FileNotFoundError:
            self.lang = 'ru'
            self.save_config()

    def save_config(self):
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump({'language': self.lang}, f, ensure_ascii=False, indent=4)

    def load_translations(self):
        try:
            with open(self.translations_file, 'r', encoding='utf-8') as f:
                self.translations = json.load(f)
        except FileNotFoundError:
            print("Ошибка: файл переводов translations.json не найден.")
            print("Пожалуйста, создайте его с необходимыми переводами.")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Ошибка: файл переводов translations.json содержит некорректный JSON.")
            sys.exit(1)

    def _(self, key):
        if self.lang in self.translations and key in self.translations[self.lang]:
            return self.translations[self.lang][key]
        if 'ru' in self.translations and key in self.translations['ru']:
            return self.translations['ru'][key]
        return key

    def show_banner(self):
        art.tprint("TORNADO")

    def main_menu(self):
        while True:
            print("\n" + "="*30)
            print(self._('main_menu_title').center(30))
            print("="*30)
            print(f"1. {self._('decrypt')}")
            print(f"2. {self._('encrypt')}")
            print(f"3. {self._('settings')}")
            print(f"4. {self._('exit')}")

            choice = input(f"\n{self._('choose_action')}")

            if choice == "1":
                self.decrypt()
            elif choice == "2":
                self.encrypt()
            elif choice == "3":
                self.settings()
            elif choice == "4":
                self.clear_screen()
                print(self._('exiting'))
                time.sleep(1)
                sys.exit()
            else:
                print(self._('invalid_choice'))
                time.sleep(1)

    def decrypt(self):
        self.clear_screen()
        print("\n" + "="*30)
        print(self._('decrypt_title').center(30))
        print("="*30)

        try:
            key = input(self._('enter_key')).encode()
            token = input(self._('enter_token')).encode()

            f = Fernet(key)
            decrypted_text = f.decrypt(token)

            print(f"\n{self._('decrypt_result')}")

            print("\n"+decrypted_text.decode())

        except Exception as e:
            print(f"\n{self._('decrypt_error')}")
        input(f"\n{self._('press_enter')}")
        self.clear_screen()

    def encrypt(self):
        self.clear_screen()
        print("\n" + "="*30)
        print(self._('encrypt_title').center(30))
        print("="*30)

        try:
            text = input(self._('enter_text')).encode()

            key = Fernet.generate_key()
            f = Fernet(key)
            token = f.encrypt(text)

            print(f"\n{self._('your_key')}")
            print("\n"+ key.decode())
            print(f"\n{self._('your_token')}")
            print("\n"+token.decode())
        except Exception as e:
            print(f"\n{self._('encrypt_error')}")
        input(f"\n{self._('press_enter')}")
        self.clear_screen()

    def settings(self):
        while True:
            self.clear_screen()
            print("\n" + "="*30)
            print(self._('settings_title').center(30))
            print("="*30)
            print(f"1. {self._('change_language')}")
            print(f"2. {self._('back')}")

            choice = input(f"\n{self._('choose_action')}")

            if choice == "1":
                self.change_language()
            elif choice == "2":
                return
            else:
                print(self._('invalid_choice'))
                time.sleep(1)

    def change_language(self):
        self.load_translations()
        self.clear_screen()
        print("\n" + "="*30)
        print(self._('choose_language').center(30))
        print("="*30)

        languages = list(self.translations.keys())
        for i, lang in enumerate(languages, 1):
            name = self.translations[lang].get('language_name', lang)
            print(f"{i}. {name}")
        print(f"{len(languages)+1}. {self._('back')}")

        choice = input(f"\n{self._('choose_action')}")

        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(languages):
                self.lang = languages[choice_num-1]
                self.save_config()
                print(self._('language_changed'))
                time.sleep(1)
            elif choice_num == len(languages)+1:
                return
            else:
                print(self._('invalid_language_choice'))
                time.sleep(1)
        except ValueError:
            print(self._('invalid_language_choice'))
            time.sleep(1)

if __name__ == "__main__":
    app = TornadoApp()
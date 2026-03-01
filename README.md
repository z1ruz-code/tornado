<div align="center">
  <h1>🌪️ Tornado</h1>
  <p><strong>A Python tool for encrypting and decrypting messages with multilingual support.</strong></p>
  <p>
    <img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python version">
    <img src="https://img.shields.io/github/license/z1ruz-code/tornado" alt="License">
  </p>
</div>

---

## 📖 About

**Tornado** is a command-line utility designed to provide a simple yet secure way to encrypt and decrypt text messages. Its key feature is its multilingual support, allowing users from different linguistic backgrounds to interact with the tool in their native language.

The encryption process generates two crucial components: a **key** and a **token**. Both are required to successfully decrypt a message, adding an extra layer of security.

## ✨ Features

*   **🔐 Secure Encryption/Decryption:** Protect your messages with a dual-component system (key + token).
*   **🌍 Multilingual Interface:** Interact with Tornado in your preferred language. New languages can be added easily via a `translations.json` file.
*   **💻 Easy to Use:** Simple command-line interface for quick encryption and decryption tasks.
*   **🔄 Auto-Update Check:** The tool includes a module (`CheckingForUpdates.py`) to check for new versions.

## 🚀 Getting Started

Follow these simple steps to install and run Tornado on your local machine.

### Prerequisites

*   **Python:** Version 3.6 or higher must be installed on your system.
*   **Git (Optional):** To clone the repository, but you can also download it directly as a ZIP file.

### Installation & Setup

1.  **Get the Code**
    *   **Option A: Clone the repository (recommended)**
        ```bash
        git clone https://github.com/z1ruz-code/tornado.git
        cd tornado
        ```
    *  **Option B: Download manually**
Download the source code from the [release page](https://github.com/z1ruz-code/tornado/releases/latest) and extract the ZIP file. Then, open your terminal or command prompt and navigate into the extracted `tornado` folder.

2. **Install Dependencies**
*  Tornado requires a few Python libraries. Install them using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**
*  Once the dependencies are installed, you can start Tornado:
   ```bash
   python tornado.py
   ```
## 🛠️ How to Use

1. Upon running `python tornado.py`, the program will start in your terminal.

2. To Encrypt: Choose the encrypt option and enter your message. The tool will output a key and a token.
> Important: Save both the key and the token in a secure place immediately. You will need both to decrypt the message.

3. To Decrypt: Choose the decrypt option, then provide the previously generated key and token. The original message will be displayed.

## 🌐 Adding a New Language

Tornado's multilingual support is managed through the translations.json file. This file contains all the text strings used by the program, organized by language.

To add your own language:

1. Open the translations.json file.

2. Find the language codes (e.g., "en" for English). Create a new entry with your desired language code (e.g., "es" for Spanish, "fr" for French).

3. Translate all the text strings (the values on the right) into your language, keeping the keys (the text on the left) exactly the same.

4. Save the file. The next time you run Tornado, it should detect and allow you to use the new language, depending on how language selection is implemented .

## 📁 Project Structure
- `tornado.py`: The main script to run the application.

- `CheckingForUpdates.py`: A module to check for newer versions of Tornado.

- `config.json`: Configuration file for the tool (purpose to be detailed by the author).

- `translations.json`: Contains all text strings for multilingual support.

- `requirements.txt`: Lists the Python dependencies needed for the project.

- `LICENSE`: The license file for the project.

## ⭐ Support
If you find this tool useful, please consider giving it a star on GitHub! Your support is appreciated.

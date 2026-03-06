import json
import os
import requests
from packaging.version import Version


CONFIG_PATH = os.path.join(os.path.dirname(__file__), "configuration", "config.json")

def get_current_version():
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config.get("version")
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return None

def get_latest_release():
    url = "https://api.github.com/repos/z1ruz-code/tornado/releases/latest"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        tag = data.get("tag_name", "")
        return tag.lstrip('v')
    except requests.exceptions.RequestException:
        return None

def check_version():

    current = get_current_version()
    latest = get_latest_release()

    print(f"Current version: {current if current else 'unknown'}")
    print(f"Latest version: {latest if latest else 'unknown'}")

    if current and latest:
        try:
            if Version(latest) > Version(current):
                print("A new version is available!")
                return current, latest, True
            else:
                print("You are using the latest version.")
                return current, latest, False
        except Exception:
            print("Could not compare versions (invalid format).")
            return current, latest, None
    else:
        print("Could not retrieve version information.")
        return current, latest, None

if __name__ == "__main__":
    check_version()

import requests
from packaging.version import Version

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

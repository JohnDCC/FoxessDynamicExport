import hashlib
import time
import requests
import json
import sys

TOKEN = "YOUR_API"
SN = "YOUR_INVERTER_SERIAL"
URL_PATH = "/op/v0/device/setting/set"
FULL_URL = f"https://www.foxesscloud.com{URL_PATH}"

# Look for an input value passed from Home Assistant (e.g., sys.argv[1])
# Default back to '150' if called without arguments
try:
    target_watts = str(sys.argv[1])
except IndexError:
    target_watts = "150"

timestamp = str(int(time.time() * 1000))

# The working escape signature rule we unlocked
sig_string = f"{URL_PATH}\\r\\n{TOKEN}\\r\\n{timestamp}"
signature = hashlib.md5(sig_string.encode('utf-8')).hexdigest().lower()

headers = {
    "token": TOKEN,
    "timestamp": timestamp,
    "signature": signature,
    "lang": "en",
    "Content-Type": "application/json"
}

payload = {
    "sn": SN,
    "key": "ExportLimit",
    "value": target_watts
}

try:
    response = requests.post(FULL_URL, headers=headers, json=payload, timeout=10)
    print(response.text)
except Exception as e:
    print(f"Error: {e}")

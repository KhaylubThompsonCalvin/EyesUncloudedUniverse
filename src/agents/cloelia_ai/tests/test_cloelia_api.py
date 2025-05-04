# =====================================================
# Cloelia API Test Client – EyesUnclouded Frontend
# Description: Sends emotion to Cloelia FastAPI backend
# File: tests/test_cloelia_api.py
# Author: Khaylub Thompson-Calvin
# =====================================================

import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

API_KEY = os.getenv("CLOELIA_API_KEY")
if not API_KEY:
    print("❌ CLOELIA_API_KEY not found in .env file.")
    exit()

url = "https://cloeliaai.onrender.com/analyze-emotion"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
payload = { "emotion": "focus" }

try:
    response = requests.post(url, headers=headers, json=payload)
    print("✅ Status Code:", response.status_code)
    print("🧠 Response JSON:", response.json())
except Exception as e:
    print("❌ Request Error:", str(e))

# EyesUnclouded Universe Gateway
# File: database.py
# Project: Atlas Signature Gateway Interface
# Author: Khaylub Thompson-Calvin
# Date: 5/1/2025
# Description:
# This script verifies database connectivity for the EyesUnclouded Universe Gateway,
# the primary entrypoint in the symbolic architecture of perception-aware AI systems.
# It loads secure variables from the .env file and connects to the MongoDB Atlas cloud.
#
# Primary Goals:
# - Validate that the MongoDB Atlas cluster is reachable
# - Log the active database name and all visible collections
# - Confirm all required .env secrets are present
# - Provide a simple terminal check to confirm the data gateway is online
#
# Symbolic Context:
# In the broader Atlas Signature system, this database module acts as the "Root Perception Lens."
# It verifies that the digital nervous system (CloeliaAI, Role Engines, Virtue Nodes, Legacy Vaults)
# can access and transmit data securely. It is the first verification check for symbolic integrity.
#
# Expected .env Configuration:
# DB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/eyes_unclouded
# SECRET_KEY=<flask_secret_key>
# OPENAI_KEY=<api_key>
# ELEVENLABS_KEY=<api_key>
# CLOELIA_API_KEY=<api_key>
# ALGORITHM_KEY=<internal_algorithm_key>
#
# References:
# - MongoDB Atlas: https://cloud.mongodb.com/
# - Pymongo: https://pymongo.readthedocs.io/
# - Python Dotenv: https://pypi.org/project/python-dotenv/
# -------------------------------------------------------------

import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pprint import pprint

# Load environment variables from .env
load_dotenv()

# Define required keys for security audit
required_keys = [
    "DB_URI", "SECRET_KEY", "OPENAI_KEY",
    "ELEVENLABS_KEY", "CLOELIA_API_KEY", "ALGORITHM_KEY"
]

print("\nChecking Environment Keys:")
for key in required_keys:
    value = os.getenv(key)
    if value:
        print(f"  {key}: [OK]")
    else:
        print(f"  {key}: [MISSING]")

# Attempt to connect to MongoDB
try:
    client = MongoClient(os.getenv("DB_URI"))
    db = client.get_database()
    print("\nConnection Successful")
    print(f"  Connected Database: {db.name}")
    print("  Available Collections:")
    pprint(db.list_collection_names())
except Exception as e:
    print("\nConnection Failed:", str(e))



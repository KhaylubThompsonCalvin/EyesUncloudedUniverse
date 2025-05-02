EyesUnclouded Universe Gateway
# File: main.py
# Project: Atlas Signature Gateway Interface
# Author: Khaylub Thompson-Calvin
# Date: 5/1/2025
# Description:
# This is the central API gateway for the EyesUnclouded Universe architecture. It acts as the symbolic
# and service-entry point for multiple perception-aware systems, including EyesUnclouded.ai and CloeliaAI.
#
# Features:
# - Connects to MongoDB Atlas cloud for data services
# - Loads environmental secrets from .env
# - Provides a root route for verifying gateway status
# - Designed as the first interface layer in the Entity-Relationship Design (ERD) structure
# - Will evolve to handle routing logic to all symbolic agents, microservices, and modules
#
# Symbolic Role:
# This Gateway represents the "Door of Perception" in the EyesUnclouded knowledge system. All agents,
# data pipelines, and reflection mechanisms pass through this node, making it both a literal and philosophical
# entry point into the perception-based AI logic web.
#
# Source References:
# - Flask documentation: https://flask.palletsprojects.com/
# - MongoDB Atlas connection methods
# - Project memory structure: Atlas Signature Scaffold Plan
# -------------------------------------------------------------------------------

from flask import Flask
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# MongoDB connection (prints DB name to confirm it works)
client = MongoClient(os.getenv("DB_URI"))
db = client.get_database()

@app.route("/")
def home():
    """Root route for checking server and DB status."""
    return f"\U00002705 Atlas Gateway is active. Connected to MongoDB: {db.name}"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
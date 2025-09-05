import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access MongoDB URI
MONGO_URI = os.getenv("CONNECTION_URL")

print(MONGO_URI)

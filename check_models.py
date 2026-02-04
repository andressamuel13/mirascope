from dotenv import load_dotenv
import os
from google.genai import Client

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(f"API Key found: {bool(api_key)}")

try:
    client = Client(api_key=api_key)
    # Note: Method name might vary based on SDK version (list_models vs models.list)
    # provider.py showed: client.models.generate_content
    # Let's try to find list method. Usually client.models.list()
    if hasattr(client, 'models') and hasattr(client.models, 'list'):
        print("Listing models...")
        for m in client.models.list():
            print(f"Model: {m.name}")
    else:
        print("Could not find models.list method on client.")
        print(dir(client))
except Exception as e:
    print(f"Error: {e}")

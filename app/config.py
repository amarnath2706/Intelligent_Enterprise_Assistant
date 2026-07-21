import os 
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file  

class Settings:

   GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
   QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
   QDRANT_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT")
   QDRANT_COLLECTION = "enterprise_assistant_collection" #name of the collection in qdrant database
   GROQ_API_KEY = os.getenv("GROQ_API_KEY")
   GROQ_MODEL = "llama-3.3-70b-versatile"
   GROQ_SLUG = "gqgateway"
   GROQ_SLUG_2 = "gqgateway1"
   PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")  # Set Portkey API key in environment
   #GROQ_FALLBACK_API_KEY = os.getenv("GROQ_FALLBACK_API_KEY")  # Optional fallback API

settings = Settings()
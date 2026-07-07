import time
import logfire
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import settings


#Define some variables
BATCH_SIZE = 50
_GEMINI_DIM = 3072
_FALLBACK_DIM = 768 #Fallback model for embeddings - "all-mpnet-base-v2"
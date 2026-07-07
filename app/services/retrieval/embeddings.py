import time
import logfire
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import settings


#Define some variables
BATCH_SIZE = 50
_GEMINI_DIM = 3072
_FALLBACK_DIM = 768 #Fallback model for embeddings - "all-mpnet-base-v2"

_activ_model = None
_model_type: str | None = None

def _probe_gemini():
    """"Try a embed call to verify whether the Gemini is reachable.Returns model or None. It is a kind of health call to check if the Gemini API is reachable and working."""
    try:
        model = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-2-preview",
            google_api_key=settings.GEMINI_API_KEY,
        )
        model.embed_query("probe")
        logfire.info("Gemini embeddings ready (gemini-embedding-2-preview, 3072-dim).")
        return model
    except Exception as e:
        logfire.warning(f"Gemini probe failed: {e}. Will use sentence-transformers fallback.")
        return None
    
def _load_fallback():
    from sentence_transformers import SentenceTransformer
    logfire.info("Loading sentence-transformers fallback (all-mpnet-base-v2, 768-dim).")
    return SentenceTransformer("all-mpnet-base-v2")
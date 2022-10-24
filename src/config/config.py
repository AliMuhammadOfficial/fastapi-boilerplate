from src.utils.config import config
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app_name = config("APP_NAME", "FastAPI Boilerplate")
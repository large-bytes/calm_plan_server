import os
from pathlib import Path
from dotenv import load_dotenv

# Determine environment
ENV = os.getenv("FASTAPI_ENV", "development")

# Load the appropriate .env file
env_file = Path(f".env.{ENV}")
load_dotenv(dotenv_path=env_file)


# Configuration class
class Settings:
	ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
	SUPABASE_URL: str = os.getenv("SUPABASE_URL")
	SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

# Add other configuration settings as needed


# Create settings instance
settings = Settings()
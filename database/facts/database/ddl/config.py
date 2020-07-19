from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

db_path = os.getenv("DB_PATH")
db_pass = os.getenv("DB_PASS")
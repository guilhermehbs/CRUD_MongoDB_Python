from dotenv import load_dotenv
import os
load_dotenv()

mongo_db_infos = {
    "host": os.getenv("HOST"),
    "port": os.getenv("PORT"),
    "db_name": os.getenv("DB_NAME")
}
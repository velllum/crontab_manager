import os

from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


load_dotenv()


engine = create_engine(os.getenv("URL_DB"))
Session = sessionmaker(engine)
session = Session()



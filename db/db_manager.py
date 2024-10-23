from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from neurons.utils.get_pg_url import get_postgres_url

Base = declarative_base()

class PromptsTable(Base):
    __tablename__ = 'promptstable'
    timestamp = Column(String, primary_key = True)
    miner_uid = Column(Integer)
    input_data = Column(String)
    task_type = Column(String)
    source_language = Column(String)
    target_language = Column(String)
    miner_response = Column(String)
    text_score = Column(Float)
    rms_score = Column(Float)
    snr_score = Column(Float)
    overall_score = Column(Float)
    module_name = Column(String)

class DBManager:
    def __init__(self, url = get_postgres_url()) -> None:
        self.engine = create_engine(url)
        self.Session = sessionmaker(bind = self.engine)

        Base.metadata.create_all(self.engine)
    
    def add_entry(self, miner_uid, input_data, task_type, source_language, target_language, miner_response, text_score, rms_score, snr_score, overall_score, module_name):
        timestamp = datetime.now().timestamp()
        new_entry = PromptsTable(timestamp = timestamp, miner_uid = miner_uid, input_data = input_data, task_type = task_type, 
                                 source_language = source_language, target_language = target_language, miner_response = miner_response, 
                                 text_score = text_score, rms_score = rms_score, snr_score = snr_score, overall_score = overall_score, 
                                 module_name= module_name)
        with self.Session() as session:
            session.add(new_entry)
            session.commit()
from django.apps import AppConfig
from pymongo import MongoClient
import os
from dotenv import load_dotenv
# 在應用關閉時關閉 MongoDB 連接
import atexit

# 讀取 .env 檔案
load_dotenv()

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    def ready(self):
        # 在應用啟動時建立 MongoDB 連接
        self.mongodb_client = MongoClient(os.getenv("MONGO_URL"))
        self.database = self.mongodb_client[os.getenv("MONGO_DB")]
        print("==========Connected to MongoDB!==========")
        # 註冊關閉連接的信號
        atexit.register(self.shutdown_db_client)

    def shutdown_db_client(self):
        # 關閉 MongoDB 連接
        if hasattr(self, 'mongodb_client'):
            self.mongodb_client.close()
            print("==========Disconnected from MongoDB!==========")

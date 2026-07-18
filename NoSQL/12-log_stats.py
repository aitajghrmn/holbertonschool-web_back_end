#!/usr/bin/env python3
"""
MongoDB-də saxlanılan Nginx loqları haqqında statistika təqdim edən skript.
"""
from pymongo import MongoClient


def log_stats():
    """
    Nginx kolleksiyasındakı sənədlərin sayını, metodları və
    status check sayını hesablayıb çap edir.
    """
    # MongoDB bağlantısını qururuq
    client = MongoClient('mongodb://127.0.0.1:27017')
    # logs verilənlər bazasının nginx kolleksiyasını seçirik
    nginx_collection = client.logs.nginx

    # 1. Ümumi loqların sayı
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. HTTP Metodlarının statistikası
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Status check sayı (həm GET metodu, həm də /status path-i olmalıdır)
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()

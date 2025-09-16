import random

def create_header():
    return {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11{random.randint(0, 9)}.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
    }
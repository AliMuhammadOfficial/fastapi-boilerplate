import os

def config(value: str, default=""):
    return os.getenv(value, default)
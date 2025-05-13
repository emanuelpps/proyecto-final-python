from functools import wraps
import requests

class LoggerObserver:
    def update(self, message):
        print(f"[LOG]: {message}")
        try:
            requests.post("http://localhost:9090", json={"message": message})
        except Exception as e:
            print(f"[ERROR AL ENVIAR LOG]: {e}")

class LoggerSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

logger = LoggerSubject()
logger.attach(LoggerObserver())

def log_action(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logger.notify(f"{func.__name__} fue ejecutado")
            return result
        return wrapper
    return decorator
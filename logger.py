from functools import wraps
import requests
import datetime

# Patrón Observador


class Observer:
    def update(self, message):
        raise NotImplementedError(
            "El observer debe implementar el método update()")


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Observers


class ConsoleLogger(Observer):
    def update(self, message):
        print(f"[CONSOLE LOG] {datetime.datetime.now()}: {message}")


class FileLogger(Observer):
    def update(self, message):
        with open("logs_observer.txt", "a", encoding="utf-8") as f:
            f.write(f"[FILE LOG] {datetime.datetime.now()}: {message}\n")


class ServerLogger(Observer):
    def update(self, message):
        try:
            requests.post("http://localhost:9090", json={"message": message})
        except Exception as e:
            print(f"[SERVER LOG ERROR] {e}")

# Conf del Subject


logger_subject = Subject()
logger_subject.attach(ConsoleLogger())
logger_subject.attach(FileLogger())
logger_subject.attach(ServerLogger())


# Decorador
def log_action(logger: Subject):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logger.notify(
                f"{func.__name__} fue ejecutado con args: {args}, kwargs: {kwargs}")
            return result
        return wrapper
    return decorator

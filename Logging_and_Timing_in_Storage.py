from abc import ABC, abstractmethod
from time import perf_counter,sleep

#data - переменная в которой будут храниться данные от файла - name_file

def log_execution(method_class):
    def wrapper(*args):
        print(f"Запуск {method_class.__name__}.")
        return method_class(*args)
    return wrapper


def track_time(method_class):
    def wrapper(*args):
        start = perf_counter()
        method = method_class(*args)
        session = perf_counter() - start
        print(f"{method_class.__name__} сессия составила {session}.")
        return method
    return wrapper


class Storage(ABC):
    @abstractmethod
    def save(self,name_file,data):
        pass


class LocalStorage(Storage):
    @log_execution
    @track_time
    def save(self,name_file,data):
        with open(name_file) as file:
            file.write(data)
        print(f"File {name_file} successfully saved to variable {data}.")


class CloudStorage(Storage):
    @log_execution
    @track_time
    def save(self,name_file,data):
        sleep(2) # типо файл загружен в облако
        print(f"File {name_file} successfully loaded in cloud storage.")

import time
from colorama import Fore


def measure_time(func):
    def wrapper(self, *args, **kwargs):
        start_time = time.perf_counter()
        result = func(self, *args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        class_name = self.__class__.__name__
        print("Class " + Fore.GREEN + f"'{class_name}'" + Fore.RESET + " - Method " + Fore.GREEN + f"'{func.__name__}'" + Fore.RESET + "executed in " + Fore.RED + f"{elapsed_time:.8f}" + Fore.RESET + " seconds.")
        return result
    return wrapper
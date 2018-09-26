import psutil


def find_processes(name):
    return [proc for proc in psutil.process_iter() if proc.name() == name]



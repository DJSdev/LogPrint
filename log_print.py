import time


py_print = print
file_name = time.strftime("%Y%m%d-%H%M%S")

def log(msg):
    with open(f'{file_name}.txt', "a+") as file:
        file.write(msg)

def print(var):
    py_print(var)
    try:
        log(str(var) + "\r\n")
    except Exception as e:
        py_print(e)
        raise e

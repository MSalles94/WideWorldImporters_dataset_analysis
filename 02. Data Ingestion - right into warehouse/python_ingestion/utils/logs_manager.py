import logging
import datetime
import os

def map_log_folder():
    # create a folder for log files
    log_version=f"{str(datetime.datetime.today()).replace(' ','_').replace(':','-')[:-10]}"
    log_folder_path =f"./output/log_{log_version}"
    os.mkdir(log_folder_path)
    #define a func to build the log_file_path
    log_file_path =lambda  log_file: f"{log_folder_path}/{log_file}.log"

    return log_file_path



def define_log(process_name,log_file_path='./test_output'):
    #func to create a log element
    logger = logging.getLogger(process_name)
    logger.setLevel(logging.INFO)

    # clean old handlers
    logger.handlers.clear()

    file_handler = logging.FileHandler(log_file_path(process_name))
    stream_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
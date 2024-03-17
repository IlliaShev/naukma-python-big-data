import pandas as pd


def console_input():
    """
    This function read user's input from console
    :return: user's input
    """
    return input("Input: ")


def file_input(path):
    """
    This function read file using python builtin functions
    :param path: path to file
    :return file content
    """
    with open(path, "r") as file:
        return file.read()


def file_input_pandas(path) -> pd.DataFrame:
    """
    This function read csv file using pandas
    :param path: path to file
    :return file content
    """
    return pd.read_csv(path)

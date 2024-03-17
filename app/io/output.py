def console_write(output):
    """
    This function writes output to the console
    :param output: text to write to the console
    """
    print(output)


def file_write(path, output):
    """
    This function writes output to the file
    :param path: path to the file
    :param output: output to write to the file
    """
    with open(path, 'w') as f:
        f.write(output)

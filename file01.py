def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, 'r')
    s = f.read()

    numbers = s.split(',')

    return numbers

# Read data from file
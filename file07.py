def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """

    n = 0
    for i in data:
        if i.isdigit():
            n += int(i)

    return n
    
# Read data from file
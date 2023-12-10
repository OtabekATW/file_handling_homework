def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, 'r')
    s = f.read()

    list1 = []
    for i in s:
        if i.isdigit():
            list1.append(i)

    return list1

# Read data from file

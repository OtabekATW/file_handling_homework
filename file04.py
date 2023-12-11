def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    list1 = []
    for i in data:
        if not i.isdigit():
            list1.append(i)
    
    return list1
    
# Read data from file

def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

    list1 = []
    for i in data:
        if i.isdigit():
            list1.append(int(i))
    
    return min(list1)

# Read data from file
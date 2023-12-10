def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data, 'r')
    s = f.read()

    list1 = s.split('\n')
    
    mx = len(list1[0])
    for i in list1:
        if mx < len(i):
            mx = len(i)

    return mx

# Read data from file
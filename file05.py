def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, 'r')
    s = f.read()
    
    list1 = []
    list2 = []
    for i in s:
        if i.isdigit():
            list1.append(i)
        else:
            list2.append(i)
    return [len(list1), len(list2)]
    
# Read data from file
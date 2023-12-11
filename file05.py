def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    list1 = []
    list2 = []
    for i in data:
        if i.isdigit():
            list1.append(i)
        else:
            list2.append(i)
    return [len(list1), len(list2)]
    
# Read data from file
f = open('data/data05.txt')
print(main(f.read()))
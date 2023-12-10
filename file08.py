def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data, 'r')
    s = f.read()
    list1 = s.split()

    for i in list1:
        if i.isalpha():
            list1.remove(i)
    
    list2 = []
    for i in list1:
        list2.append(float(i))
    
    return max(list2)

# Read data from file
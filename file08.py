def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

    list1 = data.split()

    for i in list1:
        if i.isalpha():
            list1.remove(i)
    
    list2 = []
    for i in list1:
        list2.append(i)
    
    return max(list2)

# Read data from file
def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

    #list1 = data.split()

    for i in data:
        if i.isalpha():
            data.remove(i)
    
    list1 = []
    for i in data:
        list1.append(i)
    
    return min(list1)

# Read data from file
f = open('data/data09.txt')
print(main(f.read()))
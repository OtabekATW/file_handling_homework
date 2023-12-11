def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    language = data.split()

    list1 = []
    for i in language:
        list1.append(len(i))
    
    return list1
    
# Read data from file
f = open('data/data06.txt')
print(main(f.read()))
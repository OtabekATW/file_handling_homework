def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list1 = data.split('\n')

    mx = len(list1[0])
    for i in list1:
        if mx < len(i):
            mx = len(i)

    return mx

# Read data from file
f = open('data/data10.txt')
print(main(f.read()))
def findMax( elements : list, start : int = 0, end : int = -1) -> int:
    max_element : int = elements[0]

    if end == -1:
        end = len(elements)

    for i in range(start,end):
        
        if elements[i] > max_element:
            max_element = elements[i]
        
    return max_element

# Main

data : list = [1,2,10,4,5]

print(findMax(data))

            



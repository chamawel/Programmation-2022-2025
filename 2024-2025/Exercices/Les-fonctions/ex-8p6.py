def findHighestValIndex(data : list) -> float:
    max_val = data[0]

    for index in range(len(data)):
        
        if data[index] > max_val:
            max_val = data[index]
            found_at = index
    
    return found_at

# Main
values  : list = [5, 8, 2, 1, 9, 3, 6, 4]

print(findHighestValIndex(values))
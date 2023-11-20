while True:
    n_u = int(input("donner un nombre"))
    n_u10plus = n_u + 10

    while n_u < n_u10plus:
        n_u += 1
        print(n_u)
    
    isexiting = input("partir ? (Y/N)")

    if isexiting == "Y" or isexiting =="y":
        exit("Closing program") 
    else:
        print("continuing")
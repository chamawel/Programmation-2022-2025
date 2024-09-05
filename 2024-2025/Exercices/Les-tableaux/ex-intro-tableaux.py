# n_student       : int = int(input("Cmb,d'éleves?: "))

# if n_student < 30:    
#     phone_age       : int = int(input("Premier élève: "))
#     current_student : int = 0
    
#     list_of_ages    : list = [0] * n_student
#     list_of_ages[current_student] = phone_age

#     while current_student <= n_student:
#         phone_age         = int(input("Premier élève: "))
#         current_student  += 1
#         list_of_ages[current_student] = phone_age
#         print(list_of_ages)    

# else:
#     print("Trop d'élèves")

# list.index 


n_student       : int = int(input("Cmb,d'éleves?: "))



if n_student < 30:    
    phone_age       : int = int(input("Premier élève: "))
    current_student : int = 1
    sum             : int = phone_age

    while current_student < n_student:
        phone_age        = int(input("élève Suivant: "))
        current_student  += 1
        sum             += phone_age

    print(f"la moyenne { sum/n_student:.2f}")

else:
    print("Trop d'élèves")
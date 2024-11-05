days            : list = [31,28,31,30,31,30,31,31,30,31,30,31]
months          : list = ['Janvier','Février','Mars','Avril','Mai','Juin','Julliet','Aout','Septembre','Octobre','Novembre','Décembre']
days_and_months : list = [0] * 24


for i in range(len(days_and_months)):
    if i%2 == 0:
        days_and_months[i] = months[]
        

    elif i%2 !=0:
        days_and_months[i] = days[]
    
        
print(days_and_months)
days            : list = [31,28,31,30,31,30,31,31,30,31,30,31]
months          : list = ['Janvier','Février','Mars','Avril','Mai','Juin','Julliet','Aout','Septembre','Octobre','Novembre','Décembre']
days_and_months : list = [0] * 24


for i in range(12):
    days_and_months[i * 2] = months[i]
    days_and_months[i * 2 + 1]     = days[i]


    

print(days_and_months)
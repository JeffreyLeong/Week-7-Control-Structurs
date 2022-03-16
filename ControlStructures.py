vaccinationNames = ['pfizer-alpha', 'moderna-alpha', 'johnson-alpha', 'pfizer-kappa', 'pfizer-omega', 'moderna-delta', 'moderna-gamma', 'moderna-zeta'] 

name = input("Please enter your name: ")
age = input("Please enter your age: ")
medicalCondition = input("Do you have a medical condition?: ")
teacher = input("Are you a teacher?: ")

if ((age >= str(65)) and (medicalCondition == 'yes') and (teacher == 'yes')):
    print("You are eligible for a booster vaccination.")
else:
    print("You are not eligble for a booster vaccination.")
    quit()

for vaccine in vaccinationNames:
    print(vaccine)



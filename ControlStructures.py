vaccinationNames = ['pfizer-alpha', 'moderna-alpha', 'johnson-alpha', 'pfizer-kappa', 'pfizer-omega', 'moderna-delta', 'moderna-gamma', 'moderna-zeta'] 

question1 = input("Please enter your name: ")
question2 = input("Please enter your age: ")
question3 = input("Do you have a medical condition?: ")
question4 = input("Are you a teacher?: ")

if ((question2 >= str(65)) and (question3 == 'yes') and (question4 == 'yes')):
    print("You are eligible for a booster vaccination.")
else:
    print("You are not eligble for a booster vaccination.")
    quit()

for vaccine in vaccinationNames:
    print(vaccine)



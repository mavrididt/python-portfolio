
# ΑΣΚΗΣΗ 3: Παιχνίδι Πέτρα-Ψαλίδι-Χαρτί

import random

print("Παιχνίδι: Πέτρα - Ψαλίδι - Χαρτί")
user_choice = input("Διάλεξε (πέτρα / ψαλίδι / χαρτί): ").lower()

# Υπολογιστής διαλέγει τυχαία
choices = ["πέτρα", "ψαλίδι", "χαρτί"]
computer_choice = random.choice(choices)

print("Ο υπολογιστής διάλεξε:", computer_choice)

# Έλεγχος αποτελέσματος
if user_choice == computer_choice:
    print("Ισοπαλία!")
elif (user_choice == "πέτρα" and computer_choice == "ψαλίδι") or      (user_choice == "ψαλίδι" and computer_choice == "χαρτί") or      (user_choice == "χαρτί" and computer_choice == "πέτρα"):
    print("Κέρδισες!")
elif user_choice in choices:
    print("Έχασες!")
else:
    print("Μη έγκυρη επιλογή.")

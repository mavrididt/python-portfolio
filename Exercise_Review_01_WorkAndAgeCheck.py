
# Άσκηση Εξάσκησης 01: Έλεγχος ετών εργασίας και ηλικίας

while True:
    try:
        age = int(input("Γράψε την ηλικία σου: "))
        break
    except ValueError:
        print("Παρακαλώ γράψε έναν αριθμό για ηλικία!")

while True:
    try:
        year_of_work = int(input("Πόσα χρόνια δουλεύεις: "))
        break
    except ValueError:
        print("Παρακαλώ γράψε έναν αριθμό για χρόνια εργασίας!")

if year_of_work < 1:
    print("Καλώς ήρθες στον κόσμο της εργασίας!")
elif year_of_work > age:
    print("Μάλλον κάτι πήγε λάθος με τα δεδομένα...")
elif year_of_work > 30:
    print("Έχεις μεγάλη εμπειρία!")
else:
    print("Καλή συνέχεια στη σταδιοδρομία σου!")

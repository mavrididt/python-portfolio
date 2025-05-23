
# ΠΡΟΓΡΑΜΜΑ: Καταγραφή Προσωπικών Στοιχείων με Έλεγχο και Μορφοποίηση

# Δημιουργία πίνακα με επικεφαλίδες
table = [["#", "Όνομα", "Ηλικία", "Επάγγελμα"]]

counter = 1  # Μετρητής για αρίθμηση γραμμών

while True:
    name = input("Γράψε το όνομα: ")

    # Έλεγχος εγκυρότητας ηλικίας
    while True:
        try:
            age = int(input("Γράψε την ηλικία: "))
            if 18 <= age <= 100:
                break
            else:
                print("Η ηλικία πρέπει να είναι από 18 έως 100.")
        except ValueError:
            print("Παρακαλώ γράψε έναν έγκυρο αριθμό.")

    job = input("Γράψε το επάγγελμα: ")

    # Προσθήκη νέας γραμμής στον πίνακα
    table.append([str(counter), name, str(age), job])
    counter += 1

    # Έξοδος από το loop;
    cont = input("Θες να καταχωρήσεις άλλο άτομο; (ναι/όχι): ")
    if cont.lower() != "ναι":
        break

# Εκτύπωση του πίνακα
print("\nΠίνακας στοιχείων:\n")
for row in table:
    print(" | ".join(row))

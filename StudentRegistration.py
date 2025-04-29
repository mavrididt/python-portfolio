
# ΠΡΟΓΡΑΜΜΑ: Καταγραφή Μαθητών με Λίστα από Λεξικά

students = []

while True:
    name = input("Γράψε το όνομα του μαθητή: ")

    while True:
        try:
            age = int(input("Γράψε την ηλικία του μαθητή: "))
            if 5 <= age <= 18:
                break
            else:
                print("Η ηλικία πρέπει να είναι από 5 έως 18.")
        except ValueError:
            print("Παρακαλώ γράψε έναν έγκυρο αριθμό.")

    school_class = input("Γράψε τη τάξη που ανήκεις: ")

    student = {"Όνομα": name, "Ηλικία": age, "Τάξη": school_class}

    students.append(student)

    cont = input("Θέλεις να καταχωρήσεις άλλον μαθητή; (ναι/όχι): ")
    if cont.lower() != "ναι":
        break

print("\nΛίστα των Μαθητών:\n")
for student in students:
    print(f"Όνομα: {student['Όνομα']}, Ηλικία: {student['Ηλικία']}, Τάξη: {student['Τάξη']}")

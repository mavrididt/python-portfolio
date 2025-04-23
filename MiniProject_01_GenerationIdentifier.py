
# Mini Project 1: Προσδιορισμός Γενιάς και Χαιρετισμός

name = input("Γράψε το όνομά σου: ")

while True:
    try:
        age = int(input("Γράψε την ηλικία σου: "))
        break
    except ValueError:
        print("Παρακαλώ γράψε έναν αριθμό για ηλικία!")

year = 2025
year_of_birth = year - age

if 1940 < year_of_birth < 1980:
    print("Είσαι boomer,", name)
elif 1981 < year_of_birth < 2000:
    print("Είσαι millennial,", name)
else:
    print("Είσαι Gen Z ή μικρότερος,", name)

print("Γεννήθηκες περίπου το", year_of_birth)

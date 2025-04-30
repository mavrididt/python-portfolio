
# Mini Project: Καταγραφή Βιβλίων με χρήση Συναρτήσεων

# Λίστα που θα κρατά όλα τα βιβλία
books = []

# Συνάρτηση για έλεγχο έγκυρης χρονιάς
def get_valid_year():
    while True:
        try:
            year = int(input("Γράψε το έτος έκδοσης του βιβλίου: "))
            if 1500 <= year <= 2025:
                return year
            else:
                print("Το έτος πρέπει να είναι μεταξύ 1500 και 2025.")
        except ValueError:
            print("Παρακαλώ γράψε έναν έγκυρο αριθμό.")

# Συνάρτηση για εισαγωγή βιβλίου
def add_book():
    title = input("Γράψε τον τίτλο του βιβλίου: ")
    author = input("Γράψε τον συγγραφέα: ")
    genre = input("Γράψε το είδος του βιβλίου: ")
    year = get_valid_year()

    book = {
        "Τίτλος": title,
        "Συγγραφέας": author,
        "Είδος": genre,
        "Έτος": year
    }

    books.append(book)

# Συνάρτηση για εμφάνιση όλων των βιβλίων
def display_books():
    print("\nΛίστα Βιβλίων:\n")
    for book in books:
        print(f"Τίτλος: {book['Τίτλος']}, Συγγραφέας: {book['Συγγραφέας']}, Είδος: {book['Είδος']}, Έτος: {book['Έτος']}")

# Κύριο πρόγραμμα
while True:
    add_book()
    cont = input("Θέλεις να καταχωρήσεις άλλο βιβλίο; (ναι/όχι): ")
    if cont.lower() != "ναι":
        break

display_books()

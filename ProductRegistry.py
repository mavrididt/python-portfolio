
# Mini Project: Καταγραφή Προϊόντων σε Κατάστημα

# Δημιουργία κενής λίστας για τα προϊόντα
products = []

# Ξεκινάμε επαναλαμβανόμενο loop
while True:
    product_name = input("Γράψε το όνομα του προϊόντος: ")

    # Έλεγχος εγκυρότητας τιμής
    while True:
        try:
            product_price = float(input("Γράψε την τιμή του προϊόντος: "))
            if 0 < product_price:
                break
            else:
                print("Η τιμή πρέπει να είναι θετικός αριθμός π.χ. 1.5, 10.99 κτλ.")
        except ValueError:
            print("Παρακαλώ γράψε έναν έγκυρο αριθμό.")

    product_category = input("Γράψε την κατηγορία που ανήκει το προϊόν: ")

    # Δημιουργούμε λεξικό για το κάθε προϊόν
    product = {"Όνομα": product_name, "Τιμή": product_price, "Κατηγορία": product_category}

    # Προσθέτουμε το προϊόν στη λίστα
    products.append(product)

    # Ρωτάμε αν θέλει να συνεχίσει
    cont = input("Θέλεις να καταχωρήσεις άλλο προϊόν; (ναι/όχι): ")
    if cont.lower() != "ναι":
        break

# Εκτύπωση όλων των προϊόντων
print("\nΛίστα των Προϊόντων:\n")
for product in products:
    print(f"Όνομα: {product['Όνομα']}, Τιμή: {product['Τιμή']}€, Κατηγορία: {product['Κατηγορία']}")

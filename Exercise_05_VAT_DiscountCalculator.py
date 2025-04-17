
# ΑΣΚΗΣΗ 5: Υπολογισμός τελικής τιμής με ΦΠΑ και έκπτωση

print("Υπολογιστής τελικής τιμής προϊόντος")

# Είσοδοι από τον χρήστη
initial_price = float(input("Δώσε αρχική τιμή προϊόντος (€): "))
vat_percent = float(input("Ποσοστό ΦΠΑ (%): "))
discount_percent = float(input("Ποσοστό έκπτωσης (%): "))

# Υπολογισμοί
price_with_vat = initial_price + (initial_price * vat_percent / 100)
final_price = price_with_vat - (price_with_vat * discount_percent / 100)

# Αποτελέσματα
print("Τιμή με ΦΠΑ: {:.2f} €".format(price_with_vat))
print("Τελική τιμή μετά την έκπτωση: {:.2f} €".format(final_price))

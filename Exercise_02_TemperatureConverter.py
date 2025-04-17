
# ΑΣΚΗΣΗ 2: Μετατροπέας θερμοκρασίας (Celsius <-> Fahrenheit)

# Ζητάμε από τον χρήστη να επιλέξει μετατροπή
print("Θες να κάνεις μετατροπή:")
print("1. Από Κελσίου σε Φαρενάιτ")
print("2. Από Φαρενάιτ σε Κελσίου")

choice = input("Δώσε 1 ή 2: ")

if choice == "1":
    celsius = float(input("Δώσε θερμοκρασία σε Κελσίου: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Η θερμοκρασία σε Φαρενάιτ είναι:", fahrenheit)
elif choice == "2":
    fahrenheit = float(input("Δώσε θερμοκρασία σε Φαρενάιτ: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Η θερμοκρασία σε Κελσίου είναι:", celsius)
else:
    print("Μη έγκυρη επιλογή. Δώσε 1 ή 2.")


# ΑΣΚΗΣΗ 4: Quiz ερωτήσεων

score = 0  # Βαθμολογία

print("Καλώς ήρθες στο Quiz! Απάντησε με 'σωστό' ή 'λάθος'.")

# ΕΡΩΤΗΣΗ 1
answer1 = input("1. Ο ήλιος είναι αστέρι. ").lower()
if answer1 == "σωστό":
    print("Σωστά!")
    score += 1
else:
    print("Λάθος!")

# ΕΡΩΤΗΣΗ 2
answer2 = input("2. Το 5 είναι μεγαλύτερο από το 10. ").lower()
if answer2 == "λάθος":
    print("Σωστά!")
    score += 1
else:
    print("Λάθος!")

# ΕΡΩΤΗΣΗ 3
answer3 = input("3. Η Python είναι γλώσσα προγραμματισμού. ").lower()
if answer3 == "σωστό":
    print("Σωστά!")
    score += 1
else:
    print("Λάθος!")

# Τελικό σκορ
print("Το τελικό σου σκορ είναι:", score, "από 3.")

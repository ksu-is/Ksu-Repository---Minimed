score = 0
print("Patient: 28-year-old pregnant woman with headache and high BP")

print("What do you want to do?")
print("1. Order labs")
print("2. Give medication")
print("3. Ask more history")

choice = input("Enter choice (1, 2, or 3): ")

if choice == "1":
    print("Labs show protein in urine which suggests preeclampsia")
    print("Correct! This points toward preeclampsia.")
    score += 1 
elif choice == "2":
    print("Not first step. You need more info first.")
    print("Incorrect. Try again.")
elif choice == "3":
    print("She reports vision changes -> an important clue")
    print("Nice try, but this answer is not the best next step.")
else:
    print("Invalid choice. Please enter 1, 2, or 3")

print("What is your diagnosis?")
print("1. Preeclampsia")
print("2. Migraine")
print("3. Anxiety")

diagnosis = input("Enter choice (1, 2, or 3): ")

if diagnosis == "1":
    print("Correct! The diagnosis is preeclampsia.")
    score += 1
elif diagnosis == "2":
    print("Incorrect. This is not a migraine.")
elif diagnosis == "3":
    print("Incorrect. This is not anxiety.")
else:
    print("Invalid choice.")

print("Your score:", score)
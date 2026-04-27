print("Patient: 28-year-old pregnant woman with headache and high BP")

print("What do you want to do?")
print("1. Order labs")
print("2. Give medication")
print("3. Ask more history")

choice = input("Enter choice (Type 1, 2, or 3): ")

if choice == "1":
    print("Labs show protein in urine which, suggests preeclampsia")
elif choice == "2":
    print("Not first step. You need more info first.")
elif choice == "3":
    print("She reports vision changes -> an important clue")
else:
    print("Invalid choice")
print("Welcome to MiniMed!")
print("This program helps you practice clinical decision-making.\n")

score = 0
print("--- Case 1 ---")
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

print("\n--- Case 2 ---")
print("Patient: 35-year-old woman with episodic retrosternal chest pain radiating to her back.")
print("Pain is triggered by emotional stress and hot/cold foods. ECG, stress test, chest x-ray, and endoscopy are normal.")
print("Nitroglycerin improves the pain.")

print("\nWhat do you want to do next?")
print("1. Try a proton pump inhibitor")
print("2. Order esophageal motility studies")
print("3. Reassure the patient that the cardiac workup is normal")

case2_step1 = input("Enter choice (1, 2, or 3): ")

if case2_step1 == "1":
    print("This is reasonable because reflux can cause chest discomfort, but the temperature triggers and nitroglycerin relief suggest another cause.")
elif case2_step1 == "2":
    print("Best choice. Motility studies are the most helpful next test for suspected esophageal spasm.")
    score += 1
elif case2_step1 == "3":
    print("The normal cardiac workup is reassuring, but she still needs evaluation because her symptoms continue.")
else:
    print("Invalid choice.")

print("\nAfter considering the history and workup, what is the main diagnosis?")
print("1. GERD")
print("2. Esophageal spasm")
print("3. Stable angina")

case2_final = input("Enter choice (1, 2, or 3): ")

if case2_final == "1":
    print("Close, but not the best conclusion. GERD is less likely because symptoms are triggered by hot/cold foods and relieved by nitroglycerin.")
elif case2_final == "2":
    print("Correct! The main diagnosis is esophageal spasm.")
    score += 1
elif case2_final == "3":
    print("Incorrect. Stable angina is less likely because the stress test and ECG are normal.")
else:
    print("Invalid choice.")

print("\nCase complete.")
print("Your score:", score)

again = input("\nWould you like to try again? (yes/no): ").lower().strip()

if again == "yes":
    print("Restart the program to try again.")
else:
    print("Thanks for using MiniMed!")


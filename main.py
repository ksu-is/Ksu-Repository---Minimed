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
elif choice == "3":
    print("She reports vision changes -> an important clue")
    print("Nice try, but this answer is not the best next step.")
else:
    print("Invalid choice. Please enter 1, 2, or 3")

case1_done = False

while not case1_done:
    print("\nWhat is your diagnosis?")
    print("1. Preeclampsia")
    print("2. Migraine")
    print("3. Anxiety")

    diagnosis = input("Enter choice (1, 2, or 3): ")

    if diagnosis == "1":
        print("Correct! The diagnosis is preeclampsia.")
        score += 1
        case1_done = True
    elif diagnosis == "2":
        print("Incorrect. This is not a migraine. Try again.")
    elif diagnosis == "3":
        print("Incorrect. This is not anxiety. Try again.")
    else:
        print("Invalid choice. Try again.")


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

case2_done = False

while not case2_done:
    print("\nAfter considering the history and workup, what is the main diagnosis?")
    print("1. GERD")
    print("2. Esophageal spasm")
    print("3. Stable angina")

    case2_final = input("Enter choice (1, 2, or 3): ")

    if case2_final == "1":
        print("Close, but not the best conclusion. GERD is less likely because symptoms are triggered by hot/cold foods and relieved by nitroglycerin.")
        print("Try again.")
    elif case2_final == "2":
        print("Correct! The main diagnosis is esophageal spasm.")
        score += 1
        case2_done = True
    elif case2_final == "3":
        print("Incorrect. Stable angina is less likely because the stress test and ECG are normal.")
        print("Try again.")
    else:
        print("Invalid choice. Try again.")


print("\n--- Case 3 ---")
print("Patient: 61-year-old man had a heart attack and cardiac arrest 2 months ago.")
print("He now has nightmares, wakes up sweating, sleeps poorly, and feels overwhelmed at work.")
print("He has no chest pain, shortness of breath, or abnormal ECG findings.")

print("\nWhat is the best next step?")
print("1. Obtain an echocardiogram")
print("2. Recommend cognitive behavioral therapy")
print("3. Reassure him and follow up later")

case3_step1 = input("Enter choice (1, 2, or 3): ")

if case3_step1 == "1":
    print("This is reasonable to consider because of his heart history, but it is not the best next step because he has no current cardiac symptoms.")
elif case3_step1 == "2":
    print("Best choice. His symptoms after a life-threatening event suggest PTSD, and therapy is appropriate.")
    score += 1
elif case3_step1 == "3":
    print("Reassurance may help, but it is not enough because his symptoms are affecting his daily life.")
else:
    print("Invalid choice.")

case3_done = False

while not case3_done:
    print("\nAfter considering the history, what is the main diagnosis?")
    print("1. Post-traumatic stress disorder")
    print("2. Medication side effect")
    print("3. Normal recovery after a heart attack")

    case3_final = input("Enter choice (1, 2, or 3): ")

    if case3_final == "1":
        print("Correct! The main conclusion is post-traumatic stress disorder.")
        score += 1
        case3_done = True
    elif case3_final == "2":
        print("Incorrect. His symptoms are more related to trauma than a medication side effect.")
        print("Try again.")
    elif case3_final == "3":
        print("Incorrect. Nightmares, sweating, poor sleep, and avoidance after a life-threatening event suggest PTSD.")
        print("Try again.")
    else:
        print("Invalid choice. Try again.")


print("\nCase complete.")
print("Your score:", score)

again = input("\nWould you like to try again? (yes/no): ").lower().strip()

if again == "yes":
    print("Restart the program to try again.")
else:
    print("Thanks for using MiniMed!")
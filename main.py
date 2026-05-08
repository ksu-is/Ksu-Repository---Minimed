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
        print("Correct! The main diagnosis is post-traumatic stress disorder.")
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

print("\n--- Case 4 ---")
print("Patient: 36-year-old man has a chronic productive cough that is worse at night.")
print("Chest x-ray is normal. He has a smoking history and no fever or weight loss.")

print("\nWhat is the best next step?")
print("1. Order pulmonary function testing")
print("2. Start antibiotics")
print("3. Order bronchoscopy immediately")

case4_step1 = input("Enter choice (1, 2, or 3): ")

if case4_step1 == "1":
    print("Best choice. Pulmonary function testing helps evaluate chronic cough and possible obstructive lung disease.")
    score += 1
elif case4_step1 == "2":
    print("This could be considered if infection was likely, but he has no fever and the chest x-ray is normal.")
elif case4_step1 == "3":
    print("Bronchoscopy is too invasive as the first step for this presentation.")
else:
    print("Invalid choice.")

case4_done = False

while not case4_done:
    print("\nAfter considering the history and workup, what is the main diagnosis?")
    print("1. Chronic bronchitis")
    print("2. Pneumonia")
    print("3. Lung cancer")

    case4_final = input("Enter choice (1, 2, or 3): ")

    if case4_final == "1":
        print("Correct! The main diagnosis is chronic bronchitis.")
        score += 1
        case4_done = True
    elif case4_final == "2":
        print("Incorrect. Pneumonia is less likely because he has no fever and a normal chest x-ray.")
        print("Try again.")
    elif case4_final == "3":
        print("Incorrect. Lung cancer is less likely with a normal chest x-ray and no weight loss, but risk factors should still be considered.")
        print("Try again.")
    else:
        print("Invalid choice. Try again.")

print("\n--- Case 5 ---")
print("Patient: 24-year-old woman has burning with urination, urinary frequency, and no fever or flank pain.")

print("\nWhat is the best next step?")
print("1. Order CT scan")
print("2. Treat with antibiotics for uncomplicated UTI")
print("3. Admit to the hospital")

case5_step1 = input("Enter choice (1, 2, or 3): ")

if case5_step1 == "1":
    print("CT scan is not needed for simple UTI symptoms.")
elif case5_step1 == "2":
    print("Best choice. Symptoms suggest uncomplicated cystitis.")
    score += 1
elif case5_step1 == "3":
    print("Admission is not needed because she has no fever or flank pain.")
else:
    print("Invalid choice.")

case5_done = False

while not case5_done:
    print("\nWhat is the main diagnosis?")
    print("1. Pyelonephritis")
    print("2. Kidney stone")
    print("3. Uncomplicated cystitis")

    case5_final = input("Enter choice (1, 2, or 3): ")

    if case5_final == "3":
        print("Correct! The main diagnosis is uncomplicated cystitis.")
        score += 1
        case5_done = True
    elif case5_final == "1":
        print("Incorrect. Pyelonephritis usually has fever and flank pain. Try again.")
    elif case5_final == "2":
        print("Incorrect. Kidney stones usually cause severe flank pain. Try again.")
    else:
        print("Invalid choice. Try again.")

print("\n--- Case 6 ---")
print("Patient: 70-year-old woman has hip pain after a fall and cannot bear weight.")

print("\nWhat is the best next step?")
print("1. Tell her to rest at home")
print("2. Start antibiotics")
print("3. Order hip x-ray")

case6_step1 = input("Enter choice (1, 2, or 3): ")

if case6_step1 == "1":
    print("Not best. Inability to bear weight after a fall needs evaluation.")
elif case6_step1 == "2":
    print("Not best. There are no signs of infection.")
elif case6_step1 == "3":
    print("Best choice. Hip fracture should be evaluated with imaging.")
    score += 1
else:
    print("Invalid choice.")

case6_done = False

while not case6_done:
    print("\nWhat is the main concern?")
    print("1. Muscle soreness")
    print("2. Hip fracture")
    print("3. Cellulitis")

    case6_final = input("Enter choice (1, 2, or 3): ")

    if case6_final == "2":
        print("Correct! The main concern is hip fracture.")
        score += 1
        case6_done = True
    elif case6_final == "1":
        print("Incorrect. She cannot bear weight, which is concerning. Try again.")
    elif case6_final == "3":
        print("Incorrect. This does not sound like cellulitis. Try again.")
    else:
        print("Invalid choice. Try again.")

print("\nCase complete.")
print("Your score:", score)

again = input("\nWould you like to try again? (yes/no): ").lower().strip()

if again == "yes":
    print("Restart the program to try again.")
else:
    print("Thanks for using MiniMed!")
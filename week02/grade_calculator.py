total_students = 0
total_score = 0

while True:
    name = input("Enter student name (or q to quit): ")

    if name == "q":
        break

    score = float(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: {score:g} -> {grade}")

    total_students += 1
    total_score += score
print(f"Total students: {total_students}")

average = total_score / total_students
print(f"Average score: {average:.2f}")

if total_students == 0:
    print("No students entered.")



## Week 02

**AI Tool Used:** ChatGPT

**Prompt Used:** Explain my MIS203 Week 02 Python grade calculator assignment step by step  and help me understand the code. Also explain the why we use that codes theres.

**What did you change?**  
I changed the code to calculate the total number of students and the average score. I also tested invalid scores and the `q` option.

**What does break do in your program?**  
The `break` statement stops the loop when the user enters `q`.




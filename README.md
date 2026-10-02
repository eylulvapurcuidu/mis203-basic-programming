# mis203-basic-programming


Name: Eylül VAPURCU 
Student Number: 2404109022
Department: Managment Information Systems
Course Name: MIS203 Basic Programming


## AI Usage

AI Tool Used: ChatGPT

Prompt Used: Create a simple Python program that ask the user for their name,department,age, and career goal, then prints a student profile.

What did you change?
I reviewed the code and changed the output format to make to student profile easier to read.

## Week 03

### AI Tool Used
ChatGPT

### Prompt Used
Create a Python cinema ticket office program using input, type conversion, f-strings, loops, if/elif/else, conditions, boundaries, and input validation. The program should calculate ticket prices based on age, day, and student status.

### What did you change?
I wrote the ticket office program and tested different ages, days, and student answers. I also added input validation and a summary of the tickets sold.

### Tests
1. Age 5, weekend, no student → 0.00 TRY (Free)
2. Age 65, weekday, no student → 100.00 TRY (Senior)
3. Age 20, weekday, yes student → 140.00 TRY (Student)

### Why does the order of the rules matter?
The rules are checked from top to bottom. For example, a 10-year-old student must get the Child discount, so the Child rule must come before the Student rule. 
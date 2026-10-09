import random
import datetime


def lucky_fortune():
    print("✨✨✨ WELCOME TO THE LUCKY FORTUNE GENERATOR ✨✨✨")

    name = input("What is your name? ")

    today = datetime.date.today()

    lucky_numbers = [3, 7, 11, 17, 21, 42]
    lucky_colors = ["Purple", "Blue", "Green", "Red", "Pink"]

    lucky_number = random.choice(lucky_numbers)
    lucky_color = random.choice(lucky_colors)
    luck_score = random.randint(1, 100)

    print()
    print("Hello", name + "!")
    print("Today's date:", today)
    print()
    print("🍀 Your lucky number:", lucky_number)
    print("🎨 Your lucky color:", lucky_color)
    print("⭐ Your luck score:", luck_score, "/ 100")

    if luck_score >= 80:
        print("🔥 AMAZING! Today is your lucky day!")
    elif luck_score >= 50:
        print("😊 GOOD! Something nice may happen today!")
    else:
        print("🌱 Don't worry! Better days are coming!")

    print()
    print("✨ Have a wonderful day,", name + "! ✨")


lucky_fortune()

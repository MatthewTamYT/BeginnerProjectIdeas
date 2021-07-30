# Mad Libs Game

# Introduction For User
print("We are going to play a Mad Libs Game, shall we?")
print("To play this game, you have to enter some information when I ask you and I would give you a paragraph based on the information I was given.")
print(" ")

# Creating Variables
first_name = input("Please enter your first name here: ")
last_name = input("Please enter your last name here: ")
middle_name = input("Please enter your middle name here: ")
full_name = first_name + " " + middle_name + " " + last_name
age = input("Please enter your age here: ")
profession = input("What do you do for a living: ")
free_time = input("Please enter something you would do in your free time: ")
current_car = input("Please enter what car you have now (If you don't have one, just enter a car of someone you know): ")
car_plate = input("Please enter the vehicle license plate here: ")
dream_car = input("Please enter your dream car here: ")
year_of_birth = input("Please enter your year of birth here: ")
month_of_birth = input("Please enter your month of birth here: ")
date_of_birth = input("Please enter your date of birth here: ")
book = input("Please enter your favourite book here: ")
author = input("Please enter author of your favourite book here: ")
hero = input("Please enter your hero or role model here: ")
address = input("Please enter your full address here: ")
telephone_nu = input("Please enter your telephone number here: ")
email = input("Please enter your email address here: ")
gender = input("Please enter your gender here: ")
race = input("Please enter your race here: ")
wage = input("Please enter your wage per year in pounds here: ")
net_worth = input("Please enter your net worth in pounds here: ")
hobby = input("Please enter your hobby here: ")
friend_name1 = input("Please enter a friend's name here: ")
friend_name2 = input("Please enter another friend's name here: ")
friend_name3 = input("Please enter another friend's name here: ")
regular_sport = input("Please enter a sport that you regularly do here: ")
occasional_sport = input("Please enter a sport that you occasionally do here: ")
rare_sport = input("Please enter a sport which you like but rarely do here: ")
hate_sport = input("Please enter a sport which most people but you like here: ")

# Paragraph Printing
print(first_name + ", your full name is " + full_name + " and I find your middle name rather weird (and funny). You are " + age + " of age and a " + profession + ". You were born on the " + date_of_birth + "th of " + month_of_birth + ", " + year_of_birth + ". You are " + race + " and a " + gender + ". You like " + free_time + " and " + hobby + ". You have a " + current_car + " with a vehicle license plate of " + car_plate + ", although you do dream to have a " + dream_car + ". You really enjoy the book " + book + " by " + author + "! Actually, I like that book very much too, but I'll keep my favourite a secret (for now)! You are very much inspired by " + hero + " and I don't blame you, that's a good hero. Here is where everything's going to start getting rather personal. You live at " + address + " and I honestly hope you enjoy your house. It's a lovely place! " + "You have a telephone number of " + telephone_nu + " and an email address of " + email + ". You earn £" + wage + ", adding up to your total net worth of £" + net_worth + ". You have friends (who doesn't care about you, so don't bother anyway) with names " + friend_name1 + ", " + friend_name2 + ", and " + friend_name3 + ". You really like " + regular_sport + " and you do it regularly. However, you do occasionally do " + occasional_sport + ". You also really like " + rare_sport + ", but unfortunately, you don't do it very often. You hate " + hate_sport + ", but I hope you realize that makes you extremely unpopular (like me) because most people like it. ")
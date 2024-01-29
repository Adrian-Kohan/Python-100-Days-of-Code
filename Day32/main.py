##################### Extra Hard Starting Project ######################
import random
import datetime as dt
import smtplib
import pandas

MAIL = "f.kohansal.fk@gmail.com"
PASS = ""

# letters
with open("letter_templates/letter_1.txt") as text_file:
    letter_1 = text_file.read()
with open("letter_templates/letter_2.txt") as text_file:
    letter_2 = text_file.read()
with open("letter_templates/letter_3.txt") as text_file:
    letter_3 = text_file.read()

letter_list = [letter_1, letter_2, letter_3]

# 1. Update the birthdays.csv
data_file = pandas.read_csv("birthdays.csv")
birthdays = data_file.to_dict(orient="records")
print(birthdays)

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
day = now.day
month = now.month

for person in birthdays:
    if person["month"] == month and person["day"] == day:
        # 3. If step 2 is true, pick a random letter from letter templates and
        # replace the [NAME] with the person's actual name from birthdays.csv
        chosen_letter = random.choice(letter_list)
        birthday_letter = chosen_letter.replace("[NAME]", person["name"])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MAIL, password=PASS)
            connection.sendmail(
                from_addr=MAIL,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday\n\n{birthday_letter}"
            )

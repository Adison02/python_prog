import random
import smtplib
import datetime as dt

my_email = "testing.email.python.001@gmail.com"
password = "mfrhizehvitkdgex"

now = dt.datetime.now()

if now.weekday() == 6:
    with open("quotes.txt", "r") as data_file:
        quotes = data_file.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="agusia.witkowska@interia.pl",
            msg=f"Subject:Your daily quote\n\n"
                f"{random.choice(quotes)}"
        )


# import smtplib
#
# my_email = "testing.email.python.001@gmail.com"
# password = "mfrhizehvitkdgex"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="agusia.witkowska@interia.pl",
#         msg="Subject:Hello\n\nThis is the body of email"
#     )


# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# day = now.day
#
# date_of_birth = dt.datetime(year=2002, month=11, day=6)
# print(date_of_birth)
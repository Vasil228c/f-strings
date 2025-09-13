import random

def generate_ticket(last_name, destination, departure_time, date, price, seat):
    ticket_number = random.randint(100000, 999999)
    sd = date.split(".")
    return (
        f"Квиток №{ticket_number}\n"
        f"Прізвище: {last_name}\n"
        f"Пункт призначення: {destination}\n"
        f"Час відправлення: {departure_time}\n"
        f"День: {sd[0]}\n"
        f"Місяць: {sd[1]}\n"
        f"Рік: {sd[2]}\n"
        f"Місце: {seat}\n"
        f"Ціна квитка: {price:.2f} грн"
    )


last_name = input("Введіть ваше прізвище: ")
destination = input("Введіть пункт призначення: ")
departure_time = input("Введіть час відправлення: ")
date = input("Введіть дату відправлення, у форматі ДД.ММ.РРРР: ")
price = int(input("Введіть ціну квитка: "))
seat = input("Введіть номер місця: ")

print(generate_ticket(last_name, destination, departure_time, date, price, seat))


import random

def generate_ticket(last_name, destination, departure_time, date):
  ticket_number = random.randint(100000, 999999)
  sd = date.split(".")
  return f"Квиток №{ticket_number}\nПрізвище: {last_name}\nПункт призначення: {destination}\nЧас відправлення: {departure_time}\nДень: {sd[0]}\nМісяць: {sd[1]}\nРік: {sd[2]}"


last_name = input("Введіть ваше прізвище: ")
destination = input("Введіть пункт призначення: ")
departure_time = input("Введіть час відправлення: ")
date = input("Введіть дату відправлення, у форматі ДД.ММ.РРРР: ")

print(generate_ticket(last_name, destination, departure_time,date))

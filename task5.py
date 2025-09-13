def weather_report(city, forecasts):
    report = f"Погода в місті {city}:\n"
    for day, forecast in enumerate(forecasts, 1):
        report += (
            f"День {day}:\n"
            f"  Температура: {forecast['temperature']}°C\n"
            f"  Вологість: {forecast['humidity']}%\n"
            f"  {forecast['description']}\n"
        )
    return report

city = input("Введіть назву міста: ")
days = int(input("Скільки днів показати прогноз? "))

forecasts = []
for i in range(days):
    print(f"\nДень {i+1}:")
    temperature = float(input("  Введіть температуру: "))
    humidity = int(input("  Введіть вологість: "))
    description = input("  Введіть опис погоди: ")
    forecasts.append({
        "temperature": temperature,
        "humidity": humidity,
        "description": description
    })

print(weather_report(city, forecasts))

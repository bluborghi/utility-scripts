import datetime

def generate_week_text(week_number, year):
    # Calculate the date of the first day of the week
    first_day_of_week = datetime.datetime.strptime(f'{year}-W{week_number}-1', "%Y-W%W-%w")

    # Calculate the dates for the days of the week
    week_days = [first_day_of_week + datetime.timedelta(days=i) for i in range(7)]

    # Format the text
    week_text = f'WEEK {week_number}\nWeek goals\n'
    for day in week_days:
        formatted_date = day.strftime("%a %d.%m.%y")
        week_text += f"{formatted_date}\n"

    week_text += 'Week recap'

    return week_text

# User input
week_number = int(input("Enter the week number: "))
year = int(input("Enter the year: "))

result = generate_week_text(week_number, year)
print(result)

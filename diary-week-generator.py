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

def main():
    user_input = input("Enter week number(s) (e.g., '38' or '38-40'): ")

    # Split the input into parts based on '-'
    input_parts = user_input.split('-')

    if len(input_parts) == 1:
        # Single week input
        week_numbers = [int(input_parts[0])]
    elif len(input_parts) == 2:
        # Range of weeks input
        start_week = int(input_parts[0])
        end_week = int(input_parts[1])
        week_numbers = list(range(start_week, end_week + 1))
    else:
        print("Invalid input format. Please enter a single week or a range of weeks.")
        return

    year = int(input("Enter the year: "))

    for week_number in week_numbers:
        result = generate_week_text(week_number, year)
        print(result)

if __name__ == "__main__":
    main()

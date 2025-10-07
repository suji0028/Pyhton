# Input year and month
year = int(input("Enter year (e.g. 2025): "))
month = int(input("Enter month (1-12): "))

# Days in each month (non-leap year)
month_days = [31, 28, 31, 30, 31, 30, 
              31, 31, 30, 31, 30, 31]

# Month names
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

# Print header
print("\n-----", month_names[month - 1], year, "-----")
print("Sun Mon Tue Wed Thu Fri Sat")

# Just start on Sunday with no weekday alignment
days = month_days[month - 1]
day = 1

# Print calendar (simplified, starts on Sunday)
while day <= days:
    for i in range(7):
        if day > days:
            break
        print(f"{day:>3}", end=" ")
        day += 1
    print()

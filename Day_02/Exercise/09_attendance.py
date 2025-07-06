attendance_names =[]
attendance_count = int(input("attendee count: "))

for count in range(attendance_count):
    attendance_name = input("Attendee Name: ")
    attendance_names.append(attendance_name)

print("--------OUTPUT HERE---------")
print(*attendance_names)

print(attendance_names.index("nathan"))

if "nathan" in attendance_names:
    attendance_names.remove("nathan")
    print(*attendance_names)
else:
    print("Not in the list")

remove_last_attendee = attendance_names.pop(-1)
print(remove_last_attendee)

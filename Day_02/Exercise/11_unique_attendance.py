attendance_names =set()
attendance_count = int(input("attendee count: "))

#you can change your avariable into '_' if the variable not use.
for _ in range(attendance_count):
    attendance_name = input("Attendee Name: ")
    attendance_names.add(attendance_name)

print(attendance_names)
attendance_names.discard("nathan")
print(attendance_names)
print("random raffle winner!: ",attendance_names.pop())
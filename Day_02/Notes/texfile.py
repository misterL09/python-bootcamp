# with open("test.txt", "a") as file:
#     file.write("\n ddworld!")
#
# with open("test.txt", "w") as file:
#     file.write("New Line\n")
#     file.write("Hellow world!")

attendees = ['Mia Anderson',
'Ethan Roberts',
'Liam Johnson',
'Sophia Martinez',
'Olivia Davis',
'Noah Thompson']

with open("test.txt", "w") as file:
    for item in attendees:
        file.write(item)
        file.write("\n")

with open("test.txt", "a") as file:
    file.write("Alex Freze")

with open("test.txt", "r") as file:
    file_contents = file.read().splitlines()
print(file_contents)
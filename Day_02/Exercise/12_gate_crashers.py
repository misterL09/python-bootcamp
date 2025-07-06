invited = {'Ana','Ben','Carlo','Dani'}
attended = {'Ben','Carlo','Ely'}

print("Involved Members: ",*invited.union(attended))
print("Absent: ",*invited.difference(attended))
print("Not Enrolled but attended: ",attended.difference(invited))
print("Attended properly: ",invited.intersection(attended))
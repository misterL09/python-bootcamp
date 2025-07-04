battery = int(input("Battery percentage: "))
if battery >= 80:
    print("Full Battery")
if battery >= 40:
    print("Good Battery")
if battery >= 15:
    print("Low Battery")
if battery > 0:
    print("Critically Low Battery")
else:
    print("No Battery")

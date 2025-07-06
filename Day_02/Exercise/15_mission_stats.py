mission = "Orbiter Alpha"
distance_km = 1500000.4567
duration_days = 92.6
speed = distance_km / (duration_days * 24)
missnlog = " Mission Log "
print(f"{missnlog:=^25}")
print(f"Mission: {mission}")
print(f"Distance: {distance_km:,.2f} km")
print(f"Duration: {duration_days:.0f} days")
print(f"Speed: {speed:.02f} km/h")

"""
Old version:
response = input("Proceed: ")
if response == "Yes" or response == "yes" or response =="y":
	print("Proceeding")
"""

# Updated version
response = input("Proceed: ")
if response in ("Yes","yes","y"):
	print("Proceeding")

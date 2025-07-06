country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "JP": "Japan",
    "CND": "Canada"
}
country_code = input("Enter country code: ")
#use get it has return value and it will not throw error if not found
print(country_codes.get(country_code),"UNKNOWN")

for code in country_codes.keys():
    print(code)

for country in country_codes.values():
    print(country)

for code,country in country_codes.items():
    print(code,country)
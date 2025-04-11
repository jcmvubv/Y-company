import phonenumbers
from phonenumbers import geocoder, carrier, timezone

print("x" * 50)

entered_num = input("Please enter a phone number: ")


phone_num = phonenumbers.parse(entered_num, None)


print(phone_num)


print(geocoder.description_for_number(phone_num, "ar"))


print(carrier.name_for_number(phone_num, "en"))


print(timezone.time_zones_for_number(phone_num))

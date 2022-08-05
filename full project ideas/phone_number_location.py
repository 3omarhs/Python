import phonenumbers
from phonenumbers import geocoder
phone_number = phonenumbers.parse("+962795965910")
print(geocoder.description_for_number(phone_number, 'en'))
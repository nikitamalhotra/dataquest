## 1. Programming And Data Science ##

print(1288)
print(639)
print(1288 + 639)

1288 + 639

## 2. Arithmetic Operators ##

print(sum([749, 371, 828, 503, 1379])/len([749, 371, 828, 503, 1379]))

## 3. Variables ##

albuquerque = 749
anaheim = 371
anchorage = 828
arlington = 503
atlanta = 1379
print(anaheim)

## 4. Data Types ##

atlanta_string = 'Atlanta'
atlanta_float = '1379.5'

## 5. The Type Function ##

atlanta_string = 'Atlanta'
print(type(atlanta_string))

## 6. Using A List To Store Multiple Values ##

cities = list()
crime_rates = list()

for item in ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]:
    cities.append(item)

for item in [749, 371, 828, 503, 1379]:
    crime_rates.append(item)
    
print(cities)
print(crime_rates)

## 7. Creating Lists With Values ##

crime_rates = [749, 371, 828, 503, 1379]

## 8. Comments ##

# A comment
crime_rates = [749, 371, 828, 503, 1379]
print(crime_rates)
# Does jack shit

## 9. Accessing Elements In A List ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]

anchorage_str = cities[2]
anchorage_cr = crime_rates[2]

## 10. Retrieving The Length Of A List ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]
# Add your code here.

two_sum = len(cities) + len(crime_rates)

## 11. Slicing Lists ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]

cities_slice = cities[1:4]
cr_slice = crime_rates[-2:]
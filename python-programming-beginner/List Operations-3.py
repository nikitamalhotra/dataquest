## 2. Parsing the File ##

weather_data = []

data = open('la_weather.csv', 'r').read()
rows = data.split('\n')
for row in rows:
    weather_data.append(row.split(','))


## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = [item[1] for item in weather_data]

## 4. Counting the Items in a List ##

count = len(weather)

## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = 'cat' in animals
space_monster_found = 'space_monster' in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = [type in new_weather for type in weather_types]

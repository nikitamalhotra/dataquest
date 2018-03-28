## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, thing in enumerate(things):
    things[i].append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled = list(map(lambda x: x*2, apple_prices))
apple_prices_lowered = list(map(lambda x: x-100, apple_prices))

## 5. Counting Female Names ##

name_counts = dict()

for row in legislators:
    if row[3] == 'F' and row[-1] > 1940:
        name = row[1]
        name_counts[name] = name_counts.get(name, 0) + 1
    

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = [value is not None and value > 30 for value in values]

## 8. Highest Female Name Count ##

max_value = max(name_counts.values())

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for key, value in plant_types.items():
    print(key)
    print(value)

## 10. Finding the Most Common Female Names ##

top_female_names = [key for key, value in name_counts.items() if value == 2]



## 11. Finding the Most Common Male Names ##

top_male_names = []

male_name_counts = dict()

for row in legislators:
    if row[3] == 'M' and row[-1] > 1940:
        name = row[1]
        male_name_counts[name] = male_name_counts.get(name, 0) + 1

highest_male_count = max(male_name_counts.values())
top_male_names = [name for name in male_name_counts if male_name_counts[name] == highest_male_count]

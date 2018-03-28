## 2. Sets ##

gender = set([row[3] for row in legislators])

for item in gender:
    print(item)

## 3. Exploring the Dataset ##

party = set([row[6] for row in legislators])

for item in party:
    print(item)
    
print(legislators)

## 4. Missing Values ##

for row in legislators:
    if row[3] == '':
        row[3] = 'M'

## 5. Parsing Birth Years ##

birth_years = []
for row in legislators:
    parts = row[2].split('-')
    birth_years.append(parts[0])

## 6. Try/except Blocks ##

try:
    float('hello')
except ValueError:
    print('Error converting to float.')

## 7. Exception Instances ##

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for year in birth_years:
    try:
        year = int(year)       
    except Exception:
        pass
    converted_years.append(year)
    
print(converted_years[:10])


## 9. Convert Birth Years to Integers ##

for row in legislators:
    try:
        row.append(int(row[2].split('-')[0]))
    except Exception:
        row.append(0)

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    else:
        last_value = row[7]
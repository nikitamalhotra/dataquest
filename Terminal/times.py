import read
from collections import Counter
from dateutil.parser import parse

df = read.load_data()

times = df['submission_time'].dropna()

def extract_times(string):
    return parse(string).hour

hours = (times.apply(extract_times)
         .value_counts()
         .to_dict())

for hour, count in hours.items():
    print(hour, count)
    
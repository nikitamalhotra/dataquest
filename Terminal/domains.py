import read
from collections import Counter

df = read.load_data()

domains = df['url'].dropna()

def remove_subdomain(string):
        pieces = string.split('.')
        domain = pieces[-2:]
        joined = '.'.join(domain)
    
        return joined

domains = domains.apply(remove_subdomain)
domain_dict = domains.value_counts().to_dict()

c = Counter(domain_dict)

for domain, count in c.most_common(100):
    print(domain, count)
    
## 2. Extract Line Numbers ##

raw_hamlet = sc.textFile("hamlet.txt")
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)

def format_id(x):
    num = x[0].split('@')[1]
    results = [num]
    if len(x) > 1:
        for y in x[1:]:
            results.append(y)
    return results

hamlet_with_ids = split_hamlet.map(format_id)

## 3. Remove Blank Values ##

hamlet_with_ids.take(5)

hamlet_text_only = hamlet_with_ids.filter(lambda x: len(x) > 1)
hamlet_text_only = hamlet_text_only.map(lambda x: [l for l in x if l != ''])

## 4. Remove Pipe Characters ##

hamlet_text_only.take(10)

def clean_pipe(line):
    results = []
    for word in line:
        if word == '|':
            pass
        elif '|' in word:
            clean_word = word.replace('|', '')
            results.append(clean_word)
        else:
            results.append(word)
    return results

clean_hamlet = hamlet_text_only.map(clean_pipe)
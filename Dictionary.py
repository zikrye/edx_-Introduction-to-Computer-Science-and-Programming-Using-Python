grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A'}
grades['Sylvan'] = 'A'
'John' in grades
del(grades['Ana'])
grades.keys()
grades.values()

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

# exercise
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    sum = 0
    for w in aDict:
        sum += len(aDict[w])
    return sum
how_many(animals)

def biggest(aDict):
    temp = 0
    for k in aDict:
        if len(aDict[k]) >= temp:
            temp = len(aDict[k])
            key = k
    return key

biggest(animals)

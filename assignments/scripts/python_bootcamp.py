from collections import Counter
from string import punctuation
import re

wine = open('data/wine.txt').readlines()
stopwords = open('data/stopwords.txt').readlines()

#keep track of how many times each star value appears
ratings = {} 
for line in wine:
    review_and_rating = line.strip().split('\t')
    '''['Lovely delicate, fragrant Rhone wine. Polished leather and
    strawberries. Perhaps a bit dilute, but good for drinking now.', '***']'''
    #print review_and_rating
    stars = review_and_rating[1]
    if stars not in ratings:
        ratings[stars] = 0
    ratings[stars] += 1
print ("This is the number of stars aggregated from reviews")
sorted = ratings.items()
sorted.sort()
for k,v in sorted:
    print k,v
print



#10 most common words
print ("These are the 10 most common words including stopwords")
wordcount = {}
for line in wine:
    line= line.strip().split('\t')
    sentence=line[0]
    words = sentence.split(" ")
    for word in words:
        if word not in wordcount:
            wordcount[word]=0
        wordcount[word]+=1
new_dict = dict(Counter(wordcount).most_common(10))
sorted = new_dict.items()
sorted.sort()
for k,v in sorted:
    print k,v
print


#how many times do the words a, fruit, and mineral appear
print ("This is how many times a, fruit, and mineral appear respectively")
a_count = 0
fruit_count = 0
mineral_count = 0
for line in wine:
    line= line.strip().split('\t')
    sentence=line[0]
    words = sentence.split(" ")
    for word in words:
        if word == "a":
            a_count+=1
        if word == "fruit":
            fruit_count+=1
        if word == "mineral":
            mineral_count+=1
print (a_count)
print (fruit_count)
print (mineral_count)
print

print ("These are the 10 most common words without stopwords")
word_count={}
for line in wine:
    line= line.strip(",.()!").split('\t')
    sentence=line[0] #Lovely delicate, fragrant Rhone wine. Polished leather
                    #and strawberries. Perhaps a bit dilute, but good for
                    #drinking now.
    words = sentence.split(" ")
    # ['Lovely', 'delicate,', 'fragrant', 'Rhone', 'wine.', 'Polished',
    #'leather', 'and', 'strawberries.', 'Perhaps', 'a', 'bit', 'dilute,',
    #'but', 'good', 'for', 'drinking', 'now.']
    for word in words:
        word = word.lower() # lovely
        for stopword in stopwords:
            stopword = stopword.strip()
            if word==stopword:
                word = word.replace(word,"")
        if word not in word_count:
            word_count[word]=0
        word_count[word]+=1
del(word_count[''])
new_dict = dict(Counter(word_count).most_common(10))
sorted = new_dict.items()
sorted.sort()
for k,v in sorted:
    print k,v
print


print ("These are the 10 most common words amongst the 5 star reviews")
word_count1={}
for line in wine:
    review_and_rating = line.strip(",()!").split('\t')
    '''['Lovely delicate, fragrant Rhone wine. Polished leather and
    strawberries. Perhaps a bit dilute, but good for drinking now.', '***']'''
    stars = review_and_rating[1].strip()
    if stars == "*****":
        sentence = review_and_rating[0]
        words = sentence.split(" ")

        for word in words:
            word = word.lower() # lovely
            for stopword in stopwords:
                stopword = stopword.strip()
                if word==stopword:
                    word = word.replace(word,"")
            if word not in word_count1:
                word_count1[word]=0
            word_count1[word]+=1
del(word_count1[''])
new_dict = dict(Counter(word_count1).most_common(10))
sorted = new_dict.items()
sorted.sort()
for k,v in sorted:
    print k,v
print

print ("These are the 10 most common words amongst the 1 star reviews")
word_count1={}
for line in wine:
    review_and_rating = line.strip(",()!").split('\t')
    '''['Lovely delicate, fragrant Rhone wine. Polished leather and
    strawberries. Perhaps a bit dilute, but good for drinking now.', '***']'''
    stars = review_and_rating[1].strip()
    if stars == "*":
        sentence = review_and_rating[0]
        words = sentence.split(" ")

        for word in words:
            word = word.lower() # lovely
            for stopword in stopwords:
                stopword = stopword.strip()
                if word==stopword:
                    word = word.replace(word,"")
            if word not in word_count1:
                word_count1[word]=0
            word_count1[word]+=1
del(word_count1[''])
new_dict = dict(Counter(word_count1).most_common(10))
sorted = new_dict.items()
sorted.sort()
for k,v in sorted:
    print k,v
print

print ("These are the 10 most frequent words in 'red' reviews that aren't in 'white' reviews")
word_count = {}
for line in wine:
    line= line.strip().split('\t')
    sentence=line[0]
    words = sentence.split(" ")
    for word in words:
        word = word.lower()
        if word == "red" or word == "red." or word == "red," or word=="Red" or word=="Red." or word=="Red,":
            for word in words:
                word = word.lower()
                for stopword in stopwords:
                    stopword = stopword.strip()
                    if word==stopword:
                        word = word.replace(word,"")
                if word not in word_count:
                    word_count[word]=0
                word_count[word]+=1
del(word_count[''])
del(word_count['-'])
new_dict = dict(Counter(word_count).most_common(10))
sorted = new_dict.items()
sorted.sort()
for k,v in sorted:
    print k,v
print

print ("These are the 10 most frequent words in 'white' reviews that aren't in 'red' reviews")
word_count = {}
for line in wine:
    line= line.strip().split('\t')
    sentence=line[0]
    words = sentence.split(" ")
    for word in words:
        word = word.lower()
        if word == "white" or word == "white." or word == "white," or word=="White" or word=="White." or word=="White,":
            for word in words:
                word = word.lower()
                for stopword in stopwords:
                    stopword = stopword.strip()
                    if word==stopword:
                        word = word.replace(word,"")
                if word not in word_count:
                    word_count[word]=0
                word_count[word]+=1
del(word_count[''])
del(word_count['-'])
new_dict = dict(Counter(word_count).most_common(10))
sorted = new_dict.items()
sorted.sort()
for k,v in sorted:
    print k,v
print
            
            


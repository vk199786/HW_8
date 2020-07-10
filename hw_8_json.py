import json

with open('newsafr.json') as f:
    json_data = json.load(f)

#news_list = json_data['rss']['channel']['items']
#print(f'Количество новостей: {len(news_list)}')

#for news in news_list:
    #print(news['title'])

#with open('newsafr2.json', 'w') as f:
    #json.dump(json_data, f, ensure_ascii=False, indent=4)

news_list = json_data['rss']['channel']['items']
news_pull = []

for news in news_list:
    #print(news['description'])
    news_pull.append(news['description'].split())
#print(news_pull)

words_pull = []
count = 0
for each_news in news_pull:
    for words in each_news:
        if len(words) >= 6:
                words_pull.append(words)
#print(words_pull)

word_dict = {}
for word in words_pull:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
#print(word_dict)
the_most_popular_words = sorted(word_dict, key = word_dict.get, reverse=True)
print(f'Наиболее встречающиеся слова: {the_most_popular_words[0:10]}')

#most_common = 0
#qty_most_common = 0
#for item in words_pull:
    #qty = words_pull.count(item)
    #if qty > qty_most_common:
       #qty_most_common = qty
        #most_common = item
#print(most_common, qty_most_common)

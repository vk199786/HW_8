import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
#print(root.tag)
#print(root.text)
#print(root.attrib)

#channel_node = root.find('channel')
#print(channel_node.tag)
#items_list = channel_node.findall('item')
#print(len(items_list))

#items_list2 = root.findall('channel/item/title')
#print(len(items_list2))
#print(items_list2)
#for title in items_list2:
    #print(title.text)

news_list = []
items_list = root.findall('channel/item/description')
#print(len(items_list))
#print(items_list)
for news_text in items_list:
    #print(news_text.text)
    news_list.append(news_text.text.split())
    #print(news_list)

words_pull = []
count = 0
for each_news in news_list:
    for words in each_news:
        if len(words) >= 6:
                words_pull.append(words)
#print(words_pull)

word_dict = {}
for each_word in words_pull:
    if each_word in word_dict:
        word_dict[each_word] += 1
    else:
        word_dict[each_word] = 1
#print(word_dict)
the_most_popular_words = sorted(word_dict, key = word_dict.get, reverse=True)
print(f'Наиболее встречающиеся слова: {the_most_popular_words[0:10]}')
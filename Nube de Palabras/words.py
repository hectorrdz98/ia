import re

words = {}
l1 = 1
l2 = 12

with open('biblia.txt') as file:
    for line in file:
        for word in re.split(r'\s', line):
            only_w = re.findall(r'\w+', word)
            if only_w:
                only_w = only_w[0]
                if l1 <= len(only_w) <= l2:
                    if only_w in words:
                        words[only_w] += 1
                    else:
                        words[only_w] = 1

sorted_words = sorted(words.items(), key=lambda kv: kv[1], reverse=True)

with open('output.txt', 'w', encoding="utf-8") as file:
    for key,val in sorted_words:
        file.writelines('{},{}\n'.format(key, val))

print('Success')


from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(max_font_size=100, max_words=50, background_color="white")
wordcloud.generate_from_frequencies(dict(sorted_words))
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
import jieba
from wordcloud import WordCloud
import os
import PIL.Image as Image

cur_path = os.path.dirname(__file__)

def chinese_jieba(txt):
    wordlist_jieba = jieba.cut(txt) # 将文本分割，返回列表
    txt_jieba = " ".join(wordlist_jieba) # 将列表拼接为以空格为间断的字符串
    return txt_jieba


stopwords = [line.strip() for line in open('stop_words.txt', 'r', encoding='utf-8').readlines()]  

with open(os.path.join(cur_path, 'word.txt'), encoding='UTF-8') as fp:
    txt = fp.read()
    txt = chinese_jieba(txt)
    # print(txt)
    wordcloud = WordCloud(font_path = 'simsun.ttc', # 字体
                          background_color = 'black', # 背景色
                          max_words = 30, # 最大显示单词数
                          max_font_size = 60, # 频率最大单词字体大小
                          stopwords = stopwords # 过滤噪声词
                        ).generate(txt)
    image = wordcloud.to_image()
    image.save("./word.jpg")
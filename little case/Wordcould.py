"""
生成词云
"""
import jieba
import wordcloud
import matplotlib.pyplot as plt
def main():
    l="G:\case\practise\mnc.txt"
    with open(l,"r",encoding=" utf-8") as km:
        bn=km.read()
        split=jieba.cut(bn,cut_all=False)
        vv=" ".join(split)
        my_cloud=wordcloud.WordCloud(font_path="C:\windows\Fonts\simhei.ttf").generate(vv)
        plt.imshow(my_cloud)
        plt.axis("off")
        plt.show()

if __name__=="__main__":
    main()
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 停用词文件路径
stopwords_file = "cn_stopwords.txt"

# 读取停用词文件
def load_stopwords(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stopwords = set(file.read().splitlines())  # 读取每行作为停用词
        print(f"成功加载 {len(stopwords)} 个停用词！")
        return stopwords
    except FileNotFoundError:
        print(f"错误：停用词文件 {file_path} 未找到！")
        return set()
    except Exception as e:
        print(f"发生错误: {e}")
        return set()

# 读取帖子内容文件
def read_posts(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到！")
        return ""
    except Exception as e:
        print(f"发生错误: {e}")
        return ""

# 生成词云图
def generate_wordcloud(text, stopwords):
    print("分词中...")
    words = jieba.cut(text)
    filtered_words = [word for word in words if word not in stopwords and len(word) > 1]  # 过滤停用词和单字

    print("生成词云...")
    wordcloud = WordCloud(
        font_path="simhei.ttf",  # 中文字体路径
        background_color="white",
        width=800,
        height=600,
        stopwords=stopwords
    ).generate(" ".join(filtered_words))

    # 显示词云图
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("NGA 帖子标题词云")
    plt.show()

    # 保存词云图到文件
    wordcloud.to_file("nga_wordcloud.png")
    print("词云图已保存为 nga_wordcloud.png")

# 主程序
if __name__ == "__main__":
    stopwords = load_stopwords(stopwords_file)  # 加载停用词
    posts_content = read_posts("posts.txt")  # 读取帖子内容文件
    if posts_content:  # 如果内容非空，生成词云
        generate_wordcloud(posts_content, stopwords)


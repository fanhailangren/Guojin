import jieba
import re

# 读取原始文本
with open("news.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 清理文本的函数
def clean_text(text):
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'【.*?】(- 财经时讯,)?', '', text)
    text = re.sub(r'#\S+', '', text)
    text = re.sub(r'[\，\。\“\”\！\？\：\；\（\）\【\】\{\}\|\`\~\^]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# 清理后的文本
words = clean_text(text)

# 分词处理
words = jieba.lcut(words)

# 将结果写入文件
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(words))


import jieba
import re

# 读取原始文本
with open("news.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 清理文本的函数
def clean_text(text):
    # 1. 去掉时间戳
    text = re.sub(r'\[.*?\]', '', text)
    # 2. 去掉来源和标题
    text = re.sub(r'【.*?】(- 财经时讯,)?', '', text)
    # 3. 删除 # 标签
    text = re.sub(r'#\S+', '', text)
    # 4. 删除多余的标点符号（保留必要标点如句号、逗号等）
    text = re.sub(r'[\，\。\“\”\！\？\：\；\（\）\【\】\{\}\|\`\~\^]', '', text)
    # 4. 清理多余的空格和换行
    text = re.sub(r'\s+', ' ', text)
    return text

# 清理后的文本
words = clean_text(text)

# 分词处理
words = jieba.lcut(words)

# 将结果写入文件
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(words))


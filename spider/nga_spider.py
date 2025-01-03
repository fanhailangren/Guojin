import requests
import os
import time
from bs4 import BeautifulSoup

# NGA 论坛目标页面基础 URL
base_url = "https://nga.178.com/thread.php?fid=706"

# 请求头部，模拟浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://nga.178.com"
}

# 如果需要登录，设置 cookies
cookies = {
    "ngaPassportUid": "60660005",
    "ngaPassportCid": "X95ggsrf9g2ue1aagbsqs57bug41tf2kufvkk9k4"
}

# 爬取帖子标题和链接
def fetch_nga_posts(base_url, pages):
    try:
        # 自动创建文件保存路径
        file_path = "posts.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            # 遍历每一页
            for page in range(1, pages + 1):
                # 构造分页 URL
                url = f"{base_url}&page={page}"
                print(f"正在爬取第 {page} 页: {url}")
                # 发送 HTTP 请求
                response = requests.get(url, headers=headers, cookies=cookies)
                if response.status_code != 200:
                    print(f"请求失败，第 {page} 页状态码：", response.status_code)
                    continue
                # 解析 HTML 内容
                soup = BeautifulSoup(response.text, "html.parser")
                threads = soup.find_all("a", class_="topic")  # 查找帖子链接
                # 判断是否找到帖子
                if not threads:
                    print(f"第 {page} 页未找到帖子，请检查页面结构。")
                    continue

                # 写入帖子标题和链接到文件
                for thread in threads:
                    title = thread.get_text(strip=True)
                    link = thread['href']
                    if not link.startswith("http"):
                        link = "https://nga.178.com" + link  # 补全链接
                    file.write(f"标题: {title}\n")
        print(f"所有帖子信息已保存到文件: {file_path}")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    pages_to_fetch = 15  # 修改此值爬取更多页
    fetch_nga_posts(base_url, pages_to_fetch)

"""
    分析爬取的页面
    作者：https://www.cnblogs.com/airnew/p/10101698.html
        这次是爬取京东图书中计算机书籍类的信息

"""

# 通过分析发现，所搜框的 css 代码是id = 'key',查询按钮的 css 代码是 class = “button”
# 下面是使用 selenium 调用 chrome 浏览器在所搜框输入关键字 “计算机书籍” 并点击查询安妮u发出查询请求的代码

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pyquery import PyQuery as pq
import time
# 通过 chrome 浏览器打开chrome 浏览器
broswer = webdriver.Chrome()
# 访问京东网站
broswer.get("http://www.jd.com")
# 等待 50 秒
wait = WebDriverWait(broswer, 50)
# 通过 css 选择器的 id 获得输入框
input = broswer.find_element_by_id("key")
# 在输入框中输入要查询的信息
input.send_keys('计算机书籍')
# 获取查询的按钮
submit_button = broswer.find_element_by_class_name("button")
# 点击搜索按钮
submit_button.click()

# 上面代码成功启动 chrome浏览器，自动完成搜索框中输入关键字点击查询按钮的操作


# 模拟下滑到底部的操作
for i in range(1,5):
    broswer.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

# 商品列表的总页数
total = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b')
    )
)

html = broswer.page_source.replace('xmlns', 'another_attr')

doc = pq(html)
# 一个商品是放在class = “get-item” 的li节点内， items()方法是获取所有的商品列表
li_list = doc('.gl-item').items()

# 循环分析每个商品的信息

for item in li_list:
    image_html = item('.gl-item .p-img')
    book_img_url = item.find('img').attr('data-lazy-img')
    if book_img_url == "done":
        book_img_url = item.find("img").attr("src")
    print("t图片地址："+ book_img_url)
    item('p-name').find('font').remove()
    book_name = item.find('p-name').find("em").text()
    print("图书名称："+ book_name)
    price = item('.p-price').find('em').text() + str(item('.p-price').find('i').text())
    print('价格：' + price)
    commit = item('.p-commit').find('strong').text()
    print('评价数量：' + commit)
    shopnum = item('.p-shopnum').find('a').text()
    print('出版社：' + shopnum)
    print('++++++++++++++++++++++++++++++++++++++++++++')

def next_page():
    """
    获取“下一页”按钮，然后调用 click 方法
    :return:
    """
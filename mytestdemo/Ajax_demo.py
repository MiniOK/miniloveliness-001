import requests
from urllib.parse import urlencode

# 出处：https://www.cnblogs.com/airnew/p/10085424.html

# 目前很多网站都使用ajax技术动态加载数据，和常规的网站不一样，数据是动态加载的
# 如果我们使用常规的方式爬取网页的话，得到的只是一堆 html 代码，没有任何数据。

# 请看如下代码：
# url = 'https://www.toutiao.com/search/?keyword=美女'
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
# response = requests.get(url,headers=headers)
# print(response.text)


def parse_ajax_web(offset):
    url = 'https://www.toutiao.com/search_content/?'
    # 请求头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
        # referer作用：防盗链 具体查看站点-->https://blog.csdn.net/shenqueying/article/details/79426884
        "referer": "https://www.toutiao.com/search/",
        'x-requested-with': 'XMLHttpRequest'
    }
    # 每个ajax请求要传递的参数
    parm = {
        "aid": 24,
        "app_name": "web_search",
        "offset": offset,
        "format": "json",
        # 'offset': offset,
        # 'format': 'json',
        'keyword': '美女',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    # 构造ajax请求url
    ajax_url = url + urlencode(parm)
    # 调用ajax请求
    response = requests.get(ajax_url, headers=headers)
    # ajax请求返回的是json数据，通过调用json()方法得到json数据
    json = response.json()
    data = json.get('data')
    # print(data)
    for item in data:
        if item.get('title') is not None:
            print(item.get('title'))


def main():
    # 调用ajax的次数，这里调用5次。
    for offset in (range(0, 5)):
        parse_ajax_web(offset * 20)


if __name__ == '__main__':
    main()

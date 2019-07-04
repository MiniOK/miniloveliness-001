from selenium import webdriver

"""

                
                
                
    selenium作者地址：https://www.cnblogs.com/Snail-offort/p/8761652.html
    HTTP请求报文和HTTP响应报文：https://blog.csdn.net/a_fool_program_ape/article/details/81748544
    
    一、Selenium 爬虫入门
　　Selenium 的初衷是打造一款优秀的自动化测试工具，
但是慢慢的人们就发现，Selenium 的自动化用来做爬虫正合适。
我们知道，传统的爬虫通过直接模拟 HTTP 请求来爬取站点信息，
由于这种方式和浏览器访问差异比较明显，很多站点都采取了一些反爬的手段，
而 Selenium 是通过模拟浏览器来爬取信息，其行为和用户几乎一样，
反爬策略也很难区分出请求到底是来自 Selenium 还是真实用户。
而且通过 Selenium 来做爬虫，不用去分析每个请求的具体参数，
比起传统的爬虫开发起来更容易。Selenium 爬虫唯一的不足是慢，
如果你对爬虫的速度没有要求，那使用 Selenium 是个非常不错的选择。
Selenium 提供了多种语言的支持（Java、.NET、Python、Ruby 等），
不论你是用哪种语言开发爬虫，Selenium 都适合你。


    实践出真知
                代理是爬虫开发人员永恒的话题
                    浏览器大抵有五种代理设置方式，
                    第一种是直接使用系统代理，
                    第二种是使用浏览器自己的代理配置，
                    第三种通过自动检测网络的代理配置，这种方式利用的是 WPAD 协议，让浏览器自动发现代理服务器，
                    第四种是使用插件控制代理配置，譬如 Chrome 浏览器的 Proxy SwitchyOmega 插件，
                    最后一种比较少见，是通过命令行参数指定代理。这五种方式并不是每一种浏览器都支持
                    
                    
                    
"""

browser = webdriver.Chrome()
browser.get("http://www.douban.com/")
#!/usr/bin/env python
# coding=utf-8
'''
爬取小说
'''

import urllib2
import re
from bs4 import BeautifulSoup


# GB2312汉字编码库， GBK扩展版
# 根据 url发送 request 请求，获取服务器相应内容
def OpenPage(url):
    # 构造请求头
    Myheaders = {}
    # 构造request请求
    req = urllib2.Request(url, headers=Myheaders)
    # 激活 request 请求， 向服务器端发送请求
    # 服务器端的响应被获取， 一种类文本的对象
    f = urllib2.urlopen(req)
    # decode解码函数 encode编码函数
    data = f.read()
    # 从 GBK 解码，再编码为 utf-8
    # 错误处理方式：ignore replace
    data = data.decode("GBK", errors="ignore").encode("utf-8")
    return data


def Test1():
    # print OpenPage("http://www.shengxu6.com/book/2967.html")
    print OpenPage("http://www.shengxu6.com/read/2967_2008176.html")


# 解析主页内容，获取各个章节的 url 网址
def ParseMainPage(page):
    soup = BeautifulSoup(page, "html.parser")
    # re.compile Pattern对象
    GetUrl = soup.find_all(href=re.compile("read"))
    # 每一个元素都是一个类的实例化对象
    UrlList = []
    for item in GetUrl:
        UrlList.append("http://www.shengxu6.com" + item["href"])
    return UrlList


def Test2():
    page = OpenPage("http://www.shengxu6.com/book/2967.html")
    List = ParseMainPage(page)
    print List


#解析章节内容，获取标题与正文
def ParseDetailPage(page):
    soup = BeautifulSoup(page,"html.parser")


if __name__ == "__main__":
    Test1()

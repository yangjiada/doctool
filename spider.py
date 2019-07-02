#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan Yang
@software: PyCharm Community Edition
@time: 2019/5/24 18:17
"""


import requests
import time
import html2markdown
import tomd

from lxml.etree import HTML
from lxml import etree
from urllib.parse import urljoin

from settings import HEADERS


def crawl_links(url, xpath):
    # links = []
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        tree = HTML(response.text)
        links = tree.xpath(xpath)
        links = [('{}.{}'.format(i+1, j), urljoin(response.url, j)) for i, j in enumerate(links)]
        print(links)
        return links

def download(url, to_file, remove_xpath=None):
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        response.encoding = 'utf-8'
        tree = HTML(response.content)
        # tree.remove(tree.xpath(remove_xpath))
        # print(tree.tostring(pretty_print=True))
        # print(response.content)
        # print(etree.to)
        html2md(response.text, 'test.md')
        # with open(to_file, 'wb') as f:

            # f.write(response.content)
            # print(response.text)
            # print()
            # print(response.content)
            # x = etree.tounicode(tree.xpath(remove_xpath)[0])
            # print(response.text.replace(x, ''))
            # print()
            # print(etree.tounicode(tree).encode())
            # f.write(etree.tounicode(tree).encode())
        # print(etree.tostring(tree))
        #     print(type(response.content))

def html2md(html, to_file):
    with open('1.html', 'r', encoding='utf-8') as f:
        text = f.read()

    with open(to_file, 'wb') as f:
        f.write(tomd.convert(text).encode())



if __name__ == '__main__':
    # crawl_links('https://docs.scrapy.org/en/latest', "//li[@class='toctree-l1']/a[@class='reference internal']/@href")
    # download('http://docs.scrapy.org/en/latest/intro/overview.html', 'overview.html', '//html/body/div[1]/nav/div')
    html2md('s', 'test.md')
    # print(html2markdown.convert('<h2>Test</h2><pre><code>Here is some code</code></pre>'))
    # print(type('<h2>Test</h2><pre><code>Here is some code</code></pre>'))
    # print(html2markdown.convert("""<h1>Scrapy一目了然</h1>"""))
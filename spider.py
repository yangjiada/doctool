#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan Yang

"""


import requests
import time
import html2markdown
import tomd
import os
import lxml.etree as et

from lxml.etree import HTML
from lxml import etree
from urllib.parse import urljoin

from settings import HEADERS
from trans import *


def crawl_links(url, xpath):
    """ 获取指定链接
    """
    # links = []
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        tree = HTML(response.text)
        links = tree.xpath(xpath)
        links = [('{}.html'.format(i), urljoin(response.url, j)) for i, j in enumerate(links)]
        print(links)
        return links

def download_links(url, xpath):
    """ 下载所有链接
    """
    links = crawl_links(url, xpath)

    for name, link in links:
        download(link, name)


def download(url, filename, remove_xpath=None):
    """ 下载单个链接
    """
    response = requests.get(url, headers=HEADERS)
    save_path = 'html/'
    if os.path.exists(save_path):
        pass
    else:
        os.makedirs(save_path)

    if response.status_code == 200:
        response.encoding = 'utf-8'
        tree = HTML(response.content)
        
        # tree = tree.remove(tree.xpath(remove_xpath))
        # print(tree.tostring(pretty_print=True))

        # print(et.tostring(tree, encoding='utf-8', pretty_print=True))
        with open(save_path+filename, 'wb') as f:
            f.write(et.tostring(tree, encoding='utf-8', pretty_print=True))

            # f.write(response.content)
            # f.write(etree.tounicode(tree).encode())

def html2md(html, to_file):
    with open('1.html', 'r', encoding='utf-8') as f:
        text = f.read()

    with open(to_file, 'wb') as f:
        f.write(tomd.convert(text).encode())



if __name__ == '__main__':
    # crawl_links('https://docs.scrapy.org/en/latest', "//li[@class='toctree-l1']/a[@class='reference internal']/@href")
    # download('http://docs.scrapy.org/en/latest/intro/overview.html', 'overview.html', '//html/body/div[1]/nav/div')
    download_links('https://docs.scrapy.org/en/latest', "//li[@class='toctree-l1']/a[@class='reference internal']/@href")
    # html2md('s', 'test.md')
    # print(html2markdown.convert('<h2>Test</h2><pre><code>Here is some code</code></pre>'))
    # print(type('<h2>Test</h2><pre><code>Here is some code</code></pre>'))
    # print(html2markdown.convert("""<h1>Scrapy一目了然</h1>"""))
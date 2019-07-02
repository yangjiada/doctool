#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan Yang
@software: PyCharm Community Edition
@time: 2019/5/24 18:18
"""

NAME = ''

URL = ''

LINK = '#leftcolumn a'

HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "zh-cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cache-Control": "no-cache"
}

"""
fname：保存的文件名称
url：目录页 URL
link：链接<a>的选择器
base：链接<a>的前缀
title：文章页的标题选择器
content：文章页的内容选择器
remove：文章页需要移除的元素的选择器
credit：是否显示原文链接
processMath：是否处理 TeX 公式
processDecl：是否处理 sphinx 类定义
hdrs：HTTP 请求的协议头
list：如果这个列表不为空，则抓取这个列表，忽略url
"""
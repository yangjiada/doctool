
> 原文：[ https://docs.scrapy.org/en/latest/intro/overview.html ](https://docs.scrapy.org/en/latest/intro/overview.html)

# Scrapy一目了然

Scrapy是一种用于抓取网站和提取结构化数据的应用程序框架，可用于广泛的有用应用程序，如数据挖掘，信息处理或历史存档。

尽管Scrapy最初是为[网页抓取](https://en.wikipedia.org/wiki/Web_scraping)设计的，但它也可以用于使用API​​（例如[ Amazon Associates Web Services ](https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html)）或作为通用网络爬虫来提取数据。

## 一个示例蜘蛛的走过

为了向您展示Scrapy带来的内容，我们将以最简单的方式运行蜘蛛，向您介绍Scrapy Spider的示例。

这是一个蜘蛛的代码，它在网页[ http://quotes.toscrape.com ](http://quotes.toscrape.com)上删除着名的引号，然后分页：

把它放在一个文本文件中，将其命名为`  quotes_spider.py  `并使用[ `  runspider  ` [运行蜘蛛] HTG9]命令：](../topics/commands.html#std:command-runspider)

完成后，您将在`  quotes.json  `文件中包含JSON格式的引号列表，其中包含文本和作者，如下所示（为了更好的可读性，此处重新格式化）：

### 刚刚发生了什么？

当您运行命令`  scrapy   runspider   quotes_spider.py  `时，Scrapy在其中查找Spider定义并通过其爬虫引擎运行它。

通过向`  start_urls  `属性中定义的URL发出请求（在这种情况下，只有** humor **类别中的引号的URL）并且调用默认值回调方法` 解析 `，将响应对象作为参数传递。在` 解析 `回调中，我们使用CSS Selector循环遍历quote元素，生成带有提取的引用文本和作者的Python dict，查找指向下一页和日程表的链接另一个请求使用相同的` 解析 `方法作为回调。

在这里你会注意到Scrapy的一个主要优点：请求[ 被异步调度和处理 ](../topics/architecture.html#topics-architecture)。这意味着Scrapy不需要等待请求完成和处理，它可以在此期间发送另一个请求或执行其他操作。这也意味着即使某些请求失败或在处理错误时发生错误，其他请求也可以继续运行。

虽然这使您能够进行非常快速的爬网（以容错的方式同时发送多个并发请求），Scrapy还可以通过[ 进行一些设置来控制爬行的礼貌](../topics/settings.html#topics-settings-ref)。您可以执行以下操作：在每个请求之间设置下载延迟，限制每个域或每个IP的并发请求数量，甚至[ 使用自动限制扩展 ](../topics/autothrottle.html#topics-autothrottle)试图找出这些自动。

注意

这是使用[  Feed导出 ](../topics/feed-exports.html#topics-feed-exports)生成JSON文件，您可以轻松更改导出格式（例如XML或CSV）或存储后端（FTP或[ Amazon S3 ](https://aws.amazon.com/s3/)，例如）。您还可以编写[ 项目管道 ](../topics/item-pipeline.html#topics-item-pipeline)来存储数据库中的项目。

## 还有什么？

您已经了解了如何使用Scrapy从网站中提取和存储项目，但这只是表面。 Scrapy提供了许多强大的功能，可以轻松高效地进行抓取，例如：

- 内置支持[ 使用扩展的CSS选择器和XPath表达式从HTML / XML源中选择和提取 ](../topics/selectors.html#topics-selectors)数据，并使用正则表达式提取辅助方法。
- 一个[ 交互式shell控制台 ](../topics/shell.html#topics-shell)（知道IPy）用于尝试使用CSS和XPath表达式来抓取数据，在编写或调试蜘蛛时非常有用。
- 内置支持[ 以多种格式（JSON，CSV，XML）生成Feed  ](../topics/feed-exports.html#topics-feed-exports)并将其存储在多个后端（FTP，S3，本地文件系统）中
- 强大的编码支持和自动检测，用于处理外部，非标准和损坏的编码声明。
- [ 强大的可扩展性支持 ](../index.html#extending-scrapy)，允许您使用[ 信号 ](../topics/signals.html#topics-signals)和定义良好的API（中间件，[）插入您自己的功能扩展 ](../topics/extensions.html#topics-extensions)和[ 管道 ](../topics/item-pipeline.html#topics-item-pipeline)）。
<li>广泛的内置扩展和中间件用于处理：<ul>
- cookie和会话处理
- HTTP功能，如压缩，身份验证，缓存
- 用户代理欺骗
- 的robots.txt
- 爬行深度限制
- 和更多

## 下一步是什么？

接下来的步骤是[ 安装Scrapy  ](install.html#intro-install)，[ 按照教程 ](tutorial.html#intro-tutorial)学习如何创建一个完整的Scrapy项目和[加入社区](https://scrapy.org/community/)。谢谢你的关注！

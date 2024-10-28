from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quote_scrapy_project.spiders.quotes import QuotesSpider

process = CrawlerProcess(settings=get_project_settings())

process.crawl(QuotesSpider)

process.start()
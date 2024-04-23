import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class DocumentSpider(CrawlSpider):
    name = 'document_spider'

    def __init__(self, seed_url, max_pages, max_depth, *args, **kwargs):
        super(DocumentSpider, self).__init__(*args, **kwargs)
        self.start_urls = [seed_url]
        self.allowed_domains = [seed_url.split('//')[-1].split('/')[0]]
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.count = 0

    rules = (
        Rule(LinkExtractor(allow=(), unique=True), callback='parse', follow=True),
    )

    def parse(self, response):
        if self.count < self.max_pages:
            self.count += 1
            # Extract title and content
            title = response.xpath('//h1/text()').get()
            content = ' '.join(response.xpath('//p//text()').getall())
            yield {
                'title': title,
                'content': content
            }
            # Save crawled data to natural.txt
            with open('natural.txt', 'a', encoding='utf-8') as f:
                f.write(f'Title: {title}\n\nContent: {content}\n\n')

def run_spider(seed_url, max_pages, max_depth):
    process = CrawlerProcess(settings={
        'LOG_LEVEL': 'INFO',
        'CLOSESPIDER_PAGECOUNT': max_pages,
        'DEPTH_LIMIT': max_depth,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'CONCURRENT_REQUESTS': 8,  # Concurrent crawling
        'AUTOTHROTTLE_ENABLED': True,  # AutoThrottle
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 0.5,  # Target concurrency
        'AUTOTHROTTLE_START_DELAY': 5,  # Initial delay
        'AUTOTHROTTLE_MAX_DELAY': 60,  # Maximum delay
        'AUTOTHROTTLE_DEBUG': True,  # Debug mode
    })
    process.crawl(DocumentSpider, seed_url=seed_url, max_pages=max_pages, max_depth=max_depth)
    process.start()

# usage on Wikipedia natural language specifically
run_spider('https://en.wikipedia.org/wiki/Natural_language_processing', 20, 3)

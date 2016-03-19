BOT_NAME = 'cdep'
SPIDER_MODULES = ['cdep.spiders']
NEWSPIDER_MODULE = 'cdep.spiders'

# TODO USER_AGENT = 'cdep (+http://www.yourdomain.com)'

CONCURRENT_REQUESTS=1
COOKIES_ENABLED=False

DOWNLOADER_MIDDLEWARES = {
  'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 1,
}
HTTPCACHE_ENABLED = True
HTTPCACHE_GZIP = True

BOT_NAME = 'weberetikettenbg'

SPIDER_MODULES = ['weberetikettenbg.spiders']
NEWSPIDER_MODULE = 'weberetikettenbg.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'weberetikettenbg.pipelines.WeberetikettenbgPipeline': 100,

}
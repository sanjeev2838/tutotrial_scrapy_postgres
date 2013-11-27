# Scrapy settings for living_social project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'living_social'

SPIDER_MODULES = ['living_social.spiders']
NEWSPIDER_MODULE = 'living_social.spiders'
DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'username': 'postgres',
	'password': '',
	'database': 'scrape'
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'living_social (+http://www.yourdomain.com)'
ITEM_PIPELINES = {'living_social.pipelines.LivingSocialPipeline' :300}

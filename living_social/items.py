# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class LivingSocialItem(Item):
    """Livingsocial container (dictionary-like object) for scraped data"""
    title = Field()
    description = Field()
    link = Field()
    category = Field()
    location = Field()
    original_price = Field()
    price = Field()

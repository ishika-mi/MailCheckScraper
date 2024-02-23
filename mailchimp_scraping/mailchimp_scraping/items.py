# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MailchimpScrapingItem(scrapy.Item):
    # Define the fields for your item here like:
    url = scrapy.Field()
    alphabet = scrapy.Field()
    domain_names = scrapy.Field()

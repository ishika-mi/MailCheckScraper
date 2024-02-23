import scrapy
import json
import os
from .utils import extract_with_xpath_get_all, extract_with_xpath


class MailcheckSpider(scrapy.Spider):
    name = "mailcheck"
    allowed_domains = ["mailcheck.ai"]

    def start_requests(self):
        """
        Entry point for the spider. Initiates the scraping process.
        """
        yield scrapy.Request(url='https://www.mailcheck.ai/', callback=self.parse)

    def parse(self, response):
        """
        Parses the given response using XPath to extract domain links and their associated alphabet.
        Parameters:
            - response: the response object to be parsed
        Returns:
            - None
        """
        all_domain_link = response.xpath("//a[contains(@title,'Domains starting with')]")
        for domain in all_domain_link:
            url = extract_with_xpath(domain, xpath="./@href")
            alphabet = extract_with_xpath(domain, xpath="./@title").replace('Domains starting with ', '')
            yield scrapy.Request(url=url, callback=self.parse_domain_page, meta={'alphabet': alphabet})

    def parse_domain_page(self, response):
        """
        Parses the given response using XPath to extract domain names.
        Parameters:
            - response: the response object to be parsed
        Returns:
            - None
        """
        current_page_domain_names = extract_with_xpath_get_all(response, "//a[contains(@title,'View domain')]//text()")
        current_page_domain_names = [name.strip().replace('\n', '') for name in current_page_domain_names]
        alphabet = response.meta['alphabet']
        self.save_to_json(alphabet, current_page_domain_names)

        if next_page := extract_with_xpath(response, xpath="//a[contains(@rel,'next')]/@href"):
            yield scrapy.Request(next_page, callback=self.parse_domain_page, meta={'alphabet': alphabet})

    def save_to_json(self, alphabet, current_page_domain_names):
        """
        Saves the given domain names to a JSON file.
        Parameters:
            - alphabet: the alphabet associated with the domain names
            - current_page_domain_names: the domain names to be saved
        Returns:
            - None
        """
        filename = 'result.json'
        data = {}

        if os.path.exists(filename):
            with open(filename, 'r') as json_file:
                data = json.load(json_file)

        if alphabet in data:
            data[alphabet].extend(current_page_domain_names)
        else:
            data[alphabet] = current_page_domain_names

        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        self.log(f'Saved data for alphabet "{alphabet}" to {filename}')

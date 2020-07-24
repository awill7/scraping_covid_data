import scrapy


class TrendingSpider(scrapy.Spider):
    name = "trendy"
    start_urls = ["https://apps.npr.org/dailygraphics/graphics/coronavirus-d3-us-map-20200312/table.html?initialWidth=1238&childId=responsive-embed-coronavirus-d3-us-map-20200312-table&parentTitle=Coronavirus%20Map%20And%20Graphics%3A%20Track%20The%20Spread%20In%20The%20U.S.%20%3A%20Shots%20-%20Health%20News%20%3A%20NPR&parentUrl=https%3A%2F%2Fwww.npr.org%2Fsections%2Fhealth-shots%2F2020%2F03%2F16%2F816707182%2Fmap-tracking-the-spread-of-the-coronavirus-in-the-u-s%2Frobots.txt"]

    def parse(self, response):
        states = response.css('.stateName::text').getall()
        states = states[1:53]
        states = [item.strip() for item in states]
        print(states)


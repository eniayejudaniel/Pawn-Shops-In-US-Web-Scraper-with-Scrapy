import scrapy

class PawnShopInUS(scrapy.Spider):
    name = "pawn_shop"
    allowed_domains = ["www.pawnshops.net"]
    start_urls = ["https://www.pawnshops.net/search.php?whatcountry=US&whatstate=&s=1"]
    page = 1

   
    def parse(self, response):
        link = response.css('a[href^="https://www.pawnshops.net/store/"]::attr(href)').getall()
        for url in link:
            yield scrapy.Request(url, callback=self.parse_pawnshop_details)
        
        next_page = f"https://www.pawnshops.net/search.php?whatcountry=US&whatstate=&s={str(PawnShopInUS.page)}"
        if PawnShopInUS.page < 1292:
            yield scrapy.Request(next_page, callback=self.parse)
            PawnShopInUS.page += 1

    def parse_pawnshop_details(self, response):
        pawnshop_name = response.css('span[itemprop="name"]::text').get()
        street_address = response.css('span[itemprop="streetAddress"]::text').get()
        locality = response.css('span[itemprop="addressLocality"]::text').get()
        region = response.css('span[itemprop="addressRegion"]::text').get()
        postal_code = response.css('span[itemprop="postalCode"]::text').get()
        telephone = response.css('span[itemprop="telephone"] a::text').get()

        yield {
            'name': pawnshop_name.strip() if pawnshop_name else '',
            'street_address': street_address.strip() if street_address else '',
            'locality': locality.strip() if locality else '',
            'region': region.strip() if region else '',
            'postal_code': postal_code.strip() if postal_code else '',
            'telephone': telephone.strip() if telephone else '',
        }

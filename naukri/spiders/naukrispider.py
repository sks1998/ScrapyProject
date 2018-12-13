import scrapy
from naukri.items import NaukriItem
from scrapy.loader import ItemLoader

class NaukriSpider(scrapy.Spider):
    name = "naukrispider"
    # crawl url
    start_urls = ['https://www.naukri.com/data-analytics-jobs-in-delhi-ncr']
    #https://www.naukri.com/data-analytics-jobs-in-delhi-ncr-2'
    #'https://www.naukri.com/data-analytics-jobs-in-delhi-ncr-3'
    #'https://www.naukri.com/data-analytics-jobs-in-delhi-ncr-4'
    #'https://www.naukri.com/data-analytics-jobs-in-delhi-ncr-5'

    # response parser function
    def parse(self, response):

        all_jobs = response.css('.row')

        # Fetching the rows
        for jobs in all_jobs:
            job_loader = ItemLoader(NaukriItem(), selector=jobs)
            try:
                # Scraping the fields using their HTML attributes
                job_loader.add_css("job_title", '.desig::text')
                job_loader.add_css("exp_req", 'span.exp::text')
                job_loader.add_css("loc", 'span.loc span::text')
                job_loader.add_css("comp_name", 'span.org::text')
                job_loader.add_css("job_desp_page", '.content::attr(href)')
                job_loader.add_css("key_skills", 'span.skill::text')
                job_loader.add_css("job_desp", 'span.desc::text')
                job_loader.add_css("sal", 'span.salary::text')
            #job_loader.add_css(posted_by, 'a.rec_name.active::text')
            #job_loader.add_css(posted_on, 'div.rec_details span.date::text')
            except:
                continue
            
        
            yield job_loader.load_item()

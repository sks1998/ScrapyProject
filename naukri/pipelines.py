# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NaukriPipeline(object):
    def process_item(self, item, spider):
        try:
            item['comp_name']
            if(item['comp_name']=='Not Mentioned'):
                item['comp_name']='N/A'
        except:
            raise print("not available")
            pass
        
        try :
            item['job_title']    
        except KeyError:
            item['job_title'] = 'N/A'
            
        try:
          item['exp_req']  
        except KeyError:
            item['exp_req'] = 'N/A'    
        
        try:
          item['loc']    
        except KeyError:
            item['loc'] = 'N/A'

        

        try :
            item['key_skills']
        except KeyError:
            item['key_skills'] = 'N/A'
        
        try :
            item['job_desp']
        except KeyError:
            item['job_desp'] = 'N/A'

        try :
            item['sal']
        except KeyError:
            item['sal'] = 'N/A'

        try :
            item['job_desp_page']
        except KeyError:
            item['job_desp_page'] = 'N/A'

        return item


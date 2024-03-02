from webScraping.components.data_extraction import DataExtraction
from webScraping.utils import getFullUrl

class CancerTypesPipeline:

    def extract(self, url='https://www.cancer.net/cancer-types'):
        try:
            data_extraction = DataExtraction('cancer-types')
            cancer_catalogs = data_extraction.get_cancer_catalogs(url)
            for cancer_catalog in cancer_catalogs:
                try:
                    cancer_types = cancer_catalog.select('.view .view-content .item-list ul li')
                    for cancer_type in cancer_types:
                        try:
                            base_url = getFullUrl(cancer_type.find('a').get('href'))
                            cancer_name = base_url.split('/')[-1]       
                            cancer_details_url = data_extraction.get_cancer_details_url(base_url)
                            cancer_details = data_extraction.get_cancer_details(cancer_details_url, cancer_name)
                        except:
                            continue
                except:
                    continue

        except Exception as e:
            pass
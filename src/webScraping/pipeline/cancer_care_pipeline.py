from webScraping.components.data_extraction import DataExtraction


class CancerCarePipipine:

    def extract(self, url='https://www.cancer.net/navigating-cancer-care'):
        try:
            data_extraction = DataExtraction('cancer-care')
            sections = data_extraction.get_sections(url)
            for section_url in sections:
                try:
                    section_topics = data_extraction.get_section_topics(section_url)
                    for section_topic_url in section_topics:
                        try:
                            data_extraction.get_topic_content(section_topic_url)
                        except:
                            continue
                except:
                    continue

        except Exception as e:
            pass
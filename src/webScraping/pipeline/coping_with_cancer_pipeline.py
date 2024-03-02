from webScraping.components.data_extraction import DataExtraction


class CopingWithCancerPipipine:

    def extract(self, url='https://www.cancer.net/coping-with-cancer'):
        try:
            data_extraction = DataExtraction('coping-with-cancer')
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
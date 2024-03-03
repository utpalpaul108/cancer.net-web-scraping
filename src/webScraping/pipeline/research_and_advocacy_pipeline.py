from webScraping.components.data_extraction import DataExtraction


class ResearchAndAdvocacyPipipine:

    def extract(self, url='https://www.cancer.net/research-and-advocacy'):
        try:
            data_extraction = DataExtraction('research-and-advocacy')
            sections = data_extraction.get_sections(url)
            for section_url in sections:
                try:
                    section_topics = data_extraction.get_section_topics(section_url)
                    for section_topic_url in section_topics:
                        try:
                            data_extraction.get_topic_content(topic_url=section_topic_url)
                        except:
                            continue
                except:
                    continue

        except Exception as e:
            pass
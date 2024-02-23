from webScraping.pipeline.research_and_advocacy_pipeline import ResearchAndAdvocacyPipipine
from webScraping.pipeline.survİvorshİp_pipeline import SurvivorshipPipipine

if __name__ == '__main__':
    # Extract Research and Advocacy
    # research_and_advocacy = ResearchAndAdvocacyPipipine()
    # research_and_advocacy.extract()

    # Extract Survivorship
    survivorship = SurvivorshipPipipine()
    survivorship.extract()

from webScraping.pipeline.research_and_advocacy_pipeline import ResearchAndAdvocacyPipipine
from webScraping.pipeline.survİvorshİp_pipeline import SurvivorshipPipipine
from webScraping.pipeline.blog_posts_pipeline import BlogPostsPipipine
from webScraping.pipeline.cancer_types_pipeline import CancerTypesPipeline
from webScraping.pipeline.cancer_care_pipeline import CancerCarePipipine
from webScraping.pipeline.coping_with_cancer_pipeline import CopingWithCancerPipipine

if __name__ == '__main__':
    # Extract Types of Cancer
    cancer_types = CancerTypesPipeline()
    cancer_types.extract()

    # Extract Cancer Care
    cancer_care = CancerCarePipipine()
    cancer_care.extract()

    # Extract Coping With Cancer
    coping_with_cancer = CopingWithCancerPipipine()
    coping_with_cancer.extract()

    # Extract Research and Advocacy
    research_and_advocacy = ResearchAndAdvocacyPipipine()
    research_and_advocacy.extract()

    # Extract Survivorship
    survivorship = SurvivorshipPipipine()
    survivorship.extract()

    # Extract Blog Posts
    blog_posts = BlogPostsPipipine()
    blog_posts.extract()


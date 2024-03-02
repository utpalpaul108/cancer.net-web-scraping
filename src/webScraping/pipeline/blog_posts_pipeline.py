from webScraping.components.data_extraction import DataExtraction


class BlogPostsPipipine:

    def extract(self, url='https://www.cancer.net/blog'):
        try:
            data_extraction = DataExtraction('blog')
            pages = data_extraction.get_total_blog_pages(url)
            
            for page in pages:
                try:
                    blog_posts = data_extraction.get_blog_posts(page)
                    for blog_post_url in blog_posts:
                        try:
                            data_extraction.get_topic_content(blog_post_url)
                        except:
                            continue
                except:
                    continue

        except Exception as e:
            pass
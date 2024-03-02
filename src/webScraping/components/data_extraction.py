# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import re

from webScraping.constants import *
from webScraping.utils import getSectionUrl, getFullUrl


class DataExtraction:

    def __init__(self, dir_name):
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
        self.dir_path = os.path.join('artifacts','data',dir_name)
        self.skip_contents = skip_contents
        self.partially_skip_contents = partially_skip_contents
        os.makedirs(self.dir_path, exist_ok=True)
        

    def get_sections(self, URL):
    
        response = requests.get(URL, headers = self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        sections_url = []
        sections = soup.find('article')
        sections = sections.find('div', class_='field-name-field-page-sub-pages').find('div', class_='field-items')
        sections = sections.find_all('article')
        

        for section in sections:
            sections_url.append(getSectionUrl(section))

        return sections_url
    

    def get_section_topics(self, section_url):
        response = requests.get(section_url, headers = self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        section_topics_url = []
        section_topics = soup.find('article')
        
        if section_topics is not None:
            section_topics = section_topics.find('div',class_='field-name-field-page-sub-pages')
        if section_topics is None:
            self.get_topic_content(section_url)
        
        else:
            section_topics = section_topics.find('div',class_='field-items')

            for section_topic in section_topics:
                section_topics_url.append(getSectionUrl(section_topic))
        
        return section_topics_url
    

    def get_total_blog_pages(self, base_url='https://www.cancer.net/blog', single_page_url='https://www.cancer.net/blog?page='):
        response = requests.get(base_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        total_pages = []
        pages = soup.find('li', {'class': 'pager-last'})
        if pages is not None:
            total_pages = int(pages.a['href'].split('=')[-1])
            total_pages = [(single_page_url + str(page_no)) for page_no in range(1, (total_pages+1))]

        return total_pages
    

    def get_blog_posts(self, page_url):
        response = requests.get(page_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        all_posts = []
        posts = soup.find('div',{'class' : 'view-content'})
        if posts is not None:
            posts = posts.find_all('div', {'class' : 'views-row'})
            for post in posts:
                blog_post_url = post.find('div',{'class' : 'views-field-title'}).a['href']
                all_posts.append(getFullUrl(blog_post_url))
        return all_posts
    

    def get_topic_content(self, topic_url):

        response = requests.get(topic_url, headers = self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        df = {
            'question':[],
            'answer':[]
        }

        articles = soup.find_all('article')
        
        if len(articles) > 1:
            section_topics = self.get_section_topics(topic_url)
            for section_topic_url in section_topics:
                self.get_topic_content(section_topic_url)
        
        topic_name = topic_url.split('/')[-1]
        questions = soup.find_all('h3')
        skip_contents = [content.lower() for content in self.skip_contents]
        partially_skip_contents = [content.lower() for content in self.partially_skip_contents]
        questions = [question for question in questions if question.text.strip() != '' and question.text.strip().lower() not in skip_contents and not any(re.findall(r"\b(" + "|".join(partially_skip_contents) + r")\b", question.text.strip().lower()))]
        
        for question in questions:
            df['question'].append(question.text.strip())
            answer = ""
            next_element = question.find_next_sibling()
            while next_element and next_element.name != 'h3':
                answer += next_element.text.strip() + " "
                next_element = next_element.find_next_sibling()
            
            df['answer'].append(answer)

        
        if len(df['question']) > 0 and len(df['answer']) > 0:
            data_path = os.path.join(self.dir_path,topic_name+'.csv')
            df = pd.DataFrame(df)
            df.to_csv(data_path, index=False)

        
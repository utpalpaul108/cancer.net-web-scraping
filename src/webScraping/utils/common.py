

def getSectionUrl(section):
    section_url = section.select('header h3 a')[0]['href']
    if not section_url.startswith('https:'):
        section_url = 'https://www.cancer.net' + section_url
    
    return section_url
    
    
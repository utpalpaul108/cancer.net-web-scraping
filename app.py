from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

from webScraping.pipeline.research_and_advocacy_pipeline import ResearchAndAdvocacyPipipine
from webScraping.pipeline.survİvorshİp_pipeline import SurvivorshipPipipine
from webScraping.pipeline.cancer_types_pipeline import CancerTypesPipeline
from webScraping.pipeline.cancer_care_pipeline import CancerCarePipipine
from webScraping.pipeline.coping_with_cancer_pipeline import CopingWithCancerPipipine
from webScraping.pipeline.blog_posts_pipeline import BlogPostsPipipine


all_sections = {
    "cancer_types": CancerTypesPipeline(),
    "cancer_care": CancerCarePipipine(),
    "coping_with_cancer": CopingWithCancerPipipine(),
    "research_and_advocacy": ResearchAndAdvocacyPipipine(),
    "survivorship": SurvivorshipPipipine(),
    "blog_posts": BlogPostsPipipine()
}

@app.route('/')
def index():
   return render_template('index.html')


@app.route('/api/data-extraction', methods=['GET','POST'])
def new_fetch_data():
   if request.method == 'POST':
      try:
         selected_sections = request.json.get('selectedSections', [])
         if not selected_sections:
               raise BadRequest('No data provided')
         
         for selected_section in selected_sections:
            obj = all_sections.get(selected_section)
            if obj:
               obj.extract()
            
         return jsonify('Data extracted successfully')
         
      except Exception as e:
         return jsonify(str(e))
   

if __name__ == '__main__':
   app.run(debug=True)
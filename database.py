import os
from sqlalchemy import create_engine, text

db_conn_string = os.environ['DB_CONN_STRING']

engine = create_engine(db_conn_string,
                      connect_args={
                        "ssl" : {
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })

def load_skills_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('select * from skills'))
    
    skills = []
    for row in result.all():
      skills.append(dict(row._mapping))

    return skills  

def load_projects_from_db(domain):
  with engine.connect() as conn:
    result = conn.execute(
      text('select * from projects where domain=:val order by created desc'),
      {'val' : domain}
    )
    
    projects = []
    for row in result.all():
      projects.append(dict(row._mapping))

    return projects  

def get_domain_projects():
  projects = {}

  projects['ML'] = load_projects_from_db('Machine Learning')
  projects['NLP'] = load_projects_from_db('NLP')
  projects['CV'] = load_projects_from_db('Computer Vision')
  projects['WD'] = load_projects_from_db('Web Development')
  
  return projects
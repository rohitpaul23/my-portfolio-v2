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
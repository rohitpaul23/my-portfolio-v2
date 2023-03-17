from flask import Flask, render_template, jsonify
from database import load_skills_from_db, get_domain_projects

app = Flask(__name__)
  
@app.route('/')
def home():
  skills = load_skills_from_db()
  return render_template('home.html', skills=skills)

@app.route("/contact")
def contact():
  return render_template('contact.html')

@app.route("/project")
def project():
  projects = get_domain_projects()
  return render_template('project.html', projects=projects)

@app.route("/qualification")
def qualification():
  return render_template('qualification.html')


@app.route("/api/skills")
def list_skills():
  skills = load_skills_from_db()
  return jsonify(skills)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
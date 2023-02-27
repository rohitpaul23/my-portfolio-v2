from flask import Flask, render_template, jsonify

app = Flask(__name__)

SKILLS = [
  {
    'id':1,
    'name': 'Python',
    'level': 7
  },
  {
    'id':2,
    'name': 'Pandas',
    'level': 7 
  },
  {
    'id':3,
    'name': 'Numpy',
    'level': 7 
  },
  {
    'id':4,
    'name': 'JAVA',
    'level': 4 
  },
  {
    'id':5,
    'name': 'C',
    'level': 6 
  }
]


@app.route('/')
def home():
  return render_template('home.html', skills=SKILLS)

@app.route("/contact")
def contact():
  return render_template('contact.html')

@app.route("/project")
def project():
  return render_template('project.html')

@app.route("/qualification")
def qualification():
  return render_template('qualification.html')


@app.route("/api/skills")
def list_skills():
  return jsonify(SKILLS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
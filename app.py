from flask import Flask, render_template, jsonify

app = Flask(__name__)

SKILLS = [
  {
    'id':1,
    'name': 'Python',
    'icon': 'https://cdn.iconscout.com/icon/free/png-512/python-2-226051.png?f=avif&w=256',
    'level': 7
  },
  {
    'id':2,
    'name': 'Pandas',
    'icon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/1200px-Pandas_mark.svg.png',
    'level': 7 
  },
  {
    'id':3,
    'name': 'Numpy',
    'icon': 'https://seeklogo.com/images/N/numpy-logo-479C24EC79-seeklogo.com.png',
    'level': 7 
  },
  {
    'id':4,
    'name': 'Matplotlib',
    'icon': 'https://image.pngaaa.com/242/4152242-middle.png',
    'level': 6
  },
  {
    'id':5,
    'name': 'Sklearn',
    'icon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png',
    'level': 6
  },
  {
    'id':6,
    'name': 'TensorFlow',
    'icon': 'https://banner2.cleanpng.com/20180610/wis/kisspng-tensorflow-machine-learning-python-deep-learning-s-deep-learning-5b1dd8531b6746.9515387715286825791123.jpg',
    'level': 6
  },
  {
    'id':7,
    'name': 'PyTorch',
    'icon': 'https://www.clipartmax.com/png/small/476-4769276_pytorch-logo-png.png',
    'level': 5
  },
  {
    'id':8,
    'name': 'JAVA',
    'icon': 'https://cdn.iconscout.com/icon/free/png-512/java-60-1174953.png?f=avif&w=256',
    'level': 4 
  },
  {
    'id':9,
    'name': 'C',
    'icon': 'https://www.clipartmax.com/png/middle/351-3515666_c-language-global-or-external-variables-with-examples-c-programming-logo.png',
    'level': 6 
  },
  {
    'id':10,
    'name': 'C++',
    'icon': 'https://w7.pngwing.com/pngs/46/626/png-transparent-c-logo-the-c-programming-language-computer-icons-computer-programming-source-code-programming-miscellaneous-template-blue.png',
    'level': 6
  },
  {
    'id':11,
    'name': 'SQL',
    'icon': 'https://w7.pngwing.com/pngs/28/601/png-transparent-sql-logo-illustration-microsoft-azure-sql-database-microsoft-sql-server-database-blue-text-logo.png',
    'level': 7
  },
  {
    'id':12,
    'name': 'LaTex',
    'icon': 'https://i.stack.imgur.com/AarYf.png',
    'level': 7
  },
  {
    'id':13,
    'name': 'LaTex',
    'icon': 'https://cdn.freebiesupply.com/logos/large/2x/flask-logo-png-transparent.png',
    'level': 7
  },
  {
    'id':14,
    'name': 'HTML',
    'icon': 'https://w7.pngwing.com/pngs/390/229/png-transparent-logo-html5-brand-design-text-logo-number.png',
    'level': 7
  },
  {
    'id':15,
    'name': 'CSS',
    'icon': 'https://e7.pngegg.com/pngimages/893/87/png-clipart-web-development-html-cascading-style-sheets-css3-bootstrap-minimalist-resume-blue-angle.png',
    'level': 7
  },
  {
    'id':16,
    'name': 'Javascript',
    'icon': 'https://e7.pngegg.com/pngimages/602/440/png-clipart-javascript-open-logo-number-js-angle-text.png',
    'level': 5
  },
  {
    'id':17,
    'name': 'HuggingFace',
    'icon': 'https://workable-application-form.s3.amazonaws.com/advanced/production/61557f91d9510741dc62e7f8/c3635b59-a3d2-444a-b636-a9d0061dcdde',
    'level': 4
  },
  {
    'id':18,
    'name': 'Git',
    'icon': 'https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png',
    'level': 6
  },
  {
    'id':19,
    'name': 'GitHub',
    'icon': 'https://w7.pngwing.com/pngs/914/758/png-transparent-github-social-media-computer-icons-logo-android-github-logo-computer-wallpaper-banner-thumbnail.png',
    'level': 6
  },
  {
    'id':20,
    'name': 'Linux',
    'icon': 'https://w7.pngwing.com/pngs/970/403/png-transparent-tux-linux-mint-logo-linux-logo-vertebrate-bird.png',
    'level': 6
  },
  {
    'id':21,
    'name': 'replit',
    'icon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/New_Replit_Logo.svg/1200px-New_Replit_Logo.svg.png',
    'level': 5
  },
  {
    'id':22,
    'name': 'render',
    'icon': 'https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/j8z02ssteea4zj1k1nyz',
    'level': 5
  },
  {
    'id':23,
    'name': 'heroku',
    'icon': 'https://e7.pngegg.com/pngimages/855/935/png-clipart-heroku-logo-heroku-logo-icons-logos-emojis-tech-companies.png',
    'level': 5
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
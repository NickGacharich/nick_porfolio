from flask import render_template
import os
from app import app

NICK_FOLDER = os.path.join('static', 'nick_photo')
app.config['UPLOAD_FOLDER'] = NICK_FOLDER

@app.route('/')



@app.route('/index')
def index():
    user = {'username': 'Nick'}

    globe = {'globe': 'Earth'}


    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_0699.png')
    globe = os.path.join(app.config['UPLOAD_FOLDER'], 'world.jpg')
    sky = os.path.join(app.config['UPLOAD_FOLDER'], 'sky.jpg')

    hobbies = [
        {
            'topic': {'hobby': 'Drawing'}
        },
        {
            'topic': {'hobby': 'Working out'}
        },
        {
            'topic': {'hobby': 'Reading'}
        }
    ]

    skills = [
        {
            'skill': {'language': 'Python'}
        },
        {
            'skill': {'language': 'SQL'}
        },
        {
            'skill': {'language': 'C++'}
        },
        {
            'skill': {'language': 'HTML'}
        },
        {
            'skill': {'language': 'CSS'}
        },
        {
            'skill': {'language': 'javascript'}
        },
        {
            'skill': {'language': 'Flask'}
        }
    ]

    BS_degree = [
        {
            'degree': {'diploma': 'Bachelor of Science'},
            'type': {'major': 'CS'},
            'graduation': {'date': '08/10/2018'}
        }
    ]

    MS_degree = [
        {
            'degree': {'diploma': 'Master of Science'},
            'type': {'major': 'CS'},
            'graduation': {'date': '4/20/2021'}
        }
    ]
    return render_template('index.html', title='Home', user=user, hobbies=hobbies, skills=skills, BS_degree=BS_degree, MS_degree=MS_degree, user_image = full_filename, globe_image = globe, sky_image = sky)

@app.route('/projects')
def projects():
    town_square = os.path.join(app.config['UPLOAD_FOLDER'], 'town square.jpg')
    pokemon = os.path.join(app.config['UPLOAD_FOLDER'], 'pokemon .jpg')
    anime_generator= os.path.join(app.config['UPLOAD_FOLDER'], 'anime generator.jpg')

    return render_template('projects.html', town_square_img = town_square, pokemon_img = pokemon, anime_generator_img = anime_generator)
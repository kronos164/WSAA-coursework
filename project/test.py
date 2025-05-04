from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from db_keys import db


app = Flask(__name__)



app.config['MYSQL_HOST'] = db['host']
app.config['MYSQL_USER'] = db['user']
app.config['MYSQL_PASSWORD'] = db['password']
app.config['MYSQL_DB'] = db['database']

mysql = MySQL(app)

# function to get anime by value from the database

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
def index():
    if request.method == 'POST':
        
        anime = request.form
        id = anime['id']
        name = anime['name']
        jp_name = anime['jp_name']
        type = anime['type']
        episodes = anime['episodes']
        studio = anime['studio']
        release_season = anime['release_season']
        tags = anime['tags']
        rating = anime['rating']
        release_year = anime['release_year']
        end_year = anime['end_year']
        content_warning = anime['content_warning']
        if id != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE id = %s", (id,))
            anime = cursor.fetchone()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif name != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE name LIKE %s", ('%' + name + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif jp_name != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE jp_name LIKE %s", ('%' + jp_name + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif type != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE type LIKE %s", ('%' + type + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif release_season != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE release_season LIKE %s", ('%' + release_season + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif studio != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE studio LIKE %s", ('%' + studio + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif rating != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE rating LIKE %s", ('%' + rating + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif release_year != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE release_year LIKE %s", ('%' + release_year + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif end_year != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE end_year LIKE %s", ('%' + end_year + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif tags != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE tags LIKE %s", ('%' + tags + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif content_warning != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE content_warning LIKE %s", ('%' + content_warning + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        elif episodes != None:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM animes WHERE episodes LIKE %s", ('%' + episodes + '%',))
            anime = cursor.fetchall()
            if anime:
                return render_template('anime.html', anime=anime)
            else:
                return render_template('index.html', error="Anime not found")
        else:
            return render_template('index.html', error="Please enter a value to search for")

if __name__ == '__main__':
    app.run(debug=True)
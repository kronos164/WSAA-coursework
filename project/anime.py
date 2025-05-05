from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from db_keys import db


app = Flask(__name__)



app.config['MYSQL_HOST'] = db['host']
app.config['MYSQL_USER'] = db['user']
app.config['MYSQL_PASSWORD'] = db['password']
app.config['MYSQL_DB'] = db['database']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
def new_id():
    cursor = mysql.connection.cursor()
    resultValue = cursor.execute("SELECT id FROM animes ORDER BY id DESC LIMIT 1")
    if resultValue > 0:
        last_id = cursor.fetchone()[0]
        return last_id + 1
    return 1

@app.route('/search', methods=['POST'])

def search():
    anime_id = request.form['id']
    if anime_id != '':
        cursor = mysql.connection.cursor()
        resultValue = cursor.execute("SELECT * FROM animes WHERE id = %s", (anime_id,))
        if resultValue > 0:
            animeDetails = cursor.fetchall()
            return render_template('oneanime.html', animeDetails=animeDetails)
        else:
            return render_template('animenotfound.html')
    else:
        cursor = mysql.connection.cursor()
        resultValue = cursor.execute("SELECT * FROM animes")
        if resultValue > 0:
            animeDetails = cursor.fetchall()
            return render_template('anime.html', animeDetails=animeDetails)
        else:
            return render_template('animenotfound.html')
        
@app.route('/all', methods=['POST'])

def all_anime():
    cursor = mysql.connection.cursor()
    resultValue = cursor.execute("SELECT * FROM animes")
    if resultValue > 0:
        animeDetails = cursor.fetchall()
        return render_template('anime.html', animeDetails=animeDetails)
    else:
        return render_template('animenotfound.html')
        
@app.route('/add', methods=['POST'])

def redirect():
    return render_template('add.html')


@app.route('/added', methods=['POST'])


def add_anime():
    id = new_id()
    name = request.form['name']
    jp_name = request.form['jp_name']
    type = request.form['type']
    episodes = request.form['episodes']
    studio = request.form['studio']
    release_season = request.form['release_season']
    tags = request.form['tags']
    rating = request.form['rating']
    release_year = request.form['release_year']
    end_year = request.form['end_year']
    content_warning = request.form['content_warning']
    
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO animes (id, name, jp_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, content_warning) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (id, name, jp_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, content_warning))
    mysql.connection.commit()
    cursor.close()
    
    cursor = mysql.connection.cursor()
    resultValue = cursor.execute(f"SELECT * FROM animes WHERE id = {id}")
    if resultValue > 0:
        animeDetails = cursor.fetchall()
        return render_template('animeadded.html', animeDetails=animeDetails)
    else:
        return render_template('animenotfound.html')
    
@app.route('/update', methods=['POST'])
    
def update():   
    anime_id = request.form['anime_id']
    name = request.form['name']
    jp_name = request.form['jp_name']
    type = request.form['type']
    episodes = request.form['episodes']
    studio = request.form['studio']
    release_season = request.form['release_season']
    tags = request.form['tags']
    rating = request.form['rating']
    release_year = request.form['release_year']
    end_year = request.form['end_year']
    content_warning = request.form['content_warning']
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE animes SET name = %s, jp_name = %s, type = %s, episodes = %s, studio = %s, release_season = %s, tags = %s, rating = %s, release_year = %s, end_year = %s, content_warning = %s WHERE id = %s", (name, jp_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, content_warning, anime_id))
    mysql.connection.commit()
    cursor.close()
    return render_template('animeupdated.html')
    
    
@app.route('/delete', methods=['POST'])

def delete():
    anime_id = request.form['anime_id']
    if anime_id != '':
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM animes WHERE id = %s", (anime_id,))
        mysql.connection.commit()
        return render_template('animedeleted.html')
    else:
        return render_template('animenotfound.html')

if __name__ == '__main__':
    app.run(debug=True)
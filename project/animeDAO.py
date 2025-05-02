import mysql.connector as mysql
from db_credentials import db

class AnimeDAO:
    
    host = ""
    user = ""
    password = ""
    database = ""
    connection = ""
    cursor = ""
    
    def __init__(self):
    
        self.host = db['host']
        self.user = db['user']
        self.password = db['password']
        self.database = db['database']

    def getCursor(self):
        self.connection = mysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def get_anime_by_id(self, id):
        query = "SELECT * FROM animes WHERE id = %s"
        self.getCursor()
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()

    def get_all_anime(self):
        query = "SELECT * FROM animes"
        self.getCursor()
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_anime(self, id, name, jp_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, content_warning):
        query = "INSERT INTO animes (id, name, jp_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, content_warning) VALUES (%s, %s, %s)"
        self.getCursor()
        self.cursor.execute(query, (id, name, jp_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, content_warning))
        self.connection.commit()
    
    def update_anime(self, id=None, name=None, jp_name=None, type=None, episodes=None, studio=None, release_season=None, tags=None, rating=None, release_year=None, end_year=None, content_warning=None):
        query = "UPDATE animes SET "
        params = []
        if id:
            query += "id = %s, "
            params.append(id)
        if name:
            query += "name = %s, "
            params.append(name)
        if jp_name:
            query += "jp_name = %s, "
            params.append(jp_name)
        if type:
            query += "type = %s, "
            params.append(type)
        if episodes:
            query += "episodes = %s, "
            params.append(episodes)
        if studio:
            query += "studio = %s, "
            params.append(studio)
        if release_season:
            query += "release_season = %s, "
            params.append(release_season)
        if tags:
            query += "tags = %s, "
            params.append(tags)
        if rating:
            query += "rating = %s, "
            params.append(rating)
        if release_year:
            query += "release_year = %s, "
            params.append(release_year)
        if end_year:
            query += "end_year = %s, "
            params.append(end_year)
        if content_warning:
            query += "content_warning = %s, "
            params.append(content_warning)

        # Remove the last comma and space
        query = query.rstrip(", ")
        query += " WHERE id = %s"
        params.append(id)
        
        self.getCursor()
        self.cursor.execute(query, tuple(params))
        self.connection.commit()
    
    def delete_anime(self, id):
        query = "DELETE FROM animes WHERE id = %s"
        self.getCursor()
        self.cursor.execute(query, (id,))
        self.connection.commit()
    
    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")
    
animeDAO = AnimeDAO()

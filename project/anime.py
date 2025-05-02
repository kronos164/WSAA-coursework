from flask import Flask, request, jsonify
from animeDAO import animeDAO

app = Flask(__name__)
# get all anime by id from the sql database

# get all anime from the sql database
@app.route('/anime/<string:identifier>', methods=['GET'])
def get_anime(identifier):
    if identifier == "all":
        # Fetch all anime from the database
        all_anime = animeDAO.get_all_anime()
        return jsonify(all_anime), 200
    else:
        try:
            anime_id = int(identifier)
            # Fetch anime by ID from the database
            anime = animeDAO.get_anime_by_id(anime_id)
            if anime:
                return jsonify(anime), 200
            else:
                return jsonify({"error": "Anime not found"}), 404
        except ValueError:
            return jsonify({"error": "Invalid identifier"}), 400

@app.route('/anime', methods=['POST'])
#add anime to the sql database using the animeDAO class
def add_anime():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    # Extract anime details from the request data
    name = data.get('name')
    jp_name = data.get('jp_name')
    type = data.get('type')
    episodes = data.get('episodes')
    studio = data.get('studio')
    release_season = data.get('release_season')
    tags = data.get('tags')
    rating = data.get('rating')
    release_year = data.get('release_year')
    end_year = data.get('end_year')
    content_warning = data.get('content_warning')

    # Add anime to the database
    animeDAO.add_anime(name, jp_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, content_warning)
    
    return jsonify({"message": "Anime added successfully"}), 201
    
    

@app.route('/anime/<int:anime_id>', methods=['PUT'])
def update_anime(anime_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    # Extract anime details from the request data
    name = data.get('name')
    jp_name = data.get('jp_name')
    type = data.get('type')
    episodes = data.get('episodes')
    studio = data.get('studio')
    release_season = data.get('release_season')
    tags = data.get('tags')
    rating = data.get('rating')
    release_year = data.get('release_year')
    end_year = data.get('end_year')
    content_warning = data.get('content_warning')

    # Update anime in the database
    animeDAO.update_anime(anime_id, name, jp_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, content_warning)
    
    return jsonify({"message": "Anime updated successfully"}), 200

@app.route('/anime/<int:anime_id>', methods=['DELETE'])
def delete_anime(anime_id):
    # Delete anime from the database
    animeDAO.delete_anime(anime_id)
    
    return jsonify({"message": "Anime deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
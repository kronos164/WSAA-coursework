from flask import Flask, request, jsonify
from animeDAO import animeDAO

app = Flask(__name__)
# get all anime by id from the sql database

# get all anime from the sql database
@app.route('/anime', methods=['GET'])
def get_anime():
    anime_id = request.args.get('id')
    if anime_id:
        # Fetch anime by ID from the database
        anime = get_anime_by_id(anime_id)
        if anime:
            return jsonify(anime), 200
        else:
            return jsonify({"error": "Anime not found"}), 404
    else:
        # Fetch all anime from the database
        all_anime = get_all_anime()
        return jsonify(all_anime), 200

@app.route('/anime', methods=['POST'])
def add_anime():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    # Extract anime details from the request data
    id = data.get('id')
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
    add_anime(id, name, jp_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, content_warning)
    
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
    update_anime(anime_id, name, jp_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, content_warning)
    
    return jsonify({"message": "Anime updated successfully"}), 200

@app.route('/anime/<int:anime_id>', methods=['DELETE'])
def delete_anime(anime_id):
    # Delete anime from the database
    delete_anime(anime_id)
    
    return jsonify({"message": "Anime deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
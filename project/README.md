# Anime: Flask project

![Anime](https://cdn.magicdecor.in/com/2023/10/20174720/Anime-Scenery-Wallpaper-for-Walls-710x488.jpg)


## About This Project

Japanese anime culture is a vibrant and influential part of modern entertainment, originating in Japan in the early 20th century. Anime encompasses a wide range of genres and artistic styles, often characterized by colorful visuals, imaginative storytelling, and deep emotional themes. Over the decades, anime has grown from a domestic phenomenon into a global cultural force, captivating audiences worldwide through television, movies, and streaming platforms. Its impact can be seen in fashion, art, and even language, as international fans embrace conventions, cosplay, and fan communities. The universal appeal of anime lies in its ability to blend unique Japanese cultural elements with stories and characters that resonate across cultures, making it a truly global phenomenon.
With that being said, this project was create with the purpose to consolidate as many anime titles as possible in a database and create a flask API to access, update and delete the titles on this database.

The database was create on a AWS cloud system using MySQL code. On this database, was added 1326 titles. These titles were categorised by the variables below:
   - Name (English)
   - Name (Japanese)
   - Type (TV Series, Movies, and OVAs)
   - Number of episodes
   - Studio
   - Release seasons (Spring, summer, fall, and winter)
   - Tags
   - Rating (from 0 to 5)
   - Release year
   - End year
   - Content warnings

An ID number is assigned to every individual title.

## Flask API

The flask API created consist of a few HTML templates. They were created to be user friendly and to make very easy and intuitive the process of interacting with the database.

## How to use this script

   - Install the required libraries and applications on the `requirements.txt`.
   - Contact the author owner to acquire the dataset credentials key (`db_keys.py`). This is needed for the script to access the database.
   - Open the python file called `anime.py` and execute the code. The script will initiate a Flask API that can be operated on your browser.
   - On the terminal, a link with your IP address will be created. Click the link and it will redirect you to your browser and start the API.
   - On the API you will be able to search the animes on the database, and also update, add and delete information/animes.

   Note: in case you want to have this database locally, just use the MySQL backup on the backups folder and create a local dataset. Then just change the connection credentials on the file `db_keys.py`.

## Technical Requirements

```
python = 3.12.7
Flask = 2.3.2
flask_mysqldb = 0.2.0
```

## Repository Structure

```
WSAA-coursework/project/
|
├── backups/                                             # Folder with latest mySQL anime database in case you want to ran it locally
├── templates/                                           # Folder with html templates
├── anime.py                                             # Python Flask API
├── db_keys.py                                           # Python key/config file with credentials for the dataset (not available on 
                                                           github, please contact owner for access)
├── README.md                                            # README file                                                         
├── requirements.txt                                     # Text file requirements to run the API
|
```

## References:

### Anime dataset reference

   1. https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset


### Code


   1. Flask documentation: https://flask.palletsprojects.com/
   2. Flask-MySQLdb documentation: https://flask-mysqldb.readthedocs.io/
   3. Jinja2 templating (used by render_template): https://jinja.palletsprojects.com/
   4. Python DB-API (PEP 249): https://peps.python.org/pep-0249/
   5. MySQL documentation (SQL syntax): https://dev.mysql.com/doc/

### HTML templates


   1. https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form 
   2. https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input
   3. https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select 

Note: Copilot was used to help with the general layout of the HTMLs (input box positioning and size)


***
***

## Author


#### About me:

My name is Cainã Oliveira. I hold a Master's degree in Psychology from the [University of Porto](https://www.up.pt/portal/en/) and am currently advancing my education in data analytics through a postgraduate course at the [Atlantic Technological University: ATU](https://www.atu.ie/). Simultaneously, I am pursuing a Master's in Artificial Intelligence at the [International University of Applied Sciences](https://www.iu.org/). My academic journey reflects a strong commitment to integrating the insights of human behavior with the cutting-edge technologies of AI and data science, aiming to harness these disciplines in innovative and impactful ways.

![IT](https://erp.today/wp-content/uploads/2022/12/Artificial_Intelligence-2048x1024.jpg)
import random
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()#
    movie2 = get_random_movie()
    #while movie2 == movie:
        #movie2 = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"#
    
    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + movie2 + "</li>"
    content += "</ul>"
    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    return content

def get_random_movie():
    movie_list = ["Ordinary People", "Spartacus", "Training Day", "Biutiful", "Trading Places"] # TODO: make a list with at least 5 movie titles
    #selected_movie = random.choice(movie_list)
    return random.choice(movie_list)  # TODO: randomly choose one of the movies, and return it
    


app.run()

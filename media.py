# By Adam Hussain
import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG13", "R"]
    # Method to initiate the values each Movie will have.
    def __init__(self, movie_title, movie_storyline, poster_image,
               trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # Method used to show the movie trailer of the movie selected by the user.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

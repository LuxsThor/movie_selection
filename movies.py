import webbrowser

class Movie:
    def __init__(self, movie_title, movie_storyline, movie_trailer, movie_image):
        self.title = movie_title
        self.story = movie_storyline
        self.trailer = movie_trailer
        self.image = movie_image

    def show_trailer(self):
        webbrowser.open(self.trailer)


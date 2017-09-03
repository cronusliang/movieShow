import webbrowser

class Movie():
    '''Movie presentation entity class '''
    def __init__(self,title,original_title,movie_storyline,poster_image,trailer_youtube):
        """init movie Attributes"""
        self.title = title
        self.original_title = original_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """open video by browser"""
        webbrowser.open(self.trailer_youtube_url)


class Subject():
    '''Recently released film parse entity class'''
    def __init__(self,id,title,alt,image):
        """init Subject Attributes"""
        self.id = id
        self.title = title
        self.alt = alt
        self.image = image

import fresh_tomatoes
import media

avatar =  media.Movie("avatar", "a story of a boy and his toys that come to life",
            "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
            "https://s3.cn-north-1.amazonaws.com.cn/u-vid-hd/MnDs5GF3AMs.mp4")


toy = media.Movie("toy story", "a story of a boy and his toys that come to life",
                   "http://video.1speaking.com/pic/uploadimg/2012-1/20121302144442769.jpg",
                   "https://www.youtube.com/watch?v=sarLaVnB1Eo")


moves = [avatar,toy]
fresh_tomatoes.open_movies_page(moves)
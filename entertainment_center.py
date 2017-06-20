# By Adam Hussain
import fresh_tomatoes
import media

# List of my favorite movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


warriors = media.Movie("The Warriors",
                       "A battle of gigantic proportions is looming in the neon underground of New York City. The gang called the Warriors must battle their way home to their turf in Coney Island.",
                       "http://blog.signalnoise.com/wp-content/uploads/2011/11/i_mpm31.jpg",
                     "https://www.youtube.com/watch?v=4GxSwUcm_XE")


spacejam = media.Movie("Space Jam",
                       "Looney Tunes seek Micheal Jordan's help to save their universe",
                       "https://upload.wikimedia.org/wikipedia/en/1/14/Space_jam.jpg",
                       "https://www.youtube.com/watch?v=oKNy-MWjkcU")

fourbrothers = media.Movie("Four Brothers",
                           "Four adopted brothers seek revenge for murdered woman that raised them",
                           "http://www.gstatic.com/tv/thumb/movieposters/36171/p36171_p_v8_af.jpg",
                           "https://www.youtube.com/watch?v=vZPi0K6UoP8")

bourneidentity = media.Movie("The Bourne Identity",
                             "A man is picked up by a fishing boat, bullet-riddled and suffering from amnesia, before racing to elude assassins and regain his memory.",
                             "http://www.gstatic.com/tv/thumb/movieposters/28900/p28900_p_v8_ai.jpg",
                             "https://www.youtube.com/watch?v=FpKaB5dvQ4g")

thefighter = media.Movie("The Fighter",
                         "A look at the early years of boxer Micky Ward and his brother who helped train him before going pro in the mid 1980s. ",
                         "http://www.gstatic.com/tv/thumb/movieposters/8175505/p8175505_p_v8_aa.jpg",
                         "https://www.youtube.com/watch?v=1_zijS_UAtw")



# Array of the my favorite movies
movies = [toy_story, warriors, spacejam, fourbrothers, bourneidentity, thefighter]

# Web page displaying movies page
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)
print("The name of the class is " + media.Movie.__name__)
print("The name of the module is " + media.Movie.__module__)

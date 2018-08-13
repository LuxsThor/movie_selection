import movies
import fresh_tomatoes

Toy_Story = movies.Movie("Toy Story", "a toy that comes to live", "https://www.youtube.com/watch?v=KYz2wyBy3kc", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg")
School_of_Rock = movies.Movie("School of Rock", "A fake teacher rocks with some school kids", "https://www.youtube.com/watch?v=AiJauwvuXbQ", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg")
Imitation_Game = movies.Movie("Imitation Game", "Alan Turing saving the world but getting fucked cause hes gay", "https://www.youtube.com/watch?v=nuPZUUED5uk", "https://upload.wikimedia.org/wikipedia/en/8/87/The_Imitation_Game_%282014%29.png")


movies = [Toy_Story, School_of_Rock, Imitation_Game]

fresh_tomatoes.open_movies_page(movies)





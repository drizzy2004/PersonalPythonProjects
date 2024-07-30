current_movies = {
    "The Grinch": "11:00am",
    "Rudolph": "1:00pm",
    "Frosty The Snowman": "3:00pm",
    "Christmas Vacation": "5:00pm"
    }

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movis would you like to see times for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing.")
else:
    print(f"Here are the times playing for {movie}: {showtime}")
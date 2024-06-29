class Movie:
    def __init__(self, title, showtimes):
        self.title = title
        self.showtimes = showtimes
class Theater:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = [['O' for _ in range(seats_per_row)] for _ in range(rows)]

    def display_seats(self):
        for row in self.seats:
            print(' '.join(row))

def book_tickets(movie, showtime, num_tickets):
    theater.display_seats()
    selected_seats = []
    for _ in range(num_tickets):
        row = int(input("Enter row number: ")) - 1
        seat = int(input("Enter seat number: ")) - 1
        if theater.seats[row][seat] == 'O':
            theater.seats[row][seat] = 'X'
            selected_seats.append((row, seat))
        else:
            print("Seat already booked. Please choose another seat.")
    print("Tickets booked successfully!")
    print(f"Movie: {movie.title}, Showtime: {showtime}")
    print("Seats booked:")
    for row, seat in selected_seats:
        print(f"Row {row + 1}, Seat {seat + 1}")


if __name__ == "__main__":
    movies = [
        Movie("Moneyheist", ["10:00 AM", "1:00 PM","3:00 PM"]),
        Movie("Avengers", ["11:00 AM", "3:00 PM","6:00 PM"]),
        Movie("The Jungle Book", ["6:00 PM", "9:00 PM"])
    ]
    theater = Theater(5, 10)

    print("Available Movies:")
    for idx, movie in enumerate(movies, start=1):
        print(f"{idx}. {movie.title}")

    movie_choice = int(input("Enter the movie name: "))
    selected_movie = movies[movie_choice - 2]

    print("Available showtimes:")
    for idx, showtime in enumerate(selected_movie.showtimes, start=1):
        print(f"{idx}. {showtime}")

    showtime_choice = int(input("Enter the showtime you prefer: "))
    selected_showtime = selected_movie.showtimes[showtime_choice - 2]

    num_tickets = int(input("Enter the number of tickets: "))
    book_tickets(selected_movie, selected_showtime, num_tickets)

import sqlite3

db="movies.db"

def get_connection():
    return sqlite3.Connection(db)

# CreateIn table in database

def Create_table():
    with get_connection() as con:
        con.execute('''CREATE TABLE IF NOT EXISTS MOVIES( 
                            TITLE TEXT NOT NULL,
                            DIRECTOR TEXT NOT NULL,
                            YEAR INT NOT NULL,
                            RATING REAL NOT NULL,
                            WATCHED BOOL NOT NULL,
                            PRIMARY KEY (TITLE, YEAR)
                            )
                    ''')
        
# Adding movie into the database

def add_movie():
    title=input("Enter title of the movie: ")
    director=input("Enter Director name: ")
    try:
        year=int(input("Enter year of the movie released"))
        rating=float(input("Enter the movie rating (0.0–10.0): "))
    except ValueError:
        print("Invalid year or rating. Please try again.")
        return
    with get_connection() as con:
        con.execute('''INSERT INTO MOVIES (TITLE,DIRECTOR,YEAR,RATING,WATCHED) VALUES
                    (?,?,?,?,?)''',(title,director,year,rating,0))
    print("sucessfully added movie")


# get all list of movies

def list_movies():
    with get_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM MOVIES")
        rows = cur.fetchall()

    if not rows:
        print("No movies found.")
    for row in rows:
        print(f"{row[0]} directed by {row[1]} in {row[2]} - IMDb: {row[3]} - Watched: {row[4]}")

# to find movie

def find_movie():
    search_options = {
        't': "TITLE",
        'd': "DIRECTOR",
        'y': "YEAR",
        'r': "RATING"
    }

    while True:
        choice = input("\nSearch by:\nt -> title\nd -> director\ny -> year\nr -> rating\nq -> quit search\nYour choice: ").strip().lower()
        if choice == 'q':
            break
        column = search_options.get(choice)
        if not column:
            print("Invalid choice. Try again.")
            continue

        search_value = input(f"Enter the {column.lower()}: ").strip()
        query = f"SELECT * FROM MOVIES WHERE {column} LIKE ?"

        param = f"%{search_value}%" if column in ["TITLE", "DIRECTOR"] else search_value
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(query, (param,))
            rows = cur.fetchall()

        if not rows:
            print("No matching movie found.")
        for row in rows:
            print(f"{row[0]} directed by {row[1]} in {row[2]} - IMDb: {row[3]} - Watched: {row[4]}")

#updating all 

def update_movie():
    title = input("Enter the movie title to update: ").strip()

    update_options = {
        't': "TITLE",
        'd': "DIRECTOR",
        'y': "YEAR",
        'r': "RATING"
    }

    while True:
        choice = input("\nUpdate:\nt -> title\nd -> director\ny -> year\nr -> rating\nq -> done updating\nYour choice: ").strip().lower()
        if choice == 'q':
            break
        column = update_options.get(choice)
        if not column:
            print("Invalid choice.")
            continue

        new_value = input(f"Enter new {column.lower()}: ").strip()
        try:
            if column == "YEAR":
                new_value = int(new_value)
            elif column == "RATING":
                new_value = float(new_value)
        except ValueError:
            print("Invalid input type. Try again.")
            continue

        with get_connection() as conn:
            conn.execute(f"UPDATE MOVIES SET {column} = ? WHERE TITLE = ?", (new_value, title))
        print(f"{column} updated successfully.")

# deleting movie through title

def delete_movie():
    title = input("Enter the movie title to delete: ").strip()
    with get_connection() as conn:
        conn.execute("DELETE FROM MOVIES WHERE TITLE = ?", (title,))
    print("Movie deleted.")

# clearing all movies from database

def clear_movies():
    confirm = input("Are you sure you want to delete all movies? (y/n): ").strip().lower()
    if confirm == 'y':
        with get_connection() as conn:
            conn.execute("DELETE FROM MOVIES")
        print("All movies cleared.")



def menu():
    user_options = {
        'a': add_movie,
        'l': list_movies,
        'f': find_movie,
        'u': update_movie,
        'd': delete_movie,
        'c': clear_movies
    }
    while True:
        choice=input('''Enter:
            a -> Add movie
            l -> List movies
            f -> Find movie
            u -> Update movie
            d -> Delete movie
            c -> Clear all movies
            q -> Quit
            Your choice: ''').lower().strip()
        if choice=='q':
            print("good bye!")
            break
        elif choice in user_options:
             user_options[choice]()
        else:
            print("you entered unknown command Try again!")        

if __name__=="__main__":
    Create_table()
    menu()
    
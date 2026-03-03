# read_movies.py
# Reads all items from the DynamoDB Movies table and prints them.
# Part of Lab 09 — feature/read-dynamo branch
# testing testing 123
# this is a test
import boto3
from boto3.dynamodb.conditions import Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Movies"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)
def get_movie_by_title():
    title_input = input("Enter a movie title: ")

    # Scan table with filter
    response = table.scan(
        FilterExpression=Attr("Title").eq(title_input)
    )
    items = response.get("Items", [])

    # Check if movie was found
    if items:
        print("\nMovie Found:\n")
        for movie in items:
            print_movie(movie)
    else:
        print("\nMovie not found.")

def print_movie(movie):
    title = movie.get("Title", "Unknown Title")
    year = movie.get("Year", "Unknown Year")
    ratings = movie.get("Ratings", "No ratings")
    genre = movie.get("Genre", "Unknown Genre")   # ← FIXED

    print(movie)
    print(f"  Title  : {title}")
    print(f"  Year   : {year}")
    print(f"  Ratings: {ratings}")
    print(f"  Genre  : {genre}")
    print()


def print_all_movies():
    """Scan the entire Movies table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No movies found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} movie(s):\n")
    for movie in items:
        print_movie(movie)


def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_movies()


if __name__ == "__main__":
    main()

    if __name__ == "__main__":
        get_movie_by_title()

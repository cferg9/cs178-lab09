import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # change region if needed
table = dynamodb.Table('Recipes')  # your Recipes table

def print_all_recipes():
    response = table.scan()  # scan fetches all items
    recipes = response.get('Items', [])

    if recipes:
        for recipe in recipes:
            print("Recipe:")
            for key, value in recipe.items():
                print(f"  {key}: {value}")
            print()
    else:
        print("No recipes found in the table.")

# Run the function when script is executed
if __name__ == "__main__":
    print_all_recipes()
def main():
    # Step 2: Create a complex data structure
    data_structure = {
        'full_name': 'Azeez',
        'student_id': 123456789,
        'pizza_toppings': ['Mushrooms', 'Extra Cheese', 'Chicken'],
        'movies': [
            {'title': 'maze runner', 'genre': 'action'},
            {'title': 'godzilla', 'genre': 'adventure'}
        ]
    }

    # Step 3: Add another movie to the data structure
    new_movie = {'title': 'cars 1', 'genre': 'comedy'}
    data_structure['movies'].append(new_movie)

    # Step 4: Use a function to print student name and ID
    print_student_info(data_structure)

    # Step 5: Use a function to add pizza toppings to the data structure
    pizza_toppings_to_add = ('steak', 'spinach')
    add_pizza_toppings(data_structure, pizza_toppings_to_add)

    # Step 6: Use a function to print a bullet list of pizza toppings
    print_pizza_toppings(data_structure)

    # Step 7: Use a function to print a comma-separated list of movie genres
    print_movie_genres(data_structure)

    # Step 8: Use a function to print a comma-separated list of movie titles
    print_movie_titles(data_structure['movies'])


def print_student_info(data_structure):
    # Extracting first name from full name
    first_name = data_structure['full_name'].split()[0]
    
    # Printing student information
    print(f"My name is {data_structure['full_name']}, but you can call me Sir {first_name}.")
    print(f"My student ID is {data_structure['student_id']}.\n")


def add_pizza_toppings(data_structure, toppings_to_add):
    # Adding pizza toppings to the list
    data_structure['pizza_toppings'].extend(toppings_to_add)
    
    # Sorting and converting pizza toppings to lowercase
    data_structure['pizza_toppings'] = sorted(map(str.lower, data_structure['pizza_toppings']))


def print_pizza_toppings(data_structure):
    # Printing pizza toppings as a bullet list
    print("My favourite pizza toppings are:")
    for topping in data_structure['pizza_toppings']:
        print(f"- {topping.capitalize()}")
    print()


def print_movie_genres(data_structure):
    # Extracting movie genres and printing them in a comma-separated list
    genres = [movie['genre'] for movie in data_structure['movies']]
    print(f"I like to watch {', '.join(genres)} movies.\n")


def print_movie_titles(movie_list):
    # Printing movie titles with uppercase first letters
    titles = [movie['title'].title() for movie in movie_list]
    print(f"Some of my favourite movies are {', '.join(titles)}!\n")


if __name__ == '__main__':
    main()
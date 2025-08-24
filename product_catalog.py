from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
# print(products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    preference = input("Input a preference: ")
    customer_preferences.append(preference)
    # Add the customer preference to the list

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
for product in products:
     product_tags = product['tags'] =set(product['tags'])

# print(product['tags'])    



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(customer_tags.intersection(product_tags))

count_matches(product_tags, customer_tags)


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for product in products:    
        matches = count_matches(product['tags'], customer_tags)
        if matches > 0:
            recommendations.append((product['name'], count_matches(product['tags'], customer_tags)))
    return recommendations

# TODO: Step 7 - Call your function and print the results

count_matches(product_tags, customer_tags)
print(recommend_products(products, customer_tags))



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?


# I used both loops and intersections. The .intersection() allowed me to compare different sets to find matches while
# the loops helped to sort through all the products and their tags to find the matches within lists. It took me a few 
# attempts to learn that I cannot use the .intersection() function for lists and it is only for sets. I only used it 
# once in the count_matches function because both of the variables were sets. I had to use loops using the 'for' statement 
# the other times because only one of the variables was a set and I needed to loop throughout all of the products to find every 
# match. I'm not sure how much the code would need to change for that many products, but I don't think it would need 
# to change significantly. I think the biggest changes would be code that's more effiecient and organized for larger data sets.
# The product data already has a good number of products and the code sorts through them well. I believe my code would be able to 
# handle 1000+ products, but it might not be the most time efficient. I would for sure need to research different ways to handle large
# amounts of data to implement different solutions and an improved code. 
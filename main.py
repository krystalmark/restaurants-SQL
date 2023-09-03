from models import Restaurant, Customer, Review, session

if __name__ == "__main__":
    
    fanciest_restaurant = Restaurant.fanciest()
    print(f"Fanciest restaurant: {fanciest_restaurant.name}")

    restaurant1 = session.query(Restaurant).filter_by(name="Restaurant 1").first()
    reviews_for_restaurant1 = restaurant1.all_reviews()
    print("Reviews for Restaurant 1:")
    for review in reviews_for_restaurant1:
        print(review)

    new_customer = Customer(first_name="Alice", last_name="Johnson")
    session.add(new_customer)
    session.commit()

    new_review = Review(customer=new_customer, restaurant=restaurant1, star_rating=4)
    session.add(new_review)
    session.commit()

    customer2 = session.query(Customer).filter_by(first_name="Jane").first()
    favorite_restaurant = customer2.favorite_restaurant()
    if favorite_restaurant:
        print(f"Favorite restaurant for Jane Smith: {favorite_restaurant.name}")
    else:
        print("Jane Smith has not reviewed any restaurants yet.")

    customer1 = session.query(Customer).filter_by(first_name="John").first()
    restaurant_to_delete_reviews = restaurant1  
    customer1.delete_reviews(restaurant_to_delete_reviews)
    print("Deleted reviews by John Doe for Restaurant 1")

    has_reviewed = session.query(Review).filter(
        Review.customer_id == new_customer.id,
        Review.restaurant_id == restaurant1.id
    ).first() is not None
    if has_reviewed:
        print("Alice Johnson has reviewed Restaurant 1.")
    else:
        print("Alice Johnson has not reviewed Restaurant 1.")

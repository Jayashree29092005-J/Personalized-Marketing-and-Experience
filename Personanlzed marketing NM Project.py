import pandas as pd

# Sample customer data with specific data types
customers = pd.DataFrame({
    'customer_id': pd.Series([101, 102, 103], dtype='int'),
    'name': pd.Series(['Alice', 'Bob', 'Charlie'], dtype='string'),
    'segment': pd.Series(['Premium', 'Standard', 'Premium'], dtype='string'),
    'last_purchase': pd.to_datetime(['2025-04-20', '2025-04-15', '2025-04-22']),
    'interests': pd.Series(['electronics', 'books', 'fitness'], dtype='string')
})

# Function to generate personalized messages
def generate_message(name, customer_id, segment, interests):
    if segment == 'Premium':
        offer = "an exclusive 20% discount just for you"
    else:
        offer = "a special 10% discount on your next purchase"

    return f"Hi {name} (Customer #{customer_id}), we noticed you're interested in {interests}. Here's {offer}!"

# Apply personalization
customers['personalized_message'] = customers.apply(
    lambda row: generate_message(row['name'], row['customer_id'], row['segment'], row['interests']),
    axis=1
)

# Print result
print(customers[['name', 'personalized_message']])
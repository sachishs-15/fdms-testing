from api_tests.customer_api import run_customer_tests
from api_tests.delivery_agent_api import run_delivery_agent_tests
from api_tests.management_api import run_management_tests
from api_tests.restaurant_api import run_restaurant_tests
from add_data.add_data import generate_test_database

# initialize the database with test data
print("Initializing test database...")
generate_test_database()
print("Running tests...\n")
# run the tests

# run the customer tests
run_customer_tests()

# run the delivery agent tests
run_delivery_agent_tests()

# run the restaurant tests
run_restaurant_tests()

# run the management tests
run_management_tests()

import unittest
from pact import Consumer, Provider, requests

class FlaskApiContractTest(unittest.TestCase):

    def setUp(self):
        
        self.consumer = Consumer('Dashboard')
        self.provider = Provider('FlaskAPI')

    def get_all_employees(self):
        # Defining the expected interaction
        expected_interaction = (
            self.consumer
            .has_pact_with(self.provider)
            .upon_receiving('request to get all employees')
            .with_request('GET', '/empnvDB/employee')
            .will_respond_with(200, body={'emps': []})
        )

        # Verifying the interaction
        with expected_interaction:
            # Making a request to the Flask API
            response = requests.get('http://localhost:8080/empnvDB/employee')
            self.assertEqual(response.status_code, 200)

    def post_create_employee(self):
       
        expected_interaction = (
            self.consumer
            .has_pact_with(self.provider)
            .upon_receiving('request to create a new employee')
            .with_request('POST', '/empnvDB/employee')
            .will_respond_with(201, body={'id': '561', 'name': 'Aman', 'age' : 23, 'department': 'SDE'})
        )

        with expected_interaction:

            response = requests.post('http://localhost:8080/empnvDB/employee', json={'id': '561', 'name': 'Aman', 'age' : 23, 'department': 'SDE'})
            self.assertEqual(response.status_code, 201)

    def get_employee_by_id(self):

        expected_interaction = (
            self.consumer
            .has_pact_with(self.provider)
            .upon_receiving('request to get an employee by ID')
            .with_request('GET', '/empnvDB/employee/561')
            .will_respond_with(200, body={'id': '561', 'name': 'Aman', 'age' : 23, 'department': 'SDE'})
        )

        with expected_interaction:

            response = requests.get('http://localhost:8080/empnvDB/employee/561')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['id'], '561')

    def put_update_employee(self):
        
        expected_interaction = (
            self.consumer
            .has_pact_with(self.provider)
            .upon_receiving('request to update an existing employee')
            .with_request('PUT', '/empnvDB/employee/561')
            .will_respond_with(200, body={'id': '561', 'name': 'Aman', 'department': 'SDE'})
        )

        with expected_interaction:
            
            response = requests.put('http://localhost:8080/empnvDB/employee/561', json={'name': 'Aman'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['name'], 'Aman')

if __name__ == '__main__':
    unittest.main()

#Generating provider contract which represents the contarct b/w the consumer and provider services as defined by the pact tests
with open('emp_service_contract.json', 'w') as file:
    file.write(consumer.to_json())

#Ensuring that the consumer contract is a subset of provider contract
pact = Pact(provider=provider, consumer=consumer)
pact.verify()

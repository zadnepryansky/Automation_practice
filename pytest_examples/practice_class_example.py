import requests
# Particular test using Class


def save_data(data):
    with open('from_test_example.txt', 'a') as f:
        f.write(f"{data}\n")


url = "https://ithillel.ua/-"
url_1 = "https://www.aqa.science/?format=json"


class TestSuite_1:

    def setup_class(self):
        print('Tests suite started')

    def teardown_class(self):
        print('Tests suite done')

    def setup(self):
        print('single test started')

    def teardown(self):
        print("single test finished")

    def test_first_check(self):
        response = requests.get(url)
        assert response.status_code == 200, save_data(response.status_code)



    def test_second_check(self):
        response = requests.get(f'{url}/n/')
        assert response.status_code == 404, save_data(response.status_code)



    def test_third_check(self):
        response = requests.get(url_1)
        assert response.text ==\
               '{"users":"https://www.aqa.science/users/?format=json","groups":"https://www.aqa.science/groups/?format=json"}'


import requests
# Particular test using fixture


def save_data(data):
    with open('from_test_example.txt', 'a') as f:
        f.write(f"{data}\n")


url = "https://ithillel.ua/-"
url_1 = "https://www.aqa.science/?format=json"


def test_first_check(request):
    request.user_data = []
    response = requests.get(url)
    code = response.status_code
    assert code == 200, save_data(response.status_code)


def test_second_check(request):
    request.user_data.append('d')
    response = requests.get(f'{url}/n/')
    code = response.status_code
    assert code == 404, save_data(response.status_code)


def test_third_check():
    response = requests.get(url_1)
    assert response.text == \
           '{"users":"https://www.aqa.science/users/?format=json","groups":"https://www.aqa.science/groups/?format=json"}'

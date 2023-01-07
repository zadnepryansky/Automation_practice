import requests


def save_data(data):
    with open('log.txt', 'a') as f:
        f.write(data)


class TestSuite:

    def setup_class(self):
        # something before all tests
        # from ... import ...
        # local_variable =
        self.variable = []
        print('Tests suite started')

    def teardown_class(self):
        save_data(str(self.variable))
        print('Tests suite done')

    def setup(self):
        save_data('started \n')
        print('single test started')

    def teardown(self):
        save_data('finished \n')
        print("single test finished")

    def test_first_check(self):
        print('inside test')
        status = requests.get("http://google.com").status_code
        self.variable.append(status)
        assert status == 200

    def test_second_check(self):
        print('inside test')
        status = requests.get("http://google.com").status_code
        self.variable.append(status)
        assert status == 404

    def test_third_check(self):
        print('inside test')
        status = requests.get("http://wikipedia.com").status_code
        self.variable.append(status)
        assert status == 200

    def test_forth_check(self):
        print('inside test')
        status = requests.get("http://aqa.science").status_code
        self.variable.append(status)
        assert status == 200

    def test_fifth_check(self):
        print('inside test')
        status = requests.get("http://aqa.science/123").status_code
        self.variable.append(status)
        assert status == 200
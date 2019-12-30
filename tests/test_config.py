import anytialize.config as config
from unittest import TestCase, main

class TestConfig(TestCase):
    config_content = {
        "template-path": [
        "/some/path",
        "/something",
        "/else"
        ]
    }

    def test_config_from_path(self):
        result = config.config_from_path("./testfiles/config_test.yaml")
        self.assertEqual(self.config_content, result)

    def test_config_from_file(self):
        with open("./testfiles/config_test.yaml", "r") as file:
            result = config.config_from_file(file)
            self.assertEqual(self.config_content, result)

if __name__ == "__main__":
    main()
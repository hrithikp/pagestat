from unittest import TestCase
from pagestat import Parser
test_html = """
<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1>Parse me!</h1>
        <h1>Me too!!</h1>
    </body>
</html>
"""
class TestParser(TestCase):
    def setUp(self):
        self.parse = Parser()
    def test_counts(self):
        data = self.parse(test_html, 'tags')
        self.assertTrue(len(data) == 5)
        self.assertTrue(sum([c for t,c in data.items()]) == 6)

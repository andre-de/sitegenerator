import unittest

from htmlnode import HTMLNode


class TestTHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p","the text inside", None,{"href": "https://www.google.com", "target": "_blank"})
        print(node.props_to_html())
        print(node)

    def test_none(self):
        node1 = HTMLNode()
        print(node1)

    def test2(self):
        node = HTMLNode("p","the text inside", None,{"href": "https://www.google.com"})
        print(node.props_to_html())
        print(node)       
        

if __name__ == "__main__":
    unittest.main()
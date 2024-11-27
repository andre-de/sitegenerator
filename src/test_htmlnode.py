import unittest

from htmlnode import HTMLNode, LeafNode


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
        
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
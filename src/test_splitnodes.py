import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from split_nodes import split_nodes_delimiter





'''class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")'''

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_balanced_delimiters(self):
        node = TextNode("This is `code` in a text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected_result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" in a text", TextType.TEXT)
        ]

        # Check if the result matches the expected outcome
        self.assertEqual(result, expected_result)

    def test_no_delimiters(self):
        node = TextNode("Just plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected_result = [TextNode("Just plain text", TextType.TEXT)]
        
        # Check if the result matches the expected outcome
        self.assertEqual(result, expected_result)

    def test_edge_cases(self):
        # Test empty string
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_result = [TextNode("", TextType.TEXT)]
        self.assertEqual(result, expected_result)
        
        # Test starting with delimiter
        node = TextNode("`code` at the start", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected_result = [
            TextNode("", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" at the start", TextType.TEXT)]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

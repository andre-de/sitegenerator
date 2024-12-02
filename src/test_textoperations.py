import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from text_operations import *





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

class TestTextoperations(unittest.TestCase):
    def test_image_extraction(self):
        text =  "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected_result = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(result, expected_result)

    def test_image_extraction2(self):
        text =  "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected_result = [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(result, expected_result)

    def test_link_extraction(self):
        text =  "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_links(text)
        expected_result = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]
        self.assertEqual(result, expected_result)

class TestSplitNodesLink(unittest.TestCase):
    def test_single_link(self):
        node = TextNode("Visit [Boot.dev](https://www.boot.dev) for more.", TextType.TEXT)
        result = split_nodes_link([node])
        expected_result = [TextNode("Visit ", TextType.TEXT), TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),TextNode(" for more.", TextType.TEXT)]
        self.assertEqual(result, expected_result)
    def test_multiple_links(self):
        node = TextNode("Check [Google](https://www.google.com) and [Bing](https://www.bing.com).", TextType.TEXT)
        result = split_nodes_link([node])
        expected_result = [TextNode("Check ", TextType.TEXT), TextNode("Google", TextType.LINK, "https://www.google.com"),TextNode(" and ", TextType.TEXT), TextNode("Bing", TextType.LINK, "https://www.bing.com"), TextNode(".", TextType.TEXT)]
        self.assertEqual(result, expected_result)
    
    def test_no_links(self):
        node = TextNode("Hello World!", TextType.TEXT)
        result = split_nodes_link([node])
        expected_result = [TextNode("Hello World!", TextType.TEXT)]
        self.assertEqual(result, expected_result)
    
    def test_link_at_start(self):
        node = TextNode("[Start](https://start.com) text.", TextType.TEXT)
        result = split_nodes_link([node])
        expected_result = [TextNode("Start", TextType.LINK, "https://start.com"), TextNode(" text.", TextType.TEXT)]
        self.assertEqual(result, expected_result)

    def test_link_at_end(self):
        node = TextNode("End of text [here](https://here.com).", TextType.TEXT)
        result = split_nodes_link([node])
        expected_result = [TextNode("End of text ", TextType.TEXT), TextNode("here", TextType.LINK, "https://here.com"), TextNode(".", TextType.TEXT)]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

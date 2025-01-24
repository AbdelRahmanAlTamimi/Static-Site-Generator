import unittest
from htmlnode import HTMLNode,LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        leaf = LeafNode("p", "this is a test for leafNode", {"class": "helloClass"})
        
        self.assertEqual(
            leaf.__repr__(),
            "LeafNode(p, this is a test for leafNode, {'class': 'helloClass'})"
        )
    def test_to_html(self):
        leaf = LeafNode(
            "a",
            "boot.dev",
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            leaf.to_html(),
            '<a class="greeting" href="https://boot.dev">boot.dev</a>'
        )
        
    def test_to_html_no_tag(self):
        leaf = LeafNode(None, "Just some text.")
        self.assertEqual(leaf.to_html(), "Just some text.")
    
    def test_to_html_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

if __name__ == "__main__":
    unittest.main()

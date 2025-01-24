import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode


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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        # Test with multiple LeafNode children
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_no_tag(self):
        # Test that a ValueError is raised when tag is None
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("b", "Bold text")]).to_html()
        self.assertEqual(str(context.exception), "ParentNode requires a tag")

    def test_to_html_no_children(self):
        # Test that a ValueError is raised when children is None
        with self.assertRaises(ValueError) as context:
            ParentNode("p", None).to_html()
        self.assertEqual(str(context.exception), "ParentNode requires children")

    def test_to_html_empty_children(self):
        # Test with an empty list of children
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_to_html_nested_parent_nodes(self):
        # Test nesting ParentNode objects
        inner_node = ParentNode(
            "span",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
        )
        outer_node = ParentNode(
            "div",
            [
                inner_node,
                LeafNode("i", "italic text"),
            ],
        )
        self.assertEqual(
            outer_node.to_html(),
            "<div><span><b>Bold text</b>Normal text</span><i>italic text</i></div>",
        )

    def test_to_html_with_props(self):
        # Test that props are correctly added to the HTML tag
        node = ParentNode(
            "div",
            [LeafNode("p", "Hello, world!")],
            {"class": "container", "id": "main"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container" id="main"><p>Hello, world!</p></div>',
        )

    def test_to_html_with_no_props(self):
        # Test that props are optional
        node = ParentNode("div", [LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")

    def test_to_html_with_mixed_children(self):
        # Test with mixed ParentNode and LeafNode children
        inner_node = ParentNode(
            "span",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node = ParentNode(
            "div",
            [
                inner_node,
                LeafNode("i", "italic text"),
                ParentNode("p", [LeafNode(None, "Another paragraph")]),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><span><b>Bold text</b>Normal text</span><i>italic text</i><p>Another paragraph</p></div>",
        )

    def test_to_html_with_deeply_nested_children(self):
        # Test deeply nested ParentNode objects
        innermost_node = ParentNode(
            "span",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
        )
        inner_node = ParentNode(
            "div",
            [
                innermost_node,
                LeafNode("i", "italic text"),
            ],
        )
        outer_node = ParentNode(
            "section",
            [
                inner_node,
                LeafNode("p", "A paragraph"),
            ],
        )
        self.assertEqual(
            outer_node.to_html(),
            "<section><div><span><b>Bold text</b>Normal text</span><i>italic text</i></div><p>A paragraph</p></section>",
        )
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    
if __name__ == "__main__":
    unittest.main()

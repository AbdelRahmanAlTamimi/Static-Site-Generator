# Static Site Generator

Converts Markdown files to HTML using a template system. Processes content from `content/` directory and generates a complete static website in `docs/`.

## What is This App?

A Python command-line tool that transforms Markdown content into a production-ready static website. Handles all common Markdown syntax (headings, bold/italic, code, links, images) and generates HTML pages ready for deployment.

## Requirements

- **Python 3.7+**
- **Bash** (optional, for build scripts)
- No external dependencies

## Quick Start

```bash
chmod +x build.sh
./build.sh
```

Or manually:
```bash
python3 src/main.py              # Default base path "/"
python3 src/main.py "/path/"     # Custom base path
```

Run tests:
```bash
bash test.sh
```

## Main Components

| Component | File | Purpose |
|-----------|------|---------|
| HTML Nodes | `htmlnode.py` | `HTMLNode`, `LeafNode`, `ParentNode` classes for rendering |
| Text Nodes | `textnode.py` | Handles text formatting (bold, italic, code) |
| Inline Parser | `inline_markdown.py` | Parses **bold**, *italic*, `code`, links, images |
| Block Parser | `blocks_markdown.py` | Parses headings, lists, quotes, code blocks |
| Generator | `website.py` | `generate_page()` and `generate_pages_recursive()` functions |
| Entry Point | `main.py` | Orchestrates build, copies static assets, generates pages |

## Directory Structure

```
content/          → Input Markdown files
static/           → CSS, images (copied as-is)
docs/             → Generated HTML output
src/              → Python source code
template.html     → HTML template with {{ Title }} and {{ Content }}
```

## Example

**Input:** `content/blog/post/index.md`
```markdown
# My Post

This is **bold** text.
```

**Output:** `docs/blog/post/index.html` (rendered from template)


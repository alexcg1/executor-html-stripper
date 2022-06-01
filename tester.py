from executor import HtmlStripper
from docarray import Document, DocumentArray

html = """
<div>
    <p>
        Some text
        <span>more text</span>
        even more text
    </p>
    <ul>
        <li>list item</li>
        <li>yet another list item</li>
    </ul>
</div>
<p>Some other text</p>
<ul>
    <li>list item</li>
    <li>yet another list item</li>
</ul>
"""

docs = DocumentArray(
    [
        Document(text=html),
        Document(text=html)
    ]
)

print([doc.text for doc in docs])

e = HtmlStripper()
e.strip_html(docs)

print([doc.text for doc in docs])

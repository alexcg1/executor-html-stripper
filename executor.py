from jina import Executor, DocumentArray, requests
from html2text import html2text

def strip_html(doc):
    doc.text = html2text(doc.text)


class HtmlStripper(Executor):
    @requests
    def strip_html(self, docs: DocumentArray, **kwargs):
        for doc in docs:
            strip_html(doc)

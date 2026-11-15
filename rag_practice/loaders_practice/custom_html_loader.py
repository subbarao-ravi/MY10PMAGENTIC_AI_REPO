from bs4 import BeautifulSoup
import requests
from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader
from typing import Iterator

class CustomHTMLLoader(BaseLoader):
    def __init__(self, url : str):
       self.url = url

    def lazy_load(self)-> Iterator[Document]:
        response = requests.get(self.url)
        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )
        # Remove non-content tags
        for tag in soup(["script", "style", "noscript", "nav", "footer"]):
                tag.decompose()

        text = soup.get_text(separator="\n", strip=True)
        title = soup.title.string.strip() if soup.title else soup.title.string

        yield Document(
             page_content= text,
             metadata = {
                "source": self.url,
                "title": title,
             }
        )

loader = CustomHTMLLoader("https://search.yahoo.com/search?fr=mcafee&type=E211US1358G0&p=Google")
documents = loader.load()
print(f"Loaded {len(documents)} documents ")
document = documents[len(documents)-1]
print('text ',document.page_content)
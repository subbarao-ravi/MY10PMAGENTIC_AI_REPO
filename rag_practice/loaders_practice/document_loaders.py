from langchain_core.documents import Document

document = Document(
    page_content='python is a programming language',
    metadata = {
        "source":"langchain.pdf",
        "department":"learning"
    }
)

print(document)
print(document.metadata.get("source"))

documents = [
    Document(
        page_content='learning python',
        metadata = {
             "source":"python.pdf",
             "department":"python"
        }
    ),
    Document(
            page_content='learning langchain',
            metadata = {
                 "source":"langchain.pdf",
                 "department":"langchain"
            }
    ),
    Document(
                page_content='learning rag',
                metadata = {
                     "source":"rag.pdf",
                     "department":"rag"
                }
    )
]

print(len(documents))

for number, document in enumerate(documents, start=1):
    print('page number', number, 'pagecontent ',document.page_content)
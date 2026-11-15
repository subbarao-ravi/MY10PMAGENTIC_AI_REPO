from langchain_community.document_loaders import TextLoader
from pathlib import Path

base_dir = Path(__file__).resolve().parent / "LoaderDocs"
base_dir.mkdir(exist_ok= True)

print('============Loading single text file==============')

file_path = base_dir / "sampletext.txt"
print('file_path ', file_path)

textLoader = TextLoader(
    file_path=str(file_path),
    encoding='utf-8'
)

documents = textLoader.load()
document = documents[0]
metadata = document.metadata
metadata['subject']='langchain'
print(document.page_content)
print(document.metadata)
print(Path(document.metadata['source']).name)
print(file_path.name)
print(type(document).__name__)

print('============Loading multiple text files==============')

all_documents = []
for file in base_dir.glob("*.txt"):
    if not file.is_file():
        print('----not a file---')

    textLoader = TextLoader(
        file_path=file
    )
    documents = textLoader.load()
    all_documents.extend(documents)

for index , document in enumerate(all_documents, start=1):
    print('document ',index, 'document content ', document.page_content)
    print('--------------------------------------------')
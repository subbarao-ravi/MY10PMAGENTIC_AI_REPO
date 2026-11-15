from langchain_community.document_loaders import WebBaseLoader

webloader = WebBaseLoader(
    web_paths=["https://sports.yahoo.com/articles/zealand-vs-india-2nd-odi-010001305.html?fr=sycsrp_catchall",
    "https://search.yahoo.com/search?fr=mcafee&type=E211US1358G0&p=ind+vs+nz+odi"],
    encoding='utf-8',
    default_parser="html.parser",
    requests_kwargs={"timeout":15},
    raise_for_status=True,
    bs_get_text_kwargs={
        "separator":"",
        "strip":True
    }
)

documents = webloader.load()
print(len(documents))
for index , document in enumerate(documents):
    print(document.page_content)
    print('-----------------------')
    print(document.metadata)
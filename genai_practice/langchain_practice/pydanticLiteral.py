from typing import Literal
from pydantic import BaseModel,Field
from dotenv import load_dotenv,find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

parser = StrOutputParser()

class Sentiment(BaseModel):
    sentiment : Literal[
        "positive",
        "negitive",
        "nuetral"
    ] = Field(description="overall sentiment")

    confidence : float = Field(
        le = 1,
        ge= 0,
        description='Confidence score between 0 and 1'
    )


# text = input('enter customer feed back ')


# structured_llm = llm.with_structured_output(Sentiment)
# result = structured_llm.invoke(text)
# print(result)

class SupportTicket(BaseModel):

    category: Literal[
        "Billing",
        "Technical",
        "Account",
        "Other"
    ] = Field(description="Main category of the customer issue") 

    priority: Literal[ 
            "low", 
            "medium", 
            "high" 
    ] = Field( description="Priority level of the issue" ) 

    severity: int = Field( 
                ge=1, 
                le=5, 
                description="Severity from 1 to 5" )
    
    summary: str = Field( description="Very short summary of the customer issue" )  

text = input('enter customer issue ')
structured_llm = llm.with_structured_output(SupportTicket)
result = structured_llm.invoke(text)
print(result)


import os
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# 내 랭귀지 모델이 웹사이트를 참조할 수 있게 함
# Tavily API key는 tvly- 로 시작하는 문자열입니다.
# API Key를 입력했다면, 이 셀을 실행해서 API Key를 환경 변수에 등록합니다.
# Tavily 사이트에서 바로 key 발급 가능

os.environ["TAVILY_API_KEY"] = "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"

from langchain_community.tools.tavily_search import TavilySearchResults

tavily_search_tool = TavilySearchResults(max_results=5)
response = tavily_search_tool.invoke({"query": "Trump와 일론머스크는 무슨 관계야?"})


llm = ChatOllama(model="mistral:7b")
embeddings = OllamaEmbeddings(model="mistral:7b")

def tavily_search_and_concat(query: str) -> str:
    results = tavily_search_tool.invoke({"query": query})
    return "\n".join([result["content"] for result in results])

def init_chain():
    messages_with_contexts = [
        ("system", "웹 검색을 통해 수집한 정보를 바탕으로 질문에 답하세요."),
        ("human", "정보: {context}.\n{question}."),
    ]

    prompt_with_context = ChatPromptTemplate.from_messages(messages_with_contexts)

    # 체인 구성
    # Context로 Tavily Serach API 결과를 이어 붙이는 함수를 사용합니다.
    qa_chain = (
        {"context": tavily_search_and_concat, "question": RunnablePassthrough()}
        | prompt_with_context
        | llm
        | StrOutputParser()
    )
    
    return qa_chain

qa_chain = init_chain()

question = "Trump와 일론머스크는 무슨 관계야?"

print(qa_chain.invoke(question))
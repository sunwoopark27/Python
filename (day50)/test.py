from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage  # 수정 완료
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

# 접속하려면 ollama run mistral:7b
# 대화창 끄려면 ctrl + c

llm = ChatOllama(model="mistral:7b")

print(llm.invoke("당신은 누구입니까?"))

messages = [
    SystemMessage(content=f"당신은 친절한 AI 어시스턴트 입니다."),
    HumanMessage(content="당신을 소개해주세요."),
]

response = llm.invoke(messages)

# print(response)

parser = StrOutputParser()
# Parser가 제대로 답변만을 리턴하는지 확인한다.
parsed_response = parser.invoke(response)

chain = llm | parser

chained_response = chain.invoke(messages)

message_with_variable = [
    ("system", "당신은 {role} 입니다."),
    ("human", "{question}")
]

prompt = ChatPromptTemplate.from_messages(message_with_variable)

chain = prompt | llm | parser

chain.invoke({"role" : "친절한 페어 프로그래머", "question" : "당신을 소개해주세요."})
print(chain)
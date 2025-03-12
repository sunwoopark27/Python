import contextlib #컨텍스트 관리 위한
import io #입출력 관리 위한
import os #환경 변수 관리 위한

import pandas as pd #데이터 분석 라이브러리
from langchain_community.chat_models import ChatOllama #챗모델 모듈
from langchain_community.embeddings import OllamaEmbeddings #임베딩 모듈
from langchain_core.output_parsers import StrOutputParser #출력 파서 모듈
from langchain_core.prompts import ChatPromptTemplate #프롬프트 템플릿 모듈
from langchain_core.runnables import RunnablePassthrough #실행 가능한 파이썬 코드 모듈
from langchain_experimental.tools.python.tool import PythonAstREPLTool #파이썬 코드 실행 모듈

# Ollama 모델 설정
llm = ChatOllama(model="mistral:7b")
embeddings = OllamaEmbeddings(model="mistral:7b")

# 타이타닉 데이터 불러오기
from sklearn.datasets import fetch_openml
titanic = fetch_openml(name='titanic', version=1, as_frame=True)
df_titanic = titanic.data
df_titanic['survived'] = titanic.target

# 변수명 저장
df_name = "df_titanic"
df_columns = ", ".join(df_titanic.columns)

# 시스템 프롬프트 작성
system_message = "당신은 타이타닉 데이터를 분석하는 데이터 분석가입니다.\n"
system_message += f"주어진 DataFrame에서 데이터를 출력하여 주어진 질문에 답할 수 있는 파이썬 코드를 작성하세요. {df_name} DataFrame에는 액세스할 수 있습니다.\n"
system_message += f"`{df_name}` DataFrame에는 다음과 같은 열이 있습니다: {df_columns}\n"
system_message += "각 열의 의미:\n"
system_message += "- pclass: 승객 등급 (1 = 1등석, 2 = 2등석, 3 = 3등석)\n"
system_message += "- sex: 성별 (male/female)\n"
system_message += "- age: 나이\n"
system_message += "- sibsp: 함께 탑승한 형제자매 및 배우자의 수\n"
system_message += "- parch: 함께 탑승한 부모 및 자녀의 수\n"
system_message += "- fare: 운임 요금\n"
system_message += "- embarked: 승선한 항구 (C = Cherbourg, Q = Queenstown, S = Southampton)\n"
system_message += "- boat: 탈출한 구명보트 번호\n"
system_message += "- body: 시신 식별 번호\n"
system_message += "- home.dest: 집/목적지\n"
system_message += "- survived: 생존 여부 (1 = 생존, 0 = 사망)\n"
system_message += "데이터는 이미 로드되어 있으므로 데이터 로드 코드를 생략해야 합니다."

message_with_data_info = [
    ("system", system_message),
    ("human", "{question}"),
]

# 프롬프트 템플릿 생성
prompt_with_data_info = ChatPromptTemplate.from_messages(message_with_data_info)

# 코드 생성 체인 구성
code_gen_chain = (
    {"question": RunnablePassthrough()}
    | prompt_with_data_info
    | llm
    | StrOutputParser()
)

# 코드 파서 함수 정의
def python_code_parser(input: str) -> str:
    processed_input = input.replace("```python", "```").strip()
    parsed_input_list = processed_input.split("```")
    
    if len(parsed_input_list) == 1:
        return processed_input
    
    parsed_code_list = []
    for i in range(1, len(parsed_input_list), 2):
        parsed_code_list.append(parsed_input_list[i])
    
    return "\n".join(parsed_code_list)

# 코드 파서 체인 구성
code_gen_chain_with_parser = (
    code_gen_chain
    | python_code_parser
)

# 코드 실행 함수 정의
def run_code(input_code: str):
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(input_code, {"df_titanic": df_titanic})
    except Exception as e:
        print(f"Error: {e}", file=output)
    return output.getvalue()

# 코드 실행 체인 구성 - 이 부분이 누락되었습니다
code_execute_chain = (
    code_gen_chain_with_parser |
    run_code
)

# 설명 체인 구성
analysis_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 타이타닉 데이터 분석 결과를 해석하고 설명하는 전문가입니다. 제공된 데이터 분석 결과를 바탕으로 사용자의 질문에 명확하게 답변해주세요."),
    ("human", "사용자 질문: {question}\n\n데이터 분석 결과: {analysis_result}")
])

explain_chain = (
    {"question": lambda x: x, "analysis_result": code_execute_chain}
    | analysis_prompt
    | llm
    | StrOutputParser()
)

# 예시 질문 실행
print(explain_chain.invoke("나이가 가장 많은 승객은 누구인가요?"))
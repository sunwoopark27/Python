https://wikidocs.net/book/14314 참고 공부 추천

여러가지 벡터저장소 사용해서 성능 보며 실습
![[Pasted image 20250313094000.png]]
## 1. RAG(Retrieval-Augmented Generation)의 주요 목적으로 가장 적절한 것은?

A) 언어 모델의 학습 속도 향상
B) 언어 모델의 매개변수 수 줄이기
C) 대규모 언어 모델의 기존 지식에 외부 데이터를 결합하여 더 정확한 답변 생성 
D) 텍스트 생성 비용 절감 
E) 사용자 인터페이스 개선

	답 : C (example>Tavily.py 코드 참고(웹서치해서 이해하고 요약해줌))

## 2. RAG 시스템의 사전 준비단계(인덱싱 파이프라인)에 포함되지 않는 과정은?

A) 도큐먼트 로드(Document Loader)
B) 텍스트 분할(Text Splitter)
C) 임베딩(Embedding)
D) 벡터스토어(Vector Store)저장 
E) LLM을 통한 답변 생성

	답 : E (Runtime 단계 )
	A -> B -> chuncking(문단을 살짝 겹치게 나누고) -> C -> D 

## 3. RAG 시스템에서 텍스트 분할(Text Splitter)의 주요 목적은?

A) 문서의 저작권 보호 
B) 로드된 문서를 처리 가능한 작은 단위(청크)로 분할 
C) 텍스트의 언어 감지 
D) 텍스트에서 수식 제거 
E) 텍스트를 다양한 언어로 번역

	답 : B

## 4. RAG의 임베딩(Embedding) 단계에서 수행하는 작업은?

A) 텍스트를 압축하여 저장 공간 절약
B) 텍스트를 암호화하여 보안 강화
C) 각 문서 청크를 벡터 형태로 변환하여 의미를 수치화
D) 텍스트를 다른 형식(PDF, HTML 등)으로 변환
E) 텍스트의 문법적 오류 수정

	답 : C

## 5. RAG 시스템의 런타임 단계에서 검색기(Retriever)의 역할은?

A) 사용자 질문과 의미적으로 관련된 문서 청크를 벡터 데이터베이스에서 검색
B) 웹에서 새로운 정보 크롤링
C) 사용자 질문의 언어 감지
D) 사용자의 의도 분류 
E) 답변 생성 속도 최적화

	답 : A

## 6. RAG 시스템에서 벡터스토어(Vector Store)의 주요 기능으로 가장 적절한 것은?

A) 이미지 데이터 저장
B) 사용자 정보 관리
C) 임베딩된 벡터들을 효율적으로 저장하고 검색할 수 있는 데이터베이스 제공
D) 모델 가중치 저장
E) 하드웨어 리소스 관리

	답 : C 
	youtube 테디노트 langchain노트의 한국어 튜토리얼 추천 (테디노트 위키 검색)

## 7. RAG의 프롬프트(Prompt) 단계에서 주로 수행하는 작업은?

A) 사용자 질문의 철자 오류 수정
B) 검색된 문서와 사용자 질문을 통합한 프롬프트 템플릿 설계
C) 벡터 데이터베이스 최적화
D) 모델 파라미터 조정
E) 이미지 프로세싱

	답 : B
	내 질문을 잘 가공해서 넣어줘야함 설계 중요

## 8. RAG 구현 시 청크 크기가 너무 작을 경우 발생할 수 있는 문제는?

A) 저장 공간 낭비
B) 처리 속도 저하
C) 컨텍스트 손실 
D) 보안 취약성 증가 
E) 배터리 소모 증가

	답 : C 
	문맥이해능력(의미파악)이 떨어질 수 있음 

## 9. RAG의 장점으로 볼 수 없는 것은?

A) LLM의 환각(Hallucination) 감소
B) 맞춤형 응답 생성 가능
C) 모델 재학습 없이 지식 확장 가능
D) 모델 크기의 축소 
E) 답변의 출처 추적 가능(투명성 향상)

	답 : D
	이미 모델은 Free trained 이기 때문에 상관없음.

## 10. RAG 시스템에서 '체인(Chain) 생성' 단계의 주요 목적은?

A) 다중 모델 앙상블 구축
B) 보안 강화
C) 사용자 인증 관리
D) 이전의 모든 과정을 하나의 파이프라인으로 통합
E) 데이터 백업 자동화

	답 : D

## 11. 다음 중 도큐먼트 로더(Document Loader)의 작업 내용으로 적절하지 않은 것은?

A) 다양한 형식(PDF, TXT, CSV, HTML 등)의 문서 수집
B) 데이터베이스, API, 웹 크롤링 등에서 데이터 가져오기
C) 임베딩 벡터 생성
D) 문서의 메타데이터 추출 및 정리
E) 초기 문서 처리

	답 : C (그 다음 단계이다.)

## 12. RAG 시스템에서 사용자 질의를 임베딩 벡터로 변환하는 단계는?

A) 도큐먼트 로드
B) 텍스트 분할
C) 임베딩
D) 검색기
E) LLM

	답 : C

## 13. RAG의 "환각(Hallucination) 감소" 장점은 어떻게 달성되는가?

A) 더 큰 모델 사용 
B) 실제 데이터에 기반한 답변 생성 
C) 프롬프트 길이 축소 
D) 더 많은 학습 데이터 사용 
E) 응답 속도 최적화

	답 : B

## 14. RecursiveCharacterTextSplitter와 TokenTextSplitter는 RAG의 어떤 단계에서 사용되는 도구인가?

A) 도큐먼트 로드 
B) 텍스트 분할 
C) 임베딩 
D) 벡터스토어 
E) LLM

	답 : B
## 15. RAG 구현 시 고려사항으로 적절하지 않은 것은?

A) 데이터 품질 
B) 청크 크기 최적화 
C) 임베딩 모델 선택 
D) 하드웨어 가속기 종류 
E) 프롬프트 엔지니어링

	답 : D

## 16. RAG 시스템에서 코사인 유사도는 주로 어떤 단계에서 활용되는가?

A) 텍스트 분할 
B) 임베딩 
C) 검색기 
D) 프롬프트 
E) 체인 생성

	답 : C

## 17. RAG 시스템에서 검색된 정보를 기반으로 최종 답변을 생성하는 구성 요소는?

A) 검색기(Retriever) 
B) 프롬프트(Prompt)
C) 임베딩(Embedding) 
D) LLM(Large Language Model)
E) 벡터스토어(Vector Store)

	답 : D

## 18. 다음 중 벡터스토어(Vector Store)의 예시 도구가 아닌 것은?

A) Pinecone 
B) Chroma 
C) FAISS 
D) Weaviate 
E) RecursiveCharacterTextSplitter

	답 : E
	 E 는 텍스트 분할 할때 사용
	 위의 링크에 렝체인 노트의 벡터 저장소에 설명이 있음
	 그때그때 성능이 달라질 수 있어 해봐야 정확히 알 수 있다.

## 19. RAG 시스템에서 "피드백 루프"의 주요 목적은?

A) 하드웨어 성능 모니터링 
B) 사용자 피드백을 통한 지속적인 시스템 개선 
C) 자동 백업 생성 
D) 개발자 알림 전송 
E) 배터리 사용량 최적화

	답 : B
	시스템을 계속 개선하기 위해서는 피드백 루프가 필요

## 20. RAG 시스템의 사전 준비단계와 런타임 단계를 올바르게 구분한 것은?

A) 사전 준비: 도큐먼트 로드, 텍스트 분할, 임베딩, 벡터스토어 저장 런타임: 검색기, 프롬프트, LLM, 체인 생성 
B) 사전 준비: 도큐먼트 로드, 텍스트 분할 런타임: 임베딩, 벡터스토어 저장, 검색기, 프롬프트, LLM, 체인 생성 
C) 사전 준비: 도큐먼트 로드, 텍스트 분할, 임베딩, 벡터스토어 저장, 검색기 런타임: 프롬프트, LLM, 체인 생성 
D) 사전 준비: 도큐먼트 로드, 텍스트 분할, 임베딩 런타임: 벡터스토어 저장, 검색기, 프롬프트, LLM, 체인 생성 
E) 사전 준비: 도큐먼트 로드 런타임: 텍스트 분할, 임베딩, 벡터스토어 저장, 검색기, 프롬프트, LLM, 체인 생성

	답 : A
	 
# 출력파서(Output Parser) 관련 객관식 문제

자연어가 아닌 json이나 다른 형태로 출력해야할 때
## 1. 출력파서(Output Parser)의 주요 목적으로 가장 적절한 것은?

A) 언어 모델의 훈련 데이터를 전처리하는 것 
B) 언어 모델의 매개변수를 최적화하는 것 
C) 언어 모델의 출력을 구조화된 형식으로 변환하는 것 
D) 언어 모델의 추론 속도를 향상시키는 것 
E) 언어 모델의 메모리 사용량을 줄이는 것

	답 : C
	
## 2. LangChain에서 제공하는 출력파서 종류 중 가장 단순한 형태의 파서는?

A) JSONOutputParser 
B) StringOutputParser 
C) PydanticOutputParser
D) RouterOutputParser
E) XMLOutputParser

	답: B (역시 맨위 링크에서 보며 공부)

## 3. `get_format_instructions()` 메서드의 주요 목적은 무엇인가?

A) 파서의 버전 정보를 제공 
B) LLM에게 출력 형식에 대한 명확한 지침 제공 
C) 파서의 성능을 평가
D) 출력 결과를 다른 형식으로 변환
E) 모델의 temperature 값을 자동으로 설정

	답 : B

## 4. 다음 중 출력파서의 핵심 역할이 아닌 것은?

A) 형식 변환 - LLM의 텍스트 출력을 구조화된 데이터로 변환 
B) 일관성 유지 - 일관된 출력 형식을 보장 
C) 모델 학습 - 언어 모델의 학습 과정 최적화 
D) 오류 처리 - 잘못된 출력 형식에 대한 오류 감지 및 처리 
E) 프롬프트 최적화 - 특정 형식의 출력을 유도하는 프롬프트 생성 지원

	답 : D

## 5. 다음 중 Pydantic 출력파서(PydanticOutputParser)의 주요 특징으로 올바른 것은?

A) 출력을 XML 형식으로만 변환 
B) 출력을 항상 리스트 형태로 변환 
C) Pydantic 모델을 사용하여 출력 검증 및 변환 
D) 파싱 실패 시 자동으로 재시도
E) 쉼표로 구분된 항목만 파싱 가능

	답 : C 
	내가 출력한 형태가 맞는지 검증

## 6. 출력파서를 사용하는 주요 장점으로 가장 적절하지 않은 것은?

A) 데이터 통합이 용이해진다 
B) 일관된 구조의 출력을 보장한다 
C) 모델의 추론 속도가 빨라진다 
D) 후처리 과정이 단순화된다 
E) 출력에 대한 자동 검증이 가능하다

	답 : C

## 7. 맞춤형 출력파서를 개발할 때 필요한 기본 클래스는?

A) CustomParser 
B) BaseOutputParser 
C) MainOutputParser 
D) ParserBase 
E) OutputParserFactory

	답 : B

# 콘다(Conda) 가상환경 관련 객관식 문제

## 1. 콘다(Conda)의 주요 목적이 아닌 것은?

A) 패키지 관리 
B) 가상 환경 관리 
C) 의존성 해결 
D) 웹 서버 호스팅 
E) 다양한 프로그래밍 언어 지원

	답 : D (오늘 streamlit사용해서 해볼 것임)
## 2. 콘다 가상환경을 생성하는 올바른 명령어는?

A) `conda new myenv python=3.9` 
B) `conda create -n myenv python=3.9` 
C) `conda venv myenv python=3.9` 
D) `conda init -n myenv python=3.9` 
E) `conda install myenv python=3.9`

	답 : conda create -n (이름) python=3.9 -> 버전을 꼭 적어주기! 안그러면 나중에 고생
## 3. 콘다 환경에서 패키지를 업데이트하는 올바른 명령어는?

A) `conda refresh package_name`
B) `conda update package_name` 
C) `conda upgrade package_name` 
D) `conda new-version package_name`
E) `conda latest package_name`

	답 : B
## 4. 콘다 가상환경에서 현재 설치된 모든 패키지 목록을 확인하는 명령어는?

A) `conda show` 
B) `conda packages` 
C) `conda list` 
D) `conda installed` 
E) `conda check`

	답 : C 
	❤️ conda env list : 내가 만든 환경 모두 보기 

## 5. 콘다에서 가상환경을 삭제하는 올바른 명령어는?

A) `conda delete -n myenv` 
B) `conda remove -n myenv` 
C) `conda env remove -n myenv`
D) `conda uninstall myenv` 
E) `conda erase myenv`

	답 : C (conda env remove -n (내가 삭제할 이름))
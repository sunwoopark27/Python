==**Day 1(3/14)**==

**주제선정**
	세계 행복 보고서 데이터 (World Happiness Report)

주제 설명

156개국의 주관적 행복 지표와 그 결정요인을 조사하여 국가별 행복 순위를 매긴 공개 데이터셋입니다 ([Analysis | The World Happiness Report](https://worldhappiness.report/analysis/#:~:text=The%20World%20Happiness%20Report%20is,combine%20to%20affect%20our%20happiness)). CSV 형식으로 여러 연도의 지표가 제공되며, 경제 규모, 사회적 지원, 기대수명 등의 변수도 포함되어 있습니다. 분석 아이디어: 나라별 행복 점수와 GDP, 사회적 지원 등 요인 간 상관관계를 분석하여 삶의 질에 영향을 미치는 주요 요인을 탐색하거나, 지역별로 행복도가 어떤 패턴을 보이는지 시각화해 볼 수 있습니다.
	
**Data :** 
https://worldhappiness.report/analysis/#:~:text=The%20World%20Happiness%20Report%20is,combine%20to%20affect%20our%20happiness

* 여기서 년도 하나 클릭 -> Appendices & Data -> Data for Figure 2.1 (첫번째 데이터셋 다운)
* csv파일 kaggle에서도 조회 가능

* 변수
* 

| **변수 구분**   | **WHR**                            | **변수 설명**                                                                |
| ----------- | ---------------------------------- | ------------------------------------------------------------------------ |
| 국가          | country                            |                                                                          |
| 지역          | region                             |                                                                          |
| 행복 점수       | happiness_score                    | 해당 국가의 전반적인 행복 수준을 수치화한 값  <br>점수가 높을수록 해당 국가의 전반적인 행복도가 높음을 의미          |
| 경제 수준 (GDP) | gdp_per_capita                     | 국가의 경제적 풍요 정도를 나타내는 지표로, 1인당 국내총생산을 의미  <br>경제적 여건이 행복에 미치는 영향을 평가할 때 사용 |
| 사회 지원       | social_support                     | 국민이 위기 상황에서 받을 수 있는 사회적 지원의 정도를 나타냄  <br>사회적 연결망과 신뢰 수준을 반영하는 변수         |
| 건강한 기대 수명   | healthy_life_expectancy            | 국민이 건강하게 기대할 수 있는 평균 수명을 나타냄  <br>건강 상태가 행복도에 미치는 영향을 분석할 때 중요한 요소       |
| 삶의 선택 자유    | freedom_to_make_life_choices       | 개인이 자신의 삶에 대해 선택을 할 수 있는 자유의 정도를 평가하는 변수                                 |
| 관대함         | generosity                         | 해당 사회 구성원들이 얼마나 관대하고 서로 도와주는지를 나타내는 지표                                   |
| 부패 인식       | perceptions_of_corruption          | 정부나 공공기관에 대한 부패 인식 정도를 나타내며, 사회적 신뢰와 관련된 요인으로 작용                         |
| 외부 데이터      | - 각 나라의 교육 수준  <br>- 전쟁의 영향  <br>- | 근거를 뒷받침할만한 추가 데이터를 가져올 수 있다.                                             |



1. 데이터 병합을 위해 각 데이터에 연도를 추가

	- 2019~2022년 파일을 분석 -> 파일 내에 년도 컬럼이 따로 없음
		- 유니온을 하면 년도 정보가 나오지 않음
	    - 조인 -> 년도별로 컬럼이름을 다르게 설정해야 한다.

* year 컬럼을 추가 csv파일을 저장 

```python
import pandas as pd # CSV 파일 읽기 
df = pd.read_csv('/content/WHR_2020.csv') 

# 'Year' 컬럼 추가 및 모든 값을 2020으로 설정
df['Year'] = 2022

# csv 파일 저장
df_2022.to_csv('/content/WHR_2022_year.csv', index=False)
```

==목표==
ㄷ

[^1]: ㅁㅇㄹㅁㅇ

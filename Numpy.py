# Numpy
# Python을 사용한 벡터의 산술연산 가능한 기본 패키지
# 반복문 없이 전체 데이터 배열 일괄 연산기능 제공(모든 요소가 동일한 데이터 타입이어야 함)
# 선형대수, 난수 생성, 푸리에 변환 등을 제공

!pip install numpy
import numpy as np

# 1. Array 생성
# Numpy 에서 Array를 만드는 법

# 1차원 배열 생성
d1 = [1,2,3,4]
np.array(d1) # 결과 : array([1, 2, 3, 4])

# 다른 데이터 타입끼리도 가능
mix_l = [1,2,'a',4]
np.array(mix_l)

# 2차원 배열 생성                 
np.array([[1,2,3],
          [4,5,6],
          [7,8,9]])

# 2. arange 함수를 이용한 배열 생성
# 문법
# numpy.arange(start, stop, step)
# 수의 범위를 만들어 주는 함수로, range와 다르게 실수 범위도 생성 가능(step이 존재한다면 start도 존재해야 함)

np.arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(0.1, 1.1, 0.1) # array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ])

# 3. linspace 함수를 이용한 배열 생성
# : 수의 범위를 균일하게 나누고자 할 때 사용
# 문법
# numpy.linspace(start, stop, num(몇개))

np.linespace(1,10,3) # array([ 1. ,  5.5, 10. ])

# 4. 기타 함수를 이용한 배열 생성
# ones(shape) : 1로 채워진 배열
# zeros(shape) : 0으로 채워진 배열
# full(shape,value) : value로 채워진 배열
# eye(N),indentity(N) : N차원 단위행렬

np.ones((2))          # array([1., 1.])
np.ones((2,2))        # array([[1., 1.],
                      #        [1., 1.]])
np.zeros((2,2))       # array([[0., 0.],
                      #        [0., 0.]])
np.full((2,2), -1)    # array([[-1, -1],
                      #        [-1, -1]])
np.eye(3)             # array([[1., 0., 0.],
                      #        [0., 1., 0.],
                      #        [0., 0., 1.]])

#

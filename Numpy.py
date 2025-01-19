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
numpy.arange(start, stop, step)
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

# 5. Numpy Array 속성
# - ndim : ndarray의 차원
# - shape : 각 차원의 ndarray 크기를 튜플 형태로 나타냄
# - size : ndarray에 있는 요소의 총 수
# - dtype : ndarray의 데이터 유형
# - T : 전치행렬, ndarray의 전치된 결과 반환(행열 바꾸기)

array = np.array([[1,2], [3,4]]) # array([[1, 2],
                                 #        [3, 4]])

print('array의 차원:', array.ndim)          # array의 차원: 2
print('array의 각 차원별 크기:', array.shape)  # array의 각 차원별 크기: (2, 2)
print('array의 요소의 총 개수:', array.size)   # array의 요소의 총 개수: 4
print('array의 데이터 유형:', array.dtype)     # array의 데이터 유형: int64

print('array (원본)')
print(array)
print('array (전치)')
print(array.T)

# array (원본)       # array (전치)
#[[1 2]             # [[1 3]
# [3 4]]            #  [2 4]]

# 5-1. Reshape : 배열 형태 변경
# ** 단, 변경 전 데이터의 개수와 변경 후 데이터의 개수(size) 같아야 함
#  문법
array.reshape(shape)
numpy.reshape(array, shape)
# -1은 딱 한번만 사용할 수 있으며, 자동으로 적절한 형태를 계산

array = np.arange(16)
print(array)           # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
array.shape            # (16,)

array4 = array.reshape(4,4)
print(array4)
array4.shape # (4,4)
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]
# [12 13 14 15]]

array8 = array.reshape(1,4,-1)
# 윗줄을 보면 array의 원본 배열의 크기가 16
# -1의 의미는 자동 계산 => array.reshape(1,4,n) 으로 1*4*n = 16이 되어야 한다
# 최종 모양은 (1,4,4)
print(array8) # 0 ~ 15 까지 네개씩 끊어 만듬
array8.shape # (1, 4, 4)

# 5-2. atype : 데이터 유형 변경
# Numpy Array를 생성시 dtype 지정을 생략하는 경우 자동으로 데이터 타입 결정
# 이미 만들어진 배열의 데이터 유형 변경하기 위해서는 astype함수 또는 특정 데이터 유형의 이름을 가진 함수 사용

# 문법
array.astype(nupmy.datatype)
numpy.datatype(array)
array.astype('datatype')

a = np.array([[1,2,3], [4,5,6]])
a.dtype # dtype('int64')

a_f = np.array([[1,2,3], [4,5,6]], dtype='float64')
a_f = np.array(np.arange(1,7).reshape(2,-1), dtype='float64')
print(a_f) # [[1. 2. 3.]
           #  [4. 5. 6.]]
a_f.dtype  # dtype('float64')
a.astype(np.float32) # array([[1., 2., 3.],
                     #        [4., 5., 6.]], dtype=float32)
np.int32(a_f)        # array([[1, 2, 3],
                     #        [4, 5, 6]], dtype=int32)
a.astype('int32')    # array([[1, 2, 3],
                     #        [4, 5, 6]], dtype=int32)


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

# 6. Numpy Array 연산

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

# 같은 자리끼리 더하기
print(a+b)
print(np.add(a,b))
# 같은 자리끼리 빼기
print(a-b)
print(np.subtract(a,b))
# 같은 자리끼리 곱하기
print(a*b)
print(np.multiply(a,b))
# 같은 자리끼리 나누기
print(a/b)
print(np.divide(a,b))

# 6-1. Array와 Scalar 연산(Broadcast)
print(a + 2) # 각 원소에 2 더하기
print(a - 2) # 각 원소에 2 빼기
print(a * 2) # 각 원소에 2 곱하기
print(a / 2) # 각 원소에 2 나누기

# 6-2. Array와 Array 연산 (내적 연산, 행렬곱, 제곱근)

print(a@b)                       # [[19 22] 
print(np.matmul(a,b))            #  [43 50]]            
print(np.dot(a,b))

print(np.sqrt(a))                # [[1.         1.41421356]
                                 #  [1.73205081 2.        ]]

print(a**0.5)                    # [[1.         1.41421356]
                                 #  [1.73205081 2.        ]]
 
print(np.sqrt(a))                # [[1.         1.41421356]
                                 #  [1.73205081 2.        ]]

# 7. 인덱싱 : [행 인덱스, 열 인덱스]

array = np.arange(9).reshape(3,3) # array([[0, 1, 2],
                                  #        [3, 4, 5],
                                  #        [6, 7, 8]])

array[0] # array([0, 1, 2])
array[0,0] # 0
# -1은 마지막을 뜻함!
array[-1,-1] # 8

# 7-1. 조건 인덱싱
# - Boolean Array를 이용하여 인덱싱하는 방법

# array([[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8]])

# array 의 모양이 위와 같다고 할 때
bidx = array % 2 == 0
print(bidx)
# [[ True False  True]
#  [False  True False]
#  [ True False  True]]

array[bidx] # array([0, 2, 4, 6, 8])
array[array % 2 ==0]  # array([0, 2, 4, 6, 8])
array[array > 5] # array([6, 7, 8])

# 7-2. 팬시 인덱싱(Fancy Indexing)
#      다른 Array를 이용하여 인덱싱하는 방법
#      선택하고자 하는 위치를 Array로 묶어서 데이터 접근 가능

# array 설정
# array([[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8]])

row = [0,1]
col = [2,1]
# array [[0,1],[2,1]]
# 똑같은 위치의 값끼리 연결 되어 [0,2]와 [1,1]의 값을 가져와 저장
a1 = array[row,col] # array([2, 4])
# array[0,2]의 값을 10으로 변경
array[0,2] = 10     # (array([[ 0,  1, 10],
                    #         [ 3,  4,  5],
                    #         [ 6,  7,  8]])

# 8. Numpy Array 슬라이싱
#  : 콜론(:) 을 사용하여 특정 범위의 값에 접근 가능

# array([[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8]])

array[0,:]    # array[0,다] # array([0, 1, 2])
array[:,1]    # array[다,1] # array([1, 4, 7])
array[:2,1:]  # array[0~1행,1~끝 열] # array([[1, 2],
                               #        [4, 5]])
array[-1:,1:3] # -1은 마지막을 뜻함 : 뒤에 아무것도 오지 않아 끝을 지정하지 않았으므로 마지막만!
               # array[마지막행,1~2열] # array([[7, 8]])


# --- 슬라이싱 시 고려사항
# Numpy는 다차원배열(ndarray)을 염두하고 설계되었기 때문에 데이터의 복사를 남발하지 않음
# 원본 배열을 슬라이싱하여 새로운 배열을 만든 경우, 새로운 배열은 원본과 값을 공유하고 속성은 별도로 관리함

# ** 슬라이싱한 새 배열 수정하면 원본 배열도 수정됨!!
# 값을 복사하여 저장하고 싶은 경우 copy() 함수 이용
# array([[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8]])

sliceA = array[:,1]    # array([1, 4, 7])
id(array), id(sliceA)  # (134251804389328, 134251804392784) #둘이 다르다는 게 포인트
np.shares_memory(array, sliceA) # True

# slice 한 것을 변형해도 원본이 바뀐다!!
sliceA[0] = 10 #array([[ 0, 10, 10],
array          #       [ 3,  4,  5],
               #       [ 6,  7,  8]])
# 복사해서 사용
copyA = array[:,1].copy()
copyA          # array([1, 4, 7])

# 변경해도 원본이 바뀌지 않음!!!!!!!!!
copyA[0] = 1
copyA

# 9. Numpy 주요 함수
# - np.where
# - np.random
# - 통계함수

# 9-1. np.where(조건,[x,y]) ([x,y]생략가능)
# : 조건을 만족하는 요소의 위치를 반환 (row, col) 형태로
#   x, y를 지정하는 경우, 값이 대체된 배열을 반환
#   - x : 요소의 조건이 True인 경우 지정할 값
#   - y : 요소의 조건이 False인 겨우 지정할 값

array = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])
indices = np.where(array % 2 == 0)
print(indices)                       
# (array([0, 1, 1]), array([1, 0, 2]))
# 짝수는 2, 4, 6 으로 array[0, 1] = 2 / array[1, 0] = 4 / array[1, 2] = 6

# 응용 : 배열 생성
values = array[np.where(array % 2 == 0)]
print(values)                            # [2,4,6]

# 2로 나눠 나머지가 0인 것은 'reserve' 아닌 것은 'available'
np.where(array%2==0, 'reserve','available')

# 9-2. 난수 배열 생성 np.random

# -- rand는 0과 1사이에서 난수 생성 --
# numpy.random.rand(shape)
# numpy.random.randint(low, high, size=shape)
# numpy.random.normal(loc=평균, scale=표준편차, size=shape)

np.random.rand()

#### 1) numpy.random.rand(shape)

np.random.rand(2,3) # size가 (2,3)인 행렬

# 랜덤 시드 설정 (재현 가능성을 위해)
np.random.seed(24)

# 2x3x4 크기의 배열 생성
# 2개의 "블록": [[ ... ]] 두 개.
# 각 블록에는 3개의 "행".
# 각 행에는 4개의 난수.
array = np.random.rand(2, 3, 4) 
print(array)
# 결과
#array([[[0.15169108, 0.02158908, 0.33476293, 0.47580486],
#        [0.84139183, 0.42119277, 0.53586629, 0.93188997],
#        [0.19607132, 0.00137107, 0.80817883, 0.03800177]],

#       [[0.49144389, 0.14264389, 0.44990434, 0.36686108],
#        [0.02523468, 0.35343412, 0.22153686, 0.26543055],
#        [0.50269416, 0.74898668, 0.85437948, 0.4210761 ]]])

#### 2) numpy.random.randint(low, high, size=shape)
# int 정수 값으로
np.random.randint(30)

# 1부터 30까지 (2,3) 사이즈로 랜덤 배열
np.random.randint(1,30,size=(2,3))

# 0부터 30까지 (2,3) 사이즈로 랜덤 배열
np.random.randint(30,size=(2,3))

#### 3) numpy.random.normal(loc=평균, scale=표준편차, size=shape)
np.random.normal(0,1,size=(2,3))

# 9-3. 통계함수
# : 배열의 주어진 요소로부터, 최소, 최대, 백분위수, 표준편차, 분산 등을 찾는 통계함수가 존재
#   axis옵션을 통해 연산 방향을 지정
#   axis 지정이 안된 경우 모든 요소의 연산 결과가 반환
#   axis=0 : 행과 행의 연산 결과를 반환
#   axis=1 : 열과 열의 연산 결과를 반환

array.min(), array.max()
np.quantile(array,0.1)
array.quantile(0.1)
np.min(array)
array.sum()
array.mean()
array.std()
array.var()
array.argmin()
array.argmax())
array.prod()
array.cumsum()
array.cumprod()
array.sum()
array.sum(axis=0)
array.sum(axis=1)
array.argmin(axis=1), array.argmax(axis=0)

# 10. Numpy 입출력
#  : Numpy 배열을 파일로 저장 또는 저장된 파일에서 Numpy배열을 불러올수 있음
#    Numpy배열을 파일로 저장하기 위해 save savez 함수 이용
#    파일에서 불러오기 위해 load 함수 이용

# 문법
numpy.save(<파일명>, array)
numpy.savez(<파일명>, **arrays)
numpy.load(<파일명>)

array1 = np.arange(9).reshape(3,3)
array2 = np.arange(4).reshape(2,2)

np.save('array', array1)

array = np.load('array.npy')
array

np.savez('arrayZip', array1, array2)
arrayZip = np.load('arrayZip.npz')
arrayZip  # NpzFile 'arrayZip.npz' with keys: arr_0, arr_1
arrayZip['arr_0'] # 이렇게 해야 배열 array1 출력

np.savez('arrayZip', array1=array1, array2=array2) # key 명을 지정해 줄 수도 있음
arrayZip['array2']









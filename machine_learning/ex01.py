# import warnings
# warnings.simplefilter(action='ignore', category='FutureWarning')

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
 
#상수 정의 하기
a = tf.constant(120, name = 'a')
b = tf.constant(130, name = 'b')
 
#변수 정의 및 초기 값 할당하기
v = tf.Variable(0, name='v')
 
result = a + b
 
#세션 실행하기
sess = tf.Session()
 
#내용 출력하기
print('결과 :', sess.run(result))
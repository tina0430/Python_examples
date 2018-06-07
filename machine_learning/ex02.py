# import warnings
# warnings.simplefilter(action='ignore', category='FutureWarning')

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
 
#상수 정의 하기
a = tf.constant(14, name = 'a')
b = tf.constant(5, name = 'b')
 
#변수 정의 및 초기 값 할당하기
v = tf.Variable(0, name='v')
 
plus = a + b
subtract = a - b
multiply = a * b
division = a / b
 
#세션 실행하기
sess = tf.Session()
 
#내용 출력하기
print('더하기 :', sess.run(plus))
print('배기 :', sess.run(subtract))
print('나누기 :', sess.run(multiply))
print('곱하기 :', sess.run(division))
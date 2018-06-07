import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(2)
b = tf.constant(1)

x = tf.Variable(5)

result = tf.add(tf.multiply(a, x), b)

sess = tf.Session()

sess.run(tf.global_variables_initializer())

#a는 정수형 상수 값으로 텐서
print('a 는', a, end= '    ')
print(type(a))
print('a 결과 출력 :', sess.run(a))

print('실행 결과 :', sess.run(result))
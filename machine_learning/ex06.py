import tensorflow as tf

#상수, 변수 선언하기
a = tf.constant(100, name='a')
b = tf.constant(100, name='b')
c = tf.constant(100, name='c')
v = tf.constant(100, name='v')

#곱셈을 수행하는 그래프 정의하기
calc_op = a - b *c
assign_op = tf.assign(v, calc_op)

#세션 생성하기
sess = tf.Session()

#텐서보드 사용하기
tw = tf.summary.FileWriter('log_dir', graph=sess.graph)

#세션 실행하기
sess.run(assign_op)
print(sess.run(v))
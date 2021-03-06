# coding=UTF-8
import tensorflow as tf

# 设置了gpu加速提示信息太多了，设置日志等级屏蔽一些
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

# 创建一个常量 Operation (操作)
hw = tf.constant("Hello World! Mtianyan love TensorFlow!")

# 启动一个 TensorFlow 的 Session (会话)
sess = tf.Session()

# 运行 Graph (计算图)
print (sess.run(hw))

# 关闭 Session（会话）
sess.close()

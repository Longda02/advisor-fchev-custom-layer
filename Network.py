import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

def NetworkInput(SoCbat, SoCuc, V, Pdemand, Puc):
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph('MODEL/1/1.ckpt.meta')
        saver.restore(sess, tf.train.latest_checkpoint('MODEL/1'))
        graph = tf.get_default_graph()
        W1 = graph.get_tensor_by_name('Actor/target_net/l1/w1:0')
        B1 = graph.get_tensor_by_name('Actor/target_net/l1/b1:0')
        W2 = graph.get_tensor_by_name('Actor/target_net/l2/w2:0')
        B2 = graph.get_tensor_by_name('Actor/target_net/l2/b2:0')
        W3 = graph.get_tensor_by_name('Actor/target_net/l3/w3:0')
        B3 = graph.get_tensor_by_name('Actor/target_net/l3/b3:0')
        W4 = graph.get_tensor_by_name('Actor/target_net/l4/w4:0')
        B4 = graph.get_tensor_by_name('Actor/target_net/l4/b4:0')
        V = round((V - 10) / 50, 2)
        Pdemand = round(Pdemand / 23.5, 2)
        s = np.array([SoCbat, SoCuc, V, Pdemand, Puc]);
        s = tf.cast(s[np.newaxis, :], dtype=tf.float32)
        l1 = tf.nn.relu(tf.matmul(s, W1) + B1)
        l2 = tf.nn.relu(tf.matmul(l1, W2) + B2)
        l3 = tf.nn.relu(tf.matmul(l2, W3) + B3)
        l4 = tf.nn.sigmoid(tf.matmul(l3, W4) + B4)
        action = tf.multiply(l4, 1)
        act = sess.run(action)
        act1 = float(np.round(act[0], 2))
        return act1


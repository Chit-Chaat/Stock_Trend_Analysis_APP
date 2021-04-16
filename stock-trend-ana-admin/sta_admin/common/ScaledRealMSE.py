__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2021/4/14 4:40'

import tensorflow as tf


class ScaledRealMSE(tf.keras.metrics.Metric):
    def __init__(self, name="Scaled_Real_MSE", **kwargs):
        super(ScaledRealMSE, self).__init__(name=name, **kwargs)
        self.total = self.add_weight('total', initializer='zeros')
        self.count = self.add_weight('count', initializer='zeros')
        self.y_min = float('inf')
        self.y_max = float('-inf')

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_true = tf.cast(y_true, dtype=tf.float32)
        y_pred = tf.cast(y_pred, dtype=tf.float32)
        self.y_max, self.y_min = tf.reduce_max(y_true, axis=0), tf.reduce_min(y_true, axis=0)
        t = tf.reduce_mean(tf.math.square(y_true - y_pred), axis=-1)
        if sample_weight is not None:
            sample_weight = tf.cast(sample_weight, dtype=tf.float32)
            ndim = t.ndim
            weight_ndim = sample_weight.ndim
            t = tf.reduce_mean(t, axis=list(range(weight_ndim, ndim)))
            t = tf.multiply(t, sample_weight)

        t_sum = tf.reduce_sum(t)
        self.total.assign_add(t_sum)
        if sample_weight is not None:
            num = tf.reduce_sum(sample_weight)
        else:
            num = tf.cast(tf.size(t), dtype=tf.float32)
        self.count.assign_add(num)

    def result(self):
        return self.total * 100 / (self.y_max - self.y_min)

#
# a = tf.random.uniform([2, 3, 4])
# b = tf.random.uniform([2, 3, 4])
# w = tf.random.uniform([2, 3])
# m = tf.keras.metrics.MeanSquaredError()
# m.update_state(a, b, w)
# print(m.get_weights())
# print(m.result().numpy())
# mae = RealMSE()
# mae.update_state(a, b, w)
# print(mae.get_weights())
# print(mae.result().numpy())

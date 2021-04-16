__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2021/4/14 4:40'

import tensorflow as tf


class RealMSE(tf.keras.metrics.Metric):
    def __init__(self, name="Real_MSE", **kwargs):
        super(RealMSE, self).__init__(name=name, **kwargs)
        self.total = self.add_weight('total', initializer='zeros')
        self.count = self.add_weight('count', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_true = tf.cast(y_true, dtype=tf.float32)
        y_pred = tf.cast(y_pred, dtype=tf.float32)
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
        return self.total

#

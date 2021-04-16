__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2021/4/16 3:09'

class FloatUrlParameterConverter:
    regex = '[0-9]+\.?[0-9]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)
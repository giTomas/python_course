# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    filename='example.log',
    level=logging.DEBUG)

class LoggingDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        logging.info('Setting {} to {}'.format(key, value))


    def __getitem__(self, key):
        logging.info('Getting {} '.format(key))
        return super().__getitem__(key)

    def sum(self):
        sum = 0
        for val in super().values():
            sum += val
        logging.info('Sum of all values is {}'.format(sum))
        return sum

d = LoggingDict()
d['a'] = 15
d['a']
d['a'] = 35
d['b'] = 90
val = d.sum()
print(val)

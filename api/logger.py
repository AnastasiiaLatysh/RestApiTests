import datetime


# TODO этот модуль не относится к api, было бы логично вынести его в lib
# TODO Почему бы не использовать стандартную бибилиотеку logging?
def log(log_message='', log_level='DEBUG'):
    print('%s %s: %s' % (log_level, str(datetime.datetime.now()), log_message))

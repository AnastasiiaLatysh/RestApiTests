import datetime


def log(log_message='', log_level='DEBUG'):
    print('%s %s: %s' % (log_level, str(datetime.datetime.now()), log_message))

# coding:utf-8
import logging
import logging.config

# logging.basicConfig(level=logging.DEBUG)
clog = 'log.conf'
logging.config.fileConfig(clog)
logging = logging.getLogger()

logging.debug('debug info')
logging.info('hello 51zxw ！')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')

import logging,logging.handlers
import sys
import os


logger = logging.getLogger()

# formatter = logging.Formatter('%(asctime)s %(levelname)s  %(message)s --> %(filename)s(%(lineno)d):%(funcName)s()')
#
# super_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
# if not os.path.exists(super_path + '/logs/app'):
#     os.makedirs(super_path + '/logs/app')
#
# file_path = super_path + '/logs/app/app.log'

logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)


logger.debug('hello')

from US_Visa.logger import logging
from US_Visa.exception import USvisaException
import sys

try:
  r = 3/0
  print(r)
except Exception as e:
  logging.info(e)
  raise USvisaException(e, sys)

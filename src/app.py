import logging as log
from flask import Flask

log.basicConfig(level='ERROR')

app_instance = Flask( __name__ )

if __name__ == '__main__':
  from api import *

  log.debug( 'Starting server....' )
  app_instance.run( host='0.0.0.0' )
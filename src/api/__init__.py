from flask import app
from flask_restful import Api
from app import app_instance
from .tasks import *


service = Api( app_instance )

routes = [
  { 'resource': Status, 'path': '/status'},
  { 'resource': ChangeStatus, 'path': '/change-status'}
]

for route in routes:
  service.add_resource( route['resource'], route['path'] )
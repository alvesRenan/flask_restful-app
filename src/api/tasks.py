import logging as log
from flask_restful import Resource


class StatusOK(Resource):
  def get(self):
    return { 'code': 200, 'msg': 'Running' }

class StatusError(Resource):
  def get(self):
    return { 'code': 500, 'msg': 'Error' }

from flask_restful import Resource

STATUS_OK = True

class Status(Resource):
  def get(self):
    if STATUS_OK:
      return { 'code': 200, 'msg': 'Running' }
    
    return { 'code': 500, 'msg': 'Error' }

class ChangeStatus(Resource):
  def get(self):
    STATUS_OK = not STATUS_OK
    
    return { 'code': 200, 'msg': f'New status is {STATUS_OK}' }

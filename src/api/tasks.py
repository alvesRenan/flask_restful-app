import json
from flask_restful import Resource


class Status(Resource):

  def get(self):
    with open('api/json_response.json') as json_file:
      return json.load(json_file)

  def post(self):
    running_json = {"code": 200,"msg": "Running"}
    error_json   = {"code": 500,"msg": "Error"}

    with open('api/json_response.json') as json_file:
      data = json.load(json_file)

    with open('api/json_response.json', 'w') as json_file:
      if data.get('code') == 200:
        json.dump(error_json, json_file)
        return error_json
    
      json.dump(running_json, json_file)
      return running_json

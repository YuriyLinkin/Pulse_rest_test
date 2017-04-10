import requests

class Pulse_Api_Roles:
    def __init__(self, resourse):
        self.host = 'pulse-rest-testing.herokuapp.com'
        self.base_url = "http://{}/".format(self.host)
        self.url = self.base_url + resourse + '/'

    def create_role(self, obj):
        obj_data = obj.get_dict()
        resp = requests.post(self.url, data=obj_data)
        obj.set_id(resp.json()['id'])
        return resp


    def get_objects(self, obj):
        resp = requests.get(self.url, params=obj.set_id())
        print(resp)
        return resp

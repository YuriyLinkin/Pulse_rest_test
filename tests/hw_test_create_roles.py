import unittest

from Pulse_rest_test.fixtures.hw_pulseApiRoles import Pulse_Api_Roles
from Pulse_rest_test.models.hw_classRoles import Role


class RoleCreateTests(unittest.TestCase):
    def setUp(self):
        self.client = Pulse_Api_Roles(resourse="roles")

    def test_create_role(self):
        role = Role(name='Hemingway', type='novel', level=null, book=1)
        resp = self.client.create_role(role)
        self.assertEqual(resp.status_code, 201)
        self.assertDictEqual(resp.json(), role.get_dict_with_id())
        self.assertDictEqual(resp.json(), role.get_dict_with_null())


q = RoleCreateTests()

print(q)
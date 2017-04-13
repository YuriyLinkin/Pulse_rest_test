import pytest


from models.hw_classRoles import Role
test_data_=[Role(name="Pulse1",  type='po', level=1, book=1),
            Role(name="Pulse2", type='poo', level=2, book=1),
            Role(name="Pulse3",  type='popp', level=3, book=1),
            Role(name="Pulse4",  type='pupo', level=4, book=1)]

@pytest.mark.parametrize('role', test_data_, ids=[repr(z) for z in test_data_])
def test_create_role(app_role, role):
    resp = app_role.create_role(role)

    assert resp.status_code == 201
    assert resp.json() == role.get_dict_with_id()


# class RoleCreateTests(unittest.TestCase):
#     def setUp(self):
#         self.client = Pulse_Api_Roles(resourse="roles")
#
#     def test_create_role(self):
#         role = Role(name='Hemingway', type='novel', level=null, book=1)
#         resp = self.client.create_role(role)
#         self.assertEqual(resp.status_code, 201)
#         self.assertDictEqual(resp.json(), role.get_dict_with_id())
#         self.assertDictEqual(resp.json(), role.get_dict_with_null())
#
#
# q = RoleCreateTests()
#
# print(q)
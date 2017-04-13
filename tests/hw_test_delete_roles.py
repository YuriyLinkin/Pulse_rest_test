import pytest
from models.hw_classRoles import Role

@pytest.fixture
def book(app_role):
    z = Role (name= "For del", type= "for_del", level= 'del', book= 'fDel')
    app_role.create_role(z)
    return z

def test_delete(app_role, role):
    resp = app_role.delete_obj(role)

    assert resp.status_code == 204
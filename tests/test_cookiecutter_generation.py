# -*- coding: utf-8 -*-

# import stdlibs
import os
import re
# import third party libs
import pytest
# import local libs


@pytest.fixture
def organization_context():
    return {
        "ansible_role_organization_name": "myorg",
    }


def test_default_configuration(cookies):
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'ansible_role'
    assert result.project.isdir()

def test_organization_configuration(cookies, organization_context):
    result = cookies.bake(extra_context=organization_context)
    print result
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'myorg.ansible_role'
    assert result.project.isdir()

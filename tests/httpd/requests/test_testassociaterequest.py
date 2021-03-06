# -*- coding: utf-8 -*-
import mock

from keepass_http.httpd import requests


class TestBackend(mock.Mock):
    pass


@mock.patch.object(requests.Request, "authenticate")
def test_testassociaterequest(mock_authenticate):
    mock_authenticate.side_effect = requests.AuthenticationError

    test_dict = {"Id": "test_clientname"}
    request = requests.TestAssociateRequest()

    assert request(test_dict) == {"Success": False}


def test_testassociaterequest_invalid_clientname():
    request = requests.TestAssociateRequest()
    assert request({}) == {"Success": False}


@mock.patch.object(requests.Request, "set_verifier")
@mock.patch.object(requests.Request, "authenticate")
def test_testassociaterequest_ok(mock_authenticate, mock_set_verifier):
    test_dict = {"Id": "test_clientname"}
    request = requests.TestAssociateRequest()

    assert request(test_dict) == {"Id": "test_clientname", "Success": True}

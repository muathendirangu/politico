import json
from tests.test_base import BaseTest
from app import create_app
from api.utils.test_data import party_with_data, party_with_empty_fields, party_with_wrong_name_type
from api.utils.test_data import party_with_wrong_address_input, party_with_wrong_logo_url
from api.utils.test_data import party_with_invalid_key_name, party_with_invalid_key_address, party_with_wrong_name_input, party_with_wrong_address_type
class TestParty(BaseTest):
    def test_add_party(self):
        """test creation of a party."""
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_data),
            content_type="application/json",
            headers=self.super_token
        )
        data = json.loads(response.data.decode("utf-8"))
        print(data)
        self.assertEqual(response.status_code, 201)

    def test_add_party_with_missing_input(self):
        response = self.client.post(
            '/api/v2/parties',
            data = json.dumps(party_with_empty_fields),
            content_type = "application/json",
            headers=self.super_token
        )
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)

    def test_get_all_parties(self):
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
        )
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
        )

        response = self.client.get('/api/v2/parties')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)



    def test_party_with_name_of_wrong_data_type(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_wrong_name_type),
            content_type="application/json",
            headers=self.super_token
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_party_party_with_wrong_name_input(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_wrong_name_input),
            content_type="application/json",
            headers=self.super_token
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_party_with_wrong_address_input(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_wrong_address_input),
            content_type="application/json",
            headers=self.super_token
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_party_with_wrong_address_type(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_wrong_address_type),
            content_type="application/json",
            headers=self.super_token
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_party_with_the_wrong_url_format(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_wrong_logo_url),
            content_type="application/json",
            headers=self.super_token
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

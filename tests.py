import unittest
from confidentify_client import ApiClient
from confidentify_client.api import AuthApi, ProcessApi
from confidentify_client.models import AuthRequest, PersonNameRequest, PersonNameRequestRecord
import os

class Tests(unittest.TestCase):
    def test_vanilla_scenario(self):
        username = os.getenv("CONFIDENTIFY_USERNAME")
        password = os.getenv("CONFIDENTIFY_PASSWORD")

        if not username or not password:
            print("Skipping tests since CONFIDENTIFY_USERNAME and CONFIDENTIFY_PASSWORD environment variables are not set.")
            return
        
        with ApiClient() as api_client:
            auth_response = AuthApi(api_client).auth_post(AuthRequest(username, password))
            access_token = auth_response.access_token
            api_client.configuration.access_token = access_token

            name_records = [PersonNameRequestRecord(name="John F Kennedy")]
            name_response = ProcessApi(api_client).person_name_post(PersonNameRequest(name_records))
            name_response_entity = name_response.records[0].entities[0].to_dict()
            self.assertDictEqual({
                    'family': 'Kennedy',
                    'family_main': 'Kennedy',
                    'family_prefix': '',
                    'given': 'John',
                    'middle': 'F',
                    'name_formatted': 'John F Kennedy',
                    'nicknames': ['Jack',
                                'Johnathan',
                                'Johnathon',
                                'Johnie',
                                'Johnnie',
                                'Johnny',
                                'Jonathan'],
                    'suffix': ''
                } , name_response_entity)

if __name__ == '__main__':
    unittest.main()

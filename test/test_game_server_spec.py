# coding: utf-8

"""
    sdk.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agones_python_sdk.models.game_server_spec import GameServerSpec

class TestGameServerSpec(unittest.TestCase):
    """GameServerSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameServerSpec:
        """Test GameServerSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameServerSpec`
        """
        model = GameServerSpec()
        if include_optional:
            return GameServerSpec(
                health = agones_python_sdk.models.game_server_spec_health.GameServerSpecHealth(
                    disabled = True, 
                    period_seconds = 56, 
                    failure_threshold = 56, 
                    initial_delay_seconds = 56, )
            )
        else:
            return GameServerSpec(
        )
        """

    def testGameServerSpec(self):
        """Test GameServerSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

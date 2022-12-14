from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis, models

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="9c0384afef4e8f02edc6fce4c1e8053726cd522de13519a8236c6aaf8661f110",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.AccountApi(api_client)

    data = models.AccountVerifyRequest(
        email_address="shibbonstar@gmail.com",
    )

    try:
        response = api.account_verify(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
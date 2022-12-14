# from hellosign_sdk import HSClient

# # Initialize HSClient using email and password
# client = HSClient(email_address="shibbonstar@gmail.com", password="$e6Sb$3nQ4EESsS")

# # Initialize HSClient using api key
# client = HSClient(api_key="9c0384afef4e8f02edc6fce4c1e8053726cd522de13519a8236c6aaf8661f110")

# # Initialize HSClient using api token
# client = HSClient(access_token="9c0384afef4e8f02edc6fce4c1e8053726cd522de13519a8236c6aaf8661f110")

# # print(client.account.email_address)
# account = client.get_account_info()
# print(account)

from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="9c0384afef4e8f02edc6fce4c1e8053726cd522de13519a8236c6aaf8661f110",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.SignatureRequestApi(api_client)

    signature_request_id = "fa5c8a0b0f492d768749333ad6fcc214c111e967"

    try:
        response = api.signature_request_get(signature_request_id)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)
from pprint import pprint
from hellosign_sdk import HSClient

f = open('api.txt', 'r')
api_key = f.read()
client = HSClient(api_key=api_key)

print(client)
print(client.get_account_info())


client.send_signature_request(
        test_mode=True,
        title="title=Test Title.",
        subject="Test Subject",
        message="Please sign this.",
        signers=[{ 'email_address': 'shibbonstar@gmail.com', 'name': 'Shoto Morisaki' }], #Receiver
        files=['Medical-Doctors-Note-for-Work-Sample-Word-Download copy.jpg'] #File name
)


# from hellosign_sdk import \
#     ApiClient, ApiException, Configuration, apis

# configuration = Configuration(
#     # Configure HTTP basic authorization: api_key
#     username="9c0384afef4e8f02edc6fce4c1e8053726cd522de13519a8236c6aaf8661f110",

#     # or, configure Bearer (JWT) authorization: oauth2
#     # access_token="YOUR_ACCESS_TOKEN",
# )

# with ApiClient(configuration) as api_client:
#     api = apis.SignatureRequestApi(api_client)

#     signature_request_id = "fa5c8a0b0f492d768749333ad6fcc214c111e967"

#     try:
#         response = api.signature_request_get(signature_request_id)
#         pprint(response)
#     except ApiException as e:
#         print("Exception when calling HelloSign API: %s\n" % e)

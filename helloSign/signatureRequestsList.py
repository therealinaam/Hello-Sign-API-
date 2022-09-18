from pprint import pprint

from hellosign_sdk import HSClient
# from hellosign_sdk import ApiClient
# from hellosign_sdk import ApiException
# from hellosign_sdk import Configuration
# from hellosign_sdk import apis

api_key = open('/Users/shotomorisaki/Programming/paperlessHackathon/Files/api.txt', 'r').read()
client = HSClient(api_key=api_key)

signature_request_list = client.get_signature_request_list()
for signature_request in signature_request_list:
        print(signature_request)


client.get_signature_request_file(
    signature_request_id='SIGNATURE_REQUEST_ID',
    filename='/Medical-Doctors-Note-for-Work-Sample-Word-Download copy.jpg'
)
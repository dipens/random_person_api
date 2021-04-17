import make_request_call
import constant
import json


def random_person_api(datatype, out_file=None):
    data = make_request_call.make_request_call(constant.URL)
    if datatype == 'create':
        print(data)
    elif datatype == 'json':
        with open(out_file+'.json', 'w') as outfile:
            json.dump(data, outfile)
    else:
        print("ERR: Please provide a valid creation type.")
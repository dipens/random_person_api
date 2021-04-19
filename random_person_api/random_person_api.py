import make_request_call
import constant
import json
import sys

def random_person_api():
    data = make_request_call.make_request_call(constant.URL)
    if (len(sys.argv) > 2) and sys.argv[1] == 'json':
        with open(sys.argv[2]+'.json', 'w') as outfile:
            json.dump(data, outfile)
    elif sys.argv[1] == 'create':
        print(json.dumps(data, indent=4, sort_keys=True))
    else:
        print("ERR: Please specify the correct arguments")

random_person_api()
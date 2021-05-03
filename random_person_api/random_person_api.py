import make_request_call
from Person import Person
from PrintOption import PrintOption
import sys

def random_person_api():
    #data = make_request_call.make_request_call(constant.URL)
    random_person = Person()
    print_option = PrintOption(sys.argv)
    print_option.doPrint(random_person)
    # if (len(sys.argv) > 2) and sys.argv[1] == 'json':
    #     with open(sys.argv[2]+'.json', 'w') as outfile:
    #         json.dump(data, outfile)
    # elif sys.argv[1] == 'create':
    #     jsonData = data
    #     print(json.dumps(data, indent=4, sort_keys=True))
    # else:
    #     print("ERR: Please specify the correct arguments")

random_person_api()
import jsonschema
import simplejson as json
from jsonschema import validate
import sys

schema = {
    "type" : "object",
    "properties" : {
        "price" : {"type" : "number", "minimum" : 5},
        "name" : {"type" : "string"},
    },
}

print("Testing use of jsonschema for data validation.")
print("Using the following schema:")
print(json.dumps(schema, indent=4))


data={ "name": "Apples", "price": 3}
try:
    validate(data, schema)
except jsonschema.exceptions.ValidationError as ve:
    sys.stderr.write("Record #{}: ERROR\n".format(data))
    sys.stderr.write(str(ve) + "\n")
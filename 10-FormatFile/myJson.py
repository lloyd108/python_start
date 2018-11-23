import json


student = {
    "name": "xiaoming",
    "age": 18,
    "gender": "male"
}

print(type(student))
json_student = json.dumps(student)
print(type(json_student))
print(json_student)

dict_student = json.loads(json_student)
print(type(dict_student))
print(dict_student)
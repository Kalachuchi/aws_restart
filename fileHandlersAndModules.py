import json


def readJsonFile(fileName):
    data = ""
    try:
        with open("/home/ec2-user/aws_restart/insulin.json") as json_file:
            data = json.load(json_file)
    except IOError:
        print("Coud not read file")
    return data


print(readJsonFile("/home/ec2-user/aws_restart/insulin.json"))

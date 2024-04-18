import json


def f2tch():
    # Attempt to load JSON data from the file
    try:
        with open("data.json", "r") as file:
            return (json.load(file))
            # print(data)  # Output loaded JSON data
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
    except FileNotFoundError:
        print("File not found or path incorrect.")
    except Exception as ex:
        print("Error:", ex)


def fetch(name,sem,level):
    data = f2tch()
    if level==1:
        print(data.keys())
    if level==2:
        print(data.get(name).keys())
    if level==3:
        print(data.get(name,{}).get("it",{}).get(sem,{}).keys())
        

fetch("start","sem6",3)
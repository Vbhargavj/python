def fetch():


# Attempt to load JSON data from the file
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        print(data)  # Output loaded JSON data
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
    except FileNotFoundError:
        print("File not found or path incorrect.")
    except Exception as ex:
        print("Error:", ex)

fetch()

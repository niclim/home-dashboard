import json

DB_PATH = "./home_dashboard/routes/to_do_list.json"  # Update this path accordingly
NOTSTARTED = "Not Started"
INPROGRESS = "In Progress"
COMPLETED = "Completed"


def add_to_list(item):
    try:
        data = {}
        data["item"] = item
        data["status"] = NOTSTARTED
        try:
            with open(DB_PATH) as file:
                olddata = json.load(file)
                if "items" not in olddata:
                    olddata["items"] = []

            with open(DB_PATH, "w") as outfile:
                olddata["items"].append(data)
                json.dump(olddata, outfile)
        except Exception as e:
            print(e)
            print("Creating this file now...")
            with open(DB_PATH, "w") as outfile:
                newdata = {}
                newdata["items"] = []
                newdata["items"].append(data)
                json.dump(newdata, outfile)

        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print("Error: ", e)
        return None


def get_all_items():
    try:
        with open(DB_PATH) as file:
            data = json.load(file)
        return {"count": len(data), "items": data}
    except Exception as e:
        print("Error: ", e)
        return None


def get_status(item):
    try:
        with open(DB_PATH) as file:
            data = json.load(file)
        for d in data["items"]:
            if d["item"] == item:
                return d["status"]
    except Exception as e:
        print("Error: ", e)
        return None


def update_status(item, status):
    # Check if the passed status is a valid value
    if status.lower().strip() == "not started":
        status = NOTSTARTED
    elif status.lower().strip() == "in progress":
        status = INPROGRESS
    elif status.lower().strip() == "completed":
        status = COMPLETED
    else:
        print("Invalid Status: " + status)
        return None

    try:
        return_status = None

        with open(DB_PATH) as file:
            data = json.load(file)
        for d in data["items"]:
            if d["item"] == item:
                d["status"] = status
                return_status = {item: status}
                break
        if return_status is not None:
            with open(DB_PATH, "w") as outfile:
                json.dump(data, outfile)
        else:
            print("Error: item '", item, "' does not exist!")
        return return_status

    except Exception as e:
        print("Error: ", e)
        return None


def delete_item(item):
    try:
        return_status = None

        with open(DB_PATH) as file:
            data = json.load(file)
        for d in data["items"]:
            if d["item"] == item:
                data["items"].remove(d)
                return_status = {"deleted item": item}
                break
        if return_status is not None:
            with open(DB_PATH, "w") as outfile:
                json.dump(data, outfile)
        else:
            print("Error: item '", item, "' does not exist!")
        return return_status

    except Exception as e:
        print("Error: ", e)
        return None

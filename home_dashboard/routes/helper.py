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

        with open(DB_PATH, "w") as outfile:
            json.dump(data, outfile)

        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print("Error: ", e)
        return None

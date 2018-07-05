from datetime import datetime, timedelta
import json, io, sys

def inscribe():
    try:
        with open("tome.txt", "r") as tome_file:
            tome = json.load(tome_file)
    except IOError:
        tome = []
    activity = raw_input().decode("cp437").upper()
    if len(activity) == 0: 
        sys.exit()
    activity, data, description = ([item.strip() for item in activity.split(':')]+[None, None])[:3]
    day = datetime.today()
    log = {"activity": activity, "date": day.strftime("%Y-%m-%d"), "day": day.strftime("%A")[0:2].upper()}
    if data: log["data"] = data
    if description: log["description"] = description.lower()
    tome.append(log)

    with io.open("tome.txt", "w", encoding="utf8") as tome_file:
        tome_file.write(json.dumps(tome, ensure_ascii=False))

def study():
    try:
        with io.open("tome.txt", "r", encoding="utf8") as tome_file:
            tome = json.load(tome_file)
    except IOError:
        print("this is the start of your tome.\n")
        print("write entries as <activity>:<data>:<description>, e.g.")
        print("programming:python:writing a small time tracker for volume 1 of the zine\n")
        print("data and|or description can be left out")
        print("enjoy.")
        return
    for log in tome:
        log = {key: val.encode("cp437") for key, val in log.items()}
        print("{activity:24} {day} {date}".format(**log))

study()
while True:
    inscribe()

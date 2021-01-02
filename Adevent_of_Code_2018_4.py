import pprint
from datetime import datetime

guard_data = "guard_details.txt"


def get_file_data(filename) -> list:
    rex = r"\s+(?=\d{2}(?:\d{2})?-\d{1,2}-\d{1,2}\b)"
    with open(filename, "r") as file:
        entries = []
        for line in file:
            entry = []
            # get datetime
            dtime = line.strip()[:18].replace("[", "").replace("]", "")
            dtime = datetime.strptime(dtime, "%Y-%m-%d %H:%M")
            entry.append(dtime)

            # get activity
            activity = line.strip()[18:].strip()

            # check if shift start
            if "#" in activity:
                guard_id = int(activity.split()[1][1:])
                entry.append(guard_id)
            else:
                entry.append(None)
            # check if wake up
            if activity == "wakes up":
                entry.append(("wake", True))
            else:
                entry.append(("wake", False))
            # check if falls asleep
            if activity == "falls asleep":
                entry.append(("sleep", True))
            else:
                entry.append(("sleep", False))

            entries.append(entry)

        entries.sort()
        pprint.pprint(entries)


def main():
    shifts = get_file_data(guard_data)


if __name__ == '__main__':
    main()

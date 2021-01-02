import pprint
from datetime import datetime

# guard_data = "guard_details.txt"
guard_data = "guard_details_test.txt"


class Guard:

    guard_dict = {}

    def __init__(self, ident):
        self.ident = ident
        self.tot_sleep_time = []
        self.sleep_mins = {}
        Guard.guard_dict[ident] = []


def get_file_data(filename) -> list:
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
        return entries


def review_shifts(shift_list: list):

    for i in range(0, len(shift_list)):
        # check for guard change
        if shift_list[i][1] is not None:
            # check if the guard already has an ID, if not create one
            g_id = shift_list[i][1]
            if g_id not in Guard.guard_dict:
                Guard.guard_dict[g_id] = []
        # check for falling asleep
        elif shift_list[i][3][1] is True:
            sleep_t = shift_list[i][0].minute
        elif shift_list[i][2][1] is True:
            wake_t = shift_list[i][0].minute




def main():
    shifts = get_file_data(guard_data)
    review_shifts(shifts)
    print(Guard.guard_dict)

if __name__ == '__main__':
    main()

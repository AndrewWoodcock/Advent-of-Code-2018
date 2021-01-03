import pprint
from datetime import datetime

guard_data = "guard_details.txt"
# guard_data = "guard_details_test.txt"


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


def range_generator() -> list:
    rng_tup_list = []
    for i in range(0, 60):
        rng_tup_list.append([i, 0])
    return rng_tup_list



def review_shifts(shift_list: list):
    g_id = None
    for i in range(0, len(shift_list)):
        # check for guard change

        if shift_list[i][1] is not None:
            # check if the guard already has an ID, if not create one
            g_id = shift_list[i][1]
            print("guard id: {0}".format(g_id))
            if g_id not in Guard.guard_dict:
                Guard.guard_dict[g_id] = range_generator()
        # check for falling asleep
        elif shift_list[i][3][1] is True:
            sleep_t = shift_list[i][0].minute
            print("sleep: {0}".format(sleep_t))
        # check for waking up
        elif shift_list[i][2][1] is True:
            wake_t = shift_list[i][0].minute
            print("wake: {0}".format(wake_t))
            print(g_id)
            for min in Guard.guard_dict[g_id]:
                if (min[0] >= sleep_t) and min[0] < wake_t:
                    min[1] += 1


def guard_summary():
    guard_summary_dict = {}
    # pull out summary vals
    for guard, sleep_mins in Guard.guard_dict.items():
        tot_sleep = len([el[0] for el in sleep_mins if el[1] != 0])
        guard_summary_dict[guard] = [tot_sleep]
        mode_sleep = max([el[1] for el in sleep_mins])
        guard_summary_dict[guard].append(mode_sleep)
    return guard_summary_dict


def part_1_ans(summary: dict):
    max_guard = [None, 0]
    for guard, stats in summary.items():
        if stats[0] > max_guard[1]:
            max_guard[0] = guard
            max_guard[1] = stats[0]

    for element in Guard.guard_dict[max_guard[0]]:
        if element[1] == summary[max_guard[0]][1]:
            return max_guard[0] * element[0]


def main():
    shifts = get_file_data(guard_data)
    review_shifts(shifts)
    print(Guard.guard_dict)
    # guard_summary()
    print(part_1_ans(guard_summary()))


if __name__ == '__main__':
    main()

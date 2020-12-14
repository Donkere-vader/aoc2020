from datetime import datetime as dt
import multiprocessing as mp

PROCESSES = 16

start_time = dt.now()
puzzle_input = open('puzzle_input.txt').readlines()

earliest_time = int(puzzle_input[0])
busses = [int(bus) if bus != "x" else bus for bus in puzzle_input[1].split(",")]

print(busses)


class Planner:
    def __init__(self, busses):
        self.busses = busses
        self.minimum_start_time = 100000000000000
        self.highest_bus_id = max([bus for bus in self.busses if bus != "x"])
        self.highest_bus_id_idx = self.busses.index(self.highest_bus_id)

    def check_range(self, rnge: tuple, q: mp.Queue):
        x = rnge[0] - (rnge[0] % self.highest_bus_id)

        for t in range(x, rnge[1], self.highest_bus_id):
            t -= self.highest_bus_id_idx + 1
            start_t = t + 1
            found = True
            for bus in self.busses:
                t += 1
                if bus == "x":
                    continue
                elif t % bus != 0:
                    found = False
                    break
            if found:
                q.put({"found": True, "t": start_t})
                return

        q.put({"found": False})

    def search(self):
        process_range_size = 1000000000
        i = self.minimum_start_time
        while True:
            procs = []
            q = mp.Queue()

            for _ in range(PROCESSES):
                procs.append(mp.Process(target=self.check_range, args=((i, i+process_range_size), q)))
                i += process_range_size

            for p in procs:
                p.start()

            for p in procs:
                p.join()

            print(f"Done processing {i - (process_range_size * PROCESSES)}..{i}")

            for _ in range(len(procs)):
                result = q.get()
                if result['found']:
                    return result['t']


planner = Planner(busses)
t = planner.search()
print(t)
print("time elapsed", dt.now() - start_time)

# from datetime import datetime as dt

# start_time = dt.now()
# puzzle_input = open('puzzle_input.txt').readlines()

# earliest_time = int(puzzle_input[0])
# busses = [int(bus) if bus != "x" else bus for bus in puzzle_input[1].split(",")]

# print(busses)

# # 100001476210000
# # 100017745720000
# # 100741696600000
# minimum_time_stamp = 756261495000000
# highest_bus_id = max([b for b in busses if b != "x"])
# print(highest_bus_id)
# highest_bus_id_idx = busses.index(highest_bus_id)

# time_stamp = minimum_time_stamp - (minimum_time_stamp % highest_bus_id)
# found = False
# while not found:
#     time_stamp += highest_bus_id

#     found = True
#     for idx, bus in enumerate(busses):
#         if bus != "x" and (time_stamp - highest_bus_id_idx + idx) % bus != 0:
#             found = False
#             break

#     if time_stamp % 100000 == 0:
#         print("time_stamp =", time_stamp)

# print(time_stamp)
# print("Time elapsed:", dt.now() - start_time)

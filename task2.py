print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")

def seconds_conversion(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60

    return"%02d minutes, %02d seconds" % (minutes, remaining_seconds)

runner_numbers = []
runner_times = []

while True:
    number_and_time = input("> ")
    runner_info = number_and_time.split("::")

    if number_and_time == "END" and len(runner_numbers) == 0 and len(runner_times) == 0:
        print("No data found. Nothing to do. What a pity.")
        exit()
    if number_and_time == "END" and len(runner_times) != 0 and len(runner_times) != 0:
        break
    elif number_and_time[0] == "" or number_and_time[1] == "":
        print("Error in data stream.")
        continue
    else:
        runner_numbers.append(int(runner_info[0]))
        runner_times.append(int(runner_info[1]))

total_runners = len(runner_numbers)
average_time = (sum(runner_times)) / (len(runner_times))
fastest_time = max(runner_times)
slowest_time = min(runner_times)
best_time = runner_numbers[runner_times.index(min(runner_times))]

print("Total Runners:", total_runners)
print("Average Time:", seconds_conversion(average_time))
print("Fastest Time:", seconds_conversion(fastest_time))
print("Slowest Time:", seconds_conversion(slowest_time))
print()
print("Best time here: Runner #", best_time)

# Problems:
# 1. Can't do ::22
# 2. Plural

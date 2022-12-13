print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")

runner_numbers = []
runner_times = []
number_and_time = ""

while True:
    number_and_time = input("> ")

    runner_info = number_and_time.split("::")

    if number_and_time == "END":
        runner_numbers.append(int(runner_info[0]))
        runner_times.append(int(runner_info[1]))
        runner_info.pop()

        total_runners = len(runner_numbers)
        average_time = (sum(runner_times))/(len(runner_times))
        fastest_time = max(runner_times)
        slowest_time = min(runner_times)

        print(total_runners)
        print(average_time)
        print(fastest_time)
        print(slowest_time)

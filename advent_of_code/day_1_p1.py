def password(nums):
    score, current = 0, 50
    for i in nums:
        direction = i[0]
        number = int(i[1:])

        if direction == "L":
            current = (current - number) % 100
        else:  # direction == "R"
            current = (current + number) % 100

        if current == 0:
            score += 1

    return score


def file_util():
    with open("input.txt", "r") as f:
        my_list = f.read().splitlines()
    return my_list


if __name__ == "__main__":
    nums = file_util()
    print(password(nums))

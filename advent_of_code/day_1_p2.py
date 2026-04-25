def password_part2(nums):
    score, current = 0, 50
    for i in nums:
        direction = i[0]
        number = int(i[1:])

        if direction == "L":
            # Count how many times we pass through 0 going left
            # We pass through 0 if we cross it during rotation
            new_current = (current - number) % 100

            # How many complete wraps? number // 100
            # Plus check if we cross 0 in the partial wrap
            score += number // 100
            if new_current > current:  # We wrapped around
                score += 1

            current = new_current

        else:  # direction == "R"
            # Count how many times we pass through 0 going right
            new_current = (current + number) % 100

            # How many complete wraps? number // 100
            # Plus check if we cross 0 in the partial wrap
            score += number // 100
            if new_current < current:  # We wrapped around
                score += 1

            current = new_current

    return score


def file_util():
    with open("input.txt", "r") as f:
        my_list = f.read().splitlines()
    return my_list


if __name__ == "__main__":
    nums = file_util()
    print(password_part2(nums))

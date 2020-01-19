# a) When we pass an integer argument to your program, it should do one of
# followings
#   i) Returns ‘’my” when the number is dividable by 3
#   ii) Returns “theresa” when the number is dividable by 5
#   iii) Returns “mytheresa” when the number is dividable by 3 and 5
# iv) Returns the given number when the previous rules are not met.
# b) Hints:
#   i) Make sure the implementation is extendable
#   ii) For example:
#     (1) Return “clothes” when the number is dividable by 7
#     (2) Return “myclothes” when the number is dividable by 3 and 7 and so on


def problem(input_number):
    values = dict({
        3: "my",
        5: "theresa",
        7: "clothes"
        # you can add here many more of the pairs
    })

    output = ""
    for num in values:
        if input_number % num == 0:
            output = output + values[num]
    if output == "":
        return input_number

    return output


if __name__ == "__main__":
    print(problem(100))  # Check here

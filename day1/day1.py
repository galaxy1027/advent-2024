

def main():
    left_list = []
    right_list = []

    input_file = open("input.txt", "r")

    vals = input_file.readlines()
    pair = []

    # Get left and right list filled out and sorted
    for s in vals:
        pair = s.split("   ")
        left_list.append(int(pair[0].strip()))
        right_list.append(int(pair[1].strip()))

    left_list.sort()
    right_list.sort()


    # Find differences

    differences = []
    i = 0
    while i < len(left_list):
        differences.append(abs(left_list[i] - right_list[i]))
        i += 1

    # sum differences
    result = 0

    for d in differences:
        result += d

    print(result)

if __name__ == '__main__':
    main()


def main():
    input_file = open("input.txt", "r")

    counts = {}
    left_list = []
    right_list = []

    vals = input_file.readlines()
    pair = []

    # Get left and right list filled out and sorted
    for s in vals:
        pair = s.split("   ")
        left_list.append(int(pair[0].strip()))
        right_list.append(int(pair[1].strip()))

    left_list.sort()
    right_list.sort()



    # get value counts with sorted lists

    l = 0
    r = 0
    while (l < len(left_list) and r < len(right_list)):
        if left_list[l] == right_list[r]:
            print(f'{left_list[l]} = {right_list[r]}')
            if left_list[l] in counts.keys():
                counts[left_list[l]] += 1
            else:
                counts[left_list[l]] = 1
            r += 1
        elif left_list[l] > right_list[r]:
            print(f'{left_list[l]} > {right_list[r]}')
            r += 1
        else:
            print(f'{left_list[l]} = {right_list[r]}')
            l += 1

    # calculate similarity score
    similarity_score = 0
    print(counts)
    for k in counts.keys():
        similarity_score += counts[k] * k

    print(similarity_score)




if __name__ == '__main__':
    main()
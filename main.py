import merge_insert as mi
import comparison as cpr


with open("manual_sorting/unsorted_list.txt","r") as file:
    input_list = file.read().splitlines()


def sort_input():
    sorted_input = mi.MISort(input_list,cpr.compare2)
    with open('manual_sorting/sorted_list.txt', 'w') as outfile:
        outfile.write('\n'.join(str(sorted_input[-i-1]) for i in range(len(sorted_input))))

sort_input()

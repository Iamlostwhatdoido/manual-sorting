import random
import numpy as np
import matplotlib.pyplot as plt

# Text Comparison Function
def _bestof2(a,b):
    return max(a,b)

# Merge-Insert sort
def MISort(array,bestof2,return_comparison = False):
    number_of_comparison = 0

    # Initialisation
    if len(array)<=1:
        return array, number_of_comparison
    
    # Pairing values and comparing pairs
    upper_values = []
    lower_values = []
    for i in range(len(array)//2):
        number_of_comparison +=1
        result = bestof2(array[2*i],array[2*i+1])
        if result == array[2*i]:
            upper_values.append(array[2*i])
            lower_values.append(array[2*i+1])
        else:
            upper_values.append(array[2*i+1])
            lower_values.append(array[2*i])

    # Adding odd one to lower values
    if len(array)%2 : lower_values.append(array[-1])
    
    
    # Sorting pairs according to upper values
    sorted_upper,comparisons = MISort(upper_values,bestof2,True)
    number_of_comparison += comparisons

    # Creating according sorted_lower
    sorted_lower = []
    for e in sorted_upper:
        sorted_lower.append(lower_values[upper_values.index(e)])
    if len(lower_values)>len(sorted_lower):
        sorted_lower.append(lower_values[-1])


    # Obvious first case
    sorted_upper.insert(0,sorted_lower.pop(0))
    
    
    # Reorganising sorted_lower into optimal sort list
    insertion_list = []
    i = 2
    size = 2
    while len(sorted_lower)>0:
        storage = []
        for k in range(min(size,len(sorted_lower))):
            storage.insert(0,sorted_lower.pop(0))
        
        insertion_list = insertion_list + storage

        size = pow(2,i) - size
        i+=1


    # Sorting our lower values 1 by 1
    i = 0
    while len(insertion_list)>0:
        
        value_to_insert = insertion_list.pop(0)

        special_case = (lower_values.index(value_to_insert) <= len(upper_values))
        min_index = 0

        if special_case:
            max_index = len(sorted_upper)-1
        else:
            max_index = sorted_upper.index(upper_values[lower_values.index(value_to_insert)])


        while min_index < max_index :

            med_index = min_index + (max_index-min_index)//2

            number_of_comparison +=1
            result = bestof2(value_to_insert,sorted_upper[med_index])

            if result == value_to_insert:
                min_index = med_index + 1
            else:
                if special_case: special_case = False
                max_index = med_index


        if special_case :
            number_of_comparison +=1
            result = bestof2(value_to_insert,sorted_upper[-1])
            if result == value_to_insert:
                sorted_upper.append(value_to_insert)
            else:
                sorted_upper.insert(min_index,value_to_insert)
        else:
            sorted_upper.insert(min_index,value_to_insert)
        i+=1
    
    if return_comparison:
        return sorted_upper, number_of_comparison
    else:
        return sorted_upper

def _test():
    sort_number = [0, 1, 3, 5, 7, 10, 13, 16, 19, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111, 116, 121, 126, 131, 136, 141, 146, 151, 156, 161, 166, 171, 177, 183, 189, 195, 201, 207, 213, 219, 225, 231, 237, 243, 249, 255 ]

    size_testing = 56
    batch_tests = 5000

    size_x = [k for k in range(size_testing)]
    comparaison_max = []
    comparaison_moyenne = []
    comparaison_min = []
    inefficacités = []

    for array_size in size_x:
        inefficacité = 0
        nombres_comparaison = []

        for iter in range(batch_tests):

            reference = [ e for e in range(array_size)]
            test_array = reference.copy()
            random.shuffle(test_array)

            out,comparaison = MISort(test_array,_bestof2)

            nombres_comparaison.append(comparaison)

            if out != reference:
                print("\nERREUR DE SORT")
                print("  in : ",test_array)
                print("  out: ",out)
            if comparaison > sort_number[array_size]:
                inefficacité+=1
        
        comparaison_max.append(max(nombres_comparaison))
        comparaison_moyenne.append(np.mean(nombres_comparaison))
        comparaison_min.append(min(nombres_comparaison))
        inefficacités.append(inefficacité)

    fig, ax1 = plt.subplots() 

    ax1.plot(size_x,comparaison_max,'b--',linewidth = 1)
    ax1.plot(size_x,comparaison_moyenne,'b',linewidth = 2)
    ax1.plot(size_x,comparaison_min,'b--',linewidth = 1)
    ax1.plot(size_x,sort_number,'k',linewidth = 2)

    ax2 = ax1.twinx()
    ax2.plot(size_x,inefficacités)

    plt.show()
            

# _test()


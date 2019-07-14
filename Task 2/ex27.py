def concatenate_list_data(lists):
    output = ''
    for lis in lists:
        output += str(lis)
    return output
print(concatenate_list_data([1, 5, 12, 2]))
print(concatenate_list_data(['a', 'b']))
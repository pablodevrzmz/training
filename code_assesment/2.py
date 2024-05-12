from typing import List

def find_element_parent_group(key, group_dict):
    for group in group_dict:
        if key in group_dict[group]:
            return group
    return None



def countRelatedGroups(related: List[str])->int:

    group_dict = dict()

    isolated_groups = 0
    
    for row_index in range(len(related)):

        columns = len(related[row_index])

        used_in_groups = False

        for column_index in range(columns):

            if row_index != column_index:

                element = related[row_index][column_index]

                if element == '1':

                    key =  (row_index, column_index)

                    parent_group = find_element_parent_group(key, group_dict)

                    if parent_group is None:

                        added_to_group = False

                        for c in range(0,column_index):
                            
                            if row_index != c and related[row_index][c] == '1':
                                
                                parent_group = find_element_parent_group((row_index, c), group_dict)
                                
                                if parent_group is not None:
                                    
                                    group_dict[parent_group].add(key)
                                    group_dict[parent_group].add((column_index, row_index))
                                    added_to_group = True
                                    used_in_groups = True
                                    break

                        if not added_to_group:
                            used_in_groups = True
                            group_dict[key] = set()
                            group_dict[key].add(key)
                            group_dict[key].add((column_index, row_index))
                    else:
                        used_in_groups = True

        if not used_in_groups:
            isolated_groups += 1

    return len(group_dict) + isolated_groups

# Test cases
related_1 = [
    "1100",
    "1110",
    "0110",
    "0001"
]

expected_group_count = 2

print(countRelatedGroups(related_1) == expected_group_count)

related_2 = [
    "10000",
    "01000",
    "00100",
    "00010",
    "00001"
]

expected_group_count = 5

print(countRelatedGroups(related_2) == expected_group_count)
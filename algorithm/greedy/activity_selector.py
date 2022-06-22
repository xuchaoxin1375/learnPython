
# def activity_selector(start,finish,solved_i,scale_n):
#     next_i=solved_i+1
#     while next_i<=scale_n and start[next_i]<finish[solved_i]:
#         next_i+=1
#     if next_i<=scale_n:
#         sub_result=activity_selector(start,finish,next_i,scale_n)
#         # if sub_result is not none(empty)
#         if not sub_result:
#             return [next_i]
#         else:
#             return [next_i]+sub_result
#     else:
#         return None
import re


def activity_selector(start, finish, solved_i, scale_n):
    """[summary]

    Args:
        start ([list]): [ the soved_i is the activity which is selected to the optimal solution set(use the index of the activity to represent)]
        finish ([list]): [the start,finish are both array-like of (sperately start time and finish time)]
        solved_i ([int]): [the scale_n is the problem scale to solve original input]
        scale_n ([int]): [there,except the solved_i is variable parameter in the recursive invoke,others are keep their values]

    Returns:
        [type]: [description]
    """
    # the next_i exactly mean that the next activity which will finished firstly in the unsovled activity set,
    # meanwhile ,the next_i activity could not confflict with the solved(selected) one.
    next_i = solved_i+1
    # find the frist activity to finish in the set haven't been calculated
    while next_i <= scale_n and start[next_i] < finish[solved_i]:
        # find the first compatible activity:
        next_i += 1
    if next_i <= scale_n:
        # the next_i there is one of the optimal solution's element;and recursively invoke the function(only change the next_i)
        sub_result = activity_selector(start, finish, next_i, scale_n)
        return [next_i]+sub_result
    else:
        return []


def greedy_activity_selector(start, finish):
    """ the iteration version: """
    n = len(start)
    result_list = [1]
    selected_i = 1
    for next_i in range(2, n):
        if start[next_i] >= finish[selected_i]:
            # result_list = result_list+[finish[selected_i]]
            #iterate the result_list and the selected_i
            result_list = result_list+[next_i]
            selected_i = next_i
            
    return result_list


if __name__ == "__main__":
    # s=[1,3,0,5,3,5,6,8,8,2,12]
    activity_tuples_list = [(0, 0), (1, 4), (3, 5), (0, 6), (5, 7),
                            (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    # activity_tuples_list.sort(key=lambda tuple:tuple[1])
    print(activity_tuples_list)
    s = [activity[0] for activity in activity_tuples_list]
    f = [activity[1] for activity in activity_tuples_list]
    print("solved by recursive:")
    result = activity_selector(s, f, 0, 11)
    print(result)
    print("solved by iteration:")
    result = greedy_activity_selector(s, f)
    print(result)

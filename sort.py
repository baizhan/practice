def mean(sorted_list):
    if not sorted_list:
        return(([],[]))
    big=sorted_list[-1]
    small=sorted_list[-2]
    big_list,small_list=mean(sorted_list[:-2])
    big_list.append(small)
    small_list.append(big)
    big_list_sum=sum(big_list)
    small_list_sum=sum(small_list)
    if big_list_sum>small_list_sum:
        return((big_list,small_list))
    else:
        return((small_list,big_list))
    

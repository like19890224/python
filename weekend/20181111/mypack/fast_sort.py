from random import randint
alist = [randint(0,100) for i in range(1,11)]
def quick_sort(num_list):
    if len(num_list)<=1:
        return num_list
    middle = num_list[0]
    lager = []
    smaller = []
    for i in num_list[1:]:
        if i > middle:
            lager.append(i)
        else:
            smaller.append(i)
    return quick_sort(smaller) + [middle] + quick_sort(lager)
if __name__ == '__main__':
    alist = [randint(0,100) for i in range(1,11)]
    print(alist)
    print(quick_sort(alist))

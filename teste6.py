from math import prod
#[5,1,4,2]
#[8,40,10,20]
def function(list):
    output_list=[]
    base_list=list[:]
    for element in list:
        base_list.remove(element)
        output_list.append(prod(base_list))
        base_list = list[:]
    return output_list
lista=[5,1,4,2]
print(function(lista))

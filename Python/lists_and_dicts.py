def run():
    my_list = [1, "Hello", True, 5.5]
    my_dict = {"firstname": "Miguel", "lastname": "Contreras"}

    super_list = [
        {"firstname": "Pedro", "lastname": "Pascal"},
        {"firstname": "Mads", "lastname": "Mikelsen"},
        {"firstname": "Roberto", "lastname": "Rodriguez"},
        {"firstname": "Mario", "lastname": "Sosa"},
        {"firstname": "Carlos", "lastname": "Jimenez"}
    ]

    super_dict={
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,2.2,3.3]
    }
    #Para imprimir valores de super_list
    for item in super_list:
        print(item["firstname"] , "-" , item["lastname"])

    #Para valores de super_dic
#    for key, value in super_dict.items():
#       print(key,"-",value)


if __name__ == '__main__':
    run()


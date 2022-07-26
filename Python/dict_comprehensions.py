def run():
    #my_dict={}

    #for i in range(1,101):
    #    if i %3 !=0:
    #        my_dict[i]=i**3
    #
    my_dict={i:i**3 for i in range(1,101) if 1%3 !=0}
    print(my_dict)
    #example es un dict comp cuyas llaves son las 1000 primeros números naturales con sus raíces cuadradas
    example={y:y**0.5 for y in range(1,1000)}
    print(example)
if __name__=='__main__':
    run()
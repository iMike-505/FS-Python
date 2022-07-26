#Generación de listas con ciclos
def run():
    #squares = []
    #for i in range(1,101):
    #    if i % 3 != 0:
    #       squares.append(i**2)
    
    squares = [i**2 for i in range(1,101)if i % 3!=0]
    print(squares)

    reto = [y for y in range(1,100000)if y%4==0 and y%6==0 and y%9==0]
    print(reto)

if __name__=='__main__':
    run()
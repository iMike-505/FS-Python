def divisors(num):
    try:
        if num < 0:
            raise ValueError("Ingresa un número positivo: ")
        divisors = [i for i in range(1, num+1) if num%i==0]
        return divisors
    except ValueError as Err:
        print(Err)
        return False

def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Fin del programa.")
    except ValueError:
        print("Debes de ingresar un número: ")

if __name__=='__main__':
    run()
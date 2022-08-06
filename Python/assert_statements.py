def divisors(num):
        divisors = [i for i in range(1, num+1) if num%i==0]
        return divisors
   
def run():
        num = int(input("Ingresa un número: "))
        assert num.isnumeric() and int(num)>0, "Desbes de ingresar un número"
        print(divisors (int(num)))
        print("Terminó mi porgrama")

if __name__=='__main__':
    run()
# Задание 2
# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    x1 = int(line[0])
 
    summ = 0
    if x1 >=1:
        a = 1
        b = x1 + 1
 
    else:
        a = x1
        b = 2
 
    for i in range(a,b):
        summ = summ + i
 
        print(summ)
 
    print(summ)
 
 
    output_file.write(str(summ) + "\n")
 
    input_file.close()
    output_file.close()
 
 
if __name__ == "__main__":
    main()
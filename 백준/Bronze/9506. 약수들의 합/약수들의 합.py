while True:
    number = int(input())
    
    if number == -1:
        break

    div_list = []
    for i in range(1, number):
        if number % i == 0:
            div_list.append(i)
    div_sum = sum(div_list)

    if div_sum == number:
        result = " + ".join(map(str, div_list))
        print(f"{number} = {result}")
    else:
        print(f"{number} is NOT perfect.")

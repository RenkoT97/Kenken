from random import shuffle

n = 10
A = [[None for _ in range(n)] for _ in range(n)]
for i in range(n):

    main_random_list = [i for i in range(1, n+1)]
    shuffle(main_random_list)

    for k0 in range(i-1):
        main_random_list.remove(A[k0][i])

    for i0 in range(i, n):
        preveri = [A[i0][k] for k in range(i-1)]
        for k in main_random_list:
            if k not in preveri:
                A[i0][i] = k
                main_random_list.remove(k)
                break

    print(A)
    main_random_list = [i for i in range(1, n+1)]
    shuffle(main_random_list)

    for k1 in range(i):
        main_random_list.remove(A[i][k1])

    for i1 in range(i+1, n):
        preveri = [A[k][i1] for k in range(1, i-1)]

        for k in main_random_list:
            if k not in preveri:
                A[i][i1] = k
                main_random_list.remove(k)
                break
            
            
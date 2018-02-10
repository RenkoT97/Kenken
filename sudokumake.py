from random import shuffle

def makeSudoku(n):
    A = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):

        main_random_list = [i for i in range(1, n+1)]
        shuffle(main_random_list)

        for k0 in range(i):
            ustrezn = A[k0][i]
            if ustrezn in main_random_list:
                main_random_list.remove(A[k0][i])
            else:
                return 0

        for i0 in range(i, n):
            preveri = [A[i0][k] for k in range(i)]
            for k in main_random_list:
                if k not in preveri:
                    A[i0][i] = k
                    main_random_list.remove(k)
                    break
        
        main_random_list = [i for i in range(1, n+1)]
        shuffle(main_random_list)

        for k1 in range(i+1):
            ustrezn = A[i][k1]
            if ustrezn in main_random_list:
                main_random_list.remove(ustrezn)
            else:
                return 0

        for i1 in range(i+1, n):
            preveri = [A[k][i1] for k in range(1, i)]

            for k in main_random_list:
                if k not in preveri:
                    A[i][i1] = k
                    main_random_list.remove(k)
                    break

    return '\n'.join([str(vrstica) for vrstica in A])
                

def returnValid(n):
    while True:
        a = makeSudoku(n)
        if a != 0:
            print(a)
            return a

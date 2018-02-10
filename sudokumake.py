from random import shuffle

def makeSudoku(n):

    # prazna zacetna matrika
    A = [[None for _ in range(n)] for _ in range(n)]
    
    for i in range(n):

        # list bo uporabljen za stolpec matrike
        main_random_list = [i for i in range(1, n+1)]
        shuffle(main_random_list)

        # pogledamo kateri elementi so ze v stolpcu pred
        # nasimi novimi in jih odstranimo iz lista
        for k0 in range(i):
            ustrezn = A[k0][i]
            if ustrezn in main_random_list:
                main_random_list.remove(A[k0][i])

            # ce elementa ni v listu smo nekaj zajebali in odnehamo
            else:
                return 0

        # nafilamo vsak element stolpca posebej
        for i0 in range(i, n):

            # z zanko preverimo elemente levo od nas
            # saj morajo biti vsi drugacni,
            # desno od nas pa se ne obstajajo
            preveri = [A[i0][k] for k in range(i)]
            for k in main_random_list:
                # izberemo tistega, ki ga se ni v tej vrstici
                if k not in preveri:
                    A[i0][i] = k
                    main_random_list.remove(k)
                    break

        # enako naredimo za vrstice
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

    print('\n'.join([str(vrstica) for vrstica in A]))
    return A
                

def returnValid(n):
    while True:
        a = makeSudoku(n)
        if a != 0:
            return a

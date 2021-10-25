
''' Problema 2== subsecventa toate numerele sunt prime'''

def estePrim(a: int):
    '''
    Determina daca un numar este Prim
    :param a: int
    :return: true daca e prim false in caz contrar
    '''
    if a < 2 :
        return False
    else:
        x=2
        while x!=a:
            if a % x == 0:
                return False
            x+=1
    return True


def get_longest_all_primes(lst: list[int]) :
    i = 0
    nr = len(lst)-1
    st = 0
    dr = 0
    while i < nr:
        count = 1
        if estePrim(lst[i])==True and estePrim(lst[i + 1])==True:
            while i < nr and estePrim(lst[i])==True and estePrim(lst[i + 1])==True :
                i += 1
                count+=1
            if dr - st + 1 < count:
                st = i - count+1
                dr = i
        else:
            i += 1
    if st==dr and dr==0 and estePrim(lst[0])==False :
        i=0
        while i<=nr:
            if(estePrim(lst[i])):
                return lst[i]
            i+=1
    return lst[st:dr+1]


def test_get_longest_all_primes():
    '''
    Testeaza corectitudinea functiei get_longest_all_primes()
    :return:
    '''
    assert get_longest_all_primes([1,2,3,4,5]) ==[2,3]
    assert get_longest_all_primes([1,1,1,1]) ==[1]
    assert get_longest_all_primes([2,3,7,9,0]) ==[2,3,7]
    assert get_longest_all_primes([1,3,5,8]) ==[3,5]



''' problema 12== subsecventa toate numerele au acelasi numar de divizori'''

def nrDivizori(a: int):
    '''
    Determina numarul divizorilor
    :param a: int
    :return: numar divizori
    '''
    x=1
    s=0
    while x<=a:
        if a % x == 0:
            s+=1
        x+=1
    return s

def get_longest_same_div_count(lst: list[int]):
    i=0
    nr=len(lst)-1
    st=0
    dr=0
    while i < nr:
        count=1
        if nrDivizori(lst[i]) == nrDivizori(lst[i+1]):
            while i < nr and nrDivizori(lst[i]) == nrDivizori(lst[i+1]) :
                i+=1
                count+=1
            if dr-st+1 < count :
                st=i-count+1
                dr=i
        else:
            i+=1
    return lst[st:dr+1]


def test_get_longest_same_div_count():
    assert get_longest_same_div_count([1,2,3,4,5]) ==[2,3]
    assert get_longest_same_div_count([2,4,6,8,10]) ==[6,8,10]
    assert get_longest_same_div_count([3,5,7]) ==[3,5,7]
    assert get_longest_same_div_count([1]) ==[1]


def citire_Date():
    citit=input("Introduceti un sir de numere separate printr-o virgula: ")
    int_list=list(map(int,citit.split(',')))
    return int_list


def Consola():
    while True:
        print('1. Citire date.')
        print('2. Determinare cea mai lungă subsecvență cu proprietatea prime.')
        print('3. Determinare cea mai lungă subsecvență cu proprietatea numar divizori egal.')
        print('4. Ieșire.')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            listanr: list
            ok=1
            listanr=citire_Date()
            listaPrime = get_longest_all_primes(listanr[:])
            if (estePrim(listaPrime[0])) == False:
                ok=0
            listaNrDivizori = get_longest_same_div_count(listanr[:])
        elif optiune == '2':
            if ok==0:
                print("Nu exista numere prime in lista data.")
            else:
                print(listaPrime)
        elif optiune == '3':
            print(listaNrDivizori)
        elif optiune == '4':
            break
        else:
            print('Optiune invalida!')

Consola()

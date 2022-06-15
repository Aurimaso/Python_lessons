def skaiciu_suma(sk1, sk2, sk3):
    return sk1 + sk2 + sk3


def saraso_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius
    return suma

def didziausias_skaicius(*args):
    return max(args)

def stringas_atbulai(stringas):
    return stringas[::-1]

def info_apie_sakini(stringas):
    print(f"Šiame sakinyje yra {len(stringas.split())} žodžių")
    didziosios = 0
    mazosios = 0
    skaiciai = 0
    for simbolis in stringas:
        if simbolis.isupper():
            didziosios += 1
        if simbolis.islower():
            mazosios += 1
        if simbolis.isnumeric():
            skaiciai += 1
    return {"didziosios": didziosios, "mazolio": mazosios, "skaiciai": skaiciai}

# def unikalus_sarasas(sarasas):
#     naujas_sarasas = []
#     for skaicius in sarasas:
#         if skaicius not in naujas_sarasas:
#             naujas_sarasas.append(skaicius)
#     return naujas_sarasas


# def test_prime(n):
#     if (n == 1):
#         return False
#     elif (n == 2):
#         return True;
#     else:
#         for x in range(2, n):
#             if (n % x == 0):
#                 return False
#         return True

# def isrikiuoti_nuo_galo(sakinys):
#     zodziai = sakinys.split()[::-1]
#     return " # ".join(zodziai)


# print(isrikiuoti_nuo_galo("Vienas du trys keturi"))
import hashlib,math

def generer_constantes():
    k = []
    for i in range(64):
        k.append(math.floor(2**32 * abs(math.sin(i + 1))))
    return k

def hachage(message):
    # Pré-traitement du message
    message = bytearray(message, 'utf-8')
    longueur_originale = (8 * len(message)) % (2**64)
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)
    message += longueur_originale.to_bytes(8, byteorder='big')

    # Initialisation des variables d'état
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # Traitement par blocs de 512 bits
    for i in range(0, len(message), 64):
        block = message[i:i+64]

        # Préparation des mots de message
        w = [0] * 64
        for j in range(16):
            w[j] = int.from_bytes(block[j*4:j*4+4], byteorder='big')
        for j in range(16, 64):
            s0 = (w[j-15] >> 7 | w[j-15] << 25) ^ (w[j-15] >> 18 | w[j-15] << 14) ^ (w[j-15] >> 3)
            s1 = (w[j-2] >> 17 | w[j-2] << 15) ^ (w[j-2] >> 19 | w[j-2] << 13) ^ (w[j-2] >> 10)
            w[j] = (w[j-16] + s0 + w[j-7] + s1) % (2**32)

        # Initialisation des variables de travail
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7

        # Boucle principale
        for j in range(64):
            S1 = (e >> 6 | e << 26) ^ (e >> 11 | e << 21) ^ (e >> 25 | e << 7)
            ch = (e & f) ^ (~e & g)
            temp1 = (h + S1 + ch + k[j] + w[j]) % (2**32)
            S0 = (a >> 2 | a << 30) ^ (a >> 13 | a << 19) ^ (a >> 22 | a << 10)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) % (2**32)

            h = g
            g = f
            f = e
            e = (d + temp1) % (2**32)
            d = c
            c = b
            b = a
            a = (temp1 + temp2) % (2**32)

        # Mise à jour des variables d'état
        h0 = (h0 + a) % (2**32)
        h1 = (h1 + b) % (2**32)
        h2 = (h2 + c) % (2**32)
        h3 = (h3 + d) % (2**32)
        h4 = (h4 + e) % (2**32)
        h5 = (h5 + f) % (2**32)
        h6 = (h6 + g) % (2**32)
        h7 = (h7 + h) % (2**32)

    # Concaténation des variables d'état pour obtenir la valeur de hachage finale
    hash_value = (
        h0.to_bytes(4, byteorder='big') +
        h1.to_bytes(4, byteorder='big') +
        h2.to_bytes(4, byteorder='big') +
        h3.to_bytes(4, byteorder='big') +
        h4.to_bytes(4, byteorder='big') +
        h5.to_bytes(4, byteorder='big') +
        h6.to_bytes(4, byteorder='big') +
        h7.to_bytes(4, byteorder='big')
    )

    return hash_value.hex()

# Constantes spécifiques à l'algorithme SHA-256
k = generer_constantes()

# Test de la fonction avec une chaîne arbitraire
input_data = "Buenos, Mundo!"
hashed_value = hachage(input_data)
print(hashed_value)





# Maintenant, tu peux utiliser cette fonction pour obtenir la liste complète des constantes k


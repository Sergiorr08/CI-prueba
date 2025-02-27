def es_primo(n):
    if n < 2 or (n % 2 == 0 and n > 2):
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))
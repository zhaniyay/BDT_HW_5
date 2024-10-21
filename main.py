import random 

def is_prime(x: int) -> bool:
    if x<2:
        return False
    for i in range(2, x):
        if x%i==0:
            return False
    return True


def primes(count: int) -> list[int]:
    result_list = []
    res = 2
    while len(result_list) < count:
        if is_prime(res):
            result_list.append(res)
        res += 1
    return result_list

def checksum(x: list[int]) -> int:
    res = 0
    for i in x:
        res = (res+i)*113%10000007
    return res

def pipeline() -> int:
    prime_list = primes(1000)
    random.seed(100)
    random.shuffle(prime_list)
    return checksum(prime_list) 

if __name__ == "__main__":
    result = pipeline()
    print(f"Cумма: {result}")
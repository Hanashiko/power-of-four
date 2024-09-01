def isPowerOfFour(n: int) -> bool:
    for i in range(32):
        if 4**i == n:
            return True
    return False

def main() -> None:
    print(isPowerOfFour(16))
    print(isPowerOfFour(5))
    print(isPowerOfFour(1))
    
if __name__ == "__main__":
    main()
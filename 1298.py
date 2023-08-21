def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def find_integer_solution(A, B, C):
    if A == 0 and B == 0:
        if C == 0:
            return (0, 0)
        else:
            return "Not Exist"

    if A == 0:
        if C % B == 0:
            return (0, C // B)
        else:
            return "Not Exist"

    if B == 0:
        if C % A == 0:
            return (C // A, 0)
        else:
            return "Not Exist"

    if C % gcd(A, B) != 0:
        return "Not Exist"

    x0, y0, _ = extended_gcd(A, B)
    x = x0 * (C // gcd(A, B))
    y = y0 * (C // gcd(A, B))
    return (x, y)

def extended_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    x, y, d = extended_gcd(b, a % b)
    return (y, x - (a // b) * y, d)

# 입력 받기
A, B, C = map(int, input().split())

# 정수해 찾기
solution = find_integer_solution(A, B, C)

# 결과 출력
if solution == "Not Exist":
    print("Not Exist")
else:
    print(solution[0], solution[1])


# 반사 판별, bool 리턴
def is_reflexive(matrix):
    for i in range(5):
        if matrix[i][i] != 1:
            return False
    return True

# 대칭 판별, bool 리턴
def is_symmetric(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# 추이 판별, bool 리턴
def is_transitive(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                for k in range(5):
                    if matrix[j][k] == 1 and matrix[i][k] != 1:
                        return False
    return True

# 집합의 각 원소에 대한 동치류를 각각 출력
def print_Equivalence_class(matrix):
    class_check = [1, 2, 3, 4, 5]
    print("\n각 원소와 관계된 모든 원소의 집합은")
    for i in range(5):
        element_check = []
        print("[",i + 1 ,"] :", end=' ')
        for j in range(5):
            if matrix[i][j] == 1:
                element_check.append(j+1)
                print("(", i + 1, ", ", j + 1, "),", end=' ')
        print("\b\b = { ", end='')
        for j in range(len(element_check)):
            print(element_check[j], ",", end=' ')
        print("\b\b}")
    print("입니다.")
    print("\n따라서 동치류는 ")
    for i in range(5):
        for j in range(i + 1, 5):
            if matrix[i] == matrix[j]:
                class_check[j] = class_check[i]

    for i in range(5):
        if class_check[i] == 0:
            continue
        print("[", i+1, "] =", end=' ')
        for j in range(i+1, 5):
            if class_check[j] == 0:
                continue
            if class_check[j] == class_check[i]:
                print("[", j+1, "] =", end=' ')
                class_check[j] = 0
        print("{ ", end='')
        for j in range(5):
            if matrix[i][j] == 1:
                print(j+1, ", ", end='')
        print("\b\b}")
    print("입니다.")
            
# 각각의 관계에 대한 폐포 변환 전, 변환 후 출력
def print_matrix(matrix):
    for i in range(5):
        print("[", end='')
        for j in range(5):
            print(matrix[i][j], ",", end=' ')
        print("\b\b]")
    print("\n")

# 반사 폐포
def reflexive_closure(matrix):
    print("원래의 관계 행렬:")
    print_matrix(matrix)

    for i in range(5):
        if matrix[i][i] == 1:
            continue
        matrix[i][i] = 1

    print("반사 폐포 변환 후:")
    print_matrix(matrix)
    return matrix

# 대칭 폐포
def symmetric_closure(matrix):
    print("원래의 관계 행렬:")
    print_matrix(matrix)

    for i in range(5):
        for j in range(i, 5):
            if matrix[i][j] == matrix[j][i]:
                continue
            if matrix[i][j] == 1:
                matrix[j][i] = 1

    print("대칭 폐포 변환 후:")
    print_matrix(matrix)
    return matrix

# 추이 폐포
def transitive_closure(matrix):
    print("원래의 관계 행렬:")
    print_matrix(matrix)

    for i in range(5):
        matrix[i][i] = 1

    for k in range(5):
        for i in range(5):
            if matrix[i][k] == 1:
                for j in range(5):
                    if matrix[k][j] == 1:
                        matrix[i][j] = 1

    print("추이 폐포 변환 후:")
    print_matrix(matrix)
    return matrix

# 각각의 폐포로 변환한 후 동치 관계를 다시 판별하고 동치류 출력하기
def closure(matrix, c1, c2, c3):
    modify_matrix = matrix
    if c1 == False: # 반사폐포 필요
        modify_matrix = reflexive_closure(modify_matrix)
    if c2 == False: # 관계폐포 필요
        modify_matrix = symmetric_closure(modify_matrix)
    if c3 == False: # 추이폐포 필요
        modify_matrix = transitive_closure(modify_matrix)

    return modify_matrix

def find_3_length(matrix):
    cnt = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                for k in range(5):
                    if matrix[j][k] == 1:
                        for l in range(5):
                            if matrix[k][l] == 1:
                                print("(%d->%d->%d->%d) => (%d..%d)" % (i+1, j+1, k+1, l+1, i+1, l+1))
                                cnt += 1

    if cnt == 0:
        print("주어진 관계행렬에 대해 길이가 3인 경로가 없다.")                           

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    n = len(A)
    matrix = []
    print("5x5인 관계행렬을 입력하시오.:")
    
    for i in range(n):
        print(i + 1, " 행:", end=' ')
        row = list(map(int, input().split()))
        matrix.append(row)

    c1 = is_reflexive(matrix)
    c2 = is_symmetric(matrix)
    c3 = is_transitive(matrix)

    if c1 and c2 and c3:
        print("\n이 관계는 동치 관계입니다.")
        print_Equivalence_class(matrix)
    else:
        print("\n이 관계는", end=' ')
        if c1 == False:
            print("반사,", end=' ')
        if c2 == False:
            print("대칭,", end=" ")
        if c3 == False:
            print("추이,", end=' ')
        print("\b\b 관계가 아닙니다.")

        matrix = closure(matrix, c1, c2, c3)
        print_Equivalence_class(matrix)

    print("\n완성된 행렬에서 길이가 3인 경로들의 리스트는 다음과 같다.:")
    find_3_length(matrix)

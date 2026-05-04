import numpy as np

def menu():
    print("\n=== NUMPY MATH MENU ===")
    print("1. Create Array")
    print("2. Statistics (mean, median, std)")
    print("3. Matrix Operations")
    print("4. Dot Product")
    print("5. Reshape Array")
    print("6. Exit")

while True:
    menu()
    choice = int(input("Enter choice: "))

    if choice == 1:
        arr = np.array(list(map(int, input("Enter elements: ").split())))
        print("Array:", arr)

    elif choice == 2:
        arr = np.array(list(map(int, input("Enter elements: ").split())))
        print("Mean:", np.mean(arr))
        print("Median:", np.median(arr))
        print("Standard Deviation:", np.std(arr))

    elif choice == 3:
        print("Enter 2x2 matrix A:")
        A = np.array([list(map(int, input().split())) for _ in range(2)])
        print("Enter 2x2 matrix B:")
        B = np.array([list(map(int, input().split())) for _ in range(2)])

        print("Addition:\n", A + B)
        print("Multiplication:\n", np.dot(A, B))
        print("Transpose of A:\n", A.T)

    elif choice == 4:
        a = np.array(list(map(int, input("Enter array 1: ").split())))
        b = np.array(list(map(int, input("Enter array 2: ").split())))
        print("Dot Product:", np.dot(a, b))

    elif choice == 5:
        arr = np.array(list(map(int, input("Enter elements: ").split())))
        r, c = map(int, input("Enter rows and cols: ").split())
        print("Reshaped Array:\n", arr.reshape(r, c))

    elif choice == 6:
        print("Exit...")
        break

    else:
        print("Invalid choice!")
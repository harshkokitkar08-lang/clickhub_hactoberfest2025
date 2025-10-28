N = input().strip()  # Read as string to easily reverse

if N == N[::-1]:
    print("Yes")
else:
    print("No")

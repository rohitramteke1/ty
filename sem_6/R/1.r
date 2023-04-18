x <- as.integer(readline("x : "))
y <- as.integer(readline("y : "))

print("Before Swap")

print(paste("A : ", x))
print(paste("B : ", y))

print("After swap")

x <- x + y
y <- x - y
x <- x - y  


print(paste("A : ", x))
print(paste("B : ", y))
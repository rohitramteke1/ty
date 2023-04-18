fact <- 1

factorial <- function(n) {
    if (n > 0) {
        fact <- n * factorial(n - 1)
    } else {
        return(fact)
    }
}

n <- as.integer(readline("N : "))
print(paste("Factorial of ", n, " : ", factorial(n)))
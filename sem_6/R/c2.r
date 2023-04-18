data <- c(1:3, NA, 5, 1, 9, 7:8, 11, NA)
data[is.na(data)] <- mean(data, na.rm = TRUE)
print(data)

#mode <- function(){
#    return(sort(-table(data))[1])
#}

#for median simply replace mean with "median" keyword
#for mode call the mode function
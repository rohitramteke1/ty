data <- c(1:3, 5, 1551, 9, 11, 1005, 15, 17)
paste("No. of elements : ", length(data))
 
print("Outliers : ")
boxplot(data, plot = FALSE)$out
 
outliers <- boxplot(data, plot = FALSE)$out
data_no_outlier <- data[-which(data %in% outliers)]

paste("Outlier Recheck : ")
boxplot(data_no_outlier, plot = FALSE)$out
 
paste("Final length : ", length(data_no_outlier))
# Read in the dataset
data <- read.csv("sem_6/R/reliance.csv")

# Filter data based on certain date
filtered_data <- data[data$Date >= "2021-04-01", ]

#new_data <- table(filtered_data$Close)

pie(filtered_data$Close, label = filtered_data$Date,
    main = "Reliance Stock Closing after 2021-04-01")

plot(as.Date(data$Date), data$Close,
    main = "Stock daily Closing", xlab = "Date", ylab = "Price", )

plot(as.Date(filtered_data$Date), filtered_data$Close, type = "l",
    main = "Stock daily Closing", xlab = "Date", ylab = "Price")

hist(filtered_data$Close, xlab = "Price",
    main = "Reliace Stock Price Closings")
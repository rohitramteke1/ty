data <- read.csv("sem_6/R/nifty.csv")
openmax <- max(data$Open)
openmin <- min(data$Open)
print(openmax)
print(openmin)

openmax_data <- subset(data, Open == openmax)
openmin_data <- subset(data, Open == openmin)

print(openmax_data)
print(openmin_data)


library(dplyr)
max_value <- subset(data %>%
  filter(Symbol == "ADANIPORTS") %>%
  summarise(max_value = max(Close)))

min_value <- subset(data %>%
  filter(Symbol == "ADANIPORTS") %>%
  summarise(min_value = min(Close)))

print(max_value)
print(min_value)
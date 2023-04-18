dataset <- read.csv("sem_6/R/reliance.csv")

linear_model <- lm(High ~ Low^2, data = dataset)

#plot(linear_model)
#abline(linear_model)

predict(linear_model, newdata = data.frame(Low = c(3000, 3500, 290)))
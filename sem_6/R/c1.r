library(dplyr)

data <- read.csv("sem_6/R/iris.csv")
print("\nRAW DATA")
print(data)

plot(data$id, data$sepal_length, type = "l",
    main = "Iris Dataset", xlab = "ID", ylab = "Sepal Length")

new_data <- select(data, petal_length, petal_width, species)

new_data <- arrange(new_data, petal_length)

new_data <- filter(new_data, species == "versicolor")
print("\nDATA AFTER SELECT() , ARRANGE() AND FILTER()")
print(new_data)

new_data <- mutate(new_data,
    petal_length_to_width_ratio = petal_length / petal_width)
print("\nDATA AFTER MUTATION")
print(new_data)
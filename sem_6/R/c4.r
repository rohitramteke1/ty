df <- read.csv("sem_6/R/reliance.csv")
library(Boruta)
library(dplyr)

#processing data
columns_with_missing_data <- colnames(df)[colSums(is.na(df)) > 0]
# Remove columns with missing data
df <- df[, !colnames(df) %in% columns_with_missing_data]

# Extract features and target variable
X <- df[, -ncol(df)]  # Features (all columns except the last one)
Y <- df$High   # Target variable (last column)

# Initialize Boruta
boruta <- Boruta(X, Y, doTrace = 2)

# Fit Boruta to the data
boruta.fit <- attStats(boruta)
plot(boruta)

# Extract important features
important_features <- colnames(X)[boruta.fit$selected]

# Subset original feature set to include only important features
X_selected <- X[, important_features]

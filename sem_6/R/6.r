#uttarakhand 2012
rain1 <-
    c(38.80, 11.90, 28.10, 39.20, 9.10, 46.00, 387.10, 419.50, 220.60, 4.70, 3.40, 15.50)

#kerala 2012
rain2 <-
     c(7.40,11.00,21.00,171.10,95.30,430.30,362.60,501.60,241.10,187.50,112.90,9.40)

# Convert them to a matrix.
combined.rain <- matrix(c(rain1, rain2), nrow = 12)

# Convert it to a time series object.
rain.timeseries <- ts(combined.rain, start = c(2012, 1), frequency = 12)
# Print the timeseries data.
print(rain.timeseries)
# Give the chart file a name.
png(file = "rain_combined.png")
# Plot a graph of the time series.
plot(rain.timeseries)

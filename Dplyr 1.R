# Admin ----
library(dplyr)
library(nycflights13)
dim(flights)
flights

# Select ----
select(flights, everything())

select(flights, year)
select(flights, year:day)          # Select all columns between year and day (inclusive)
select(flights, year, month, day)  # Select columns by name
select(flights, year, month, arr_time:arr_delay)

select(flights, -(year:day))      # Select all columns except those from year to day (inclusive)
select(flights, tail_num = tailnum) 


# Filter ----
flights[flights$month == 1 & flights$day == 1, ] #base r code
filter(flights, month == 1)
filter(flights, month == 1 & day == 1)

# Arrange ----
arrange(flights, year)
arrange(flights, year, month, day)
arrange(flights, desc(arr_delay))

# Mutate and transmute----
mutate(flights, gain = arr_delay - dep_delay, speed = distance / air_time * 60)
mutate(flights, gain = arr_delay - dep_delay, gain_per_hour = gain / (air_time / 60))
transmute(flights, gain = arr_delay - dep_delay, gain_per_hour = gain / (air_time / 60)) # If you only want to keep the new variables, use transmute():


# Summarise ----
summarise(flights, delay = mean(dep_delay, na.rm = TRUE))
sample_n(flights, 10)

sample_frac(flights, 0.01)  # 1% of the overall dataset is 3368
0.01*length(flights$year)


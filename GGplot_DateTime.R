
# Data ----
head(economics)

# Basic line plot ----
ggplot(data=economics, aes(x=date, y=pop))+ geom_line()
ggplot(data=subset(economics, date > as.Date("2006-1-1")),  
       aes(x=date, y=pop))+geom_line()

ggplot(data=economics, aes(x=date, y=pop, size=unemploy/pop))+ geom_line()  # Change line size

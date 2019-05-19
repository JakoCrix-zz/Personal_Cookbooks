# Admin ----
library(fpp2)
uschange=uschange

# Forecasting Principles and Practice 
# Example 1 ----
# Estimation 
uschange=uschange
str(uschange)
head(uschange)
autoplot(uschange[,1:2], facets=TRUE) + 
  xlab("Year") + ylab("") + ggtitle("Quarterly changes in US consumption and personal income")


fit <- auto.arima(uschange[,"Consumption"], xreg=uschange[,"Income"])
summary(fit)

cbind("Regression Errors" = residuals(fit, type="regression"),"ARIMA errors" = residuals(fit, type="innovation")) %>% 
  autoplot(facets=TRUE)

checkresiduals(fit)

# Forcasting 
fcast <- forecast(fit, xreg=rep(mean(uschange[,2]),8))
autoplot(fcast) + xlab("Year") + ylab("Percentage change")

# Example 2 ----
elecdaily=elecdaily
str(elecdaily)
head(elecdaily)

xreg <- cbind(MaxTemp = elecdaily[, "Temperature"],
             MaxTempSq = elecdaily[, "Temperature"]^2,
             Workday = elecdaily[, "WorkDay"])

fit2 <- auto.arima(elecdaily[, "Demand"], xreg = xreg)
checkresiduals(fit2)

fcast2 <- forecast(fit2, xreg = 
                    cbind(rep(26,14), rep(26^2,14), c(0,1,0,0,1,1,1,1,1,0,0,1,1,1))
                  )

autoplot(fcast2) + ylab("Electricity demand (GW)")

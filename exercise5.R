aggregate(mpg ~ cyl, data = mtcars, FUN = mean)
plot(hp ~ mpg, data = mtcars, main = "mpg vs hp", xlab = "mpg", ylab = "hp")

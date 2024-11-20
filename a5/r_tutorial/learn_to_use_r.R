# Sets working dir
# setwd("C:/Users/sirsh/repos/lis4369/a5")

# Shows installed packages
# installed.packages()

# Updates packages
# update.packages()

# Displays help information
# help()

# displays pre-configured datasets
# data()

# reads data from csv file, can mess with header
# & what the value of "comma" is
# mydata <- read.csv("filename.txt")

# read data from published url (google spreadsheet)
# mydata <- read.csv("webaddress")

# Creates a barchart with data from AAPL, can specify range
# getsymbols is used to fetch historical stock prices
#getSymbols("AAPL")
#barChart(AAPL)
#barChart(AAPL["2013-04-01::2013-04-12"])

# remove data
# rm()

# saves entire R workspace
# save.image()
# save individual R objects
# save(variablename, file="filename.file")

# load files
# load("filename.file")

# head(data)
# displays first 6 rows with headers
# can specify ex. head(mtcars, 10)

# tail(data)
# works the same way, just from the bottom

# str(data)
# num rows, cols, type of object
# rownames(data) shows all values of first col

# when installing a new package
# library(command) needs to be run on every new R session

# cor(data)
# shows correlations in data, can use NA to specify 
# ex of how to use NA: mean(mtcars$mpg, na.rm = TRUE)

# names(data)
# shows all column names

# to access a column from a dataset by name
# dataset$colname

# subset data by columns
# this would subset cols 2-4: dataset[,2:4]
# R indexes from 1, and case sensitive everywhere
# negative indexing excludes, doesn't work backwards

# mtcars[mtcars$mpg>20,]
# get all rows where mpg>20, then return all cols
# can specify column locations
# mtcars[mtcars$mpg>20,c("mpg","cyl")]

# subsets can be used instead of brackets
# subset(mtcars, , c("mpg","hp"))
# similar to select * in SQL, selecting certain cols
# can find min, max using subsets

# plot() can be used to plot scatter plots
# can label axes, plot(mtcars$disp, mtcars$mpg, xlab="Engine displacement",
# ylab="mpg", main="is this title?")

# qplot() quick plot scatter. labels auto
# can determine beginning value and end, R auto determines usually
# qplot(disp, mpg, ylim=c(0,35), data=mtcars)

# barplot() used to graph barplots

mtcars 

install.packages('quantmod')
library('quantmod')
getSymbols("AAPL")
barChart(AAPL)
barChart(AAPL["2013-04-01::2013-04-12"])


head(mtcars)

tail(mtcars, 10)

str(mtcars)

cor(mtcars)

mean(mtcars$mpg, na.rm = TRUE)

# no clue
choose(15,4)

names(mtcars)

mtcars[,2:4]

# doesn't show all results, just value placement & T/F
mtcars$mpg>20

mtcars[mtcars$mpg>20,]

mtcars[mtcars$mpg>20,c("mpg","hp","cyl")]

attach(mtcars)
mpg20 <- mtcars$mpg > 20
detach()

subset(mtcars, mpg>20, c("mpg","cyl"))

subset(mtcars, , c("mpg","hp"))

# prompted error, in PDF
filter(mtcars, mpg>20)

# also error, maybe missing import? None specified
# Appears to be no immediate difference than using [] or subset
select(mtcars, mpg, hp)

table(trees$cut)

plot(mtcars$disp, mtcars$mpg)

plot(mtcars$disp, mtcars$mpg, xlab="Engine displacement",
     ylab="mpg", main="is this title?")

?par

install.packages("ggplot2")
library(ggplot2)
qplot(disp, mpg, data=mtcars)
qplot(disp, mpg, ylim=c(0,35), data=mtcars)

ggplot(cty, hwy, data=mpg, geom="jitter")
ggplot(pressure, aes(x=temperature, y=pressure)) + geom_line()
ggplot(pressure, aes(x=temperature, y=pressure)) + geom_line() + geom_point()

barplot(BOD$demand)
barplot(BOD$demand, main="Graph of demand"
        , names.arg = BOD$Time)

# sends cylcount under values
cylcount <- table(mtcars$cyl)

barplot(cylcount)
qplot(mtcars$cyl)

ggplot(mtcars, aes(factor(cyl))) + geom_bar()

boxplot(mtcars$mpg)

mycolors <- heat.colors(3)
mrecolors <- rainbow(6)
ggplot(mtcars, aes(x=factor(cyl))) + geom_bar(fill=mycolors)

barplot(BOD$demand, col=mrecolors)

save.image()

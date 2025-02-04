rm(list = ls(envir = globalenv()), envir = globalenv());
if(!is.null(dev.list())) dev.off(); gc(); cat("\014")

setwd("C:/Users/sirsh/repos/lis4369/p2")

url = "http://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv"
mtcars <- read.csv(file=url,head=TRUE,sep=",")

mtcars

# First 10 records
head(mtcars, 10)

# Last 10 records
tail(mtcars, 10)

# Internal structure
str(mtcars)

# Column names
names(mtcars)

# First record
head(mtcars, 1)

# MPG data (w/o col name)
mtcars$mpg

# CYL data (w/o col name)
mtcars$cyl

# Row 3 Col 4
mtcars[3,4]

# Data for cars w > 4 cyl
mtcars[mtcars$cyl>4,]

# Data for cars w > 4 cyl & =4 gears
mtcars[mtcars$cyl>4 & mtcars$gear==4,]

# Data for cars w >4 cyl or =4 gears
mtcars[mtcars$cyl>4 | mtcars$gear==4,]

# Data for cars w>4 cyl and !=4 gears
mtcars[mtcars$cyl>4 & !mtcars$gear==4,]

# num cols
ncol(mtcars)

# num rows
nrow(mtcars)

# dimensions
dim(mtcars)

# mean, medium, min, max, quarts, variance, std for HP
summary(mtcars$hp, na.rm=TRUE)
var(mtcars$hp, na.rm=TRUE)
sd(mtcars$hp, na.rm=TRUE)

library(ggplot2)
# quick plot
qplot(hp, mpg, ylim=c(0,35), data=mtcars) +
  ggtitle("Keith Faunce")

<<<<<<< HEAD
# install.packages("dplyr")
=======
install.packages("dplyr")
>>>>>>> af921d99ec74f4aed103dea752ff3ceb5b1a26be
library(dplyr)

# normal plot (ggplot)
avg_mpg <- mtcars %>%
  group_by(cyl) %>%
  summarize(avg_mpg = mean(mpg))

mycolors <- rev(heat.colors(3))

ggplot(avg_mpg, aes(x = factor(cyl), y = avg_mpg)) +
  geom_col(fill = mycolors) +
  ggtitle("Avg MPG per Cyl | Keith Faunce") +
  xlab("Number of cylinders") +
  ylab("Avg MPG")

sink("p2_txt.txt")
# I did the sink at the end, didn't actually copy. Will do first in the future
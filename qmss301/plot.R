library(dplyr)

df <- read.csv('alien.csv')

df_color <- df %>% mutate(color = ifelse(type=="Human", 'blue', 'red'))

plot(df_color$height, df_color$age, pch=16, col=df_color$color)

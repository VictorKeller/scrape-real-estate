library(dplyr)
library(ggplot2)
library(stringr)

setwd("C:/Users/VNFSK/Downloads")

df <- read.csv(file.choose(), stringsAsFactors = F)

str(df)


df <- unique(df)




# fix characters


for (i in c("mini_desc", "desc", "nome", "bairro")) {
  
  
  df[[i]] <- gsub("<c1>", "a", df[[i]])
  df[[i]] <- gsub("<ed>", "i", df[[i]])
  df[[i]] <- gsub("<E9>", "e", df[[i]])
  df[[i]] <- gsub("<f3>", "o", df[[i]])
  df[[i]] <- gsub("<ba>", "o", df[[i]])
  df[[i]] <- gsub("<d3>", "o", df[[i]])
  df[[i]] <- gsub("<e0>", "a", df[[i]])
  df[[i]] <- gsub("<e7>", "ç", df[[i]])
  df[[i]] <- gsub("<e3>", "a", df[[i]])
  df[[i]] <- gsub("<b2>", "2", df[[i]])
  df[[i]] <- gsub("<f5>", "o", df[[i]])
  df[[i]] <- gsub("<e1>", "a", df[[i]])
  df[[i]] <- gsub("<fa>", "u", df[[i]])
  df[[i]] <- gsub("<e2>", "a", df[[i]])
  df[[i]] <- gsub("<f4>", "o", df[[i]])
  df[[i]] <- gsub("<e9>", "é", df[[i]])
  df[[i]] <- gsub("<E9>", "e", df[[i]])
  df[[i]] <- gsub("<ea>", "e", df[[i]])
  df[[i]] <- gsub("<c0>", "a", df[[i]])
  df[[i]] <- gsub("<da>", "u", df[[i]])
  df[[i]] <- gsub("<c2>", "a", df[[i]])
  df[[i]] <- gsub("<c2>", "a", df[[i]])
  df[[i]] <- gsub("<c9>", "É", df[[i]])
  df[[i]] <- gsub("<b0>", "o", df[[i]])
  df[[i]] <- gsub("<d4>", "o", df[[i]])
  df[[i]] <- gsub("<b9>", "1", df[[i]])
  df[[i]] <- gsub("\xfa", "u", df[[i]])
  df[[i]] <- gsub("\xc1", "a", df[[i]])
  df[[i]] <- gsub("\xe3", "a", df[[i]])
  df[[i]] <- gsub("\xf4", "o", df[[i]])
  df[[i]] <- gsub("\xed", "i", df[[i]])
  df[[i]] <- gsub("\xe1", "a", df[[i]])
  df[[i]] <- gsub("\xe2", "a", df[[i]])
  df[[i]] <- gsub("\xe7", "a", df[[i]])
  df[[i]] <- gsub("\xb7", ".", df[[i]])
  df[[i]] <- gsub("\x96", "-", df[[i]])
  
  
}




# bairro

df$bairro <- gsub(", Brasilia", "", df$bairro)

df$bairro <- str_to_title(df$bairro)

df$bairro <- gsub(" Ii", " II", df$bairro)
df$bairro <- gsub(" De ", " de ", df$bairro)
df$bairro <- gsub(" Dos ", " dos ", df$bairro)
df$bairro <- gsub(" Da ", " da ", df$bairro)
df$bairro <- gsub(", Distrito Federal", ", DF", df$bairro)
df$bairro <- gsub(", Distrito Federal", "", df$bairro)


sort(unique(df$bairro))


df$bairrao <- df$bairro
df$bairrao <- ifelse(grepl("Aguas Claras", df$bairro), "Aguas Claras", df$bairrao)
df$bairrao <- ifelse(grepl("Guara", df$bairro), "Guara", df$bairrao)
df$bairrao <- ifelse(grepl("Sobradinho", df$bairro), "Sobradinho", df$bairrao)
df$bairrao <- ifelse(grepl("Taguatinga", df$bairro), "Taguatinga", df$bairrao)
df$bairrao <- ifelse(grepl("Samambaia", df$bairro), "Samambaia", df$bairrao)
df$bairrao <- ifelse(grepl("Nucleo Bandeirante", df$bairro), "Nucleo Bandeirante", df$bairrao)
df$bairrao <- ifelse(grepl("Ceilandia", df$bairro), "Ceilandia", df$bairrao)
df$bairrao <- ifelse(grepl("Riacho Fundo", df$bairro), "Riacho Fundo", df$bairrao)
df$bairrao <- ifelse(grepl("Gama", df$bairro), "Gama", df$bairrao)



ggplot(df, aes(x = reorder(bairrao, bairrao, function(x) -length(x)))) +
  geom_bar() + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1),
        axis.title.x = element_blank())




# algl

df$algl <- gsub("R\\$", "", df$algl)
df$algl <- gsub("\\.", "", df$algl)

df$algl <- as.numeric(df$algl)

df$algl <- ifelse(df$algl > 1700, NA, df$algl)


ggplot(df, aes(x = algl)) + 
  geom_histogram(bins = 15) +
  scale_x_continuous(breaks = seq(0, 1700, 200)) +
  xlab("Aluguel ($)")



# condo

df$condo <- gsub("R\\$", "", df$condo)
df$condo <- gsub("\\.", "", df$condo)
df$condo <- gsub(" Condominio", "", df$condo)

df$condo <- as.numeric(df$condo)


df$condo <- ifelse(is.na(df$condo), 0, df$condo)


ggplot(df, aes(x = condo)) + 
  geom_histogram(bins = 30) +
  scale_x_continuous(breaks = seq(0, 2000, 400)) +
  xlab("Condominio ($)")




# m2tot


df$m2tot <- gsub("m<b2>", "", df$m2tot)
df$m2tot <- gsub("\\.", "", df$m2tot)

df$m2tot <- as.numeric(df$m2tot)

df$m2tot <- ifelse(df$m2tot > 60, NA, df$m2tot)


ggplot(df, aes(x = m2tot)) + 
  geom_histogram(bins = 10) +
  scale_x_continuous(breaks = seq(0, 60, 5)) +
  xlab("m2 Total")




# m2util


df$m2util <- gsub("m<b2>", "", df$m2util)
df$m2util <- gsub("\\.", "", df$m2util)

df$m2util <- as.numeric(df$m2util)


df$m2util <- ifelse(df$m2tot < df$m2util, df$m2tot, df$m2util)


ggplot(df, aes(x = m2util)) + 
  geom_histogram(bins = 15) +
  scale_x_continuous(breaks = seq(0, 60, 5)) +
  xlab("m2 Util")




# vagas


# df$vagas <- ifelse(grepl("vaga", df$banhs), df$banhs, df$vagas)




# banhs


df$banhs <- ifelse(grepl("banheiro", df$qts), df$qts, df$banhs)




# qts


df$qts <- ifelse(grepl("quarto", df$qts), df$qts, NA)






# iptu

df$iptu_minidesc <- ifelse(grepl("iptu", tolower(df$mini_desc)), T, F)



df$iptu_desc <- NA
for (i in 1:nrow(df)) {
  
  if (grepl("iptu", tolower(df$desc[i]))) {
    
    desc <- gsub("iptu", " iptu ", tolower(df$desc[[i]]))
    desc_split <- tolower(strsplit(desc, " ")[[1]])
    index_iptu <- match("iptu", desc_split)
    words <- c(desc_split[(index_iptu - 4):index_iptu], desc_split[(index_iptu + 1):(index_iptu + 4)])
    df$iptu_desc[i] <- paste(words, collapse = " ")
    
  } else {
    df$iptu_desc[i] <- ""
  }
  
  
}





# condo_desc


df$condo_desc <- NA
for (i in 1:nrow(df)) {
  
  if (grepl("condominio", tolower(df$desc[i]))) {
    
    desc <- gsub("condominio", " condominio ", tolower(df$desc[[i]]))
    desc_split <- tolower(strsplit(desc, " ")[[1]])
    index_condo <- match("condominio", desc_split)
    index_pre <- ifelse((index_condo - 4) < 0, 0, (index_condo - 4))
    index_post <- ifelse((index_condo + 4) > length(desc_split), length(desc_split), (index_condo + 4))
    words <- c(desc_split[index_pre:index_condo], desc_split[(index_condo + 1):index_post])
    df$condo_desc[i] <- paste(words, collapse = " ")
    
  } else {
    df$condo_desc[i] <- ""
  }
  
  
}




# algl + condo

df$algl_cond <- df$algl + df$condo




# algl_cond por m2

df$algl_cond_m2 <- df$algl_cond / df$m2util




# bairros


bairros <- df %>% 
  group_by(bairrao) %>% 
  summarise(n = n(), 
            algl = round(mean(algl, na.rm = T)),
            condo = round(mean(condo, na.rm = T)),
            m2util = round(mean(m2util, na.rm = T), 1),
            algl_cond = round(mean(algl_cond, na.rm = T)), 
            algl_cond_m2 = round(mean(algl_cond_m2, na.rm = T), 1)) %>% 
  arrange(desc(n))




# aguas claras

ac <- df[df$bairrao == "Aguas Claras", ]

hist(ac$algl_cond)



# asa norte

an <- df[df$bairrao == "Asa Norte", ]

hist(an$algl_cond)



# guara

gu <- df[df$bairrao == "Guara", ]

hist(gu$algl_cond)




# diferenca do preco/m2 da media do bairro

for (i in 1:nrow(df)) {
  df$dif_custo_bairro[i] <- df$algl_cond_m2[i] - bairros$algl_cond_m2[bairros$bairrao == df$bairrao[i]]
}





# aps de interesse

df$interesse <- ifelse(df$algl_cond < 1700 & df$algl_cond > 800 & df$dif_custo_bairro < 0 & df$m2util > 35 & df$bairrao %in% c("Aguas Claras", "Asa Norte", "Guara", "Asa Sul", "Lago Norte", "Sudoeste", "Octogonal", "Nucleo Bandeirante"), "sim", NA)


int <- df[which(df$interesse == "sim"), ]






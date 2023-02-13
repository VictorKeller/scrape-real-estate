library(dplyr)
library(ggplot2)
library(stringr)

setwd("C:/Users/VNFSK/Downloads")

df <- read.csv(file.choose(), stringsAsFactors = F)

str(df)


df <- unique(df)


df <- select(df, -m2tot, -ap_id, -res_desc)



# fix characters


for (i in names(df)) {
  
  
  df[[i]] <- gsub("<c1>", "a", df[[i]])
  df[[i]] <- gsub("<aa>", "a", df[[i]])
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
  df[[i]] <- gsub("<c7>", "Ç", df[[i]])
  df[[i]] <- gsub("<c3>", "A", df[[i]])
  df[[i]] <- gsub("<c2>", "a", df[[i]])
  df[[i]] <- gsub("<cd>", "I", df[[i]])
  df[[i]] <- gsub("<ca>", "E", df[[i]])
  df[[i]] <- gsub("<c9>", "É", df[[i]])
  df[[i]] <- gsub("<b0>", "o", df[[i]])
  df[[i]] <- gsub("<d4>", "o", df[[i]])
  df[[i]] <- gsub("<d5>", "O", df[[i]])
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




# nome + bairro


df$nome <- NA
df$bairro <- NA

for (i in 1:nrow(df)) {
  
  df$nome[i] <- strsplit(df$nome_bairro[i], ", ")[[1]][1]
  df$bairro[i] <- str_to_title(strsplit(df$nome_bairro[i], ", ")[[1]][2])
  
}


df$bairro <- ifelse(df$bairro == "Sul", "Aguas Claras Sul",
                    ifelse(df$bairro == "Norte", "Aguas Claras Norte",
                           ifelse(df$bairro == "Velho", "Cruzeiro Velho",
                                  df$bairro)))



# algl


df$algl <- ifelse(as.numeric(df$algl) < 10, as.numeric(df$algl) * 1000, as.numeric(df$algl))





# m2util


df$m2util <- as.numeric(gsub(" m2", "", df$m2util))





# qts

table(df$qts)




# vagas

table(df$vagas)

df$vagas <- ifelse(grepl("Vaga", df$suite), df$suite, df$vagas)




# suite

table(df$suite)

df$suite <- ifelse(grepl("Suite", df$suite), df$suite, "")




# condo

df$condo <- ifelse(grepl("quarto", df$condo), NA, df$condo)

df$condo <- ifelse(as.numeric(df$condo) < 10, as.numeric(df$condo) * 1000, as.numeric(df$condo))

df$condo <- ifelse(is.na(df$condo), 0, df$condo)




# iptu


df$iptu_det <- NA
for (i in 1:nrow(df)) {
  
  if (grepl("iptu", tolower(df$detalhes[i]))) {
    
    detalhes <- gsub("iptu", " iptu ", tolower(df$detalhes[[i]]))
    detalhes_split <- tolower(strsplit(detalhes, " ")[[1]])
    index_iptu <- match("iptu", detalhes_split)
    words <- detalhes_split[(index_iptu):(index_iptu + 5)]
    df$iptu_det[i] <- paste(words, collapse = " ")
    
  } else {
    df$iptu_det[i] <- ""
  }
  
  
}



df$iptu <- NA
for (i in 1:nrow(df)) {
  
  df$iptu[i] <- strsplit(df$iptu_det[i], " ")[[1]][4]
  df$iptu[i] <- strsplit(df$iptu[i], "\n")[[1]][1]
  
}


df$iptu <- as.numeric(gsub("\\.", "", df$iptu))


hist(df$iptu, breaks = 30)






# algl + condo

df$algl_cond <- df$algl + df$condo




# algl_cond por m2

df$algl_cond_m2 <- round(df$algl_cond / df$m2util, 1)





# bairros


bairros <- df %>% 
  group_by(bairro) %>% 
  summarise(n = n(), 
            algl = round(mean(algl, na.rm = T)),
            condo = round(mean(condo, na.rm = T)),
            iptu = round(mean(iptu, na.rm = T)),
            m2util = round(mean(m2util, na.rm = T), 1),
            algl_cond = round(mean(algl_cond, na.rm = T)), 
            algl_cond_m2 = round(mean(algl_cond_m2, na.rm = T), 1)) %>% 
  arrange(desc(n))




# diferenca do preco/m2 da media do bairro

for (i in 1:nrow(df)) {
  df$dif_custo_bairro[i] <- df$algl_cond_m2[i] - bairros$algl_cond_m2[bairros$bairro == df$bairro[i]]
}





# aps de interesse

df$interesse <- ifelse(df$algl_cond < 1700 & df$algl_cond > 800 & df$bairro %in% c("Aguas Claras Sul", "Aguas Claras Norte", "Asa Norte", "Guara I", "Guara Ii", "Asa Sul", "Lago Norte", "Sudoeste", "Octogonal", "Nucleo Bandeirante"), "sim", NA)


int <- df[which(df$interesse == "sim"), ]





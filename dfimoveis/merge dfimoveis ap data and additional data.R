setwd("C:/Users/VNFSK/Downloads")

dfa <- read.csv(file.choose(), stringsAsFactors = F)

dfb <- read.csv(file.choose(), stringsAsFactors = F)


dfa <- dfa[, !names(dfa) %in% c("condo")]

df <- merge(dfa, dfb)


write.csv(df, "dfimoveis ap data and additional data - 2023-02-12.csv", row.names = F)

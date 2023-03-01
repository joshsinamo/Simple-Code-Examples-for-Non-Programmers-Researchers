library(data.table)
library(crayon)

fisher_binarized <- function(table_input){

  number_of_tests <- nrow(table_input) * choose(ncol(table_input), 2)
  row_names       <- rownames(table_input)

  pairs_of_columns <- rep(NA, number_of_tests)
  target_variable  <- rep(NA, number_of_tests)
  count_head       <- rep(NA, number_of_tests)
  p_value          <- rep(NA, number_of_tests)
  significance     <- rep(NA, number_of_tests)

  iterator <- 1
  for(j in 1:nrow(table_input)){

    all_column_combinations <- as.list(data.table(combn(1:ncol(table_input), 2)))
    for(i in all_column_combinations){
      toAnalyze <- NA

      if(nrow(table_input) > 2){
        target <- table_input[j, ]
        others <- colSums(table_input[setdiff(1:nrow(table_input), j), ])
        toAnalyze <- rbind(target, others)[, i]
      }
      else if(nrow(table_input)==2){
        toAnalyze <- table_input[, i]
      }
      else{
        break
      }

      target_variable[iterator]  <- paste0(row_names[j], " vs. NOT ", row_names[j])
      pairs_of_columns[iterator] <- paste(i, collapse = " AND ")
      count_head[iterator]       <- paste0(toAnalyze[1, ], collapse="-")

      p_val_out                  <- round(min(1.00,
                                               fisher.test(toAnalyze,
                                                           simulate.p.value=T,
                                                           B=100000)$p.value * number_of_tests), 4)
      p_value[iterator]          <- p_val_out
      significance[iterator]     <- ifelse(p_val_out < 0.001, "<0.001",
                                    ifelse(p_val_out < 0.005, "<0.001",
                                    ifelse(p_val_out < 0.01,  "<0.01",
                                    ifelse(p_val_out < 0.05,  "<0.05", ""))))

      iterator <- iterator + 1
    }
  }
  return(data.table(target_variable=target_variable,
                    columns_tested=pairs_of_columns,
                    checker=count_head,
                    p_value=p_value,
                    significance=significance))
}

#Sample Run
mat <- matrix(c(1,2,3,4,5,6,7,8,9), nrow=3, ncol=3,
              dimnames=list(c("Row 1", "Row 2", "Row 3"),
                            c("Col 1", "Col 2", "Col 3")))
mat1 <- as.table(mat)

fisher.test(mat)
fisher_binarized(mat1)



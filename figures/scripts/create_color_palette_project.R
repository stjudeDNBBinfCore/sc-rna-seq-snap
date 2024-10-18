# Create color palettes for `sc-rna-seq-snap` repo
# Antonia Chroni <antonia.chroni@stjude.org> for DNB Bioinformatics Core Analysis Team
#
# Usage:
# Anywhere a plot is being made, source these TSV file and use the color palette for
# each appropriate data type.
#
# Magrittr pipe
`%>%` <- dplyr::`%>%`

# Establish base dir
root_dir = file.path("./GitHub/sc-rna-seq-snap")

# Output to palette directory
output_dir <-
  file.path(root_dir, "figures", "palettes")
if (!dir.exists(output_dir)) {
  dir.create(output_dir)
}


### A color scale for `upstream-analysis` module
qc_col_palette <- c("#10559A", 
                    "#D41159")

qc_col_names <- c("vln_plot_color",
                  "min_color")

# Format as data.frame
df <- data.frame(color_names = qc_col_names,
                 hex_codes = qc_col_palette) %>%
  readr::write_tsv(file.path(output_dir, "qc_color_palette.tsv"))

########################################################################################################################
# Define colors for samples
# samplecolors <- c((brewer.pal(9, rev("YlGnBu")))[4:9],(brewer.pal(9, rev("PuBuGn")))[6:9], 
#                  (brewer.pal(9, "YlOrRd"))[3:9], (brewer.pal(9, "YlOrBr"))[3:9],(brewer.pal(9, "Reds"))[3:9], 
#                  (brewer.pal(9, "RdPu"))[3:9],(brewer.pal(9, "Purples"))[3:9], (brewer.pal(9, rev("BuPu")))[2:9])
# Order samples
#names(samplecolors) <- sample_name
  
#colourCount = length(unique(metadata$orig.ident))
#getPalette = colorRampPalette(brewer.pal(colourCount, "Dark2"))
  
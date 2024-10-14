# Create color palettes and plot theme

### Usage

The `create_color_palette_project.R` script is intended to be run via the command line from the top directory of the repository as follows:

```
Rscript create_color_palette_project.R
```

Parameters according to the project and analysis strategy will need to be specified in the following scripts:
- `create_color_palette_project.R`: define `root_dir`

## Folder content

This folder contains scripts tasked to (1) provide the plot theme to be used across data analysis, and (2) create color palettes for the project.

## Folder structure 

The structure of this folder is as follows:

```
├── img
|   └── DNB_BINF_Core_logo.png
├── palettes
|   ├── binary_color_palette.tsv
|   └── qc_color_palette.tsv
├── README.md
├── scripts
|   ├── create_color_palette_project.R
|___└── theme_plot.R
```

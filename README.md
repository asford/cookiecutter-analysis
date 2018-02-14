# cookiecutter-analysis

A simple template for `conda`-based analysis projects.

The general project framework is an env-per-project model, in which each
analysis environment is a single directory with an associated conda environment
of the same name. `direnv` is used to activate the working environment on entry. 

# Environment Setup
(From [here](https://geohackweek.github.io/Introductory/01-conda-tutorial/))

## Individually through conda

Terminal:
```conda install -c conda-forge <package-name>```

## Through environment.yaml file

Terminal:
```conda install --channel=conda-forge nb_conda_kernels```

```conda env create --file environment.yml```

```source activate haackwellenv``` 

After activating the environment, run the Jupyter notebook, and change kernels. If 'haackwellenv' isn't listed, try 'Python [conda root]', and it should work..

# List of packages needed to run all notebooks (as of 9/13/2017)
- xarray
- plotly
- matplotlib
- numpy
- pandas
- geopandas
- basemap
- nltk
- pydap
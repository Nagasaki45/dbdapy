This repo contains the solutions to the exercises of Doing Bayesian Data Analysis, 2nd Edition, by J. L. Kruschke.
I've started by following the book and the exercises as is, but somewhere around chapter 5 I've changed my mind and decided to code my solutions in python and [pymc3](https://github.com/pymc-devs/pymc3).

A summary of way I've decided to abandon R and start coding in python will be updated soon, I promise.
Meanwhile, you are also welcome to take a look at two another great resources for this book solutions, in python:

- [erikson84's BayesDataAnalysisWithPyMC](https://github.com/erikson84/BayesDataAnalysisWithPyMC)
- [aloctavodia's Doing_bayesian_data_analysis](https://github.com/aloctavodia/Doing_bayesian_data_analysis)

I think that my approach deserve its own repo because I'm not translating the R code into python and rather provide solution to the exercises using the best tools I can find.

Note that this repo will probably remains a work in progress for a long time. But you are welcome to help.

# Old, R, commentaire

### Getting the book utility scripts

    wget https://sites.google.com/site/doingbayesiandataanalysis/software-installation/DBDA2Eprograms.zip
    unzip DBDA2Eprograms.zip
    rm DBDA2Eprograms.zip

The `utils` directory contains my "improvements" to the author utilities that came with the book,
mainly by loosing some of the unnecessary dependencies between scripts.

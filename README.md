# Pythonista-archery-graphs
Archery-graphs.py is a Pythonista program that helps visualizing and comparing archery training sessions. 

The script takes it's input from the clipboard and generates two sets of plots. 
The first one is a large box plot covering all logged results. Then individual (scatter) plots are 
created for each training session.

## Example data (from the Notes app):

```
Recurve 18 m (2019)
2019-12-12, 21, 18, 23, 21, 24, 23, 24, 24, 24, 18, 26
2019-12-19, 26, 24, 23, 18, 24, 21, 22, 24, 17, 18, 15, 14, 14, 23
```

## Box plot
The first line in the example is used for the box plot´s title. Each subsequent data line consist of a date 
followed by the summary of each 3-arrow round.

## Scatter plots
Each log entry results in one scatter plot. The title is built from the date plus a calculated value 
(the mean value multiplied by 100). These values can be regarded as translations into 10-round series.

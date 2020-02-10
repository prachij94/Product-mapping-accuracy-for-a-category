# Product mapping accuracy for a category

There are two python files in this repository. They have different working and inputs but as an end point, they are used to bifurcate the data into the readable format i.e. tabular with product and the mapped microcategory. This helps judge the accuracy in bulk product mapping and analysis for improvement.

### highmedlow.py

This script reads in multiple csv files one by one, where each file has the name of the product for which it contains the data. Each file contains large number of rows of single line delimiter separated McatId, McatName, McatAccuracyLevel (i.e. high/med/low). More on the steps followed is explained in the doc file __highmedlow_README.docx__.
The output columns are 'ProductName','McatId','McatName','McatAccuracyLevel'

### label&highmedlow.py

This script reads in a single bulk text file which has data in the following format:
```
mcatid1
__label__keyword1 mcatname1 probability1 mcatname2 probability2 ...
__label__keyword2 mcatname1 probability1...
...
mcatid2
....
```
where there is an integer microcategory id at each starting line of a block and its following lines have the keywords which get matched with some with microcategory name and each with what probability. The output columns are 'PMCAT','Keyword','match','Probability'.

## Usage:
```
python highmedlow.py
```
```
python label&highmedlow.py
```

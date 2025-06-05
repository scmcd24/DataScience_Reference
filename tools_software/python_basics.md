
# Set: useful operations comparing/performing operations with data?
intersection, union, etc?

# Series
- 1D vector (list) of items, indexed, mutable, of ONE data type
- A numpy array under the hood
- Use if you need to do complicated things with a list of data

# Speed:
- Series, tuple, set < list < dataframe

# Matrices & Arrays:
- Can only contain one data type
- Faster than dataframes

# Tibble (R tidyverse)
- "Opinionated, lazy" data frames
- Does not change variable names / types
- Does not display entire object, just first 10 rows / data types

- https://r4ds.had.co.nz/tibbles.html

Python          |             Python              |         Pandas     |    Numpy       |                             | 
----------------------------------------------------------------------------------------------------------------------- 
R               |             |   R  |                     |                        R                     | Tidyverse |
-----------------------------------------------------------------------------------------------------------------------  
Feature         | Set | Tuple | List | Dictionary | Series | Dataframe | Array | Matrix | Vector | Factor | Tibble    |
-----------------------------------------------------------------------------------------------------------------------
Mutable         |
Speed           |
Ordered         |
Indexing        |
Duplicates      |
Constructor     |
Data Types      |

Python: set, list, tuple, dictionary, 
Numpy/pandas: array, dataframe, series
R: vector, matrix, list, array, dataframe
tidyverse: tibble, factors
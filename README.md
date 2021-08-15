# surfs_up
SQLite, SQLAlchemy, and Flask Module. 
## Overview of the Statistical Analysis
- We did an analysis of historical weather trends in Oahu, Hawaii to decipher the viability of a combination Surf Shop and Ice Cream shop. We gathered Oahu's historical temperatures for the months of June and December. We then ran a statistical summary on these datasets.

## Results
### Key Weather Differences in June and Decemeber
- The minimum temperature in December was 8 degrees lower than the minumum for June.
- The 25th and 50th percentile temperatures were 4 degrees lower in December than in June. While the 75th Percentile temperature was only 3 degrees lower than in December.
- The mean temperature for June was 3.9 degrees higher than that of January, when rounded.

## Summary
- The variance of the two months temperatures were much closer than one might suspect before looking into the data. The June temperatues were a bit lower than some might expect and the December temperatures were fairly warm. While the temperatures are not extremely high at any point in the year, it is rarely cold enough to prevent people from surfing or desiring ice cream. One factor we did not evaluate was the precipitation rates for each month. While rain is unlikely to significantly affect ice cream sales, an intense rainy season could dampen the sale of surfing goods. We could run a query for each month, that gathers how many days had significant precipitation in each month. This would give W.Avy additional context for his calculations on the feasibility of the surf business. It would make sense to query the temperature data of additional months. Two that come to mind would be February and August. It is possible that February is a colder month than December, and August is somewhat hotter than June. This information is worthy of consideration.

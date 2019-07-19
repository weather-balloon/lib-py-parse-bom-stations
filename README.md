# lib-py-parse-bom-stations

[![Build Status](https://dev.azure.com/weatherballoon/Weather%20Balloon/_apis/build/status/weather-balloon.lib-py-parse-bom-stations?branchName=master)](https://dev.azure.com/weatherballoon/Weather%20Balloon/_build/latest?definitionId=10&branchName=master)

Parses [weather stations published by the Bureau of Meteorology](ftp://ftp.bom.gov.au/anon2/home/ncc/metadata/sitelists/stations.zip).

```
Bureau of Meteorology product IDCJMC0014.                                       Produced: 12 Jul 2019

   Site  Dist  Site name                                 Start     End      Lat       Lon Source         STA Height (m)   Bar_ht    WMO
------- ----- ---------------------------------------- ------- ------- -------- --------- -------------- --- ---------- -------- ------
 001000 01    KARUNJIE                                    1940    1983 -16.2919  127.1956 .....          WA       320.0       ..     ..
 001001 01    OOMBULGURRI                                 1914    2012 -15.1806  127.8456 GPS            WA         2.0       ..     ..
 001002 01    BEVERLEY SP                                 1959    1967 -16.5825  125.4828 .....          WA          ..       ..     ..
 001003 01    PAGO MISSION                                1908    1940 -14.1331  126.7158 .....          WA         5.0     24.4     ..
 001004 01    KUNMUNYA                                    1915    1948 -15.4167  124.7167 .....          WA        47.0       ..     ..
 001005 01    WYNDHAM PORT                                1886    1995 -15.4644  128.1000 .....          WA        20.0       ..     ..
 001006 01    WYNDHAM AERO                                1951      .. -15.5100  128.1503 GPS            WA         3.8      4.3  95214
```

At the base of the data is a blank line followed by an informational footer.

```

19375 stations

(c) Copyright Commonwealth of Australia 2019, Bureau of Meteorology (ABN 92 637 533 532) 
Please note Copyright, Disclaimer and Privacy Notice, accessible at <http://www.bom.gov.au/other/copyright.shtml>
```

## Set up

You may notice a delay when you `git commit` - this is due to a commit hook (`.git/hooks/pre-commit`)
that checks your code prior to allowing you to commit. You can skip this check if you really need to
by using the `--no-verify` parameter with your `git commit`.

If you need to skip the Azure Pipelines CI build, 

   git commit -m '[skip ci] Pipeline work' --no-verify

The 

   git tag 0.1.7
   git push --tags
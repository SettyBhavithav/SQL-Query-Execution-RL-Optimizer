# PostgreSQL RL Optimizer Evaluation Report

Improvements are claimed only when measured execution time improved
and the EXPLAIN plan actually changed. `plan unchanged` is reported
when the selected action did not change PostgreSQL's operator tree.

## Per-query Results

| Query | Baseline Time | RL Time | Time Improvement | Baseline Cost | RL Cost | Buffer Improvement | Outcome |
| ----- | ------------- | ------- | ---------------- | ------------- | ------- | ------------------ | ------- |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 4.933 | 3.549 | 0.281 | 607.01 | 607.01 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.437 | 0.380 | 0.130 | 270.53 | 270.53 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 8.814 | 6.424 | 0.271 | 1008.50 | 1008.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 0.937 | 0.943 | -0.006 | 347.39 | 347.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 3.444 | 3.632 | -0.055 | 871.24 | 871.24 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 3.306 | 2.792 | 0.155 | 524.24 | 524.24 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.327 | 1.384 | -0.043 | 336.67 | 336.67 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_keyword mk... | 0.615 | 0.578 | 0.060 | 1120.19 | 568.28 | 0.012 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.051 | 2.081 | -0.015 | 439.50 | 439.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.791 | 2.453 | -0.370 | 323.98 | 323.98 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 1.931 | 0.899 | 0.534 | 585.64 | 430.35 | -0.009 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 0.579 | 0.632 | -0.092 | 520.60 | 520.62 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_compan... | 1.780 | 1.620 | 0.090 | 637.88 | 539.26 | -0.639 | unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 5.088 | 5.117 | -0.006 | 748.68 | 748.68 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.414 | 0.978 | 0.308 | 347.04 | 347.04 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.612 | 0.014 | 0.977 | 313.16 | 12.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.624 | 0.152 | 0.756 | 269.91 | 152.25 | 0.016 | unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 1.642 | 1.665 | -0.014 | 335.65 | 335.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.335 | 0.016 | 0.952 | 211.84 | 16.62 | 0.963 | unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 5.285 | 4.732 | 0.105 | 729.98 | 729.98 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 2.615 | 3.621 | -0.385 | 798.97 | 657.10 | 0.071 | degraded |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 2.944 | 2.804 | 0.048 | 437.94 | 437.94 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.233 | 4.497 | -1.014 | 490.29 | 490.29 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 2.616 | 2.772 | -0.060 | 696.68 | 696.68 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 2.752 | 3.927 | -0.427 | 534.35 | 534.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.248 | 1.196 | 0.042 | 267.40 | 267.40 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 2.744 | 2.559 | 0.067 | 810.93 | 666.79 | 0.079 | unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.284 | 1.404 | -0.093 | 451.02 | 405.15 | -0.004 | unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 3.031 | 1.977 | 0.348 | 697.76 | 557.53 | -0.005 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 2.792 | 2.752 | 0.014 | 654.81 | 654.81 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 3.892 | 3.878 | 0.004 | 847.71 | 847.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.391 | 3.527 | -0.040 | 495.71 | 495.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.708 | 3.757 | -0.013 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info_idx m... | 24.279 | 16.875 | 0.305 | 2762.63 | 2762.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 1.649 | 2.708 | -0.642 | 352.86 | 352.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.917 | 3.049 | -0.045 | 469.83 | 469.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.701 | 2.404 | 0.110 | 345.30 | 345.30 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 3.487 | 3.480 | 0.002 | 748.50 | 748.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 0.761 | 0.712 | 0.064 | 329.68 | 329.68 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.877 | 1.909 | -0.017 | 351.70 | 351.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.412 | 0.555 | -0.347 | 265.43 | 265.43 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 1.640 | 1.746 | -0.065 | 520.89 | 520.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.382 | 0.380 | 0.005 | 248.33 | 248.33 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.620 | 0.625 | -0.008 | 419.90 | 404.93 | -0.049 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 6.777 | 6.901 | -0.018 | 1139.21 | 1139.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 6.634 | 7.410 | -0.117 | 1209.21 | 1209.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.628 | 0.612 | 0.025 | 426.56 | 426.56 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.346 | 0.020 | 0.942 | 211.84 | 16.62 | 0.963 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 0.328 | 0.027 | 0.918 | 531.85 | 336.63 | 0.927 | unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.652 | 1.981 | 0.253 | 434.16 | 434.16 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 7.772 | 9.926 | -0.277 | 1260.11 | 1260.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.439 | 2.428 | 0.005 | 517.40 | 517.40 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 4.400 | 4.281 | 0.027 | 716.33 | 716.33 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 0.592 | 0.021 | 0.965 | 857.24 | 554.40 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.012 | 1.839 | 0.086 | 387.15 | 387.15 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=mk.movi... | 4.621 | 4.665 | -0.010 | 1104.50 | 1104.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 2.564 | 2.722 | -0.062 | 670.48 | 670.48 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 1.972 | 1.869 | 0.052 | 648.46 | 648.46 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk,movie_info_idx mi_... | 4.421 | 6.712 | -0.518 | 1072.85 | 1072.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.886 | 0.021 | 0.976 | 423.70 | 119.52 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 4.051 | 3.955 | 0.024 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.838 | 0.848 | -0.012 | 210.35 | 210.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.138 | 1.137 | 0.001 | 362.90 | 362.90 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_companies mc,movie_keyword m... | 3.212 | 3.175 | 0.012 | 851.26 | 851.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.697 | 3.938 | -0.065 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 2.222 | 2.687 | -0.209 | 599.71 | 599.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 17.172 | 15.884 | 0.075 | 2634.80 | 2634.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 1.933 | 2.788 | -0.442 | 456.83 | 456.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM cast_info ci,title t,movie_companies mc WHERE t.id=ci.mo... | 2.399 | 3.287 | -0.370 | 800.41 | 800.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 1.956 | 2.833 | -0.448 | 646.55 | 646.55 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 3.891 | 3.963 | -0.019 | 742.60 | 742.60 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 4.148 | 5.941 | -0.432 | 786.14 | 786.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 0.604 | 0.024 | 0.960 | 367.28 | 94.15 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 1.424 | 1.572 | -0.104 | 662.28 | 662.28 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 0.642 | 0.556 | 0.134 | 321.18 | 321.18 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.800 | 5.348 | -0.407 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 11.182 | 8.833 | 0.210 | 1437.21 | 1437.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 2.625 | 1.880 | 0.284 | 585.43 | 585.43 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.342 | 0.037 | 0.892 | 241.33 | 92.17 | 0.564 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 1.465 | 1.483 | -0.012 | 415.82 | 415.82 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.001 | 1.001 | 0.000 | 257.00 | 257.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 1.746 | 1.702 | 0.025 | 550.61 | 550.61 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 2.608 | 2.758 | -0.058 | 630.75 | 630.75 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 0.642 | 0.017 | 0.974 | 321.46 | 16.91 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 9.551 | 10.713 | -0.122 | 1414.70 | 1414.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 19.136 | 17.798 | 0.070 | 2932.90 | 2932.90 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 0.596 | 0.015 | 0.975 | 321.17 | 16.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 10.095 | 10.483 | -0.038 | 1899.10 | 1899.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 2.877 | 2.869 | 0.003 | 796.71 | 796.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_info_idx ... | 1.763 | 1.775 | -0.007 | 632.20 | 632.20 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM movie_keyword mk,title t,cast_info ci WHERE t.id=mk.movi... | 0.571 | 0.873 | -0.529 | 911.28 | 892.08 | 0.000 | unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 1.949 | 2.677 | -0.374 | 442.17 | 442.17 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_keyword m... | 9.174 | 13.300 | -0.450 | 1616.40 | 1616.40 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 3.099 | 2.774 | 0.105 | 589.36 | 589.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.670 | 3.680 | -0.003 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 1.412 | 1.476 | -0.045 | 554.76 | 554.76 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 6.598 | 9.431 | -0.429 | 1159.21 | 1159.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 1.440 | 0.932 | 0.353 | 1021.78 | 1021.78 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.533 | 0.544 | -0.021 | 199.21 | 199.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 4.578 | 4.634 | -0.012 | 886.63 | 886.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 18.130 | 14.871 | 0.180 | 2462.07 | 2462.07 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.082 | 1.087 | -0.005 | 227.25 | 227.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 11.140 | 12.870 | -0.155 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.494 | 1.571 | -0.052 | 334.38 | 334.38 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 5.659 | 5.826 | -0.030 | 1029.53 | 1029.53 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 3.749 | 3.903 | -0.041 | 996.00 | 996.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 5.137 | 5.095 | 0.008 | 1023.85 | 1023.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 2.413 | 2.373 | 0.017 | 538.10 | 538.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id | 5.102 | 5.141 | -0.008 | 698.36 | 698.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 3.900 | 3.912 | -0.003 | 968.35 | 968.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.327 | 1.378 | -0.038 | 232.08 | 232.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 3.021 | 2.924 | 0.032 | 595.36 | 595.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_keyword m... | 5.847 | 8.401 | -0.437 | 1206.86 | 1206.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 8.828 | 8.702 | 0.014 | 1603.86 | 1603.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.544 | 0.013 | 0.976 | 313.16 | 12.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.918 | 0.827 | 0.099 | 203.32 | 203.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 3.032 | 2.994 | 0.013 | 850.00 | 850.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 3.615 | 3.809 | -0.054 | 657.53 | 657.53 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.387 | 1.284 | 0.074 | 327.43 | 327.43 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 1.384 | 1.353 | 0.022 | 520.34 | 520.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 3.101 | 3.147 | -0.015 | 574.83 | 574.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 3.294 | 3.134 | 0.049 | 750.50 | 750.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 0.147 | 0.151 | -0.027 | 336.02 | 336.02 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 5.021 | 5.006 | 0.003 | 1119.05 | 1119.05 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 0.923 | 0.983 | -0.065 | 587.47 | 587.47 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 0.421 | 0.562 | -0.335 | 1013.15 | 470.14 | 0.018 | unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 0.939 | 0.023 | 0.976 | 849.10 | 336.63 | 0.981 | improved |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 0.868 | 0.829 | 0.045 | 342.58 | 342.58 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 0.920 | 0.986 | -0.072 | 782.83 | 782.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 4.875 | 3.358 | 0.311 | 912.25 | 912.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 0.845 | 0.023 | 0.973 | 787.56 | 262.89 | 0.981 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.406 | 1.363 | 0.031 | 336.76 | 336.76 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 3.658 | 4.024 | -0.100 | 1033.45 | 1033.45 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 5.696 | 4.040 | 0.291 | 855.97 | 855.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 10.087 | 11.490 | -0.139 | 1801.05 | 1801.05 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.988 | 0.889 | 0.100 | 288.31 | 288.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 6.216 | 6.312 | -0.015 | 1100.42 | 1100.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 4.439 | 4.458 | -0.004 | 913.59 | 913.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.577 | 1.531 | 0.029 | 465.70 | 465.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 2.657 | 1.845 | 0.306 | 680.95 | 680.95 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 6.105 | 6.135 | -0.005 | 1322.35 | 1322.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.315 | 2.159 | 0.067 | 477.85 | 477.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.785 | 3.663 | 0.032 | 511.59 | 511.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.889 | 0.921 | -0.036 | 225.14 | 225.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 6.798 | 4.657 | 0.315 | 1148.16 | 1148.16 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.775 | 0.868 | -0.120 | 268.55 | 268.55 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_info_idx ... | 8.665 | 6.269 | 0.277 | 1095.82 | 1095.82 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.750 | 0.798 | -0.064 | 307.87 | 307.87 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.784 | 0.768 | 0.020 | 286.49 | 286.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 13.568 | 11.293 | 0.168 | 1905.88 | 1905.88 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.851 | 0.850 | 0.001 | 227.83 | 227.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 1.409 | 1.333 | 0.054 | 431.84 | 431.84 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 0.486 | 0.331 | 0.319 | 433.22 | 433.19 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 2.063 | 2.028 | 0.017 | 492.51 | 492.51 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 1.771 | 1.806 | -0.020 | 563.93 | 563.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 3.291 | 3.312 | -0.006 | 740.05 | 740.05 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM cast_info ci,title t,movie_companies mc WHERE t.id=ci.mo... | 5.730 | 4.102 | 0.284 | 976.55 | 976.55 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 7.891 | 7.748 | 0.018 | 1255.43 | 1255.43 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.877 | 0.965 | -0.100 | 320.25 | 320.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.580 | 0.021 | 0.964 | 423.76 | 119.59 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 0.166 | 0.161 | 0.030 | 392.87 | 392.87 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.990 | 0.920 | 0.071 | 309.97 | 309.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.873 | 1.871 | 0.001 | 451.34 | 451.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 4.543 | 6.489 | -0.428 | 816.08 | 816.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 2.074 | 2.011 | 0.030 | 389.69 | 389.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.407 | 0.396 | 0.027 | 271.43 | 271.43 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 3.657 | 3.766 | -0.030 | 929.41 | 929.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.368 | 3.324 | -0.404 | 437.55 | 437.55 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 8.300 | 5.614 | 0.324 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 3.658 | 3.609 | 0.013 | 798.74 | 798.74 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 2.080 | 1.451 | 0.302 | 600.81 | 600.81 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 4.828 | 5.073 | -0.051 | 810.33 | 810.33 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.044 | 1.079 | -0.034 | 232.10 | 232.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.659 | 1.767 | -0.065 | 485.81 | 485.81 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 19.957 | 13.903 | 0.303 | 2280.72 | 2280.72 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info_idx m... | 0.360 | 0.026 | 0.928 | 858.88 | 663.55 | 0.929 | unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.089 | 1.117 | -0.026 | 444.39 | 444.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 2.018 | 1.996 | 0.011 | 563.63 | 563.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.092 | 1.362 | 0.349 | 336.80 | 336.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.868 | 4.054 | -0.048 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 9.090 | 8.907 | 0.020 | 1641.81 | 1641.81 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.734 | 1.722 | 0.007 | 455.77 | 455.77 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 0.576 | 0.015 | 0.974 | 321.17 | 16.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 2.923 | 3.028 | -0.036 | 632.23 | 632.23 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 2.092 | 2.043 | 0.023 | 353.14 | 353.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info_idx m... | 1.650 | 0.483 | 0.707 | 881.17 | 555.26 | 0.031 | improved |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 3.552 | 3.605 | -0.015 | 857.58 | 857.58 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 1.801 | 1.859 | -0.032 | 426.05 | 426.05 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 0.922 | 0.817 | 0.114 | 335.71 | 335.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 9.545 | 10.323 | -0.082 | 1693.75 | 1693.75 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 3.449 | 4.964 | -0.439 | 798.70 | 798.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 3.185 | 3.101 | 0.026 | 1014.76 | 1014.76 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 0.147 | 0.153 | -0.041 | 445.44 | 445.44 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 0.790 | 0.717 | 0.092 | 332.40 | 332.40 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.610 | 2.522 | 0.034 | 408.58 | 408.58 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 1.897 | 1.524 | 0.197 | 531.85 | 336.63 | 0.331 | unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.930 | 2.970 | -0.014 | 397.61 | 397.61 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.498 | 2.502 | -0.002 | 469.15 | 469.15 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 6.699 | 6.627 | 0.011 | 1208.53 | 1208.53 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.366 | 0.032 | 0.913 | 220.14 | 30.85 | 0.778 | unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 2.353 | 2.330 | 0.010 | 401.84 | 401.84 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 0.933 | 0.970 | -0.040 | 387.80 | 387.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 3.458 | 3.263 | 0.056 | 898.47 | 898.47 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 4.348 | 3.065 | 0.295 | 609.67 | 609.67 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 3.343 | 3.316 | 0.008 | 676.54 | 676.54 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.595 | 0.640 | -0.076 | 419.90 | 404.93 | -0.049 | unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 13.935 | 9.299 | 0.333 | 1731.25 | 1731.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.576 | 0.577 | -0.002 | 423.75 | 423.75 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.145 | 1.153 | -0.007 | 291.97 | 291.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 4.963 | 3.519 | 0.291 | 876.85 | 876.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 1.603 | 1.609 | -0.004 | 534.55 | 534.55 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 3.462 | 3.558 | -0.028 | 931.93 | 931.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 3.507 | 2.467 | 0.297 | 666.44 | 666.44 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 2.886 | 2.851 | 0.012 | 625.37 | 625.37 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 1.820 | 1.833 | -0.007 | 414.60 | 414.60 | 0.000 | plan unchanged |

## Execution Plan Comparisons

For every query, the original and RL-selected plans are shown.
If the plan did not change, it is reported as 'Plan unchanged'.

### Query 0: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 1: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=(t JOIN mc); join_method=merge; scan_method=indexscan; index=created:movie_companies(movie_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 2: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 3: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 4: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor...
- **Action**: join_order=(((t JOIN mk) JOIN mi_idx) JOIN mi); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 5: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 6: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 7: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_keyword mk...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=created:cast_info(movie_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_companies (mc)
    Hash
      Nested Loop
        Hash Join
          Seq Scan cast_info (ci)
          Hash
            Seq Scan movie_keyword (mk)
        Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_companies (mc)
      Hash
        Nested Loop
          Seq Scan movie_keyword (mk)
          Index Scan title (t) using title_pkey
    Index Scan cast_info (ci) using rl_tmp_5caa36da1b90
```

### Query 8: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 9: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 10: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_info(info_type_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_keyword (mk)
      Hash
        Seq Scan movie_info (mi)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_keyword (mk)
      Hash
        Bitmap Heap Scan movie_info (mi)
          Bitmap Index Scan using rl_tmp_bb45d367a75d
    Index Only Scan title (t) using title_pkey
```

### Query 11: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=((t JOIN mc) JOIN mk); join_method=merge; scan_method=indexscan; index=created:movie_companies(company_type_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 12: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_compan...
- **Action**: join_order=(((t JOIN mi) JOIN mi_idx) JOIN mc); join_method=nestloop; scan_method=seqscan; index=created:movie_info_idx(movie_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_info (mi)
    Hash
      Hash Join
        Seq Scan movie_companies (mc)
        Hash
          Hash Join
            Seq Scan movie_info_idx (mi_idx)
            Hash
              Seq Scan title (t)
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info (mi)
      Hash
        Hash Join
          Seq Scan movie_companies (mc)
          Hash
            Seq Scan title (t)
    Index Scan movie_info_idx (mi_idx) using rl_tmp_c166c2f3f2d6
```

### Query 13: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 14: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 15: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=(t JOIN mk); join_method=merge; scan_method=indexscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_keyword (mk)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Index Scan movie_keyword (mk) using rl_tmp_7eabc4e1ec9d
    Index Only Scan title (t) using title_pkey
```

### Query 16: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=(t JOIN mc); join_method=merge; scan_method=indexscan; index=created:movie_companies(company_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_companies (mc)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Bitmap Heap Scan movie_companies (mc)
      Bitmap Index Scan using rl_tmp_76ec6da366ef
    Index Only Scan title (t) using title_pkey
```

### Query 17: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 18: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:movie_companies(company_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_companies (mc)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Index Scan movie_companies (mc) using rl_tmp_d55f76909c2d
    Index Scan title (t) using title_pkey
```

### Query 19: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 20: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_companies(company_id)
- **Outcome**: degraded

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Seq Scan movie_companies (mc)
        Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Bitmap Heap Scan movie_companies (mc)
          Bitmap Index Scan using rl_tmp_7dcf28bf431d
        Index Only Scan title (t) using title_pkey
```

### Query 21: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 22: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 23: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 24: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 25: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 26: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_companies(company_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Seq Scan movie_companies (mc)
        Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Bitmap Heap Scan movie_companies (mc)
          Bitmap Index Scan using rl_tmp_62c51bdb27cd
        Index Only Scan title (t) using title_pkey
```

### Query 27: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=((t JOIN mi) JOIN mi_idx); join_method=merge; scan_method=indexscan; index=created:movie_info_idx(info_type_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info (mi)
      Hash
        Seq Scan movie_info_idx (mi_idx)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info (mi)
      Hash
        Bitmap Heap Scan movie_info_idx (mi_idx)
          Bitmap Index Scan using rl_tmp_d98e68e5a20a
    Index Scan title (t) using title_pkey
```

### Query 28: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i...
- **Action**: join_order=(t JOIN ci); join_method=default; scan_method=indexscan; index=created:cast_info(role_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Seq Scan title (t)
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Bitmap Heap Scan cast_info (ci)
      Bitmap Index Scan using rl_tmp_2ef5e6d94002
    Hash
      Seq Scan title (t)
```

### Query 29: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 30: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 31: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 32: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 33: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info_idx m...
- **Action**: join_order=(((t JOIN mi_idx) JOIN ci) JOIN mc); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 34: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 35: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 36: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 37: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 38: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 39: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 40: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=(t JOIN mc); join_method=merge; scan_method=indexscan; index=created:movie_companies(movie_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 41: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 42: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=(t JOIN mc); join_method=merge; scan_method=indexscan; index=created:movie_companies(movie_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 43: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_info_idx(info_type_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info_idx (mi_idx)
      Hash
        Seq Scan movie_keyword (mk)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Bitmap Heap Scan movie_info_idx (mi_idx)
        Bitmap Index Scan using rl_tmp_c051afdc3dfb
      Hash
        Seq Scan movie_keyword (mk)
    Index Only Scan title (t) using title_pkey
```

### Query 44: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 45: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 46: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_info_idx(info_type_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 47: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:movie_companies(company_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_companies (mc)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Index Scan movie_companies (mc) using rl_tmp_7b6dbd02e954
    Index Scan title (t) using title_pkey
```

### Query 48: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_companies(company_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_keyword (mk)
      Hash
        Seq Scan movie_companies (mc)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_keyword (mk)
      Hash
        Index Scan movie_companies (mc) using rl_tmp_c86d1daa5326
    Index Only Scan title (t) using title_pkey
```

### Query 49: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 50: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 51: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 52: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 53: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Seq Scan movie_keyword (mk)
        Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan cast_info (ci)
      Hash
        Index Scan movie_keyword (mk) using rl_tmp_ae49d8ad2a2e
    Index Only Scan title (t) using title_pkey
```

### Query 54: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 55: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=mk.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 56: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 57: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 58: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk,movie_info_idx mi_...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mk) JOIN ci); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 59: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info_idx (mi_idx)
      Hash
        Seq Scan movie_keyword (mk)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info_idx (mi_idx)
      Hash
        Index Scan movie_keyword (mk) using rl_tmp_79a429173c64
    Index Only Scan title (t) using title_pkey
```

### Query 60: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 61: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 62: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 63: SELECT COUNT(*) FROM title t,movie_info mi,movie_companies mc,movie_keyword m...
- **Action**: join_order=(((t JOIN mk) JOIN mc) JOIN mi); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 64: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 65: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 66: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 67: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 68: SELECT COUNT(*) FROM cast_info ci,title t,movie_companies mc WHERE t.id=ci.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 69: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 70: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 71: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 72: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_keyword (mk)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Bitmap Heap Scan movie_keyword (mk)
      Bitmap Index Scan using rl_tmp_2d2f01230f1f
    Index Scan title (t) using title_pkey
```

### Query 73: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 74: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:title(production_year)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 75: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 76: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 77: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 78: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:movie_companies(company_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_companies (mc)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Bitmap Heap Scan movie_companies (mc)
      Bitmap Index Scan using rl_tmp_20f503899fb5
    Index Scan title (t) using title_pkey
```

### Query 79: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 80: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 81: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 82: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 83: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_keyword (mk)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Index Scan movie_keyword (mk) using rl_tmp_624d11512d7a
    Index Scan title (t) using title_pkey
```

### Query 84: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 85: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 86: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_keyword (mk)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Index Scan movie_keyword (mk) using rl_tmp_dc315b36591c
    Index Scan title (t) using title_pkey
```

### Query 87: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 88: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 89: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_info_idx ...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mi) JOIN mc); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 90: SELECT COUNT(*) FROM movie_keyword mk,title t,cast_info ci WHERE t.id=mk.movi...
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:title(production_year)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Seq Scan movie_keyword (mk)
        Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Hash Join
        Seq Scan movie_keyword (mk)
        Hash
          Bitmap Heap Scan title (t)
            Bitmap Index Scan using rl_tmp_04e1d180722d
```

### Query 91: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 92: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_keyword m...
- **Action**: join_order=(((t JOIN mk) JOIN mi) JOIN mc); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 93: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 94: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 95: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 96: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 97: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH...
- **Action**: join_order=(((t JOIN mi) JOIN mc) JOIN ci); join_method=hash; scan_method=seqscan; index=created:cast_info(role_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 98: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 99: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 100: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 101: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 102: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 103: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 104: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 105: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 106: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 107: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 108: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id
- **Action**: join_order=original; join_method=hash; scan_method=seqscan; index=created:cast_info(movie_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 109: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 110: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 111: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 112: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_keyword m...
- **Action**: join_order=(((t JOIN mk) JOIN mi) JOIN mc); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 113: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 114: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=(t JOIN mk); join_method=merge; scan_method=indexscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_keyword (mk)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Index Scan movie_keyword (mk) using rl_tmp_63fc91f5bcb5
    Index Only Scan title (t) using title_pkey
```

### Query 115: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 116: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 117: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 118: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 119: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=seqscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 120: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 121: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 122: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 123: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 124: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i...
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:title(production_year)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 125: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=created:cast_info(movie_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Hash Join
          Seq Scan movie_info (mi)
          Hash
            Seq Scan movie_companies (mc)
        Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Nested Loop
      Hash Join
        Seq Scan movie_info (mi)
        Hash
          Seq Scan movie_companies (mc)
      Index Scan title (t) using title_pkey
    Index Only Scan cast_info (ci) using rl_tmp_d0d496bea2e8
```

### Query 126: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:cast_info(person_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_keyword (mk)
    Hash
      Nested Loop
        Seq Scan cast_info (ci)
        Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_keyword (mk)
      Hash
        Index Scan cast_info (ci) using rl_tmp_0a1da98d37fa
    Index Only Scan title (t) using title_pkey
```

### Query 127: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 128: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=((t JOIN mc) JOIN ci); join_method=merge; scan_method=indexscan; index=created:movie_companies(company_type_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 129: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 130: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=((t JOIN ci) JOIN mi); join_method=merge; scan_method=indexscan; index=created:cast_info(person_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_info (mi)
    Hash
      Nested Loop
        Seq Scan cast_info (ci)
        Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info (mi)
      Hash
        Index Scan cast_info (ci) using rl_tmp_f94c47e9fa62
    Index Scan title (t) using title_pkey
```

### Query 131: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 132: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 133: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 134: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 135: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 136: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 137: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 138: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 139: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 140: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 141: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 142: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 143: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 144: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 145: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 146: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_info_idx ...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mi) JOIN mc); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 147: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 148: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 149: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor...
- **Action**: join_order=(((t JOIN mk) JOIN mi_idx) JOIN mi); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 150: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 151: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 152: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=((t JOIN mc) JOIN mi); join_method=merge; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 153: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 154: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 155: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 156: SELECT COUNT(*) FROM cast_info ci,title t,movie_companies mc WHERE t.id=ci.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 157: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 158: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 159: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=((t JOIN mi_idx) JOIN mk); join_method=merge; scan_method=indexscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info_idx (mi_idx)
      Hash
        Seq Scan movie_keyword (mk)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info_idx (mi_idx)
      Hash
        Index Scan movie_keyword (mk) using rl_tmp_d147daf450c0
    Index Scan title (t) using title_pkey
```

### Query 160: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 161: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 162: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 163: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 164: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 165: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=(t JOIN mc); join_method=merge; scan_method=indexscan; index=created:movie_companies(movie_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 166: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 167: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 168: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 169: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 170: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 171: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 172: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 173: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 174: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 175: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info_idx m...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mc) JOIN ci); join_method=hash; scan_method=seqscan; index=created:movie_companies(company_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Hash Join
          Seq Scan movie_info_idx (mi_idx)
          Hash
            Seq Scan movie_companies (mc)
        Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Hash Join
          Seq Scan movie_info_idx (mi_idx)
          Hash
            Index Scan movie_companies (mc) using rl_tmp_aa6ff47b8359
        Index Scan title (t) using title_pkey
```

### Query 176: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 177: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 178: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 179: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 180: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 181: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 182: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_keyword (mk)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Index Scan movie_keyword (mk) using rl_tmp_59544d761032
    Index Scan title (t) using title_pkey
```

### Query 183: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 184: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 185: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info_idx m...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mc) JOIN ci); join_method=hash; scan_method=seqscan; index=created:cast_info(role_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_companies (mc)
    Hash
      Nested Loop
        Hash Join
          Seq Scan movie_info_idx (mi_idx)
          Hash
            Seq Scan cast_info (ci)
        Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_companies (mc)
    Hash
      Nested Loop
        Hash Join
          Seq Scan movie_info_idx (mi_idx)
          Hash
            Bitmap Heap Scan cast_info (ci)
              Bitmap Index Scan using rl_tmp_2c2612e9282c
        Index Only Scan title (t) using title_pkey
```

### Query 186: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 187: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 188: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 189: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 190: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 191: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 192: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 193: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 194: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 195: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_companies(company_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_keyword (mk)
      Hash
        Seq Scan movie_companies (mc)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_keyword (mk)
      Hash
        Index Scan movie_companies (mc) using rl_tmp_b399f17dfb7f
    Index Only Scan title (t) using title_pkey
```

### Query 196: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 197: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 198: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 199: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:movie_companies(company_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Nested Loop
    Seq Scan movie_companies (mc)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Bitmap Heap Scan movie_companies (mc)
      Bitmap Index Scan using rl_tmp_27ad844f7ab7
    Index Scan title (t) using title_pkey
```

### Query 200: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 201: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 202: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 203: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 204: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 205: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_info_idx(info_type_id)
- **Outcome**: unchanged

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info_idx (mi_idx)
      Hash
        Seq Scan movie_keyword (mk)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Bitmap Heap Scan movie_info_idx (mi_idx)
        Bitmap Index Scan using rl_tmp_d61ab8084be3
      Hash
        Seq Scan movie_keyword (mk)
    Index Only Scan title (t) using title_pkey
```

### Query 206: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 207: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:title(production_year)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 208: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 209: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor...
- **Action**: join_order=(((t JOIN mk) JOIN mi_idx) JOIN mi); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 210: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 211: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 212: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 213: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 214: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

## Aggregates (all queries, including failures and regressions)

- **Queries evaluated**: 215
- Mean baseline time (ms): 3.318
- Median baseline time (ms): 2.315
- Mean RL time (ms): 3.186
- Median RL time (ms): 2.404
- Mean time improvement: 0.0728
- Median time improvement: 0.0045
- Mean cost improvement: 0.0737
- **Percent improved**: 6.5%
- Percent unchanged (incl. plan unchanged): 93.0%
- Percent plan unchanged: 85.6%
- **Percent degraded**: 0.5%
- Percent failed: 0.0%
- Mean planning overhead (ms): 0.017
- Median planning overhead (ms): 0.008
- Outcome counts: {'plan unchanged': 184, 'unchanged': 16, 'improved': 14, 'degraded': 1}

# PostgreSQL RL Optimizer Evaluation Report

Improvements are claimed only when measured execution time improved
and the EXPLAIN plan actually changed. `plan unchanged` is reported
when the selected action did not change PostgreSQL's operator tree.

## Per-query Results

| Query | Baseline Time | RL Time | Time Improvement | Baseline Cost | RL Cost | Buffer Improvement | Outcome |
| ----- | ------------- | ------- | ---------------- | ------------- | ------- | ------------------ | ------- |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 5.945 | 4.285 | 0.279 | 601.89 | 601.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 19.104 | 16.591 | 0.132 | 1768.77 | 1768.77 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 22.881 | 20.019 | 0.125 | 1954.44 | 1954.44 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 8.212 | 8.043 | 0.021 | 1148.16 | 1148.16 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 7.565 | 8.168 | -0.080 | 1015.89 | 1015.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM movie_keyword mk,title t,cast_info ci WHERE t.id=mk.movi... | 12.275 | 13.174 | -0.073 | 1488.72 | 1488.72 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 4.972 | 5.183 | -0.042 | 469.82 | 469.82 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 12.608 | 8.485 | 0.327 | 1021.90 | 1021.90 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 15.479 | 14.674 | 0.052 | 1573.78 | 1573.78 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.846 | 0.989 | -0.169 | 194.86 | 194.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 1.379 | 0.048 | 0.965 | 423.70 | 119.52 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 3.911 | 3.705 | 0.053 | 712.26 | 712.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 4.263 | 5.293 | -0.242 | 530.34 | 530.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 14.965 | 14.004 | 0.064 | 1531.65 | 1531.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 3.051 | 4.733 | -0.551 | 842.27 | 842.27 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 6.721 | 7.301 | -0.086 | 1056.07 | 1056.07 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 26.997 | 29.253 | -0.084 | 2907.99 | 2907.99 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 4.533 | 3.503 | 0.227 | 493.69 | 493.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 8.112 | 9.035 | -0.114 | 893.70 | 893.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_companies mc WHERE t.id=mi.m... | 6.246 | 5.481 | 0.122 | 585.34 | 585.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 15.780 | 15.768 | 0.001 | 1374.35 | 1374.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 1.794 | 0.033 | 0.982 | 313.16 | 12.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 4.879 | 4.904 | -0.005 | 546.25 | 546.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 2.352 | 1.875 | 0.203 | 300.26 | 300.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 6.520 | 7.082 | -0.086 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 3.802 | 3.148 | 0.172 | 338.45 | 338.45 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 4.184 | 4.520 | -0.080 | 398.93 | 398.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 10.621 | 10.870 | -0.023 | 980.85 | 980.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 4.318 | 3.223 | 0.254 | 660.10 | 660.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 1.122 | 0.047 | 0.958 | 313.16 | 12.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.900 | 0.779 | 0.134 | 270.23 | 270.23 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 2.135 | 1.403 | 0.343 | 234.51 | 234.51 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 5.112 | 4.613 | 0.098 | 555.21 | 555.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 0.389 | 0.362 | 0.069 | 1111.63 | 1111.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 11.049 | 8.560 | 0.225 | 1226.42 | 1226.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 11.854 | 12.869 | -0.086 | 1238.80 | 1238.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 0.789 | 1.020 | -0.293 | 852.10 | 852.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 14.158 | 15.641 | -0.105 | 1562.08 | 1562.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx... | 7.481 | 8.399 | -0.123 | 1212.49 | 1212.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 1.599 | 0.085 | 0.947 | 367.28 | 94.14 | 0.636 | improved |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 5.097 | 4.737 | 0.071 | 467.99 | 467.99 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 10.320 | 12.631 | -0.224 | 1152.31 | 1152.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 28.768 | 22.744 | 0.209 | 2320.53 | 2320.53 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 7.306 | 9.006 | -0.233 | 1002.16 | 1002.16 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 8.713 | 7.361 | 0.155 | 591.40 | 591.40 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 10.776 | 6.852 | 0.364 | 755.85 | 755.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword... | 1.148 | 1.040 | 0.094 | 1037.66 | 1037.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 9.859 | 8.770 | 0.110 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 3.802 | 2.895 | 0.239 | 726.75 | 597.86 | -0.008 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 3.701 | 3.203 | 0.135 | 461.50 | 461.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 4.021 | 3.985 | 0.009 | 579.57 | 579.57 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM cast_info ci,title t WHERE t.id=ci.movie_id AND t.produc... | 5.156 | 6.119 | -0.187 | 622.65 | 622.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 6.912 | 6.029 | 0.128 | 774.21 | 774.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 3.489 | 3.503 | -0.004 | 653.92 | 653.92 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 3.276 | 4.432 | -0.353 | 353.37 | 353.37 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 1.168 | 0.057 | 0.951 | 526.69 | 253.55 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 6.520 | 6.912 | -0.060 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 4.124 | 4.218 | -0.023 | 457.41 | 457.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 3.932 | 5.726 | -0.456 | 477.54 | 477.54 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 7.612 | 6.798 | 0.107 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_info_idx ... | 6.458 | 6.017 | 0.068 | 762.09 | 762.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 6.100 | 6.945 | -0.139 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 13.157 | 12.106 | 0.080 | 1407.52 | 1407.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 18.731 | 16.347 | 0.127 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 3.530 | 5.391 | -0.527 | 342.42 | 342.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 7.924 | 8.175 | -0.032 | 920.49 | 920.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 0.650 | 0.060 | 0.908 | 468.03 | 297.73 | 0.945 | improved |
| SELECT COUNT(*) FROM cast_info ci,title t,movie_companies mc WHERE t.id=ci.mo... | 5.416 | 4.632 | 0.145 | 831.10 | 831.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 4.020 | 4.599 | -0.144 | 527.93 | 527.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.766 | 1.389 | -0.813 | 268.43 | 268.43 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.893 | 1.915 | -0.012 | 335.63 | 335.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 2.804 | 3.553 | -0.267 | 512.22 | 512.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc,movie_info m... | 5.504 | 3.411 | 0.380 | 825.26 | 625.06 | 0.183 | improved |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 7.148 | 6.204 | 0.132 | 522.66 | 522.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 2.704 | 2.827 | -0.045 | 447.32 | 447.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 10.438 | 12.340 | -0.182 | 1083.11 | 1083.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 35.453 | 32.618 | 0.080 | 2863.28 | 2863.28 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 9.646 | 8.316 | 0.138 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.762 | 0.882 | -0.157 | 194.59 | 194.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_keyword mk... | 5.121 | 3.397 | 0.337 | 1048.90 | 775.77 | 0.230 | improved |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 0.243 | 0.299 | -0.230 | 700.79 | 700.79 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 0.376 | 0.386 | -0.027 | 439.82 | 439.82 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.538 | 0.362 | 0.327 | 528.86 | 528.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 5.057 | 8.192 | -0.620 | 764.52 | 764.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 12.694 | 13.173 | -0.038 | 1026.14 | 1026.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 8.547 | 4.736 | 0.446 | 850.46 | 850.46 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 7.062 | 6.115 | 0.134 | 709.30 | 709.30 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.453 | 3.592 | -0.040 | 437.34 | 437.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 3.284 | 3.061 | 0.068 | 328.39 | 328.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 6.220 | 6.552 | -0.053 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.649 | 2.477 | 0.065 | 315.10 | 315.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 6.000 | 6.742 | -0.124 | 808.96 | 808.96 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 4.015 | 3.274 | 0.185 | 628.32 | 628.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_keyword mk WHER... | 1.659 | 1.775 | -0.070 | 1160.61 | 1160.57 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 17.133 | 16.948 | 0.011 | 1717.11 | 1717.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 18.977 | 16.924 | 0.108 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 18.525 | 15.784 | 0.148 | 1787.70 | 1787.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 3.117 | 3.789 | -0.216 | 406.87 | 406.87 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 8.655 | 6.848 | 0.209 | 888.36 | 888.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 2.961 | 2.506 | 0.154 | 333.97 | 333.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 4.533 | 6.268 | -0.383 | 686.66 | 686.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.169 | 2.001 | 0.077 | 360.59 | 360.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 12.435 | 9.649 | 0.224 | 1031.19 | 1031.19 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 10.092 | 9.148 | 0.094 | 977.66 | 977.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 7.976 | 8.701 | -0.091 | 863.76 | 863.76 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 5.021 | 4.888 | 0.026 | 448.70 | 448.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 22.688 | 22.415 | 0.012 | 1912.89 | 1912.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m... | 2.965 | 1.609 | 0.457 | 538.89 | 265.75 | 0.464 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 10.703 | 9.472 | 0.115 | 955.02 | 955.02 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 7.455 | 8.728 | -0.171 | 1130.22 | 1130.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 7.705 | 9.479 | -0.230 | 791.31 | 791.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.923 | 0.062 | 0.933 | 335.26 | 62.13 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND mi.info... | 4.737 | 5.646 | -0.192 | 395.10 | 395.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 0.841 | 1.080 | -0.284 | 549.83 | 388.80 | -0.037 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.649 | 0.072 | 0.889 | 224.43 | 68.23 | 0.600 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 6.059 | 6.245 | -0.031 | 623.84 | 623.84 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.438 | 1.236 | 0.140 | 191.50 | 191.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 3.921 | 2.994 | 0.236 | 330.80 | 330.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 6.908 | 6.683 | 0.033 | 1087.68 | 1087.68 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 11.946 | 13.248 | -0.109 | 1143.52 | 1143.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 2.981 | 2.917 | 0.021 | 336.26 | 336.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 5.355 | 4.893 | 0.086 | 539.47 | 539.47 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.986 | 2.346 | 0.214 | 408.50 | 408.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 16.295 | 15.273 | 0.063 | 1573.18 | 1573.18 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 22.447 | 21.310 | 0.051 | 2249.09 | 2249.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 6.338 | 5.483 | 0.135 | 562.65 | 562.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 2.561 | 2.123 | 0.171 | 301.35 | 301.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.039 | 0.955 | 0.081 | 197.08 | 197.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 5.048 | 4.482 | 0.112 | 462.86 | 462.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 4.140 | 3.878 | 0.063 | 629.39 | 629.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 1.140 | 1.278 | -0.121 | 509.74 | 509.74 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 2.845 | 2.641 | 0.072 | 453.87 | 453.87 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.724 | 1.945 | -0.128 | 308.35 | 308.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m... | 14.301 | 12.358 | 0.136 | 1329.22 | 1329.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 15.975 | 15.691 | 0.018 | 1565.42 | 1565.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 3.965 | 4.480 | -0.130 | 345.71 | 345.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 7.857 | 7.654 | 0.026 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 8.267 | 7.840 | 0.052 | 871.26 | 871.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 8.342 | 7.821 | 0.062 | 1115.04 | 1115.04 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 6.825 | 4.825 | 0.293 | 497.05 | 497.05 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 8.093 | 6.225 | 0.231 | 770.61 | 770.61 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 3.720 | 4.278 | -0.150 | 348.13 | 348.13 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 5.565 | 5.225 | 0.061 | 759.91 | 759.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 13.860 | 14.115 | -0.018 | 1374.35 | 1374.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 4.086 | 3.480 | 0.148 | 342.50 | 342.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 1.149 | 0.050 | 0.956 | 525.60 | 224.82 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 5.477 | 7.777 | -0.420 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 3.158 | 2.954 | 0.065 | 441.06 | 441.06 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.897 | 2.811 | 0.030 | 384.46 | 384.46 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 7.917 | 5.835 | 0.263 | 514.64 | 514.64 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 5.100 | 5.961 | -0.169 | 855.95 | 855.95 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 6.098 | 5.034 | 0.174 | 441.49 | 441.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 5.013 | 4.493 | 0.104 | 876.93 | 876.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 5.743 | 6.909 | -0.203 | 658.08 | 658.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 17.712 | 14.242 | 0.196 | 1569.69 | 1569.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 1.182 | 0.030 | 0.975 | 321.17 | 16.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 9.249 | 8.082 | 0.126 | 708.36 | 708.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 0.723 | 0.047 | 0.935 | 782.31 | 554.54 | 0.952 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 4.090 | 3.045 | 0.256 | 324.39 | 324.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 10.576 | 9.561 | 0.096 | 938.26 | 938.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 13.829 | 13.290 | 0.039 | 1311.83 | 1311.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 5.048 | 4.740 | 0.061 | 467.96 | 467.96 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 5.791 | 7.360 | -0.271 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 4.998 | 4.532 | 0.093 | 588.38 | 588.38 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.432 | 0.920 | 0.358 | 197.39 | 197.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 11.119 | 10.943 | 0.016 | 1291.89 | 1291.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 13.524 | 12.727 | 0.059 | 1271.45 | 1271.45 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 0.990 | 0.043 | 0.957 | 880.03 | 606.89 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 11.042 | 11.903 | -0.078 | 1114.83 | 1114.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 8.886 | 8.845 | 0.005 | 791.31 | 791.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 8.899 | 10.134 | -0.139 | 758.83 | 758.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 7.989 | 10.242 | -0.282 | 882.86 | 882.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 3.346 | 4.320 | -0.291 | 534.22 | 534.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx,movie_k... | 9.882 | 9.770 | 0.011 | 1036.00 | 1036.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 1.743 | 1.245 | 0.286 | 517.04 | 517.04 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 13.829 | 14.598 | -0.056 | 1331.73 | 1331.73 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 12.820 | 11.995 | 0.064 | 1147.83 | 1147.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 14.969 | 14.395 | 0.038 | 1474.42 | 1474.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.481 | 2.624 | 0.246 | 414.00 | 414.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 4.283 | 6.454 | -0.507 | 530.11 | 530.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.940 | 1.713 | 0.117 | 285.64 | 285.64 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.000 | 3.284 | -0.642 | 327.71 | 327.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 6.451 | 6.262 | 0.029 | 484.74 | 484.74 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 6.664 | 3.935 | 0.410 | 502.91 | 502.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.320 | 1.563 | 0.326 | 350.30 | 350.30 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 3.990 | 4.711 | -0.181 | 345.71 | 345.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM movie_companies mc,title t,movie_keyword mk WHERE t.id=m... | 3.828 | 2.408 | 0.371 | 526.69 | 253.55 | 0.490 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 9.083 | 9.076 | 0.001 | 878.25 | 878.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 10.677 | 10.546 | 0.012 | 919.06 | 919.06 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 4.194 | 2.961 | 0.294 | 452.36 | 452.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 19.791 | 22.121 | -0.118 | 1938.63 | 1938.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.413 | 3.056 | -0.266 | 317.31 | 317.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 4.001 | 4.015 | -0.003 | 435.77 | 435.77 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 5.518 | 6.953 | -0.260 | 494.49 | 494.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 2.022 | 1.971 | 0.025 | 266.03 | 266.03 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 2.125 | 2.487 | -0.170 | 226.59 | 226.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 13.390 | 23.385 | -0.746 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 6.460 | 10.019 | -0.551 | 593.58 | 593.58 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 20.374 | 26.987 | -0.325 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 6.057 | 4.790 | 0.209 | 880.42 | 880.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.600 | 1.728 | -0.080 | 270.41 | 270.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 12.758 | 12.417 | 0.027 | 1474.42 | 1474.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 4.402 | 5.141 | -0.168 | 664.32 | 664.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_id<7 | 7.953 | 7.872 | 0.010 | 689.94 | 689.94 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.190 | 1.578 | 0.279 | 348.73 | 348.73 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 1.135 | 0.041 | 0.964 | 423.70 | 119.52 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx... | 5.368 | 5.603 | -0.044 | 985.32 | 985.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.585 | 1.790 | -0.129 | 206.41 | 206.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 5.047 | 4.914 | 0.026 | 495.97 | 495.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 5.581 | 6.051 | -0.084 | 854.81 | 854.81 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 7.611 | 7.970 | -0.047 | 1186.89 | 1186.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 1.753 | 0.035 | 0.980 | 784.38 | 213.91 | 0.988 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 5.178 | 4.702 | 0.092 | 965.09 | 809.55 | -0.007 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 4.199 | 3.905 | 0.070 | 635.91 | 635.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 9.613 | 8.032 | 0.164 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword... | 0.916 | 0.917 | -0.001 | 1071.40 | 1071.40 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 6.462 | 5.593 | 0.134 | 512.66 | 512.66 | 0.000 | plan unchanged |

## Execution Plan Comparisons

For every query, the original and RL-selected plans are shown.
If the plan did not change, it is reported as 'Plan unchanged'.

### Query 0: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 1: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 2: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 3: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 4: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 5: SELECT COUNT(*) FROM movie_keyword mk,title t,cast_info ci WHERE t.id=mk.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 6: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 7: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 8: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 9: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 10: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
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
        Index Scan movie_keyword (mk) using rl_tmp_041cd4dd952f
    Index Only Scan title (t) using title_pkey
```

### Query 11: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 12: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 13: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 14: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 15: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH...
- **Action**: join_order=(((t JOIN mi) JOIN ci) JOIN mc); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 16: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 17: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 18: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 19: SELECT COUNT(*) FROM title t,movie_info mi,movie_companies mc WHERE t.id=mi.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 20: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 21: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
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
    Index Scan movie_keyword (mk) using rl_tmp_ec5ecafb41cb
    Index Only Scan title (t) using title_pkey
```

### Query 22: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 23: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 24: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 25: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 26: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 27: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 28: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 29: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
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
    Index Scan movie_keyword (mk) using rl_tmp_997945f2061a
    Index Only Scan title (t) using title_pkey
```

### Query 30: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=(t JOIN mc); join_method=merge; scan_method=indexscan; index=created:movie_companies(movie_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 31: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 32: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 33: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 34: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 35: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 36: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=((t JOIN ci) JOIN mi); join_method=merge; scan_method=indexscan; index=created:cast_info(person_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 37: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor...
- **Action**: join_order=(((t JOIN mk) JOIN mi_idx) JOIN mi); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 38: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mi) JOIN ci); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 39: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
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
      Bitmap Index Scan using rl_tmp_1d6f416839eb
    Index Scan title (t) using title_pkey
```

### Query 40: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 41: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 42: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 43: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 44: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 45: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 46: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword...
- **Action**: join_order=(((t JOIN mk) JOIN ci) JOIN mi_idx); join_method=nestloop; scan_method=seqscan; index=created:movie_keyword(movie_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 47: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 48: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=created:movie_info_idx(movie_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_info (mi)
    Hash
      Nested Loop
        Hash Join
          Seq Scan movie_keyword (mk)
          Hash
            Seq Scan movie_info_idx (mi_idx)
        Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_info (mi)
    Hash
      Nested Loop
        Nested Loop
          Seq Scan movie_keyword (mk)
          Index Only Scan movie_info_idx (mi_idx) using rl_tmp_8048cf5ef656
        Index Scan title (t) using title_pkey
```

### Query 49: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 50: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 51: SELECT COUNT(*) FROM cast_info ci,title t WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 52: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 53: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 54: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 55: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_companies (mc)
    Hash
      Nested Loop
        Seq Scan movie_keyword (mk)
        Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_companies (mc)
    Hash
      Nested Loop
        Bitmap Heap Scan movie_keyword (mk)
          Bitmap Index Scan using rl_tmp_5aefd1026e7a
        Index Only Scan title (t) using title_pkey
```

### Query 56: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 57: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 58: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 59: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 60: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_info_idx ...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mi) JOIN mc); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 61: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 62: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 63: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 64: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 65: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 66: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_companies(company_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info (mi)
      Hash
        Seq Scan movie_companies (mc)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_info (mi)
      Hash
        Index Scan movie_companies (mc) using rl_tmp_dedea2b422ab
    Index Only Scan title (t) using title_pkey
```

### Query 67: SELECT COUNT(*) FROM cast_info ci,title t,movie_companies mc WHERE t.id=ci.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 68: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 69: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=(t JOIN mc); join_method=merge; scan_method=indexscan; index=created:movie_companies(movie_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 70: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 71: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 72: SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc,movie_info m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=created:movie_companies(movie_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_info (mi)
    Hash
      Nested Loop
        Hash Join
          Seq Scan movie_keyword (mk)
          Hash
            Seq Scan movie_companies (mc)
        Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_info (mi)
    Hash
      Nested Loop
        Nested Loop
          Seq Scan movie_keyword (mk)
          Index Scan title (t) using title_pkey
        Index Scan movie_companies (mc) using rl_tmp_893d0f20808b
```

### Query 73: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 74: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 75: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 76: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=((ci JOIN t) JOIN mk); join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 77: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 78: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 79: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_keyword mk...
- **Action**: join_order=(((t JOIN mk) JOIN mc) JOIN ci); join_method=hash; scan_method=seqscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Hash Join
        Seq Scan movie_companies (mc)
        Hash
          Nested Loop
            Seq Scan movie_keyword (mk)
            Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Hash Join
        Seq Scan movie_companies (mc)
        Hash
          Nested Loop
            Bitmap Heap Scan movie_keyword (mk)
              Bitmap Index Scan using rl_tmp_ae30d108212a
            Index Only Scan title (t) using title_pkey
```

### Query 80: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 81: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 82: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 83: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 84: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 85: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 86: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 87: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 88: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 89: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 90: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 91: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 92: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 93: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_keyword mk WHER...
- **Action**: join_order=(((t JOIN mk) JOIN ci) JOIN mi); join_method=hash; scan_method=seqscan; index=created:cast_info(person_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 94: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 95: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 96: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 97: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 98: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 99: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 100: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 101: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 102: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 103: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 104: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 105: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 106: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH...
- **Action**: join_order=(((t JOIN mi) JOIN ci) JOIN mc); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 107: SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_companies (mc)
    Hash
      Nested Loop
        Seq Scan movie_keyword (mk)
        Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_companies (mc)
    Hash
      Nested Loop
        Bitmap Heap Scan movie_keyword (mk)
          Bitmap Index Scan using rl_tmp_e9165ced1152
        Index Only Scan title (t) using title_pkey
```

### Query 108: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 109: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 110: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 111: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
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
    Bitmap Heap Scan movie_keyword (mk)
      Bitmap Index Scan using rl_tmp_659cf91aa1c6
    Index Only Scan title (t) using title_pkey
```

### Query 112: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND mi.info...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 113: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_info(info_type_id)
- **Outcome**: unchanged

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
      Bitmap Heap Scan movie_info (mi)
        Bitmap Index Scan using rl_tmp_a299d0ca21a7
      Hash
        Seq Scan movie_keyword (mk)
    Index Only Scan title (t) using title_pkey
```

### Query 114: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:movie_companies(company_id)
- **Outcome**: improved

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
      Bitmap Index Scan using rl_tmp_85417634b9e6
    Index Scan title (t) using title_pkey
```

### Query 115: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 116: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 117: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 118: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=((t JOIN ci) JOIN mi); join_method=nestloop; scan_method=seqscan; index=created:movie_info(movie_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 119: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 120: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 121: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 122: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 123: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 124: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 125: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 126: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 127: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 128: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 129: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 130: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=merge; scan_method=indexscan; index=created:title(kind_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 131: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 132: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 133: SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 134: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 135: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 136: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 137: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 138: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 139: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 140: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 141: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 142: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 143: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 144: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 145: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=((t JOIN mc) JOIN mk); join_method=merge; scan_method=indexscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_companies (mc)
      Hash
        Seq Scan movie_keyword (mk)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan movie_companies (mc)
      Hash
        Index Scan movie_keyword (mk) using rl_tmp_b626a1654dd9
    Index Only Scan title (t) using title_pkey
```

### Query 146: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 147: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 148: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 149: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 150: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 151: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 152: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 153: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 154: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 155: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
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
    Index Scan movie_keyword (mk) using rl_tmp_4ce4ee643e49
    Index Scan title (t) using title_pkey
```

### Query 156: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 157: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=((t JOIN ci) JOIN mi); join_method=merge; scan_method=indexscan; index=created:movie_info(info_type_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan cast_info (ci)
      Hash
        Seq Scan movie_info (mi)
    Index Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Hash Join
      Seq Scan cast_info (ci)
      Hash
        Index Scan movie_info (mi) using rl_tmp_18470120f669
    Index Scan title (t) using title_pkey
```

### Query 158: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 159: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 160: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 161: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 162: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 163: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 164: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 165: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 166: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 167: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
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
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Bitmap Heap Scan movie_keyword (mk)
          Bitmap Index Scan using rl_tmp_7dab1d5dbff1
        Index Only Scan title (t) using title_pkey
```

### Query 168: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 169: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 170: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 171: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 172: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 173: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx,movie_k...
- **Action**: join_order=(((t JOIN mk) JOIN mi_idx) JOIN mc); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 174: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_companies(company_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 175: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 176: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 177: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 178: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 179: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 180: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 181: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 182: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 183: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 184: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 185: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 186: SELECT COUNT(*) FROM movie_companies mc,title t,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_keyword(keyword_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_companies (mc)
    Hash
      Nested Loop
        Seq Scan movie_keyword (mk)
        Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan movie_companies (mc)
    Hash
      Nested Loop
        Bitmap Heap Scan movie_keyword (mk)
          Bitmap Index Scan using rl_tmp_980efedcdbd1
        Index Only Scan title (t) using title_pkey
```

### Query 187: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 188: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 189: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 190: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 191: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 192: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 193: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 194: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 195: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 196: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 197: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 198: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 199: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 200: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 201: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 202: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 203: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_id<7
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 204: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 205: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
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
        Index Scan movie_keyword (mk) using rl_tmp_f3730d931880
    Index Only Scan title (t) using title_pkey
```

### Query 206: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mi) JOIN ci); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 207: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 208: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 209: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 210: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 211: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=((t JOIN mc) JOIN ci); join_method=merge; scan_method=indexscan; index=created:cast_info(person_id)
- **Outcome**: improved

**Original plan:**
```
Aggregate
  Nested Loop
    Nested Loop
      Seq Scan cast_info (ci)
      Seq Scan movie_companies (mc)
    Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Nested Loop
    Nested Loop
      Index Scan cast_info (ci) using rl_tmp_157e13470abe
      Seq Scan movie_companies (mc)
    Index Only Scan title (t) using title_pkey
```

### Query 212: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH...
- **Action**: join_order=(((t JOIN mi) JOIN mc) JOIN ci); join_method=hash; scan_method=seqscan; index=created:movie_info(info_type_id)
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
        Index Only Scan title (t) using title_pkey
```

**RL-selected plan:**
```
Aggregate
  Hash Join
    Seq Scan cast_info (ci)
    Hash
      Nested Loop
        Hash Join
          Bitmap Heap Scan movie_info (mi)
            Bitmap Index Scan using rl_tmp_78f7ef1a14b0
          Hash
            Seq Scan movie_companies (mc)
        Index Only Scan title (t) using title_pkey
```

### Query 213: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 214: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 215: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword...
- **Action**: join_order=(((t JOIN mk) JOIN mi_idx) JOIN ci); join_method=hash; scan_method=indexscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 216: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

## Aggregates (all queries, including failures and regressions)

- **Queries evaluated**: 217
- Mean baseline time (ms): 6.837
- Median baseline time (ms): 5.178
- Mean RL time (ms): 6.638
- Median RL time (ms): 5.183
- Mean time improvement: 0.0648
- Median time improvement: 0.0517
- Mean cost improvement: 0.053
- **Percent improved**: 8.8%
- Percent unchanged (incl. plan unchanged): 91.2%
- Percent plan unchanged: 90.3%
- **Percent degraded**: 0.0%
- Percent failed: 0.0%
- Mean planning overhead (ms): 0.011
- Median planning overhead (ms): 0.016
- Outcome counts: {'plan unchanged': 196, 'improved': 19, 'unchanged': 2}

# PostgreSQL RL Optimizer Evaluation Report

Improvements are claimed only when measured execution time improved
and the EXPLAIN plan actually changed. `plan unchanged` is reported
when the selected action did not change PostgreSQL's operator tree.

## Per-query Results

| Query | Baseline Time | RL Time | Time Improvement | Baseline Cost | RL Cost | Buffer Improvement | Outcome |
| ----- | ------------- | ------- | ---------------- | ------------- | ------- | ------------------ | ------- |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 4.919 | 5.796 | -0.178 | 601.89 | 601.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 16.873 | 18.283 | -0.084 | 1768.77 | 1768.77 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 19.170 | 21.262 | -0.109 | 1954.44 | 1954.44 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 8.482 | 10.963 | -0.293 | 1148.16 | 1148.16 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 9.833 | 7.368 | 0.251 | 1015.89 | 1015.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM movie_keyword mk,title t,cast_info ci WHERE t.id=mk.movi... | 14.967 | 14.495 | 0.032 | 1488.72 | 1488.72 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 5.019 | 5.758 | -0.147 | 469.82 | 469.82 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 11.740 | 11.725 | 0.001 | 1021.90 | 1021.90 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 16.229 | 16.936 | -0.044 | 1573.78 | 1573.78 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.081 | 0.932 | 0.138 | 194.86 | 194.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 1.234 | 1.215 | 0.015 | 423.70 | 423.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 4.360 | 5.031 | -0.154 | 712.26 | 712.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 3.877 | 4.024 | -0.038 | 530.34 | 530.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 19.067 | 18.609 | 0.024 | 1531.65 | 1531.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 4.556 | 4.756 | -0.044 | 842.27 | 842.27 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 7.638 | 8.678 | -0.136 | 1056.07 | 1056.07 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 32.987 | 29.070 | 0.119 | 2907.99 | 2907.99 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 2.991 | 5.169 | -0.728 | 493.69 | 493.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 9.103 | 7.095 | 0.221 | 893.70 | 893.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_companies mc WHERE t.id=mi.m... | 4.100 | 4.863 | -0.186 | 585.34 | 585.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 13.994 | 15.856 | -0.133 | 1374.35 | 1374.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 1.724 | 0.035 | 0.980 | 313.16 | 12.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 5.000 | 4.161 | 0.168 | 546.25 | 546.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.781 | 2.160 | -0.213 | 300.26 | 300.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 6.497 | 6.764 | -0.041 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 4.515 | 3.820 | 0.154 | 338.45 | 338.45 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 5.588 | 4.369 | 0.218 | 398.93 | 398.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 11.175 | 11.159 | 0.001 | 980.85 | 980.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 4.186 | 4.920 | -0.175 | 660.10 | 660.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.988 | 0.028 | 0.972 | 313.16 | 12.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.754 | 0.223 | 0.704 | 270.23 | 128.27 | 0.019 | improved |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.966 | 2.400 | -0.221 | 234.51 | 234.51 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 5.699 | 6.028 | -0.058 | 555.21 | 555.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 0.359 | 0.473 | -0.318 | 1111.63 | 1111.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 9.885 | 10.706 | -0.083 | 1226.42 | 1226.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 13.856 | 13.104 | 0.054 | 1238.80 | 1238.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 0.874 | 0.801 | 0.084 | 852.10 | 852.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 19.820 | 14.955 | 0.245 | 1562.08 | 1562.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx... | 9.123 | 8.344 | 0.085 | 1212.49 | 1212.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 1.034 | 1.020 | 0.014 | 367.28 | 367.28 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 4.112 | 6.031 | -0.467 | 467.99 | 467.99 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 12.013 | 10.709 | 0.109 | 1152.31 | 1152.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 28.553 | 22.380 | 0.216 | 2320.53 | 2320.53 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 7.545 | 7.607 | -0.008 | 1002.16 | 1002.16 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 6.211 | 4.993 | 0.196 | 591.40 | 591.40 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 5.718 | 5.565 | 0.027 | 755.85 | 755.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword... | 1.154 | 1.370 | -0.187 | 1037.66 | 1037.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 11.030 | 10.288 | 0.067 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 4.034 | 4.913 | -0.218 | 726.75 | 726.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 4.941 | 3.066 | 0.379 | 461.50 | 461.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 4.532 | 5.485 | -0.210 | 579.57 | 579.57 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM cast_info ci,title t WHERE t.id=ci.movie_id AND t.produc... | 6.706 | 6.357 | 0.052 | 622.65 | 622.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 7.036 | 8.395 | -0.193 | 774.21 | 774.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 5.397 | 4.539 | 0.159 | 653.92 | 653.92 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 3.821 | 4.496 | -0.177 | 353.37 | 353.37 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 1.647 | 1.386 | 0.158 | 526.69 | 526.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 8.343 | 7.442 | 0.108 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 4.942 | 5.315 | -0.075 | 457.41 | 457.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 6.433 | 5.761 | 0.104 | 477.54 | 477.54 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 7.798 | 6.668 | 0.145 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_info_idx ... | 6.625 | 6.223 | 0.061 | 762.09 | 762.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 5.936 | 6.856 | -0.155 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 18.282 | 18.037 | 0.013 | 1407.52 | 1407.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 18.710 | 18.738 | -0.001 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 3.711 | 3.914 | -0.055 | 342.42 | 342.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 8.800 | 9.672 | -0.099 | 920.49 | 920.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 0.770 | 0.797 | -0.035 | 468.03 | 468.03 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM cast_info ci,title t,movie_companies mc WHERE t.id=ci.mo... | 6.722 | 4.247 | 0.368 | 831.10 | 831.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 3.408 | 5.873 | -0.723 | 527.93 | 527.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.696 | 0.155 | 0.777 | 268.43 | 127.49 | 0.107 | improved |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.131 | 2.402 | -0.127 | 335.63 | 335.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 4.142 | 2.582 | 0.377 | 512.22 | 512.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc,movie_info m... | 4.634 | 4.587 | 0.010 | 825.26 | 825.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 6.154 | 6.006 | 0.024 | 522.66 | 522.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 2.845 | 2.722 | 0.043 | 447.32 | 447.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 10.202 | 10.378 | -0.017 | 1083.11 | 1083.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 30.418 | 35.562 | -0.169 | 2863.28 | 2863.28 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 12.303 | 10.796 | 0.122 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.993 | 1.037 | -0.044 | 194.59 | 194.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_keyword mk... | 4.931 | 4.892 | 0.008 | 1048.90 | 1048.90 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 0.271 | 0.249 | 0.081 | 700.79 | 700.79 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 0.450 | 0.434 | 0.036 | 439.82 | 439.82 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.415 | 0.572 | -0.378 | 528.86 | 528.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 9.761 | 13.532 | -0.386 | 764.52 | 764.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 9.953 | 10.923 | -0.097 | 1026.14 | 1026.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 4.643 | 5.307 | -0.143 | 850.46 | 850.46 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 7.392 | 7.653 | -0.035 | 709.30 | 709.30 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.914 | 4.432 | -0.132 | 437.34 | 437.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 3.054 | 3.300 | -0.081 | 328.39 | 328.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 7.156 | 8.012 | -0.120 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 3.027 | 2.558 | 0.155 | 315.10 | 315.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 8.426 | 7.712 | 0.085 | 808.96 | 808.96 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 3.819 | 3.026 | 0.208 | 628.32 | 628.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_keyword mk WHER... | 1.726 | 2.055 | -0.191 | 1160.61 | 1160.61 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 18.322 | 17.750 | 0.031 | 1717.11 | 1717.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 17.646 | 19.090 | -0.082 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 15.629 | 15.293 | 0.021 | 1787.70 | 1787.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 3.172 | 3.269 | -0.031 | 406.87 | 406.87 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 10.728 | 7.802 | 0.273 | 888.36 | 888.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 2.812 | 2.834 | -0.008 | 333.97 | 333.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 6.194 | 7.245 | -0.170 | 686.66 | 686.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.688 | 2.477 | -0.467 | 360.59 | 360.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 11.197 | 10.329 | 0.078 | 1031.19 | 1031.19 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 10.292 | 10.189 | 0.010 | 977.66 | 977.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 10.128 | 9.898 | 0.023 | 863.76 | 863.76 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 5.242 | 3.629 | 0.308 | 448.70 | 448.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 16.656 | 16.214 | 0.027 | 1912.89 | 1912.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m... | 2.389 | 2.274 | 0.048 | 538.89 | 538.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 10.414 | 10.102 | 0.030 | 955.02 | 955.02 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 6.785 | 8.345 | -0.230 | 1130.22 | 1130.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 7.537 | 8.058 | -0.069 | 791.31 | 791.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.812 | 0.041 | 0.950 | 335.26 | 62.13 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND mi.info... | 4.695 | 3.977 | 0.153 | 395.10 | 395.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 1.066 | 1.063 | 0.003 | 549.83 | 549.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.599 | 0.666 | -0.112 | 224.43 | 224.43 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 7.113 | 7.144 | -0.004 | 623.84 | 623.84 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.520 | 1.055 | 0.306 | 191.50 | 191.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 4.048 | 3.596 | 0.112 | 330.80 | 330.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 7.187 | 6.307 | 0.122 | 1087.68 | 1087.68 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 11.448 | 12.729 | -0.112 | 1143.52 | 1143.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 2.690 | 2.458 | 0.086 | 336.26 | 336.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 4.788 | 4.815 | -0.006 | 539.47 | 539.47 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.729 | 2.618 | 0.041 | 408.50 | 408.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 14.680 | 16.797 | -0.144 | 1573.18 | 1573.18 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 30.236 | 21.895 | 0.276 | 2249.09 | 2249.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 4.977 | 4.933 | 0.009 | 562.65 | 562.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 3.070 | 2.078 | 0.323 | 301.35 | 301.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.986 | 0.805 | 0.184 | 197.08 | 197.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 5.656 | 4.949 | 0.125 | 462.86 | 462.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 4.393 | 4.299 | 0.021 | 629.39 | 629.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 1.796 | 1.416 | 0.212 | 509.74 | 509.74 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 3.427 | 2.105 | 0.386 | 453.87 | 453.87 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.707 | 1.113 | 0.348 | 308.35 | 308.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m... | 13.377 | 14.499 | -0.084 | 1329.22 | 1329.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 17.125 | 16.073 | 0.061 | 1565.42 | 1565.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 5.015 | 5.365 | -0.070 | 345.71 | 345.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 7.618 | 7.906 | -0.038 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 10.208 | 8.501 | 0.167 | 871.26 | 871.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 6.766 | 7.769 | -0.148 | 1115.04 | 1115.04 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 4.917 | 5.797 | -0.179 | 497.05 | 497.05 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 8.383 | 8.207 | 0.021 | 770.61 | 770.61 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 4.715 | 3.966 | 0.159 | 348.13 | 348.13 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 5.363 | 7.342 | -0.369 | 759.91 | 759.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 15.120 | 15.487 | -0.024 | 1374.35 | 1374.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 5.185 | 5.705 | -0.100 | 342.50 | 342.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 1.217 | 1.419 | -0.166 | 525.60 | 525.60 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 5.533 | 6.018 | -0.088 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 3.007 | 2.951 | 0.019 | 441.06 | 441.06 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.681 | 2.610 | 0.026 | 384.46 | 384.46 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 5.878 | 5.994 | -0.020 | 514.64 | 514.64 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 6.361 | 5.722 | 0.100 | 855.95 | 855.95 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 5.137 | 3.251 | 0.367 | 441.49 | 441.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 4.012 | 6.049 | -0.508 | 876.93 | 876.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 7.111 | 5.536 | 0.221 | 658.08 | 658.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 14.683 | 14.087 | 0.041 | 1569.69 | 1569.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 0.898 | 1.283 | -0.429 | 321.17 | 321.17 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 9.674 | 8.361 | 0.136 | 708.36 | 708.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 1.110 | 0.830 | 0.252 | 782.31 | 782.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 3.585 | 2.816 | 0.215 | 324.39 | 324.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 9.708 | 11.545 | -0.189 | 938.26 | 938.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 16.362 | 13.322 | 0.186 | 1311.83 | 1311.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 4.370 | 4.417 | -0.011 | 467.96 | 467.96 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 6.609 | 6.601 | 0.001 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 4.730 | 4.912 | -0.038 | 588.38 | 588.38 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.130 | 1.327 | -0.174 | 197.39 | 197.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 10.737 | 10.433 | 0.028 | 1291.89 | 1291.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 14.077 | 13.226 | 0.060 | 1271.45 | 1271.45 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 2.115 | 1.117 | 0.472 | 880.03 | 880.03 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 10.806 | 13.897 | -0.286 | 1114.83 | 1114.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 8.963 | 8.984 | -0.002 | 791.31 | 791.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 9.040 | 12.073 | -0.336 | 758.83 | 758.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 12.200 | 9.270 | 0.240 | 882.86 | 882.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 4.461 | 3.911 | 0.123 | 534.22 | 534.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx,movie_k... | 9.109 | 7.937 | 0.129 | 1036.00 | 1036.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 2.069 | 1.551 | 0.250 | 517.04 | 517.04 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 12.858 | 13.102 | -0.019 | 1331.73 | 1331.73 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 9.757 | 10.603 | -0.087 | 1147.83 | 1147.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 13.364 | 13.123 | 0.018 | 1474.42 | 1474.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.925 | 2.913 | 0.004 | 414.00 | 414.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 5.455 | 4.712 | 0.136 | 530.11 | 530.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.673 | 2.697 | -0.612 | 285.64 | 285.64 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.574 | 2.040 | -0.296 | 327.71 | 327.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 4.763 | 5.144 | -0.080 | 484.74 | 484.74 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 4.655 | 5.962 | -0.281 | 502.91 | 502.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.711 | 1.856 | -0.085 | 350.30 | 350.30 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 4.547 | 3.325 | 0.269 | 345.71 | 345.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM movie_companies mc,title t,movie_keyword mk WHERE t.id=m... | 2.430 | 2.664 | -0.096 | 526.69 | 526.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 8.317 | 8.921 | -0.073 | 878.25 | 878.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 8.772 | 10.905 | -0.243 | 919.06 | 919.06 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 3.678 | 3.152 | 0.143 | 452.36 | 452.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 17.830 | 20.904 | -0.172 | 1938.63 | 1938.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.679 | 2.442 | 0.088 | 317.31 | 317.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 4.561 | 4.163 | 0.087 | 435.77 | 435.77 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 6.698 | 6.548 | 0.022 | 494.49 | 494.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.941 | 1.796 | 0.075 | 266.03 | 266.03 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.732 | 3.025 | -0.747 | 226.59 | 226.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 9.880 | 11.466 | -0.161 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 4.703 | 4.685 | 0.004 | 593.58 | 593.58 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 17.223 | 24.672 | -0.433 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 4.655 | 4.797 | -0.031 | 880.42 | 880.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.557 | 1.437 | 0.077 | 270.41 | 270.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 13.778 | 17.104 | -0.241 | 1474.42 | 1474.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 4.504 | 6.084 | -0.351 | 664.32 | 664.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_id<7 | 8.797 | 8.939 | -0.016 | 689.94 | 689.94 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.530 | 1.644 | -0.075 | 348.73 | 348.73 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 1.791 | 1.280 | 0.285 | 423.70 | 423.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx... | 6.551 | 7.834 | -0.196 | 985.32 | 985.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 2.307 | 1.888 | 0.182 | 206.41 | 206.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 4.669 | 5.219 | -0.118 | 495.97 | 495.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 5.966 | 7.720 | -0.294 | 854.81 | 854.81 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 11.886 | 8.209 | 0.309 | 1186.89 | 1186.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 1.589 | 1.041 | 0.345 | 784.38 | 295.45 | -0.531 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 5.647 | 7.468 | -0.322 | 965.09 | 965.06 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 4.952 | 5.535 | -0.118 | 635.91 | 635.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 8.882 | 10.926 | -0.230 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword... | 1.075 | 1.166 | -0.085 | 1071.40 | 1071.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 5.932 | 8.811 | -0.485 | 512.66 | 512.66 | 0.000 | plan unchanged |

## Execution Plan Comparisons

For every query, the original and RL-selected plans are shown.
If the plan did not change, it is reported as 'Plan unchanged'.

### Query 0: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 1: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 2: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 3: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 4: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 5: SELECT COUNT(*) FROM movie_keyword mk,title t,cast_info ci WHERE t.id=mk.movi...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 6: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 7: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 8: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 9: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 10: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 11: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 12: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 13: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 14: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 15: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH...
- **Action**: join_order=(((t JOIN mi) JOIN ci) JOIN mc); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 16: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 17: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 18: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 19: SELECT COUNT(*) FROM title t,movie_info mi,movie_companies mc WHERE t.id=mi.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 20: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 21: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_keyword(keyword_id)
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
    Index Scan movie_keyword (mk) using rl_tmp_206545bce94c
    Index Only Scan title (t) using title_pkey
```

### Query 22: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 23: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 24: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 25: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 26: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 27: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 28: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 29: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_keyword(keyword_id)
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
    Index Scan movie_keyword (mk) using rl_tmp_dbe7b882ec78
    Index Only Scan title (t) using title_pkey
```

### Query 30: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=default; index=created:movie_companies(company_id)
- **Outcome**: improved

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
      Bitmap Index Scan using rl_tmp_330ffcac55bb
    Index Only Scan title (t) using title_pkey
```

### Query 31: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 32: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 33: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 34: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 35: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 36: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 37: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor...
- **Action**: join_order=(((t JOIN mk) JOIN mi_idx) JOIN mi); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 38: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mi) JOIN ci); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 39: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=nestloop; scan_method=indexscan; index=created:title(production_year)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 40: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 41: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 42: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 43: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 44: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 45: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 46: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword...
- **Action**: join_order=(((t JOIN mk) JOIN ci) JOIN mi_idx); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 47: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 48: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor...
- **Action**: join_order=(((t JOIN mk) JOIN mi) JOIN mi_idx); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 49: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 50: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 51: SELECT COUNT(*) FROM cast_info ci,title t WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 52: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 53: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 54: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 55: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 56: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 57: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 58: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 59: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 60: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_info_idx ...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mi) JOIN mc); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 61: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 62: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 63: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 64: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 65: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 66: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 67: SELECT COUNT(*) FROM cast_info ci,title t,movie_companies mc WHERE t.id=ci.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 68: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 69: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_companies(company_id)
- **Outcome**: improved

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
      Bitmap Index Scan using rl_tmp_cab1b9ea4d11
    Index Only Scan title (t) using title_pkey
```

### Query 70: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 71: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 72: SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc,movie_info m...
- **Action**: join_order=(((t JOIN mi) JOIN mc) JOIN mk); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 73: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 74: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 75: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 76: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 77: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 78: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 79: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_keyword mk...
- **Action**: join_order=(((t JOIN mk) JOIN mc) JOIN ci); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 80: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 81: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 82: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 83: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 84: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 85: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 86: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 87: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 88: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 89: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 90: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 91: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 92: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 93: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_keyword mk WHER...
- **Action**: join_order=(((t JOIN mk) JOIN mi) JOIN ci); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 94: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 95: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 96: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 97: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 98: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 99: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 100: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 101: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 102: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 103: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 104: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 105: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 106: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH...
- **Action**: join_order=(((t JOIN mi) JOIN ci) JOIN mc); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 107: SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 108: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 109: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 110: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 111: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=nestloop; scan_method=seqscan; index=created:movie_keyword(keyword_id)
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
      Bitmap Index Scan using rl_tmp_deb6c59cd147
    Index Only Scan title (t) using title_pkey
```

### Query 112: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND mi.info...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 113: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 114: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=nestloop; scan_method=indexscan; index=created:title(production_year)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 115: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 116: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 117: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 118: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 119: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 120: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 121: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 122: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 123: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 124: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 125: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 126: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 127: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 128: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 129: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 130: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 131: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 132: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 133: SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 134: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 135: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 136: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 137: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 138: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 139: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 140: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 141: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 142: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 143: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 144: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 145: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 146: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 147: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 148: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 149: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 150: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 151: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 152: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 153: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 154: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 155: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki...
- **Action**: join_order=original; join_method=nestloop; scan_method=indexscan; index=created:title(kind_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 156: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 157: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 158: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 159: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 160: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 161: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 162: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 163: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 164: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 165: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 166: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 167: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 168: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 169: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 170: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 171: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 172: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 173: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx,movie_k...
- **Action**: join_order=(((t JOIN mk) JOIN mi_idx) JOIN mc); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 174: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 175: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 176: SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 177: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 178: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 179: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 180: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 181: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 182: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 183: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 184: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 185: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 186: SELECT COUNT(*) FROM movie_companies mc,title t,movie_keyword mk WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=created:movie_keyword(movie_id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 187: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 188: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 189: SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 190: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 191: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 192: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 193: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 194: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 195: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 196: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 197: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 198: SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 199: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 200: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 201: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 202: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 203: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_id<7
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 204: SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 205: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 206: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx...
- **Action**: join_order=(((t JOIN mi_idx) JOIN mi) JOIN ci); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 207: SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 208: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 209: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 210: SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 211: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=created:cast_info(movie_id)
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
      Seq Scan movie_companies (mc)
      Index Only Scan title (t) using title_pkey
    Index Scan cast_info (ci) using rl_tmp_783d1948a44a
```

### Query 212: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH...
- **Action**: join_order=(((t JOIN mi) JOIN mc) JOIN ci); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 213: SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m...
- **Action**: join_order=original; join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 214: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 215: SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword...
- **Action**: join_order=(((t JOIN mk) JOIN ci) JOIN mi_idx); join_method=default; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 216: SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k...
- **Action**: join_order=original; join_method=hash; scan_method=indexscan; index=existing:title(id)
- **Outcome**: plan unchanged
- **Plan**: unchanged

## Aggregates (all queries, including failures and regressions)

- **Queries evaluated**: 217
- Mean baseline time (ms): 6.926
- Median baseline time (ms): 5.185
- Mean RL time (ms): 6.954
- Median RL time (ms): 5.565
- Mean time improvement: -0.0007
- Median time improvement: 0.0014
- Mean cost improvement: 0.0203
- **Percent improved**: 2.8%
- Percent unchanged (incl. plan unchanged): 97.2%
- Percent plan unchanged: 97.2%
- **Percent degraded**: 0.0%
- Percent failed: 0.0%
- Mean planning overhead (ms): 0.022
- Median planning overhead (ms): 0.026
- Outcome counts: {'plan unchanged': 211, 'improved': 6}

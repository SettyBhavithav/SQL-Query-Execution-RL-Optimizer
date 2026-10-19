# PostgreSQL RL Optimizer Evaluation Report

Improvements are claimed only when measured execution time improved
and the EXPLAIN plan actually changed. `plan unchanged` is reported
when the selected action did not change PostgreSQL's operator tree.

## Per-query Results

| Query | Baseline Time | RL Time | Time Improvement | Baseline Cost | RL Cost | Buffer Improvement | Outcome |
| ----- | ------------- | ------- | ---------------- | ------------- | ------- | ------------------ | ------- |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 2.679 | 3.037 | -0.134 | 601.89 | 601.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 12.103 | 13.481 | -0.114 | 1768.77 | 1768.77 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 11.943 | 16.483 | -0.380 | 1954.44 | 1954.44 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 4.604 | 4.561 | 0.009 | 1148.16 | 1148.16 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 4.038 | 4.236 | -0.049 | 1015.89 | 1015.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM movie_keyword mk,title t,cast_info ci WHERE t.id=mk.movi... | 8.468 | 8.465 | 0.000 | 1488.72 | 1488.72 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.962 | 2.811 | 0.291 | 469.82 | 469.82 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 8.488 | 8.489 | -0.000 | 1021.90 | 1021.90 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 10.636 | 10.208 | 0.040 | 1573.78 | 1573.78 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.563 | 0.506 | 0.101 | 194.86 | 194.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.605 | 0.021 | 0.965 | 423.70 | 119.52 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 2.138 | 2.144 | -0.003 | 712.26 | 712.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.601 | 2.496 | 0.040 | 530.34 | 530.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 11.841 | 8.640 | 0.270 | 1531.65 | 1531.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 2.346 | 2.414 | -0.029 | 842.27 | 842.27 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 4.108 | 4.057 | 0.012 | 1056.07 | 1056.07 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 17.588 | 18.176 | -0.033 | 2907.99 | 2907.99 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 2.041 | 2.051 | -0.005 | 493.69 | 493.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 4.531 | 4.366 | 0.036 | 893.70 | 893.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_companies mc WHERE t.id=mi.m... | 2.525 | 2.618 | -0.037 | 585.34 | 585.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 11.598 | 8.777 | 0.243 | 1374.35 | 1374.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.552 | 0.018 | 0.967 | 313.16 | 12.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.882 | 2.881 | 0.000 | 546.25 | 546.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.927 | 0.976 | -0.053 | 300.26 | 300.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.860 | 3.776 | 0.022 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.961 | 1.918 | 0.022 | 338.45 | 338.45 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.427 | 2.682 | -0.105 | 398.93 | 398.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 5.889 | 5.884 | 0.001 | 980.85 | 980.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 2.336 | 2.663 | -0.140 | 660.10 | 660.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.561 | 0.014 | 0.975 | 313.16 | 12.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.415 | 0.395 | 0.048 | 270.23 | 270.23 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.060 | 1.010 | 0.047 | 234.51 | 234.51 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 2.684 | 2.829 | -0.054 | 555.21 | 555.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 0.170 | 0.158 | 0.071 | 1111.63 | 1111.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 6.689 | 6.422 | 0.040 | 1226.42 | 1226.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 7.281 | 7.552 | -0.037 | 1238.80 | 1238.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 0.494 | 0.499 | -0.010 | 852.10 | 852.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 8.836 | 8.848 | -0.001 | 1562.08 | 1562.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx... | 6.761 | 4.682 | 0.307 | 1212.49 | 1212.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 0.619 | 0.044 | 0.929 | 367.28 | 94.14 | 0.636 | improved |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.214 | 2.629 | 0.182 | 467.99 | 467.99 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 5.468 | 5.483 | -0.003 | 1152.31 | 1152.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 14.259 | 15.661 | -0.098 | 2320.53 | 2320.53 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 3.853 | 3.678 | 0.045 | 1002.16 | 1002.16 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 3.140 | 3.270 | -0.041 | 591.40 | 591.40 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 4.910 | 3.582 | 0.270 | 755.85 | 755.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword... | 0.596 | 0.617 | -0.035 | 1037.66 | 1037.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 5.589 | 5.662 | -0.013 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 2.489 | 1.820 | 0.269 | 726.75 | 597.86 | -0.008 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 1.999 | 2.009 | -0.005 | 461.50 | 461.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 2.481 | 2.354 | 0.051 | 579.57 | 579.57 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM cast_info ci,title t WHERE t.id=ci.movie_id AND t.produc... | 3.314 | 3.140 | 0.053 | 622.65 | 622.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 3.536 | 3.626 | -0.025 | 774.21 | 774.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 2.229 | 2.315 | -0.039 | 653.92 | 653.92 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.968 | 2.766 | -0.405 | 353.37 | 353.37 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 0.615 | 0.029 | 0.953 | 526.69 | 253.55 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.774 | 3.935 | -0.043 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.522 | 3.663 | -0.452 | 457.41 | 457.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 2.805 | 3.866 | -0.378 | 477.54 | 477.54 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.736 | 3.830 | -0.025 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_info_idx ... | 4.922 | 4.782 | 0.028 | 762.09 | 762.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 4.586 | 3.907 | 0.148 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 10.053 | 8.240 | 0.180 | 1407.52 | 1407.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 13.011 | 11.025 | 0.153 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.499 | 2.343 | 0.062 | 342.42 | 342.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 5.354 | 4.923 | 0.081 | 920.49 | 920.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 0.500 | 0.030 | 0.940 | 468.03 | 297.73 | 0.945 | unchanged |
| SELECT COUNT(*) FROM cast_info ci,title t,movie_companies mc WHERE t.id=ci.mo... | 2.810 | 2.978 | -0.060 | 831.10 | 831.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 2.544 | 2.536 | 0.003 | 527.93 | 527.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.370 | 0.375 | -0.014 | 268.43 | 268.43 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.070 | 1.194 | -0.116 | 335.63 | 335.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 1.727 | 1.745 | -0.010 | 512.22 | 512.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc,movie_info m... | 3.046 | 1.917 | 0.371 | 825.26 | 625.06 | 0.183 | improved |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 4.049 | 3.841 | 0.051 | 522.66 | 522.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 1.660 | 1.702 | -0.025 | 447.32 | 447.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 6.080 | 6.507 | -0.070 | 1083.11 | 1083.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 20.850 | 17.834 | 0.145 | 2863.28 | 2863.28 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 5.539 | 6.865 | -0.239 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.477 | 0.474 | 0.006 | 194.59 | 194.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_keyword mk... | 2.543 | 2.139 | 0.159 | 1048.90 | 775.77 | 0.230 | unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 0.164 | 0.157 | 0.043 | 700.79 | 700.79 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 0.150 | 0.149 | 0.007 | 439.82 | 439.82 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.168 | 0.178 | -0.060 | 528.86 | 528.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 3.809 | 3.731 | 0.020 | 764.52 | 764.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 5.786 | 5.864 | -0.013 | 1026.14 | 1026.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 3.217 | 3.140 | 0.024 | 850.46 | 850.46 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 3.908 | 3.747 | 0.041 | 709.30 | 709.30 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.125 | 2.048 | 0.036 | 437.34 | 437.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.994 | 1.875 | 0.060 | 328.39 | 328.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 4.046 | 5.818 | -0.438 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.581 | 1.640 | -0.037 | 315.10 | 315.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 3.849 | 3.481 | 0.096 | 808.96 | 808.96 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 1.721 | 1.798 | -0.045 | 628.32 | 628.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_keyword mk WHER... | 1.002 | 1.019 | -0.017 | 1160.61 | 1160.57 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 16.622 | 10.884 | 0.345 | 1717.11 | 1717.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 12.766 | 12.233 | 0.042 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 9.928 | 9.654 | 0.028 | 1787.70 | 1787.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 2.030 | 2.025 | 0.002 | 406.87 | 406.87 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 5.639 | 4.842 | 0.141 | 888.36 | 888.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 1.533 | 1.480 | 0.035 | 333.97 | 333.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 3.293 | 3.232 | 0.019 | 686.66 | 686.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.007 | 1.032 | -0.025 | 360.59 | 360.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 6.161 | 6.045 | 0.019 | 1031.19 | 1031.19 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 5.538 | 5.776 | -0.043 | 977.66 | 977.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 4.264 | 4.344 | -0.019 | 863.76 | 863.76 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.355 | 3.437 | -0.459 | 448.70 | 448.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 11.734 | 10.095 | 0.140 | 1912.89 | 1912.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m... | 1.399 | 0.900 | 0.357 | 538.89 | 265.75 | 0.464 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 5.520 | 5.449 | 0.013 | 955.02 | 955.02 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 6.601 | 4.543 | 0.312 | 1130.22 | 1130.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 4.632 | 4.552 | 0.017 | 791.31 | 791.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.543 | 0.022 | 0.959 | 335.26 | 62.13 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND mi.info... | 2.302 | 2.462 | -0.070 | 395.10 | 395.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 0.598 | 0.626 | -0.047 | 549.83 | 388.80 | -0.037 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.493 | 0.042 | 0.915 | 224.43 | 68.23 | 0.600 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 5.541 | 5.154 | 0.070 | 623.84 | 623.84 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.554 | 0.533 | 0.038 | 191.50 | 191.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 2.266 | 2.214 | 0.023 | 330.80 | 330.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 3.998 | 4.084 | -0.022 | 1087.68 | 1087.68 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 7.009 | 7.328 | -0.046 | 1143.52 | 1143.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 1.637 | 1.552 | 0.052 | 336.26 | 336.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.600 | 2.594 | 0.002 | 539.47 | 539.47 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.102 | 2.179 | -0.037 | 408.50 | 408.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 10.577 | 9.589 | 0.093 | 1573.18 | 1573.18 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 12.987 | 13.486 | -0.038 | 2249.09 | 2249.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 3.091 | 4.462 | -0.444 | 562.65 | 562.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.059 | 1.056 | 0.003 | 301.35 | 301.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.526 | 0.513 | 0.025 | 197.08 | 197.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 2.896 | 3.469 | -0.198 | 462.86 | 462.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 3.831 | 2.877 | 0.249 | 629.39 | 629.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 0.686 | 0.669 | 0.025 | 509.74 | 509.74 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.448 | 1.396 | 0.036 | 453.87 | 453.87 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.766 | 1.119 | -0.461 | 308.35 | 308.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m... | 11.487 | 8.613 | 0.250 | 1329.22 | 1329.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 9.666 | 9.525 | 0.015 | 1565.42 | 1565.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.381 | 3.632 | -0.525 | 345.71 | 345.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 4.198 | 4.437 | -0.057 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 5.021 | 4.939 | 0.016 | 871.26 | 871.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 4.360 | 4.257 | 0.024 | 1115.04 | 1115.04 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.441 | 4.903 | -0.425 | 497.05 | 497.05 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 3.928 | 4.000 | -0.018 | 770.61 | 770.61 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 2.203 | 2.252 | -0.022 | 348.13 | 348.13 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 3.476 | 3.512 | -0.010 | 759.91 | 759.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 8.633 | 8.356 | 0.032 | 1374.35 | 1374.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.276 | 2.309 | -0.014 | 342.50 | 342.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 0.626 | 0.022 | 0.965 | 525.60 | 224.82 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.716 | 3.834 | -0.032 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.694 | 1.827 | -0.079 | 441.06 | 441.06 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 1.725 | 1.714 | 0.006 | 384.46 | 384.46 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 4.096 | 4.127 | -0.008 | 514.64 | 514.64 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 4.025 | 3.751 | 0.068 | 855.95 | 855.95 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.244 | 2.202 | 0.019 | 441.49 | 441.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 2.499 | 2.518 | -0.008 | 876.93 | 876.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 3.047 | 3.068 | -0.007 | 658.08 | 658.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 13.261 | 9.009 | 0.321 | 1569.69 | 1569.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 0.552 | 0.014 | 0.975 | 321.17 | 16.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 5.378 | 5.196 | 0.034 | 708.36 | 708.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 0.481 | 0.031 | 0.936 | 782.31 | 554.54 | 0.952 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.715 | 2.011 | -0.173 | 324.39 | 324.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 5.590 | 5.481 | 0.019 | 938.26 | 938.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 8.017 | 12.289 | -0.533 | 1311.83 | 1311.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.523 | 2.594 | 0.264 | 467.96 | 467.96 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.949 | 3.877 | 0.018 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 2.924 | 2.865 | 0.020 | 588.38 | 588.38 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.537 | 0.516 | 0.039 | 197.39 | 197.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 6.478 | 6.626 | -0.023 | 1291.89 | 1291.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 7.869 | 7.720 | 0.019 | 1271.45 | 1271.45 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 0.555 | 0.028 | 0.950 | 880.03 | 606.89 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 6.758 | 6.818 | -0.009 | 1114.83 | 1114.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 6.526 | 4.578 | 0.298 | 791.31 | 791.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 5.208 | 5.312 | -0.020 | 758.83 | 758.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 5.771 | 7.514 | -0.302 | 882.86 | 882.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 2.427 | 2.249 | 0.073 | 534.22 | 534.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx,movie_k... | 5.065 | 5.194 | -0.025 | 1036.00 | 1036.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 0.577 | 0.573 | 0.007 | 517.04 | 517.04 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 8.896 | 8.307 | 0.066 | 1331.73 | 1331.73 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 6.705 | 6.719 | -0.002 | 1147.83 | 1147.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 11.077 | 9.176 | 0.172 | 1474.42 | 1474.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 1.626 | 1.635 | -0.006 | 414.00 | 414.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.707 | 2.991 | -0.105 | 530.11 | 530.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.002 | 1.021 | -0.019 | 285.64 | 285.64 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.081 | 1.143 | -0.057 | 327.71 | 327.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.074 | 3.073 | 0.000 | 484.74 | 484.74 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.631 | 2.535 | 0.036 | 502.91 | 502.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 0.971 | 0.937 | 0.035 | 350.30 | 350.30 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.392 | 2.452 | -0.025 | 345.71 | 345.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM movie_companies mc,title t,movie_keyword mk WHERE t.id=m... | 1.458 | 0.852 | 0.416 | 526.69 | 253.55 | 0.490 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 5.140 | 5.095 | 0.009 | 878.25 | 878.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 6.149 | 5.422 | 0.118 | 919.06 | 919.06 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.728 | 1.770 | -0.024 | 452.36 | 452.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 13.711 | 12.871 | 0.061 | 1938.63 | 1938.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.533 | 1.386 | 0.096 | 317.31 | 317.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.344 | 2.049 | 0.126 | 435.77 | 435.77 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.326 | 3.305 | 0.006 | 494.49 | 494.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.985 | 1.004 | -0.019 | 266.03 | 266.03 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.892 | 0.830 | 0.070 | 226.59 | 226.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 5.809 | 5.855 | -0.008 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 2.546 | 2.494 | 0.020 | 593.58 | 593.58 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 12.772 | 11.036 | 0.136 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 2.864 | 2.815 | 0.017 | 880.42 | 880.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.877 | 0.810 | 0.076 | 270.41 | 270.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 8.920 | 8.679 | 0.027 | 1474.42 | 1474.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 3.009 | 3.228 | -0.073 | 664.32 | 664.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_id<7 | 5.092 | 4.968 | 0.024 | 689.94 | 689.94 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 0.969 | 0.930 | 0.040 | 348.73 | 348.73 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.605 | 0.020 | 0.967 | 423.70 | 119.52 | 0.963 | improved |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx... | 3.561 | 3.577 | -0.004 | 985.32 | 985.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.930 | 1.000 | -0.075 | 206.41 | 206.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.359 | 3.271 | 0.026 | 495.97 | 495.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 3.731 | 3.747 | -0.004 | 854.81 | 854.81 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 4.844 | 4.978 | -0.028 | 1186.89 | 1186.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 0.901 | 0.024 | 0.973 | 784.38 | 213.91 | 0.988 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 3.164 | 4.122 | -0.303 | 965.09 | 809.55 | -0.007 | degraded |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 2.506 | 2.527 | -0.008 | 635.91 | 635.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 5.497 | 5.471 | 0.005 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword... | 0.638 | 0.596 | 0.066 | 1071.40 | 1071.40 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.883 | 3.817 | 0.017 | 512.66 | 512.66 | 0.000 | plan unchanged |

## Execution Plan Comparisons

For every query, the original and RL-selected plans are shown.
If the plan did not change, it is reported as 'Plan unchanged'.

### Query 0: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
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
        Index Scan movie_keyword (mk) using rl_tmp_77e5f5292712
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
    Index Scan movie_keyword (mk) using rl_tmp_c8620e8d3db7
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
    Index Scan movie_keyword (mk) using rl_tmp_47a4cb56e5ba
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
      Bitmap Index Scan using rl_tmp_8af30a42ef43
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
          Index Only Scan movie_info_idx (mi_idx) using rl_tmp_97bebdf088b4
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
          Bitmap Index Scan using rl_tmp_459cd250dba1
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
- **Outcome**: unchanged

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
        Index Scan movie_companies (mc) using rl_tmp_cddec1b3133b
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
        Index Scan movie_companies (mc) using rl_tmp_05eade72906e
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
- **Outcome**: unchanged

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
              Bitmap Index Scan using rl_tmp_714a9ce68cbf
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
- **Outcome**: unchanged

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
          Bitmap Index Scan using rl_tmp_d9fe0a507f35
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
      Bitmap Index Scan using rl_tmp_dac823c1a031
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
        Bitmap Index Scan using rl_tmp_1ff5723a6a55
      Hash
        Seq Scan movie_keyword (mk)
    Index Only Scan title (t) using title_pkey
```

### Query 114: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t....
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
      Bitmap Index Scan using rl_tmp_a8f5cd3150a5
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
        Index Scan movie_keyword (mk) using rl_tmp_c0b9fee48aca
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
    Index Scan movie_keyword (mk) using rl_tmp_35e61e776b1f
    Index Scan title (t) using title_pkey
```

### Query 156: SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc...
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
- **Outcome**: plan unchanged
- **Plan**: unchanged

### Query 157: SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i...
- **Action**: join_order=((t JOIN ci) JOIN mi); join_method=merge; scan_method=indexscan; index=created:movie_info(info_type_id)
- **Outcome**: unchanged

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
        Index Scan movie_info (mi) using rl_tmp_ccec16e28ee4
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
          Bitmap Index Scan using rl_tmp_8674db88947b
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
- **Action**: join_order=original; join_method=nestloop; scan_method=bitmapscan; index=none
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
          Bitmap Index Scan using rl_tmp_71e877ea451c
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
        Index Scan movie_keyword (mk) using rl_tmp_659f92efec6b
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
      Index Scan cast_info (ci) using rl_tmp_779f3732191c
      Seq Scan movie_companies (mc)
    Index Only Scan title (t) using title_pkey
```

### Query 212: SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH...
- **Action**: join_order=(((t JOIN mi) JOIN mc) JOIN ci); join_method=hash; scan_method=seqscan; index=created:movie_info(info_type_id)
- **Outcome**: degraded

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
            Bitmap Index Scan using rl_tmp_edf4946f64b7
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
- Mean baseline time (ms): 4.092
- Median baseline time (ms): 3.047
- Mean RL time (ms): 3.945
- Median RL time (ms): 3.14
- Mean time improvement: 0.0645
- Median time improvement: 0.0129
- Mean cost improvement: 0.053
- **Percent improved**: 6.5%
- Percent unchanged (incl. plan unchanged): 93.1%
- Percent plan unchanged: 90.3%
- **Percent degraded**: 0.5%
- Percent failed: 0.0%
- Mean planning overhead (ms): 0.013
- Median planning overhead (ms): 0.007
- Outcome counts: {'plan unchanged': 196, 'improved': 14, 'unchanged': 6, 'degraded': 1}

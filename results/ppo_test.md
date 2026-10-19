# PostgreSQL RL Optimizer Evaluation Report

Improvements are claimed only when measured execution time improved
and the EXPLAIN plan actually changed. `plan unchanged` is reported
when the selected action did not change PostgreSQL's operator tree.

## Per-query Results

| Query | Baseline Time | RL Time | Time Improvement | Baseline Cost | RL Cost | Buffer Improvement | Outcome |
| ----- | ------------- | ------- | ---------------- | ------------- | ------- | ------------------ | ------- |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 2.453 | 2.461 | -0.003 | 601.89 | 601.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 10.258 | 10.086 | 0.017 | 1768.77 | 1768.77 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 10.944 | 11.650 | -0.065 | 1954.44 | 1954.44 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 4.517 | 4.691 | -0.039 | 1148.16 | 1148.16 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 4.041 | 4.136 | -0.024 | 1015.89 | 1015.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM movie_keyword mk,title t,cast_info ci WHERE t.id=mk.movi... | 8.029 | 7.696 | 0.041 | 1488.72 | 1488.72 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.851 | 2.753 | 0.034 | 469.82 | 469.82 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 5.883 | 5.963 | -0.014 | 1021.90 | 1021.90 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 8.472 | 8.600 | -0.015 | 1573.78 | 1573.78 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.483 | 0.464 | 0.039 | 194.86 | 194.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.581 | 0.594 | -0.022 | 423.70 | 423.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 2.092 | 2.022 | 0.033 | 712.26 | 712.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.432 | 2.471 | -0.016 | 530.34 | 530.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 7.944 | 8.330 | -0.049 | 1531.65 | 1531.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 2.309 | 2.356 | -0.020 | 842.27 | 842.27 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 4.151 | 3.942 | 0.050 | 1056.07 | 1056.07 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 16.403 | 17.713 | -0.080 | 2907.99 | 2907.99 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.868 | 1.972 | -0.056 | 493.69 | 493.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 4.236 | 4.222 | 0.003 | 893.70 | 893.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_companies mc WHERE t.id=mi.m... | 2.518 | 2.391 | 0.050 | 585.34 | 585.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 8.125 | 8.105 | 0.002 | 1374.35 | 1374.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.550 | 0.013 | 0.976 | 313.16 | 12.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.629 | 2.727 | -0.037 | 546.25 | 546.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.918 | 0.963 | -0.049 | 300.26 | 300.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.853 | 3.670 | 0.047 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.906 | 1.945 | -0.020 | 338.45 | 338.45 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 2.374 | 2.442 | -0.029 | 398.93 | 398.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 5.580 | 5.631 | -0.009 | 980.85 | 980.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 2.346 | 2.308 | 0.016 | 660.10 | 660.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.549 | 0.013 | 0.976 | 313.16 | 12.62 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.420 | 0.114 | 0.729 | 270.23 | 128.27 | 0.019 | unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 1.035 | 0.975 | 0.058 | 234.51 | 234.51 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 2.405 | 2.559 | -0.064 | 555.21 | 555.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 0.158 | 0.168 | -0.063 | 1111.63 | 1111.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 5.688 | 5.467 | 0.039 | 1226.42 | 1226.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 6.779 | 7.036 | -0.038 | 1238.80 | 1238.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 0.423 | 0.454 | -0.073 | 852.10 | 852.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 8.397 | 8.512 | -0.014 | 1562.08 | 1562.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx... | 4.294 | 4.435 | -0.033 | 1212.49 | 1212.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 0.574 | 0.587 | -0.023 | 367.28 | 367.28 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 2.591 | 2.462 | 0.050 | 467.99 | 467.99 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 5.412 | 5.252 | 0.030 | 1152.31 | 1152.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 13.023 | 13.435 | -0.032 | 2320.53 | 2320.53 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 3.917 | 3.467 | 0.115 | 1002.16 | 1002.16 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.983 | 3.024 | -0.014 | 591.40 | 591.40 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 3.290 | 3.384 | -0.029 | 755.85 | 755.85 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword... | 0.572 | 0.538 | 0.059 | 1037.66 | 1037.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 5.687 | 5.285 | 0.071 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx,movie_keywor... | 2.513 | 2.363 | 0.060 | 726.75 | 726.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 1.851 | 1.913 | -0.033 | 461.50 | 461.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 2.342 | 2.338 | 0.002 | 579.57 | 579.57 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM cast_info ci,title t WHERE t.id=ci.movie_id AND t.produc... | 2.995 | 3.083 | -0.029 | 622.65 | 622.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 3.456 | 3.397 | 0.017 | 774.21 | 774.21 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 2.060 | 2.127 | -0.033 | 653.92 | 653.92 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.937 | 1.880 | 0.029 | 353.37 | 353.37 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 0.552 | 0.581 | -0.053 | 526.69 | 526.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.636 | 3.788 | -0.042 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.394 | 2.379 | 0.006 | 457.41 | 457.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 2.533 | 2.582 | -0.019 | 477.54 | 477.54 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.535 | 3.812 | -0.078 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi,movie_info_idx ... | 3.205 | 3.306 | -0.032 | 762.09 | 762.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.668 | 3.714 | -0.013 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 7.722 | 7.703 | 0.002 | 1407.52 | 1407.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 10.240 | 10.657 | -0.041 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.218 | 2.439 | -0.100 | 342.42 | 342.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 4.460 | 4.510 | -0.011 | 920.49 | 920.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 0.343 | 0.353 | -0.029 | 468.03 | 468.03 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM cast_info ci,title t,movie_companies mc WHERE t.id=ci.mo... | 2.608 | 2.696 | -0.034 | 831.10 | 831.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 2.493 | 2.486 | 0.003 | 527.93 | 527.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.406 | 0.109 | 0.732 | 268.43 | 127.49 | 0.107 | unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.100 | 1.111 | -0.010 | 335.63 | 335.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 1.670 | 1.702 | -0.019 | 512.22 | 512.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc,movie_info m... | 2.823 | 2.776 | 0.017 | 825.26 | 825.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.778 | 3.797 | -0.005 | 522.66 | 522.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 1.684 | 1.653 | 0.018 | 447.32 | 447.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 6.104 | 6.105 | -0.000 | 1083.11 | 1083.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 21.309 | 17.566 | 0.176 | 2863.28 | 2863.28 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 5.187 | 5.482 | -0.057 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.457 | 0.453 | 0.009 | 194.59 | 194.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_keyword mk... | 2.626 | 2.608 | 0.007 | 1048.90 | 1048.90 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 0.185 | 0.157 | 0.151 | 700.79 | 700.79 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 0.150 | 0.152 | -0.013 | 439.82 | 439.82 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.161 | 0.218 | -0.354 | 528.86 | 528.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 3.747 | 3.679 | 0.018 | 764.52 | 764.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 5.502 | 5.615 | -0.021 | 1026.14 | 1026.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 3.030 | 3.008 | 0.007 | 850.46 | 850.46 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 3.538 | 3.660 | -0.034 | 709.30 | 709.30 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.067 | 2.052 | 0.007 | 437.34 | 437.34 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.854 | 1.800 | 0.029 | 328.39 | 328.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.812 | 3.622 | 0.050 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.368 | 1.423 | -0.040 | 315.10 | 315.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 3.438 | 3.401 | 0.011 | 808.96 | 808.96 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 1.746 | 1.692 | 0.031 | 628.32 | 628.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_keyword mk WHER... | 0.967 | 0.984 | -0.018 | 1160.61 | 1160.61 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 10.538 | 10.492 | 0.004 | 1717.11 | 1717.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 10.840 | 10.769 | 0.007 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 9.246 | 9.372 | -0.014 | 1787.70 | 1787.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 1.830 | 1.927 | -0.053 | 406.87 | 406.87 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 4.501 | 4.547 | -0.010 | 888.36 | 888.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 1.478 | 1.501 | -0.016 | 333.97 | 333.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 3.346 | 3.786 | -0.132 | 686.66 | 686.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.041 | 0.975 | 0.063 | 360.59 | 360.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 5.883 | 6.145 | -0.045 | 1031.19 | 1031.19 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 5.588 | 5.428 | 0.029 | 977.66 | 977.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 4.115 | 4.280 | -0.040 | 863.76 | 863.76 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.273 | 2.611 | -0.149 | 448.70 | 448.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 9.201 | 8.959 | 0.026 | 1912.89 | 1912.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m... | 1.358 | 1.290 | 0.050 | 538.89 | 538.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 5.119 | 5.377 | -0.050 | 955.02 | 955.02 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 4.194 | 4.380 | -0.044 | 1130.22 | 1130.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 4.374 | 4.396 | -0.005 | 791.31 | 791.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 0.542 | 0.021 | 0.961 | 335.26 | 62.13 | 0.975 | improved |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND mi.info... | 2.370 | 2.241 | 0.054 | 395.10 | 395.10 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 0.575 | 0.550 | 0.043 | 549.83 | 549.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.336 | 0.320 | 0.048 | 224.43 | 224.43 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 3.360 | 3.334 | 0.008 | 623.84 | 623.84 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.497 | 0.508 | -0.022 | 191.50 | 191.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 2.119 | 2.139 | -0.009 | 330.80 | 330.80 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 3.832 | 3.869 | -0.010 | 1087.68 | 1087.68 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 6.705 | 7.323 | -0.092 | 1143.52 | 1143.52 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.kind_... | 1.572 | 1.562 | 0.006 | 336.26 | 336.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.502 | 2.481 | 0.008 | 539.47 | 539.47 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 1.426 | 1.353 | 0.051 | 408.50 | 408.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 8.493 | 8.766 | -0.032 | 1573.18 | 1573.18 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 13.087 | 12.631 | 0.035 | 2249.09 | 2249.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.843 | 2.919 | -0.027 | 562.65 | 562.65 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.964 | 1.036 | -0.075 | 301.35 | 301.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.490 | 0.499 | -0.018 | 197.08 | 197.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 2.416 | 2.397 | 0.008 | 462.86 | 462.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 2.443 | 2.499 | -0.023 | 629.39 | 629.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 0.557 | 0.560 | -0.005 | 509.74 | 509.74 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.362 | 1.289 | 0.054 | 453.87 | 453.87 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 0.745 | 0.750 | -0.007 | 308.35 | 308.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk,movie_companies mc WHERE t.id=m... | 8.191 | 8.046 | 0.018 | 1329.22 | 1329.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 8.885 | 9.647 | -0.086 | 1565.42 | 1565.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.283 | 2.282 | 0.000 | 345.71 | 345.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.755 | 3.757 | -0.001 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 4.834 | 4.856 | -0.005 | 871.26 | 871.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 4.047 | 4.185 | -0.034 | 1115.04 | 1115.04 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.327 | 3.235 | 0.028 | 497.05 | 497.05 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 3.822 | 3.812 | 0.003 | 770.61 | 770.61 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 2.260 | 2.175 | 0.038 | 348.13 | 348.13 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 3.241 | 3.373 | -0.041 | 759.91 | 759.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 8.325 | 8.171 | 0.018 | 1374.35 | 1374.35 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.098 | 2.151 | -0.025 | 342.50 | 342.50 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 0.555 | 0.556 | -0.002 | 525.60 | 525.60 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.593 | 3.656 | -0.018 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.652 | 1.737 | -0.051 | 441.06 | 441.06 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 1.540 | 1.618 | -0.051 | 384.46 | 384.46 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.427 | 3.508 | -0.024 | 514.64 | 514.64 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 3.410 | 3.354 | 0.016 | 855.95 | 855.95 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 2.126 | 2.138 | -0.006 | 441.49 | 441.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 2.431 | 2.397 | 0.014 | 876.93 | 876.93 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 2.959 | 2.871 | 0.030 | 658.08 | 658.08 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 8.548 | 8.500 | 0.006 | 1569.69 | 1569.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.ki... | 0.566 | 0.551 | 0.027 | 321.17 | 321.17 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 5.044 | 5.064 | -0.004 | 708.36 | 708.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 0.448 | 0.432 | 0.036 | 782.31 | 782.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 1.682 | 1.658 | 0.014 | 324.39 | 324.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 5.375 | 5.299 | 0.014 | 938.26 | 938.26 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 7.907 | 8.065 | -0.020 | 1311.83 | 1311.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 2.427 | 2.491 | -0.026 | 467.96 | 467.96 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.582 | 3.592 | -0.003 | 512.66 | 512.66 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 2.804 | 2.687 | 0.042 | 588.38 | 588.38 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.507 | 0.494 | 0.026 | 197.39 | 197.39 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi WHERE t.id=ci.movie_i... | 6.142 | 6.218 | -0.012 | 1291.89 | 1291.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 7.263 | 7.409 | -0.020 | 1271.45 | 1271.45 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 0.529 | 0.552 | -0.043 | 880.03 | 880.03 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 6.069 | 6.097 | -0.005 | 1114.83 | 1114.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 4.423 | 4.726 | -0.069 | 791.31 | 791.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.produc... | 5.299 | 5.118 | 0.034 | 758.83 | 758.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 4.931 | 4.930 | 0.000 | 882.86 | 882.86 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 2.203 | 2.198 | 0.002 | 534.22 | 534.22 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx,movie_k... | 4.932 | 5.022 | -0.018 | 1036.00 | 1036.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 0.534 | 0.552 | -0.034 | 517.04 | 517.04 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 7.209 | 7.334 | -0.017 | 1331.73 | 1331.73 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_keyword mk WHERE t.id=m... | 6.299 | 6.601 | -0.048 | 1147.83 | 1147.83 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 8.174 | 7.977 | 0.024 | 1474.42 | 1474.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 1.648 | 1.579 | 0.042 | 414.00 | 414.00 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.620 | 2.646 | -0.010 | 530.11 | 530.11 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.985 | 1.010 | -0.025 | 285.64 | 285.64 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 1.199 | 1.131 | 0.057 | 327.71 | 327.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.120 | 3.080 | 0.013 | 484.74 | 484.74 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info_idx mi_idx WHERE t... | 2.735 | 2.653 | 0.030 | 502.91 | 502.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 0.957 | 0.927 | 0.031 | 350.30 | 350.30 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc... | 2.380 | 2.298 | 0.034 | 345.71 | 345.71 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM movie_companies mc,title t,movie_keyword mk WHERE t.id=m... | 1.363 | 1.310 | 0.039 | 526.69 | 526.69 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 4.641 | 4.610 | 0.007 | 878.25 | 878.25 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 5.033 | 5.030 | 0.001 | 919.06 | 919.06 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_info_idx mi_idx WHERE t.id=m... | 1.540 | 1.615 | -0.049 | 452.36 | 452.36 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 11.019 | 10.983 | 0.003 | 1938.63 | 1938.63 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 1.378 | 1.299 | 0.057 | 317.31 | 317.31 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 1.949 | 1.974 | -0.013 | 435.77 | 435.77 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.062 | 3.170 | -0.035 | 494.49 | 494.49 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.928 | 0.932 | -0.004 | 266.03 | 266.03 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.818 | 0.853 | -0.043 | 226.59 | 226.59 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 5.498 | 5.591 | -0.017 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 2.462 | 2.324 | 0.056 | 593.58 | 593.58 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi,movie_keyword mk WHERE t.id=mi.mov... | 10.516 | 10.372 | 0.014 | 1727.09 | 1727.09 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 2.860 | 2.809 | 0.018 | 880.42 | 880.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND t.... | 0.790 | 0.804 | -0.018 | 270.41 | 270.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 7.951 | 7.640 | 0.039 | 1474.42 | 1474.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_i... | 2.793 | 2.881 | -0.032 | 664.32 | 664.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND t.kind_id<7 | 4.613 | 4.661 | -0.010 | 689.94 | 689.94 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info mi WHERE t.id=mi.movie_id AND t.produ... | 0.896 | 0.907 | -0.012 | 348.73 | 348.73 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx,movie_keyword mk WHERE t.i... | 0.574 | 0.536 | 0.066 | 423.70 | 423.70 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info mi,movie_info_idx mi_idx... | 3.297 | 3.411 | -0.035 | 985.32 | 985.32 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_info_idx mi_idx WHERE t.id=mi_idx.movie_id... | 0.916 | 0.944 | -0.031 | 206.41 | 206.41 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND t.pr... | 3.357 | 3.508 | -0.045 | 495.97 | 495.97 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx WHERE t.id=ci... | 3.716 | 3.856 | -0.038 | 854.81 | 854.81 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_keyword mk WHERE t.id=ci.movi... | 4.921 | 5.034 | -0.023 | 1186.89 | 1186.89 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci WHERE t.id=mc.mo... | 0.877 | 0.482 | 0.450 | 784.38 | 295.45 | -0.531 | unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,cast_info ci,movie_info mi WH... | 3.116 | 3.011 | 0.034 | 965.09 | 965.06 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_companies mc,movie_info mi WHERE t.id=mc.m... | 2.351 | 2.490 | -0.059 | 635.91 | 635.91 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci WHERE t.id=ci.movie_id AND ci.perso... | 5.351 | 5.360 | -0.002 | 768.14 | 768.14 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,cast_info ci,movie_info_idx mi_idx,movie_keyword... | 0.590 | 0.585 | 0.008 | 1071.40 | 1071.42 | 0.000 | plan unchanged |
| SELECT COUNT(*) FROM title t,movie_keyword mk WHERE t.id=mk.movie_id AND mk.k... | 3.581 | 3.613 | -0.009 | 512.66 | 512.66 | 0.000 | plan unchanged |

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
    Index Scan movie_keyword (mk) using rl_tmp_1b4a4680ddff
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
    Index Scan movie_keyword (mk) using rl_tmp_482d8cbc3c94
    Index Only Scan title (t) using title_pkey
```

### Query 30: SELECT COUNT(*) FROM title t,movie_companies mc WHERE t.id=mc.movie_id AND mc...
- **Action**: join_order=original; join_method=nestloop; scan_method=default; index=created:movie_companies(company_id)
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
      Bitmap Index Scan using rl_tmp_6e7619478e37
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
      Bitmap Index Scan using rl_tmp_e01a17fa1922
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
      Bitmap Index Scan using rl_tmp_807f5c60dfac
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
- **Outcome**: unchanged

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
    Index Scan cast_info (ci) using rl_tmp_eedf1639a9ba
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
- Mean baseline time (ms): 3.625
- Median baseline time (ms): 2.804
- Mean RL time (ms): 3.625
- Median RL time (ms): 2.753
- Mean time improvement: 0.0165
- Median time improvement: -0.005
- Mean cost improvement: 0.0203
- **Percent improved**: 1.4%
- Percent unchanged (incl. plan unchanged): 98.6%
- Percent plan unchanged: 97.2%
- **Percent degraded**: 0.0%
- Percent failed: 0.0%
- Mean planning overhead (ms): 0.017
- Median planning overhead (ms): 0.011
- Outcome counts: {'plan unchanged': 211, 'improved': 3, 'unchanged': 3}

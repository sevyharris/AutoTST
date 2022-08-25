#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/TS_groups"
short_desc = u""
long_desc = u""

entry(
    index = 0,
    label = "Root",
    group = 
"""
1 *2 R!H u0         {2,[S,D,B]} {3,S}
2 *3 R!H u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 R   u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.4450575, "d13": 2.546517, "d23": 1.1161478666666664},
        uncertainties = {"d12": 0.016676374845416668, "d13": 0.025618857167666653, "d23": 0.031871373862115554},
    ),

)

entry(
    index = 1,
    label = "Root_Ext-1R!H-R",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {4,[S,D,T,B]}
2 *3 R!H u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4    R!H ux         {1,[S,D,T,B]}
5 *1 R   u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.4329116666666668, "d13": 2.5450633333333332, "d23": 1.1264944444444447},
        uncertainties = {"d12": 0.01575518115833333, "d13": 0.024392001199999992, "d23": 0.0315919016531358},
    ),

)

entry(
    index = 62,
    label = "Root_Ext-2R!H-R",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S}
2 *3 R!H u[1,2]     {1,[S,D,B]} {4,[S,D,T,B]}
3 *4 H   u0         {1,S}
4    R!H ux         {2,[S,D,T,B]}
5 *1 R   u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.4751592857142857, "d13": 2.531732857142857, "d23": 1.0619845714285716},
        uncertainties = {"d12": 0.012381650478061222, "d13": 0.02625357244897958, "d23": 0.03194038164638775},
    ),

)

entry(
    index = 73,
    label = "Root_4R->H",
    group = 
"""
1 *2 R!H u0         {2,[S,D,B]} {3,S}
2 *3 R!H u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 H   u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.3593525, "d13": 2.2608325000000002, "d23": 0.9068637500000001},
        uncertainties = {"d12": 0.01665622311875, "d13": 0.009648780068749988, "d23": 0.005285624998187504},
    ),

)

entry(
    index = 96,
    label = "Root_N-4R->H",
    group = 
"""
1 *2 R!H       u0         {2,[S,D,B]} {3,S}
2 *3 R!H       u[1,2]     {1,[S,D,B]}
3 *4 H         u0         {1,S}
4 *1 [C,O,N,S] u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.4508916666666665, "d13": 2.6038454166666667, "d23": 1.174863875},
        uncertainties = {"d12": 0.017978413113888887, "d13": 0.01181219059149305, "d23": 0.023932546497359375},
    ),

)

entry(
    index = 2,
    label = "Root_Ext-1R!H-R_4R->O",
    group = 
"""
1 *2 C u0         {2,[S,D,B]} {3,S} {4,[S,D,T,B]}
2 *3 C u[1,2]     {1,[S,D,B]}
3 *4 H u0         {1,S}
4    C ux         {1,[S,D,T,B]}
5 *1 O u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.4903199999999999, "d13": 2.5965233333333333, "d23": 1.12068},
        uncertainties = {"d12": 0.02156003816666666, "d13": 0.0033027418222222192, "d23": 0.00955070583333333},
    ),

)

entry(
    index = 13,
    label = "Root_Ext-1R!H-R_N-4R->O",
    group = 
"""
1 *2 C         u0         {2,[S,D,B]} {3,S} {4,[S,D,T,B]}
2 *3 R!H       u[1,2]     {1,[S,D,B]}
3 *4 H         u0         {1,S}
4    R!H       ux         {1,[S,D,T,B]}
5 *1 [H,C,N,S] u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.39564, "d13": 2.51335, "d23": 1.13124},
        uncertainties = {"d12": 0.010443864527272733, "d13": 0.03551643178181818, "d23": 0.04641814862836364},
    ),

)

entry(
    index = 63,
    label = "Root_Ext-2R!H-R_2R!H->C",
    group = 
"""
1 *2 C u0         {2,S} {3,S}
2 *3 C u[1,2]     {1,S} {4,[S,D,T,B]}
3 *4 H u0         {1,S}
4    C ux         {2,[S,D,T,B]}
5 *1 R u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.4832625, "d13": 2.59633125, "d23": 1.1176629999999999},
        uncertainties = {"d12": 0.007805087543749997, "d13": 0.01630050823593749, "d23": 0.015244224272999998},
    ),

)

entry(
    index = 66,
    label = "Root_Ext-2R!H-R_N-2R!H->C",
    group = 
"""
1 *2 C u0         {2,[S,D,B]} {3,S}
2 *3 N u[1,2]     {1,[S,D,B]} {5,[S,D,T,B]}
3 *4 H u0         {1,S}
4 *1 R u[1,2,3,4]
5    O ux         {2,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 74,
    label = "Root_4R->H_Sp-2R!H-1R!H",
    group = 
"""
1 *2 R!H u0         {2,S} {3,S}
2 *3 R!H u[1,2]     {1,S}
3 *4 H   u0         {1,S}
4 *1 H   u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.2894400000000001, "d13": 2.2250366666666666, "d23": 0.9384443333333334},
        uncertainties = {"d12": 0.0026572668666666652, "d13": 0.007739673355555553, "d23": 0.003058167022888894},
    ),

)

entry(
    index = 91,
    label = "Root_4R->H_N-Sp-2R!H-1R!H",
    group = 
"""
1 *2 R!H u0         {2,D} {3,S}
2 *3 R!H u[1,2]     {1,D}
3 *4 H   u0         {1,S}
4 *1 H   u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.56909, "d13": 2.36822, "d23": 0.812122},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 97,
    label = "Root_N-4R->H_4CNOS-u1",
    group = 
"""
1 *2 R!H       u0     {2,[S,D,B]} {3,S}
2 *3 R!H       u[1,2] {1,[S,D,B]}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.4450404347826085, "d13": 2.5953760869565214, "d23": 1.1710909999999999},
        uncertainties = {"d12": 0.017938397299810963, "d13": 0.010604254997731563, "d23": 0.024631461938869562},
    ),

)

entry(
    index = 209,
    label = "Root_N-4R->H_N-4CNOS-u1",
    group = 
"""
1 *2 R!H       u0     {2,[S,D,B]} {3,S}
2 *3 R!H       u[1,2] {1,[S,D,B]}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u2    

""",
    distances = DistanceData(
        distances = {"d12": 1.58547, "d13": 2.79864, "d23": 1.26164},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 3,
    label = "Root_Ext-1R!H-R_4R->O_Ext-4O-R",
    group = 
"""
1 *2 C u0         {2,[S,D,B]} {3,S} {4,[S,D,T,B]}
2 *3 C u[1,2]     {1,[S,D,B]}
3 *4 H u0         {1,S}
4    C ux         {1,[S,D,T,B]}
5 *1 O u[1,2,3,4] {6,[S,D,T,B]}
6    O ux         {5,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.550862, "d13": 2.615656, "d23": 1.077876},
        uncertainties = {"d12": 0.0038800432159999967, "d13": 0.0017669365839999927, "d23": 0.00046775250399999966},
    ),

)

entry(
    index = 10,
    label = "Root_Ext-1R!H-R_4R->O_Sp-5R!H-1R!H",
    group = 
"""
1 *2 C u0 {2,S} {3,S} {4,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4    C u0 {1,S}
5 *1 O u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 12,
    label = "Root_Ext-1R!H-R_4R->O_N-Sp-5R!H-1R!H",
    group = 
"""
1 *2 C u0         {2,[S,D,B]} {3,S} {4,D}
2 *3 C u[1,2]     {1,[S,D,B]}
3 *4 H u0         {1,S}
4    C ux         {1,D}
5 *1 O u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.18761, "d13": 2.50086, "d23": 1.3347},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 14,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R",
    group = 
"""
1 *2 C         u0         {2,[S,D,B]} {3,S} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 C         u[1,2]     {1,[S,D,B]}
3 *4 H         u0         {1,S}
4    R!H       ux         {1,[S,D,T,B]}
5    R!H       ux         {1,[S,D,T,B]}
6 *1 [H,C,N,S] u[1,2,3,4]

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 30,
    label = "Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H",
    group = 
"""
1 *2 C u0         {2,[S,D,B]} {3,S} {4,D}
2 *3 C u[1,2]     {1,[S,D,B]}
3 *4 H u0         {1,S}
4    C ux         {1,D}
5 *1 C u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.38748, "d13": 2.6737175, "d23": 1.2904875},
        uncertainties = {"d12": 0.00362782845, "d13": 0.0005311243187500004, "d23": 0.001648631518750004},
    ),

)

entry(
    index = 37,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H",
    group = 
"""
1 *2 C         u0         {2,[S,D,B]} {3,S} {4,[S,B]}
2 *3 R!H       u[1,2]     {1,[S,D,B]}
3 *4 H         u0         {1,S}
4    C         ux         {1,[S,B]}
5 *1 [H,C,N,S] u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.4003028571428568, "d13": 2.4217114285714287, "d23": 1.0402414285714285},
        uncertainties = {"d12": 0.014278951134693883, "d13": 0.032414559669387756, "d23": 0.04922869482824488},
    ),

)

entry(
    index = 64,
    label = "Root_Ext-2R!H-R_2R!H->C_4R->C",
    group = 
"""
1 *2 C u0         r0 {2,S} {3,S}
2 *3 C u[1,2]     r0 {1,S} {4,[S,D,T,B]}
3 *4 H u0         {1,S}
4    C ux         {2,[S,D,T,B]}
5 *1 C u[1,2,3,4] r0

""",
    distances = DistanceData(
        distances = {"d12": 1.39272, "d13": 2.696195, "d23": 1.30463},
        uncertainties = {"d12": 0.003374448099999997, "d13": 0.00021564922500000172, "d23": 0.0017884440999999948},
    ),

)

entry(
    index = 65,
    label = "Root_Ext-2R!H-R_2R!H->C_N-4R->C",
    group = 
"""
1 *2 C       u0         r0 {2,S} {3,S}
2 *3 C       u[1,2]     r0 {1,S} {4,[S,D,T,B]}
3 *4 H       u0         {1,S}
4    C       ux         {2,[S,D,T,B]}
5 *1 [H,N,O] u[1,2,3,4] r0

""",
    distances = DistanceData(
        distances = {"d12": 1.5134433333333333, "d13": 2.5630433333333333, "d23": 1.0553406666666667},
        uncertainties = {"d12": 0.00563843655555555, "d13": 0.017229786322222215, "d23": 0.004193191402222226},
    ),

)

entry(
    index = 67,
    label = "Root_Ext-2R!H-R_N-2R!H->C_4R->H",
    group = 
"""
1 *2 C u0         r0 {2,D} {3,S}
2 *3 N u[1,2]     r0 {1,D} {5,[S,D,T,B]}
3 *4 H u0         {1,S}
4 *1 H u[1,2,3,4] r0
5    O ux         {2,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 68,
    label = "Root_Ext-2R!H-R_N-2R!H->C_N-4R->H",
    group = 
"""
1 *2 C       u0         {2,[S,D,B]} {3,S}
2 *3 N       u[1,2]     {1,[S,D,B]} {5,[S,D,T,B]}
3 *4 H       u0         {1,S}
4 *1 [C,N,O] u[1,2,3,4]
5    O       ux         {2,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 75,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1",
    group = 
"""
1 *2 R!H u0         {2,S} {3,S}
2 *3 R!H u1         {1,S}
3 *4 H   u0         {1,S}
4 *1 H   u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.2894400000000001, "d13": 2.2250366666666666, "d23": 0.9384443333333334},
        uncertainties = {"d12": 0.0026572668666666652, "d13": 0.007739673355555553, "d23": 0.003058167022888894},
    ),

)

entry(
    index = 90,
    label = "Root_4R->H_Sp-2R!H-1R!H_N-2R!H-u1",
    group = 
"""
1 *2 R!H u0         r0 {2,S} {3,S}
2 *3 R!H u2         r0 {1,S}
3 *4 H   u0         {1,S}
4 *1 H   u[1,2,3,4] r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 92,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_1R!H->C",
    group = 
"""
1 *2 C   u0         r0 {2,D} {3,S}
2 *3 R!H u1         r0 {1,D}
3 *4 H   u0         {1,S}
4 *1 H   u[1,2,3,4] r0

""",
    distances = DistanceData(
        distances = {"d12": 1.56909, "d13": 2.36822, "d23": 0.812122},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 93,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C",
    group = 
"""
1 *2 N   u0     {2,D} {3,S}
2 *3 R!H u[1,2] {1,D}
3 *4 H   u0     {1,S}
4 *1 H   u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 98,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O",
    group = 
"""
1 *2 O         u0     {2,[S,D,B]} {3,S}
2 *3 R!H       u[1,2] {1,[S,D,B]}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.4936299999999998, "d13": 2.5316441666666663, "d23": 1.0576194166666668},
        uncertainties = {"d12": 0.01955371123333333, "d13": 0.006102050424305556, "d23": 0.0067686865110763855},
    ),

)

entry(
    index = 135,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O",
    group = 
"""
1 *2 [C,N,S]   u0     {2,[S,D,B]} {3,S}
2 *3 R!H       u[1,2] {1,[S,D,B]}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.3920336363636363, "d13": 2.6649018181818183, "d23": 1.2948781818181818},
        uncertainties = {"d12": 0.01079093867768595, "d13": 0.006250915233057847, "d23": 0.014748532142148763},
    ),

)

entry(
    index = 210,
    label = "Root_N-4R->H_N-4CNOS-u1_1R!H->O",
    group = 
"""
1 *2 O         u0     {2,[S,D,B]} {3,S}
2 *3 R!H       u[1,2] {1,[S,D,B]}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u2    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 215,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O",
    group = 
"""
1 *2 [C,N,S]   u0     {2,[S,D,B]} {3,S}
2 *3 R!H       u[1,2] {1,[S,D,B]}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u2    

""",
    distances = DistanceData(
        distances = {"d12": 1.58547, "d13": 2.79864, "d23": 1.26164},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 4,
    label = "Root_Ext-1R!H-R_4R->O_Ext-4O-R_Sp-5R!H-1R!H",
    group = 
"""
1 *2 C u0     {2,S} {3,S} {4,S}
2 *3 C u[1,2] {1,S}
3 *4 H u0     {1,S}
4    C ux     {1,S}
5 *1 O u1     {6,[S,D,T,B]}
6    O ux     {5,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.5202974999999999, "d13": 2.5950925, "d23": 1.0883525},
        uncertainties = {"d12": 0.0001791107187500012, "d13": 9.438306874999983e-05, "d23": 3.5905368750000745e-05},
    ),

)

entry(
    index = 9,
    label = "Root_Ext-1R!H-R_4R->O_Ext-4O-R_N-Sp-5R!H-1R!H",
    group = 
"""
1 *2 C u0         {2,[S,D,B]} {3,S} {4,D}
2 *3 C u1         {1,[S,D,B]}
3 *4 H u0         {1,S}
4    C u0         {1,D}
5 *1 O u[1,2,3,4] {6,S}
6    O u1         r0 {5,S}

""",
    distances = DistanceData(
        distances = {"d12": 1.67312, "d13": 2.69791, "d23": 1.03597},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 11,
    label = "Root_Ext-1R!H-R_4R->O_Sp-5R!H-1R!H_Ext-1R!H-R",
    group = 
"""
1 *2 C   u0 r0 {2,S} {3,S} {5,S} {6,[S,D,T,B]}
2 *3 C   u1 r0 {1,S}
3 *4 H   u0 r0 {1,S}
4 *1 O   u1 r0
5    C   u0 r0 {1,S}
6    R!H ux {1,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 15,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4]
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 26,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_N-4CHNS->C",
    group = 
"""
1 *2 C     u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C     u[1,2]     {1,[S,D,B]}
3 *4 H     u0         {1,S}
4 *1 [H,S] u[1,2,3,4]
5    R!H   ux         {1,[S,D,T,B]}
6    R!H   ux         {1,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 31,
    label = "Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {4,D}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4    C   ux         {1,D}
5 *1 C   u[1,2,3,4] {6,[S,D,T,B]}
6    R!H ux         {5,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.40019, "d13": 2.675656666666667, "d23": 1.2811333333333332},
        uncertainties = {"d12": 0.004190928200000003, "d13": 0.0006931242888888887, "d23": 0.001848173622222226},
    ),

)

entry(
    index = 38,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R",
    group = 
"""
1 *2 C         u0         {2,[S,D,B]} {3,S} {4,[S,B]}
2 *3 R!H       u[1,2]     {1,[S,D,B]}
3 *4 H         u0         {1,S}
4    C         ux         {1,[S,B]}
5 *1 [H,C,N,S] u[1,2,3,4] {6,[S,D,T,B]}
6    R!H       ux         {5,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 58,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_4CHNS->C",
    group = 
"""
1 *2 C u0         {2,[S,D,B]} {3,S} {4,[S,B]}
2 *3 C u1         {1,[S,D,B]}
3 *4 H u0         {1,S}
4    C u0         {1,[S,B]}
5 *1 C u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.4378, "d13": 2.67212, "d23": 1.24799},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 61,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_N-4CHNS->C",
    group = 
"""
1 *2 C     u0         r0 {2,S} {3,S} {5,S}
2 *3 C     u[1,2]     r0 {1,S}
3 *4 H     u0         {1,S}
4 *1 [H,S] u[1,2,3,4] r0
5    C     ux         r0 {1,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 69,
    label = "Root_Ext-2R!H-R_N-2R!H->C_N-4R->H_4CNO->O",
    group = 
"""
1 *2 C u0 {2,[S,D,B]} {3,S}
2 *3 N u1 {1,[S,D,B]} {5,S}
3 *4 H u0 r0 {1,S}
4 *1 O u1
5    O u0 r0 {2,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 70,
    label = "Root_Ext-2R!H-R_N-2R!H->C_N-4R->H_N-4CNO->O",
    group = 
"""
1 *2 C     u0         {2,D} {3,S}
2 *3 N     u[1,2]     {1,D} {5,[S,D,T,B]}
3 *4 H     u0         {1,S}
4 *1 [C,N] u[1,2,3,4]
5    O     ux         {2,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 76,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O",
    group = 
"""
1 *2 O   u0         {2,S} {3,S}
2 *3 R!H u1         {1,S}
3 *4 H   u0         {1,S}
4 *1 H   u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.22693, "d13": 2.10178, "d23": 0.881007},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 79,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O",
    group = 
"""
1 *2 [C,N] u0         {2,S} {3,S}
2 *3 R!H   u1         {1,S}
3 *4 H     u0         {1,S}
4 *1 H     u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.3206950000000002, "d13": 2.286665, "d23": 0.967163},
        uncertainties = {"d12": 0.0010552752249999992, "d13": 0.0002153556249999998, "d23": 0.002112965089000003},
    ),

)

entry(
    index = 94,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C",
    group = 
"""
1 *2 N u0     {2,D} {3,S}
2 *3 C u[1,2] {1,D}
3 *4 H u0     r0 {1,S}
4 *1 H u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 95,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C",
    group = 
"""
1 *2 N u0     {2,D} {3,S}
2 *3 N u[1,2] {1,D}
3 *4 H u0     r0 {1,S}
4 *1 H u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 99,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C",
    group = 
"""
1 *2 O         u0     {2,[S,D,B]} {3,S}
2 *3 C         u[1,2] {1,[S,D,B]}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.4936299999999998, "d13": 2.5316441666666663, "d23": 1.0576194166666668},
        uncertainties = {"d12": 0.01955371123333333, "d13": 0.006102050424305556, "d23": 0.0067686865110763855},
    ),

)

entry(
    index = 120,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C",
    group = 
"""
1 *2 O         u0     {2,[S,D,B]} {3,S}
2 *3 [N,O,S]   u[1,2] {1,[S,D,B]}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 136,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 R!H     u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 O       u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.45168, "d13": 2.5406050000000002, "d23": 1.1067},
        uncertainties = {"d12": 0.018130622500000013, "d13": 0.010921295024999968, "d23": 0.0018481401000000073},
    ),

)

entry(
    index = 168,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 R!H     u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.378778888888889, "d13": 2.6925233333333334, "d23": 1.3366955555555555},
        uncertainties = {"d12": 0.00819361200987654, "d13": 0.0010168385111111117, "d23": 0.00799747582469136},
    ),

)

entry(
    index = 211,
    label = "Root_N-4R->H_N-4CNOS-u1_1R!H->O_4CNOS->C",
    group = 
"""
1 *2 O   u0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 r0 {1,S}
4 *1 C   u2

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 212,
    label = "Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C",
    group = 
"""
1 *2 O   u0     {2,[S,D,B]} {3,S}
2 *3 R!H u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 O   u2    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 216,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS",
    group = 
"""
1 *2 [C,N,S]   u0     {2,S} {3,S}
2 *3 R!H       u[1,2] {1,S}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u2    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 227,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS",
    group = 
"""
1 *2 [C,N,S] u0     {2,D} {3,S}
2 *3 R!H     u[1,2] {1,D}
3 *4 H       u0     {1,S}
4 *1 O       u2    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 5,
    label = "Root_Ext-1R!H-R_4R->O_Ext-4O-R_Sp-5R!H-1R!H_Ext-5R!H-R",
    group = 
"""
1 *2 C u0     {2,S} {3,S} {4,S}
2    C ux     {1,S} {5,[S,D,T,B]}
3 *3 C u[1,2] {1,S}
4 *4 H u0     {1,S}
5    C ux     {2,[S,D,T,B]}
6 *1 O u1     {7,[S,D,T,B]}
7    O ux     {6,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.53044, "d13": 2.61048, "d23": 1.08408},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 8,
    label = "Root_Ext-1R!H-R_4R->O_Ext-4O-R_Sp-5R!H-1R!H_Ext-1R!H-R",
    group = 
"""
1 *2 C u0 r0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 r0 {1,S}
3 *4 H u0 r0 {1,S}
4    C u0 r0 {1,S}
5    C u0 r0 {1,S}
6 *1 O u1 r0 {7,S}
7    O u1 r0 {6,S}

""",
    distances = DistanceData(
        distances = {"d12": 1.49728, "d13": 2.58356, "d23": 1.09868},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 16,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {7,[S,D,T,B]}
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}
7    R!H ux         {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 27,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_N-4CHNS->C_4HS->H",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         r0 {1,S}
4 *1 H   u[1,2,3,4]
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 28,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_N-4CHNS->C_N-4HS->H",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 S   u[1,2,3,4]
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 32,
    label = "Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R_Ext-6R!H-R",
    group = 
"""
1 *2 C   u0         {3,[S,D,B]} {4,S} {5,D}
2    C   u0         r0 {6,[S,D,T,B]} {7,[S,D,T,B]}
3 *3 C   u[1,2]     {1,[S,D,B]}
4 *4 H   u0         {1,S}
5    C   ux         {1,D}
6 *1 C   u[1,2,3,4] {2,[S,D,T,B]}
7    R!H ux         {2,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.44292, "d13": 2.68952, "d23": 1.251105},
        uncertainties = {"d12": 0.0008088336000000012, "d13": 0.0004631103999999993, "d23": 6.715802500000103e-05},
    ),

)

entry(
    index = 33,
    label = "Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R_Ext-4CHNS-R",
    group = 
"""
1 *2 C   u0 {3,S} {4,S} {5,D}
2 *1 C   u1 {6,[S,D,T,B]} {7,[S,D,T,B]}
3 *3 C   u1 {1,S}
4 *4 H   u0 {1,S}
5    C   u0 {1,D}
6    R!H ux {2,[S,D,T,B]}
7    R!H ux {2,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 35,
    label = "Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R_Sp-6R!H-4CHNS",
    group = 
"""
1 *2 C u0         {2,[S,D,B]} {3,S} {4,D}
2 *3 C u[1,2]     {1,[S,D,B]}
3 *4 H u0         {1,S}
4    C ux         {1,D}
5 *1 C u[1,2,3,4] {6,S}
6    C ux         {5,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 36,
    label = "Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R_N-Sp-6R!H-4CHNS",
    group = 
"""
1 *2 C u0         {2,[S,D,B]} {3,S} {4,D}
2 *3 C u[1,2]     {1,[S,D,B]}
3 *4 H u0         {1,S}
4    C ux         {1,D}
5 *1 C u[1,2,3,4] {6,D}
6    C ux         {5,D}

""",
    distances = DistanceData(
        distances = {"d12": 1.31473, "d13": 2.64793, "d23": 1.34119},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 39,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_6R!H->S",
    group = 
"""
1 *2 C         u0         {2,S} {3,S} {5,S}
2 *3 C         u1         {1,S}
3 *4 H         u0         {1,S}
4 *1 [H,C,N,S] u[1,2,3,4] {6,S}
5    C         u0         {1,S}
6    S         ux         {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 41,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S",
    group = 
"""
1 *2 C                      u0         {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 R!H                    u[1,2]     {1,[S,D,B]}
3 *4 H                      u0         {1,S}
4 *1 [H,C,N,S]              u[1,2,3,4] {6,[S,D,T,B]}
5    C                      ux         {1,[S,B]}
6    [I,Br,F,Cl,O,P,C,N,Si] ux         {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 59,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_4CHNS->C_4C-u1",
    group = 
"""
1 *2 C u0 {2,[S,D,B]} {3,S} {4,[S,B]}
2 *3 C u1 {1,[S,D,B]}
3 *4 H u0 r0 {1,S}
4    C u0 {1,[S,B]}
5 *1 C u1

""",
    distances = DistanceData(
        distances = {"d12": 1.4378, "d13": 2.67212, "d23": 1.24799},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 60,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_4CHNS->C_N-4C-u1",
    group = 
"""
1 *2 C u0 {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 C u1 {1,[S,D,B]}
3 *4 H u0 r0 {1,S}
4 *1 C u2
5    C u0 {1,[S,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 71,
    label = "Root_Ext-2R!H-R_N-2R!H->C_N-4R->H_N-4CNO->O_4CN->C",
    group = 
"""
1 *2 C u0         r0 {2,D} {3,S}
2 *3 N u[1,2]     r0 {1,D} {5,[S,D,T,B]}
3 *4 H u0         {1,S}
4 *1 C u[1,2,3,4] r0
5    O ux         {2,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 72,
    label = "Root_Ext-2R!H-R_N-2R!H->C_N-4R->H_N-4CNO->O_N-4CN->C",
    group = 
"""
1 *2 C u0         r0 {2,D} {3,S}
2 *3 N u[1,2]     r0 {1,D} {5,[S,D,T,B]}
3 *4 H u0         {1,S}
4 *1 N u[1,2,3,4] r0
5    O ux         {2,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 77,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_2R!H->C",
    group = 
"""
1 *2 O u0         r0 {2,S} {3,S}
2 *3 C u1         r0 {1,S}
3 *4 H u0         {1,S}
4 *1 H u[1,2,3,4] r0

""",
    distances = DistanceData(
        distances = {"d12": 1.22693, "d13": 2.10178, "d23": 0.881007},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 78,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_N-2R!H->C",
    group = 
"""
1 *2 O     u0         r0 {2,S} {3,S}
2 *3 [N,O] u1         r0 {1,S}
3 *4 H     u0         {1,S}
4 *1 H     u[1,2,3,4] r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 80,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C",
    group = 
"""
1 *2 C   u0         {2,S} {3,S}
2 *3 R!H u1         {1,S}
3 *4 H   u0         {1,S}
4 *1 H   u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.3206950000000002, "d13": 2.286665, "d23": 0.967163},
        uncertainties = {"d12": 0.0010552752249999992, "d13": 0.0002153556249999998, "d23": 0.002112965089000003},
    ),

)

entry(
    index = 85,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C",
    group = 
"""
1 *2 N   u0         {2,S} {3,S}
2 *3 R!H u1         {1,S}
3 *4 H   u0         {1,S}
4 *1 H   u[1,2,3,4]

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 100,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R",
    group = 
"""
1 *2 O         u0     {2,[S,D,B]} {3,S}
2 *3 C         u[1,2] {1,[S,D,B]}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u1     {5,[S,D,T,B]}
5    R!H       ux     {4,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.516341818181818, "d13": 2.535232727272727, "d23": 1.0397002727272726},
        uncertainties = {"d12": 0.015141401123966941, "d13": 0.006502249074380167, "d23": 0.003530873014198348},
    ),

)

entry(
    index = 118,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_4CNOS->C",
    group = 
"""
1 *2 O u0     {2,[S,D,B]} {3,S}
2 *3 C u[1,2] {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 C u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.2438, "d13": 2.49217, "d23": 1.25473},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 119,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_N-4CNOS->C",
    group = 
"""
1 *2 O u0     {2,[S,D,B]} {3,S}
2 *3 C u[1,2] {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 O u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 121,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O",
    group = 
"""
1 *2 O       u0     {2,[S,D,B]} {3,S}
2 *3 [N,O,S] u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 O       u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 125,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O",
    group = 
"""
1 *2 O       u0     {2,[S,D,B]} {3,S}
2 *3 [N,O,S] u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N]   u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 137,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 R!H     u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 O       u1     {5,[S,D,T,B]}
5    O       ux     {4,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.58633, "d13": 2.64511, "d23": 1.06371},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 152,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS",
    group = 
"""
1 *2 [C,N,S] u0     {2,S} {3,S}
2 *3 R!H     u[1,2] {1,S}
3 *4 H       u0     {1,S}
4 *1 O       u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 163,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS",
    group = 
"""
1 *2 [C,N,S] u0     {2,D} {3,S}
2 *3 R!H     u[1,2] {1,D}
3 *4 H       u0     {1,S}
4 *1 O       u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.31703, "d13": 2.4361, "d23": 1.14969},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 169,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 R!H     u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     {5,[S,D,T,B]}
5    R!H     ux     {4,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.3790383333333331, "d13": 2.6901049999999995, "d23": 1.3398599999999998},
        uncertainties = {"d12": 0.005238436647222223, "d13": 0.001365216724999999, "d23": 0.006445947333333334},
    ),

)

entry(
    index = 185,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 R!H     u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 C       u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.3782599999999998, "d13": 2.69736, "d23": 1.3303666666666665},
        uncertainties = {"d12": 0.014103558866666657, "d13": 0.0002849920666666687, "d23": 0.011040450555555562},
    ),

)

entry(
    index = 200,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 R!H     u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 N       u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 213,
    label = "Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_2R!H->C",
    group = 
"""
1 *2 O u0     r0 {2,[S,D,B]} {3,S}
2 *3 C u[1,2] r0 {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 O u2     r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 214,
    label = "Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_N-2R!H->C",
    group = 
"""
1 *2 O u0     r0 {2,[S,D,B]} {3,S}
2 *3 N u[1,2] r0 {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 O u2     r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 217,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C",
    group = 
"""
1 *2 C         u0 {2,S} {3,S}
2 *3 R!H       u1 {1,S}
3 *4 H         u0 {1,S}
4 *1 [C,O,N,S] u2

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 220,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C",
    group = 
"""
1 *2 N   u0     {2,S} {3,S}
2 *3 R!H u[1,2] {1,S}
3 *4 H   u0     {1,S}
4 *1 O   u2    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 228,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C",
    group = 
"""
1 *2 C   u0 r0 {2,D} {3,S}
2 *3 R!H u1 r0 {1,D}
3 *4 H   u0 {1,S}
4 *1 O   u2 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 229,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C",
    group = 
"""
1 *2 N   u0     {2,D} {3,S}
2 *3 R!H u[1,2] {1,D}
3 *4 H   u0     {1,S}
4 *1 O   u2    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 6,
    label = "Root_Ext-1R!H-R_4R->O_Ext-4O-R_Sp-5R!H-1R!H_Ext-5R!H-R_Ext-1R!H-R",
    group = 
"""
1 *2 C u0     {2,S} {3,S} {5,S} {8,S}
2 *3 C u[1,2] {1,S}
3 *4 H u0     {1,S}
4 *1 O u1     {6,[S,D,T,B]}
5    C ux     {1,S} {7,[S,D,T,B]}
6    O ux     {4,[S,D,T,B]}
7    C ux     {5,[S,D,T,B]}
8    C u0     {1,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 17,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_Sp-7R!H#4C",
    group = 
"""
1 *2 C   u0 r0 {2,S} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u1 r0 {1,S}
3 *4 H   u0 {1,S}
4 *1 C   u1 r0 {7,T}
5    R!H ux {1,[S,D,T,B]}
6    R!H ux {1,[S,D,T,B]}
7    R!H u0 r0 {4,T}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 18,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {7,[S,D,B]}
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}
7    R!H ux         {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 29,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_N-4CHNS->C_N-4HS->H_Ext-4S-R_Ext-7R!H-R",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         r0 {1,S}
4 *1 S   u[1,2,3,4] {7,S}
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}
7    C   u0         r0 {4,S} {8,[S,D,T,B]}
8    R!H ux         {7,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 34,
    label = "Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R_Ext-4CHNS-R_Ext-4CHNS-R",
    group = 
"""
1 *2 C   u0 r0 {2,S} {3,S} {5,D}
2 *3 C   u1 r0 {1,S}
3 *4 H   u0 r0 {1,S}
4 *1 C   u1 r0 {6,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0 r0 {1,D}
6    R!H ux {4,[S,D,T,B]}
7    R!H ux {4,[S,D,T,B]}
8    R!H ux {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 40,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_6R!H->S_Ext-2R!H-R",
    group = 
"""
1 *2 C         u0         r0 {2,S} {3,S} {5,S}
2 *3 C         u1         r0 {1,S} {7,[S,D,T,B]}
3 *4 H         u0         r0 {1,S}
4 *1 [H,C,N,S] u[1,2,3,4] r0 {6,S}
5    C         u0         r0 {1,S}
6    S         ux         r0 {4,S}
7    R!H       ux         {2,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 42,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C",
    group = 
"""
1 *2 C                      u0         {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 R!H                    u[1,2]     {1,[S,D,B]}
3 *4 H                      u0         {1,S}
4 *1 C                      u[1,2,3,4] {6,[S,D,T,B]}
5    C                      ux         {1,[S,B]}
6    [I,Br,F,Cl,O,P,C,N,Si] ux         {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 57,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_N-4CHNS->C",
    group = 
"""
1 *2 C                      u0         {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 R!H                    u1         {1,[S,D,B]}
3 *4 H                      u0         r0 {1,S}
4 *1 S                      u[1,2,3,4] {6,[S,D,T,B]}
5    C                      u0         {1,[S,B]}
6    [I,Br,F,Cl,O,P,C,N,Si] ux         {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 81,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_2R!H->C",
    group = 
"""
1 *2 C u0 {2,S} {3,S}
2 *3 C u1 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 H u1

""",
    distances = DistanceData(
        distances = {"d12": 1.35318, "d13": 2.27199, "d23": 0.921196},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 82,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C",
    group = 
"""
1 *2 C     u0         {2,S} {3,S}
2 *3 [N,O] u1         {1,S}
3 *4 H     u0         {1,S}
4 *1 H     u[1,2,3,4]

""",
    distances = DistanceData(
        distances = {"d12": 1.28821, "d13": 2.30134, "d23": 1.01313},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 86,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_2R!H->C",
    group = 
"""
1 *2 N u0 {2,S} {3,S}
2 *3 C u1 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 H u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 87,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C",
    group = 
"""
1 *2 N     u0         {2,S} {3,S}
2 *3 [N,O] u1         {1,S}
3 *4 H     u0         {1,S}
4 *1 H     u[1,2,3,4]

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 101,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS",
    group = 
"""
1 *2 O   u0     {2,[S,D,B]} {3,S}
2 *3 C   u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 C   u1     {5,D}
5    R!H u0     {4,D}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 104,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS",
    group = 
"""
1 *2 O         u0     {2,[S,D,B]} {3,S}
2 *3 C         u[1,2] {1,[S,D,B]}
3 *4 H         u0     {1,S}
4 *1 [C,O,N,S] u1     {5,[S,T,B]}
5    R!H       ux     {4,[S,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.516341818181818, "d13": 2.535232727272727, "d23": 1.0397002727272726},
        uncertainties = {"d12": 0.015141401123966941, "d13": 0.006502249074380167, "d23": 0.003530873014198348},
    ),

)

entry(
    index = 122,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R",
    group = 
"""
1 *2 O       u0     {2,[S,D,B]} {3,S}
2 *3 [N,O,S] u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 O       u1     {5,S}
5    R!H     u0     {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 126,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_4CN->C",
    group = 
"""
1 *2 O       u0 {2,S} {3,S}
2 *3 [N,O,S] u1 {1,S}
3 *4 H       u0 r0 {1,S}
4 *1 C       u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 127,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C",
    group = 
"""
1 *2 O       u0     {2,[S,D,B]} {3,S}
2 *3 [N,O,S] u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 N       u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 138,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 R!H     u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 O       u1     {5,[S,D,T,B]}
5    O       u0     {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 147,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0",
    group = 
"""
1 *2 [C,N,S] u0       {2,[S,D,B]} {3,S}
2 *3 R!H     u[1,2]   {1,[S,D,B]}
3 *4 H       u0       {1,S}
4 *1 O       u1       {5,[S,D,T,B]}
5    O       u[1,2,3] {4,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.58633, "d13": 2.64511, "d23": 1.06371},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 153,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C",
    group = 
"""
1 *2 C   u0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
4 *1 O   u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 156,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C",
    group = 
"""
1 *2 N   u0     {2,S} {3,S}
2 *3 R!H u[1,2] {1,S}
3 *4 H   u0     {1,S}
4 *1 O   u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 164,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_1CNS->C",
    group = 
"""
1 *2 C   u0 r0 {2,D} {3,S}
2 *3 R!H u1 r0 {1,D}
3 *4 H   u0 r0 {1,S}
4 *1 O   u1 r0

""",
    distances = DistanceData(
        distances = {"d12": 1.31703, "d13": 2.4361, "d23": 1.14969},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 165,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C",
    group = 
"""
1 *2 N   u0     {2,D} {3,S}
2 *3 R!H u[1,2] {1,D}
3 *4 H   u0     {1,S}
4 *1 O   u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 170,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS",
    group = 
"""
1 *2 [C,N,S] u0 {2,[S,D,B]} {3,S}
2 *3 R!H     u1 {1,[S,D,B]}
3 *4 H       u0 r0 {1,S}
4 *1 [C,N,S] u1 {5,T}
5    R!H     u0 r0 {4,T}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 171,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 R!H     u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     {5,[S,D,B]}
5    R!H     ux     {4,[S,D,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.3790383333333331, "d13": 2.6901049999999995, "d23": 1.3398599999999998},
        uncertainties = {"d12": 0.005238436647222223, "d13": 0.001365216724999999, "d23": 0.006445947333333334},
    ),

)

entry(
    index = 186,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C",
    group = 
"""
1 *2 C   u0     {2,[S,D,B]} {3,S}
2 *3 R!H u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 C   u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.3782599999999998, "d13": 2.69736, "d23": 1.3303666666666665},
        uncertainties = {"d12": 0.014103558866666657, "d13": 0.0002849920666666687, "d23": 0.011040450555555562},
    ),

)

entry(
    index = 191,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C",
    group = 
"""
1 *2 N   u0     {2,[S,D,B]} {3,S}
2 *3 R!H u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 C   u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 201,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS",
    group = 
"""
1 *2 N   u0     {2,S} {3,S}
2 *3 R!H u[1,2] {1,S}
3 *4 H   u0     {1,S}
4 *1 N   u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 206,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS",
    group = 
"""
1 *2 [C,N,S] u0 {2,D} {3,S}
2 *3 N       u1 {1,D}
3 *4 H       u0 {1,S}
4 *1 N       u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 218,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C",
    group = 
"""
1 *2 C         u0 {2,S} {3,S}
2 *3 C         u1 {1,S}
3 *4 H         u0 r0 {1,S}
4 *1 [C,O,N,S] u2

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 219,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C",
    group = 
"""
1 *2 C         u0 {2,S} {3,S}
2 *3 [N,O]     u1 {1,S}
3 *4 H         u0 r0 {1,S}
4 *1 [C,O,N,S] u2

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 221,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->C",
    group = 
"""
1 *2 N u0     {2,S} {3,S}
2 *3 C u[1,2] {1,S}
3 *4 H u0     r0 {1,S}
4 *1 O u2    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 222,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C",
    group = 
"""
1 *2 N     u0     {2,S} {3,S}
2 *3 [N,O] u[1,2] {1,S}
3 *4 H     u0     {1,S}
4 *1 O     u2    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 230,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C",
    group = 
"""
1 *2 N u0     {2,D} {3,S}
2 *3 C u[1,2] {1,D}
3 *4 H u0     r0 {1,S}
4 *1 O u2    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 231,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C",
    group = 
"""
1 *2 N u0     {2,D} {3,S}
2 *3 N u[1,2] {1,D}
3 *4 H u0     r0 {1,S}
4 *1 O u2    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 7,
    label = "Root_Ext-1R!H-R_4R->O_Ext-4O-R_Sp-5R!H-1R!H_Ext-5R!H-R_Ext-1R!H-R_Ext-8R!H-R",
    group = 
"""
1 *2 C   u0     r0 {2,S} {3,S} {5,S} {8,S}
2 *3 C   u[1,2] r0 {1,S}
3 *4 H   u0     r0 {1,S}
4 *1 O   u1     r0 {6,[S,D,T,B]}
5    C   ux     r0 {1,S} {7,[S,D,T,B]}
6    O   ux     {4,[S,D,T,B]}
7    C   ux     {5,[S,D,T,B]}
8    C   u0     r0 {1,S} {9,[S,D,T,B]}
9    R!H ux     {8,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 19,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {7,[S,D,B]}
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}
7    C   ux         {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 25,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         r0 {1,S}
4 *1 C   u[1,2,3,4] {7,[S,D,B]}
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}
7    O   ux         {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 43,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C",
    group = 
"""
1 *2 C                      u0     {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 R!H                    u[1,2] {1,[S,D,B]}
3 *4 H                      u0     {1,S}
4 *1 C                      u1     {6,T}
5    C                      ux     {1,[S,B]}
6    [I,Br,F,Cl,O,P,C,N,Si] u0     {4,T}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 44,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C",
    group = 
"""
1 *2 C                      u0         {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 R!H                    u[1,2]     {1,[S,D,B]}
3 *4 H                      u0         {1,S}
4 *1 C                      u[1,2,3,4] {6,[S,D,B]}
5    C                      ux         {1,[S,B]}
6    [I,Br,F,Cl,O,P,C,N,Si] ux         {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 83,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_2NO->N",
    group = 
"""
1 *2 C u0         r0 {2,S} {3,S}
2 *3 N u1         r0 {1,S}
3 *4 H u0         {1,S}
4 *1 H u[1,2,3,4] r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 84,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->N",
    group = 
"""
1 *2 C u0         r0 {2,S} {3,S}
2 *3 O u1         r0 {1,S}
3 *4 H u0         {1,S}
4 *1 H u[1,2,3,4] r0

""",
    distances = DistanceData(
        distances = {"d12": 1.28821, "d13": 2.30134, "d23": 1.01313},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 88,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->N",
    group = 
"""
1 *2 N u0         r0 {2,S} {3,S}
2 *3 N u1         r0 {1,S}
3 *4 H u0         {1,S}
4 *1 H u[1,2,3,4] r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 89,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->N",
    group = 
"""
1 *2 N u0         r0 {2,S} {3,S}
2 *3 O u1         r0 {1,S}
3 *4 H u0         {1,S}
4 *1 H u[1,2,3,4] r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 102,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_5R!H->C",
    group = 
"""
1 *2 O u0     r0 {2,[S,D,B]} {3,S}
2 *3 C u[1,2] r0 {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 C u1     r0 {5,D}
5    C u0     {4,D}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 103,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_N-5R!H->C",
    group = 
"""
1 *2 O u0     r0 {2,[S,D,B]} {3,S}
2 *3 C u[1,2] r0 {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 C u1     r0 {5,D}
5    O u0     {4,D}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 105,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R",
    group = 
"""
1 *2 O   u0 {2,S} {3,S}
2 *3 C   u1 {1,S}
3 *4 H   u0 {1,S}
4 *1 C   u1 {5,S} {6,[S,D,T,B]}
5    C   u0 {4,S}
6    R!H ux {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 107,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-5R!H-R",
    group = 
"""
1 *2 O         u0     {3,[S,D,B]} {4,S}
2    R!H       ux     {5,[S,T,B]} {6,[S,D,T,B]}
3 *3 C         u[1,2] {1,[S,D,B]}
4 *4 H         u0     {1,S}
5 *1 [C,O,N,S] u1     {2,[S,T,B]}
6    R!H       ux     {2,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 108,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C",
    group = 
"""
1 *2 O   u0     {2,[S,D,B]} {3,S}
2 *3 C   u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 C   u1     {5,[S,T,B]}
5    R!H ux     {4,[S,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.35102, "d13": 2.54318, "d23": 1.21249},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 113,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C",
    group = 
"""
1 *2 O   u0     {2,[S,D,B]} {3,S}
2 *3 C   u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 O   u1     {5,[S,T,B]}
5    R!H ux     {4,[S,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.532874, "d13": 2.5344379999999997, "d23": 1.0224213},
        uncertainties = {"d12": 0.013649097844000002, "d13": 0.007145526476000001, "d23": 0.0005997684320099998},
    ),

)

entry(
    index = 123,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_2NOS->N",
    group = 
"""
1 *2 O   u0     r0 {2,[S,D,B]} {3,S}
2 *3 N   u[1,2] r0 {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 O   u1     r0 {5,S}
5    R!H u0     r0 {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 124,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_N-2NOS->N",
    group = 
"""
1 *2 O   u0     r0 {2,[S,D,B]} {3,S}
2 *3 O   u[1,2] r0 {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 O   u1     r0 {5,S}
5    R!H u0     r0 {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 128,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R",
    group = 
"""
1 *2 O   u0     {2,[S,D,B]} {3,S}
2 *3 O   u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 N   u1     {5,[S,D,T,B]}
5    R!H ux     {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 133,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_2NOS->N",
    group = 
"""
1 *2 O u0     {2,[S,D,B]} {3,S}
2 *3 N u[1,2] {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 N u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 134,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_N-2NOS->N",
    group = 
"""
1 *2 O u0     {2,[S,D,B]} {3,S}
2 *3 O u[1,2] {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 N u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 139,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS",
    group = 
"""
1 *2 N   u0     {2,S} {3,S}
2 *3 R!H u[1,2] {1,S}
3 *4 H   u0     {1,S}
4 *1 O   u1     {5,[S,D,T,B]}
5    O   u0     {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 144,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS",
    group = 
"""
1 *2 [C,N,S] u0 {2,D} {3,S}
2 *3 N       u1 {1,D}
3 *4 H       u0 {1,S}
4 *1 O       u1 {5,S}
5    O       u0 {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 148,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_Sp-2R!H-1CNS",
    group = 
"""
1 *2 [C,N,S] u0 r0 {2,S} {3,S}
2 *3 R!H     u1 r0 {1,S}
3 *4 H       u0 {1,S}
4 *1 O       u1 r0 {5,[S,D,T,B]}
5    O       u1 {4,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.58633, "d13": 2.64511, "d23": 1.06371},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 149,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS",
    group = 
"""
1 *2 [C,N,S] u0       {2,D} {3,S}
2 *3 R!H     u[1,2]   {1,D}
3 *4 H       u0       {1,S}
4 *1 O       u1       {5,S}
5    O       u[1,2,3] {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 154,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C",
    group = 
"""
1 *2 C u0 {2,S} {3,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4 *1 O u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 155,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C",
    group = 
"""
1 *2 C     u0 {2,S} {3,S}
2 *3 [N,O] u1 {1,S}
3 *4 H     u0 {1,S}
4 *1 O     u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 157,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N",
    group = 
"""
1 *2 N u0     {2,S} {3,S}
2 *3 N u[1,2] {1,S}
3 *4 H u0     {1,S}
4 *1 O u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 160,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N",
    group = 
"""
1 *2 N     u0 {2,S} {3,S}
2 *3 [C,O] u1 {1,S}
3 *4 H     u0 {1,S}
4 *1 O     u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 166,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C",
    group = 
"""
1 *2 N u0     {2,D} {3,S}
2 *3 C u[1,2] {1,D}
3 *4 H u0     {1,S}
4 *1 O u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 167,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C",
    group = 
"""
1 *2 N u0     {2,D} {3,S}
2 *3 N u[1,2] {1,D}
3 *4 H u0     {1,S}
4 *1 O u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 172,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_2R!H->S",
    group = 
"""
1 *2 [C,N,S] u0     r0 {2,[S,D,B]} {3,S}
2 *3 S       u[1,2] r0 {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     r0 {5,[S,D,B]}
5    R!H     ux     {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 173,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 [C,N]   u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     {5,[S,D,B]}
5    R!H     ux     {4,[S,D,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.4059499999999998, "d13": 2.6743966666666665, "d23": 1.28892},
        uncertainties = {"d12": 0.0088884206, "d13": 0.00048234215555555577, "d23": 0.006612655266666669},
    ),

)

entry(
    index = 187,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C",
    group = 
"""
1 *2 C   u0     {2,S} {3,S}
2 *3 R!H u[1,2] {1,S}
3 *4 H   u0     {1,S}
4 *1 C   u1    

""",
    distances = DistanceData(
        distances = {"d12": 1.2947549999999999, "d13": 2.6933350000000003, "d23": 1.4019249999999999},
        uncertainties = {"d12": 0.00023608322499999883, "d13": 0.0003788862250000025, "d23": 0.0011988906250000012},
    ),

)

entry(
    index = 190,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_N-Sp-2R!H-1C",
    group = 
"""
1 *2 C   u0 {2,D} {3,S}
2 *3 R!H u1 {1,D}
3 *4 H   u0 {1,S}
4 *1 C   u1

""",
    distances = DistanceData(
        distances = {"d12": 1.54527, "d13": 2.70541, "d23": 1.18725},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 192,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C",
    group = 
"""
1 *2 N u0 {2,[S,D,B]} {3,S}
2 *3 C u1 {1,[S,D,B]}
3 *4 H u0 {1,S}
4 *1 C u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 195,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C",
    group = 
"""
1 *2 N     u0     {2,[S,D,B]} {3,S}
2 *3 [N,O] u[1,2] {1,[S,D,B]}
3 *4 H     u0     {1,S}
4 *1 C     u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 202,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->N",
    group = 
"""
1 *2 N u0     {2,S} {3,S}
2 *3 N u[1,2] {1,S}
3 *4 H u0     {1,S}
4 *1 N u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 205,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->N",
    group = 
"""
1 *2 N u0     {2,S} {3,S}
2 *3 O u[1,2] {1,S}
3 *4 H u0     {1,S}
4 *1 N u1    

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 207,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_1CNS->C",
    group = 
"""
1 *2 C u0 {2,D} {3,S}
2 *3 N u1 {1,D}
3 *4 H u0 {1,S}
4 *1 N u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 208,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_N-1CNS->C",
    group = 
"""
1 *2 N u0 {2,D} {3,S}
2 *3 N u1 {1,D}
3 *4 H u0 {1,S}
4 *1 N u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 223,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1",
    group = 
"""
1 *2 N     u0 {2,S} {3,S}
2 *3 [N,O] u1 {1,S}
3 *4 H     u0 {1,S}
4 *1 O     u2

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 226,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_N-2NO-u1",
    group = 
"""
1 *2 N     u0 r0 {2,S} {3,S}
2 *3 [N,O] u2 r0 {1,S}
3 *4 H     u0 {1,S}
4 *1 O     u2 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 20,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {7,S} {8,[S,D,T,B]}
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}
7    C   ux         {4,S}
8    R!H ux         {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 22,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {7,[S,D,B]}
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}
7    C   ux         {4,[S,D,B]} {8,[S,D,T,B]}
8    R!H ux         {7,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 23,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {7,S}
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}
7    C   ux         {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 24,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {7,D}
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}
7    C   ux         {4,D}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 45,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 R!H u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {6,[S,D,B]}
5    C   ux         {1,[S,B]}
6    C   ux         {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 56,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_N-6BrCClFINOPSi->C",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 R!H u1         {1,[S,D,B]}
3 *4 H   u0         r0 {1,S}
4 *1 C   u[1,2,3,4] {6,[S,D,B]}
5    C   u0         {1,[S,B]}
6    O   ux         {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 106,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R_Ext-4CNOS-R",
    group = 
"""
1 *2 O   u0 {2,S} {3,S}
2 *3 C   u1 {1,S}
3 *4 H   u0 r0 {1,S}
4 *1 C   u1 {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
5    C   u0 r0 {4,S}
6    R!H ux {4,[S,D,T,B]}
7    R!H ux {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 109,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C",
    group = 
"""
1 *2 O   u0     {2,[S,D,B]} {3,S}
2 *3 C   u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 C   u1     {5,S}
5    R!H ux     {4,S}

""",
    distances = DistanceData(
        distances = {"d12": 1.35102, "d13": 2.54318, "d23": 1.21249},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 112,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_N-Sp-5R!H-4C",
    group = 
"""
1 *2 O   u0 r0 {2,S} {3,S}
2 *3 C   u1 r0 {1,S}
3 *4 H   u0 r0 {1,S}
4 *1 C   u1 r0 {5,T}
5    R!H u0 r0 {4,T}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 114,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0",
    group = 
"""
1 *2 O   u0     {2,[S,D,B]} {3,S}
2 *3 C   u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 O   u1     {5,[S,T,B]}
5    R!H u0     {4,[S,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.29893, "d13": 2.36347, "d23": 1.07742},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 117,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_N-5R!H-u0",
    group = 
"""
1 *2 O   u0 r0 {2,S} {3,S}
2 *3 C   u1 r0 {1,S}
3 *4 H   u0 r0 {1,S}
4 *1 O   u1 r0 {5,S}
5    R!H u1 r0 {4,S}

""",
    distances = DistanceData(
        distances = {"d12": 1.5588677777777777, "d13": 2.5534344444444446, "d23": 1.0163103333333332},
        uncertainties = {"d12": 0.008408899439506172, "d13": 0.004330824846913578, "d23": 0.0002929702328888885},
    ),

)

entry(
    index = 129,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_5R!H->N",
    group = 
"""
1 *2 O u0 {2,S} {3,S}
2 *3 O u1 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 N u1 {5,[S,D,T,B]}
5    N u0 r0 {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 130,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N",
    group = 
"""
1 *2 O                      u0     {2,[S,D,B]} {3,S}
2 *3 O                      u[1,2] {1,[S,D,B]}
3 *4 H                      u0     {1,S}
4 *1 N                      u1     {5,[S,D,T,B]}
5    [I,Br,F,Cl,O,P,S,C,Si] ux     {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 140,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->N",
    group = 
"""
1 *2 N u0     {2,S} {3,S}
2 *3 N u[1,2] {1,S}
3 *4 H u0     {1,S}
4 *1 O u1     {5,[S,D,T,B]}
5    O u0     {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 143,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->N",
    group = 
"""
1 *2 N u0     {2,S} {3,S}
2 *3 O u[1,2] {1,S}
3 *4 H u0     r0 {1,S}
4 *1 O u1     {5,S}
5    O u0     r0 {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 145,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C",
    group = 
"""
1 *2 C u0 {2,D} {3,S}
2 *3 N u1 {1,D}
3 *4 H u0 r0 {1,S}
4 *1 O u1 {5,S}
5    O u0 r0 {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 146,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C",
    group = 
"""
1 *2 N u0 {2,D} {3,S}
2 *3 N u1 {1,D}
3 *4 H u0 r0 {1,S}
4 *1 O u1 {5,S}
5    O u0 r0 {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 150,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C",
    group = 
"""
1 *2 C   u0       {2,D} {3,S}
2 *3 R!H u[1,2]   {1,D}
3 *4 H   u0       r0 {1,S}
4 *1 O   u1       {5,S}
5    O   u[1,2,3] r0 {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 151,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C",
    group = 
"""
1 *2 N   u0       {2,D} {3,S}
2 *3 R!H u[1,2]   {1,D}
3 *4 H   u0       r0 {1,S}
4 *1 O   u1       {5,S}
5    O   u[1,2,3] r0 {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 158,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_2N-u1",
    group = 
"""
1 *2 N u0 r0 {2,S} {3,S}
2 *3 N u1 r0 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 O u1 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 159,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_N-2N-u1",
    group = 
"""
1 *2 N u0 r0 {2,S} {3,S}
2 *3 N u2 r0 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 O u1 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 161,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_2CO->C",
    group = 
"""
1 *2 N u0 r0 {2,S} {3,S}
2 *3 C u1 r0 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 O u1 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 162,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_N-2CO->C",
    group = 
"""
1 *2 N u0 r0 {2,S} {3,S}
2 *3 O u1 r0 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 O u1 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 174,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 [C,N]   u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     {5,[S,D,B]}
5    O       ux     {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 177,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 C       u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     {5,[S,D,B]}
5    [C,S]   ux     {4,[S,D,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.4059499999999998, "d13": 2.6743966666666665, "d23": 1.28892},
        uncertainties = {"d12": 0.0088884206, "d13": 0.00048234215555555577, "d23": 0.006612655266666669},
    ),

)

entry(
    index = 188,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_2R!H->C",
    group = 
"""
1 *2 C u0     r0 {2,S} {3,S}
2 *3 C u[1,2] r0 {1,S}
3 *4 H u0     r0 {1,S}
4 *1 C u1     r0

""",
    distances = DistanceData(
        distances = {"d12": 1.31012, "d13": 2.67387, "d23": 1.3673},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 189,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_N-2R!H->C",
    group = 
"""
1 *2 C u0     r0 {2,S} {3,S}
2 *3 N u[1,2] r0 {1,S}
3 *4 H u0     r0 {1,S}
4 *1 C u1     r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 193,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_Sp-2C-1N",
    group = 
"""
1 *2 N u0 r0 {2,S} {3,S}
2 *3 C u1 r0 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 C u1 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 194,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_N-Sp-2C-1N",
    group = 
"""
1 *2 N u0 r0 {2,D} {3,S}
2 *3 C u1 r0 {1,D}
3 *4 H u0 r0 {1,S}
4 *1 C u1 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 196,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1",
    group = 
"""
1 *2 N     u0 {2,[S,D,B]} {3,S}
2 *3 [N,O] u1 {1,[S,D,B]}
3 *4 H     u0 {1,S}
4 *1 C     u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 199,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_N-2NO-u1",
    group = 
"""
1 *2 N     u0 r0 {2,S} {3,S}
2 *3 [N,O] u2 r0 {1,S}
3 *4 H     u0 r0 {1,S}
4 *1 C     u1 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 203,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->N_2N-u1",
    group = 
"""
1 *2 N u0 r0 {2,S} {3,S}
2 *3 N u1 r0 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 N u1 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 204,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->N_N-2N-u1",
    group = 
"""
1 *2 N u0 r0 {2,S} {3,S}
2 *3 N u2 r0 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 N u1 r0

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 224,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->N",
    group = 
"""
1 *2 N u0 {2,S} {3,S}
2 *3 N u1 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 O u2

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 225,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->N",
    group = 
"""
1 *2 N u0 {2,S} {3,S}
2 *3 O u1 {1,S}
3 *4 H u0 r0 {1,S}
4 *1 O u2

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 21,
    label = "Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R",
    group = 
"""
1 *2 C   u0         {2,[S,D,B]} {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 C   u[1,2]     {1,[S,D,B]}
3 *4 H   u0         r0 {1,S}
4 *1 C   u[1,2,3,4] {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
5    R!H ux         {1,[S,D,T,B]}
6    R!H ux         {1,[S,D,T,B]}
7    C   ux         {4,S}
8    R!H ux         {4,[S,D,T,B]}
9    R!H ux         {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 46,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_1R!H-inRing",
    group = 
"""
1 *2 C   u0     r1 {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 R!H u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 C   u1     {6,[S,D,B]}
5    C   ux     {1,[S,B]}
6    C   u0     {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 47,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing",
    group = 
"""
1 *2 C   u0         r0 {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 R!H u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {6,[S,D,B]}
5    C   ux         {1,[S,B]}
6    C   ux         {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 110,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_5R!H->C",
    group = 
"""
1 *2 O u0     {2,[S,D,B]} {3,S}
2 *3 C u[1,2] {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 C u1     {5,S}
5    C ux     {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 111,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_N-5R!H->C",
    group = 
"""
1 *2 O u0     {2,[S,D,B]} {3,S}
2 *3 C u[1,2] {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 C u1     {5,S}
5    O ux     {4,S}

""",
    distances = DistanceData(
        distances = {"d12": 1.35102, "d13": 2.54318, "d23": 1.21249},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 115,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_5R!H->C",
    group = 
"""
1 *2 O u0     {2,[S,D,B]} {3,S}
2 *3 C u[1,2] {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 O u1     {5,[S,T,B]}
5    C u0     {4,[S,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 116,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_N-5R!H->C",
    group = 
"""
1 *2 O u0     {2,[S,D,B]} {3,S}
2 *3 C u[1,2] {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 O u1     {5,[S,T,B]}
5    O u0     {4,[S,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.29893, "d13": 2.36347, "d23": 1.07742},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 131,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_5BrCClFIOPSSi->C",
    group = 
"""
1 *2 O u0     r0 {2,[S,D,B]} {3,S}
2 *3 O u[1,2] r0 {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 N u1     r0 {5,[S,D,T,B]}
5    C ux     {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 132,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_N-5BrCClFIOPSSi->C",
    group = 
"""
1 *2 O u0     r0 {2,[S,D,B]} {3,S}
2 *3 O u[1,2] r0 {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 N u1     r0 {5,[S,D,T,B]}
5    O ux     {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 141,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->N_2N-u1",
    group = 
"""
1 *2 N u0 r0 {2,S} {3,S}
2 *3 N u1 r0 {1,S}
3 *4 H u0 {1,S}
4 *1 O u1 r0 {5,[S,D,T,B]}
5    O u0 {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 142,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->N_N-2N-u1",
    group = 
"""
1 *2 N u0 r0 {2,S} {3,S}
2 *3 N u2 r0 {1,S}
3 *4 H u0 {1,S}
4 *1 O u1 r0 {5,[S,D,T,B]}
5    O u0 {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 175,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_1CNS->C",
    group = 
"""
1 *2 C       u0     r0 {2,[S,D,B]} {3,S}
2 *3 [C,N]   u[1,2] r0 {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     r0 {5,[S,D,B]}
5    O       ux     {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 176,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_N-1CNS->C",
    group = 
"""
1 *2 [N,S]   u0     r0 {2,[S,D,B]} {3,S}
2 *3 [C,N]   u[1,2] r0 {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     r0 {5,[S,D,B]}
5    O       ux     {4,[S,D,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 178,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS",
    group = 
"""
1 *2 [C,N,S] u0     {2,[S,D,B]} {3,S}
2 *3 C       u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     {5,S}
5    [C,S]   ux     {4,S}

""",
    distances = DistanceData(
        distances = {"d12": 1.42735, "d13": 2.7054, "d23": 1.28024},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 184,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_N-Sp-5CS-4CCNSS",
    group = 
"""
1 *2 [C,N,S] u0     r0 {2,S} {3,S}
2 *3 C       u[1,2] r0 {1,S}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     r0 {5,D}
5    [C,S]   ux     {4,D}

""",
    distances = DistanceData(
        distances = {"d12": 1.28128, "d13": 2.66051, "d23": 1.39257},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 197,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->N",
    group = 
"""
1 *2 N u0 {2,[S,D,B]} {3,S}
2 *3 N u1 {1,[S,D,B]}
3 *4 H u0 {1,S}
4 *1 C u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 198,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->N",
    group = 
"""
1 *2 N u0 {2,[S,D,B]} {3,S}
2 *3 O u1 {1,[S,D,B]}
3 *4 H u0 {1,S}
4 *1 C u1

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 48,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Ext-4C-R",
    group = 
"""
1 *2 C   u0         r0 {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 R!H u[1,2]     {1,[S,D,B]}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {6,[S,D,B]} {7,[S,D,T,B]}
5    C   ux         {1,[S,B]}
6    C   ux         {4,[S,D,B]}
7    R!H ux         {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 53,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Sp-6C-4C",
    group = 
"""
1 *2 C u0 r0 {2,S} {3,S} {5,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4 *1 C u1 {6,S}
5    C u0 {1,S}
6    C u0 {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 55,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_N-Sp-6C-4C",
    group = 
"""
1 *2 C u0         r0 {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 C u[1,2]     {1,[S,D,B]}
3 *4 H u0         {1,S}
4 *1 C u[1,2,3,4] {6,D}
5    C ux         {1,[S,B]}
6    C ux         {4,D}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 179,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R",
    group = 
"""
1 *2 C   u0     {3,S} {4,S}
2 *1 C   u1     {5,S} {6,[S,D,T,B]}
3 *3 C   u[1,2] {1,S}
4 *4 H   u0     {1,S}
5    C   ux     {2,S}
6    R!H ux     {2,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 181,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C",
    group = 
"""
1 *2 C u0 {2,S} {3,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4 *1 C u1 {5,S}
5    C u0 {4,S}

""",
    distances = DistanceData(
        distances = {"d12": 1.42735, "d13": 2.7054, "d23": 1.28024},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 183,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_N-1CNS->C",
    group = 
"""
1 *2 S       u0     {2,[S,D,B]} {3,S}
2 *3 C       u[1,2] {1,[S,D,B]}
3 *4 H       u0     {1,S}
4 *1 [C,N,S] u1     {5,S}
5    [C,S]   ux     {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 49,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Ext-4C-R_2R!H->C",
    group = 
"""
1 *2 C   u0         r0 {2,S} {3,S} {5,S}
2 *3 C   u1         {1,S}
3 *4 H   u0         {1,S}
4 *1 C   u[1,2,3,4] {6,[S,D,B]} {7,[S,D,T,B]}
5    C   u0         {1,S}
6    C   ux         {4,[S,D,B]}
7    R!H ux         {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 51,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Ext-4C-R_N-2R!H->C",
    group = 
"""
1 *2 C u0     r0 {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 S u[1,2] {1,[S,D,B]}
3 *4 H u0     {1,S}
4 *1 C u1     {6,S} {7,S}
5    C ux     {1,[S,B]}
6    C u0     {4,S}
7    C u0     {4,S}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 54,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Sp-6C-4C_Ext-6C-R",
    group = 
"""
1 *2 C   u0 r0 {2,S} {3,S} {5,S}
2 *3 C   u1 r0 {1,S}
3 *4 H   u0 r0 {1,S}
4 *1 C   u1 r0 {6,S}
5    C   u0 r0 {1,S}
6    C   u0 r0 {4,S} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 180,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R",
    group = 
"""
1 *2 C   u0     r0 {2,S} {3,S}
2 *3 C   u[1,2] r0 {1,S}
3 *4 H   u0     {1,S}
4 *1 C   u1     r0 {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
5    C   ux     {4,S}
6    R!H ux     {4,[S,D,T,B]}
7    R!H ux     {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 182,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R",
    group = 
"""
1 *2 C   u0 r0 {3,S} {4,S}
2    C   u0 r0 {5,S} {6,[S,D,T,B]}
3 *3 C   u1 r0 {1,S}
4 *4 H   u0 r0 {1,S}
5 *1 C   u1 r0 {2,S}
6    R!H ux {2,[S,D,T,B]}

""",
    distances = DistanceData(
        distances = {"d12": 1.42735, "d13": 2.7054, "d23": 1.28024},
        uncertainties = {"d12": 0.0, "d13": 0.0, "d23": 0.0},
    ),

)

entry(
    index = 50,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Ext-4C-R_2R!H->C_Ext-4C-R",
    group = 
"""
1 *2 C   u0         r0 {2,S} {3,S} {5,S}
2 *3 C   u1         r0 {1,S}
3 *4 H   u0         r0 {1,S}
4 *1 C   u[1,2,3,4] r0 {6,[S,D,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0         r0 {1,S}
6    C   ux         r0 {4,[S,D,B]}
7    R!H ux         {4,[S,D,T,B]}
8    R!H ux         {4,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)

entry(
    index = 52,
    label = "Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-6C-R",
    group = 
"""
1 *2 C   u0     r0 {2,[S,D,B]} {3,S} {5,[S,B]}
2 *3 S   u[1,2] {1,[S,D,B]}
3 *4 H   u0     {1,S}
4 *1 C   u1     {6,S} {7,S}
5    C   ux     {1,[S,B]}
6    C   u0     {4,S} {9,[S,D,T,B]}
7    C   u0     r0 {4,S} {8,D}
8    C   u0     r0 {7,D}
9    R!H ux     {6,[S,D,T,B]}

""",
    distances = DistanceData(distances={}),
)



tree(
"""
L1: Root
    L2: Root_Ext-1R!H-R
        L3: Root_Ext-1R!H-R_4R->O
            L4: Root_Ext-1R!H-R_4R->O_Ext-4O-R
                L5: Root_Ext-1R!H-R_4R->O_Ext-4O-R_Sp-5R!H-1R!H
                    L6: Root_Ext-1R!H-R_4R->O_Ext-4O-R_Sp-5R!H-1R!H_Ext-5R!H-R
                        L7: Root_Ext-1R!H-R_4R->O_Ext-4O-R_Sp-5R!H-1R!H_Ext-5R!H-R_Ext-1R!H-R
                            L8: Root_Ext-1R!H-R_4R->O_Ext-4O-R_Sp-5R!H-1R!H_Ext-5R!H-R_Ext-1R!H-R_Ext-8R!H-R
                    L6: Root_Ext-1R!H-R_4R->O_Ext-4O-R_Sp-5R!H-1R!H_Ext-1R!H-R
                L5: Root_Ext-1R!H-R_4R->O_Ext-4O-R_N-Sp-5R!H-1R!H
            L4: Root_Ext-1R!H-R_4R->O_Sp-5R!H-1R!H
                L5: Root_Ext-1R!H-R_4R->O_Sp-5R!H-1R!H_Ext-1R!H-R
            L4: Root_Ext-1R!H-R_4R->O_N-Sp-5R!H-1R!H
        L3: Root_Ext-1R!H-R_N-4R->O
            L4: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R
                L5: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C
                    L6: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R
                        L7: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_Sp-7R!H#4C
                        L7: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C
                            L8: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C
                                L9: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R
                                    L10: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R
                                L9: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R
                                L9: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C
                                L9: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C
                            L8: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_4CHNS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C
                L5: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_N-4CHNS->C
                    L6: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_N-4CHNS->C_4HS->H
                    L6: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_N-4CHNS->C_N-4HS->H
                        L7: Root_Ext-1R!H-R_N-4R->O_Ext-1R!H-R_N-4CHNS->C_N-4HS->H_Ext-4S-R_Ext-7R!H-R
            L4: Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H
                L5: Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R
                    L6: Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R_Ext-6R!H-R
                    L6: Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R_Ext-4CHNS-R
                        L7: Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R_Ext-4CHNS-R_Ext-4CHNS-R
                    L6: Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R_Sp-6R!H-4CHNS
                    L6: Root_Ext-1R!H-R_N-4R->O_Sp-5R!H=1R!H_Ext-4CHNS-R_N-Sp-6R!H-4CHNS
            L4: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H
                L5: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R
                    L6: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_6R!H->S
                        L7: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_6R!H->S_Ext-2R!H-R
                    L6: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S
                        L7: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C
                            L8: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C
                            L8: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C
                                L9: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C
                                    L10: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_1R!H-inRing
                                    L10: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing
                                        L11: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Ext-4C-R
                                            L12: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Ext-4C-R_2R!H->C
                                                L13: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Ext-4C-R_2R!H->C_Ext-4C-R
                                            L12: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Ext-4C-R_N-2R!H->C
                                                L13: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-6C-R
                                        L11: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Sp-6C-4C
                                            L12: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_Sp-6C-4C_Ext-6C-R
                                        L11: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-1R!H-inRing_N-Sp-6C-4C
                                L9: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_4CHNS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_N-6BrCClFINOPSi->C
                        L7: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_Ext-4CHNS-R_N-6R!H->S_N-4CHNS->C
                L5: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_4CHNS->C
                    L6: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_4CHNS->C_4C-u1
                    L6: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_4CHNS->C_N-4C-u1
                L5: Root_Ext-1R!H-R_N-4R->O_N-Sp-5R!H=1R!H_N-4CHNS->C
    L2: Root_Ext-2R!H-R
        L3: Root_Ext-2R!H-R_2R!H->C
            L4: Root_Ext-2R!H-R_2R!H->C_4R->C
            L4: Root_Ext-2R!H-R_2R!H->C_N-4R->C
        L3: Root_Ext-2R!H-R_N-2R!H->C
            L4: Root_Ext-2R!H-R_N-2R!H->C_4R->H
            L4: Root_Ext-2R!H-R_N-2R!H->C_N-4R->H
                L5: Root_Ext-2R!H-R_N-2R!H->C_N-4R->H_4CNO->O
                L5: Root_Ext-2R!H-R_N-2R!H->C_N-4R->H_N-4CNO->O
                    L6: Root_Ext-2R!H-R_N-2R!H->C_N-4R->H_N-4CNO->O_4CN->C
                    L6: Root_Ext-2R!H-R_N-2R!H->C_N-4R->H_N-4CNO->O_N-4CN->C
    L2: Root_4R->H
        L3: Root_4R->H_Sp-2R!H-1R!H
            L4: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1
                L5: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O
                    L6: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_2R!H->C
                    L6: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_N-2R!H->C
                L5: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O
                    L6: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C
                        L7: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_2R!H->C
                        L7: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C
                            L8: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_2NO->N
                            L8: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->N
                    L6: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C
                        L7: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_2R!H->C
                        L7: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C
                            L8: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->N
                            L8: Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->N
            L4: Root_4R->H_Sp-2R!H-1R!H_N-2R!H-u1
        L3: Root_4R->H_N-Sp-2R!H-1R!H
            L4: Root_4R->H_N-Sp-2R!H-1R!H_1R!H->C
            L4: Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C
                L5: Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
                L5: Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
    L2: Root_N-4R->H
        L3: Root_N-4R->H_4CNOS-u1
            L4: Root_N-4R->H_4CNOS-u1_1R!H->O
                L5: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C
                    L6: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R
                        L7: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_5R!H->C
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_N-5R!H->C
                        L7: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R
                                L9: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R_Ext-4CNOS-R
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-5R!H-R
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C
                                L9: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C
                                    L10: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_5R!H->C
                                    L10: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_N-5R!H->C
                                L9: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_N-Sp-5R!H-4C
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C
                                L9: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0
                                    L10: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_5R!H->C
                                    L10: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_N-5R!H->C
                                L9: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_N-5R!H-u0
                    L6: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_4CNOS->C
                    L6: Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_N-4CNOS->C
                L5: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C
                    L6: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O
                        L7: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_2NOS->N
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_N-2NOS->N
                    L6: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O
                        L7: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_4CN->C
                        L7: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R
                                L9: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_5R!H->N
                                L9: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N
                                    L10: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_5BrCClFIOPSSi->C
                                    L10: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_N-5BrCClFIOPSSi->C
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_2NOS->N
                            L8: Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_N-2NOS->N
            L4: Root_N-4R->H_4CNOS-u1_N-1R!H->O
                L5: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O
                    L6: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->N
                                    L10: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->N_2N-u1
                                    L10: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->N_N-2N-u1
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->N
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_Sp-2R!H-1CNS
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C
                    L6: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_2N-u1
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_N-2N-u1
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_2CO->C
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_N-2CO->C
                    L6: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_1CNS->C
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
                L5: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O
                    L6: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_2R!H->S
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O
                                    L10: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_1CNS->C
                                    L10: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_N-1CNS->C
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O
                                    L10: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS
                                        L11: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R
                                            L12: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
                                        L11: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C
                                            L12: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
                                        L11: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_N-1CNS->C
                                    L10: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_N-Sp-5CS-4CCNSS
                    L6: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_2R!H->C
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_N-2R!H->C
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_N-Sp-2R!H-1C
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_Sp-2C-1N
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_N-Sp-2C-1N
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1
                                    L10: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->N
                                    L10: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->N
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_N-2NO-u1
                    L6: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->N
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->N_2N-u1
                                L9: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->N_N-2N-u1
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->N
                        L7: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_1CNS->C
                            L8: Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_N-1CNS->C
        L3: Root_N-4R->H_N-4CNOS-u1
            L4: Root_N-4R->H_N-4CNOS-u1_1R!H->O
                L5: Root_N-4R->H_N-4CNOS-u1_1R!H->O_4CNOS->C
                L5: Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C
                    L6: Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_2R!H->C
                    L6: Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_N-2R!H->C
            L4: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O
                L5: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS
                    L6: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C
                        L7: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C
                        L7: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C
                    L6: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C
                        L7: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
                        L7: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
                            L8: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1
                                L9: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->N
                                L9: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->N
                            L8: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_N-2NO-u1
                L5: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS
                    L6: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C
                    L6: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C
                        L7: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
                        L7: Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
"""
)


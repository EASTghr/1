import numpy as np


def gailv(syl_a, syl_b, data):
    xyg_a=syl_a
    xyg_b=syl_b
    aa_z = 0
    aa_f = 0
    bb_z = 0
    bb_f = 0
    rows, cols = data.shape
    for ii in range(100):
        syl_a=xyg_a
        syl_b=xyg_b
        print("")
        print("---------------------------")
        print(f"第{ii}次迭代 ")
        print("---------------------------")
        for i in range(rows):
            ZM = data[i, 0]
            BM = data[i, 1]

            zyl = ZM / (BM + ZM)
            zyl_cishu = 10 * zyl
            a = (syl_a ** zyl_cishu) * ((1 - syl_a) ** (10 - zyl_cishu))
            b = (syl_b ** zyl_cishu) * ((1 - syl_b) ** (10 - zyl_cishu))
            aa = a / (a + b)
            bb = b / (a + b)
            print("")
            print(f"第{i}次抛硬币 ")
            print("对应概率")
            print(f"E-Step，A的概率: {round(aa, 3)}, E-Step，B的概率: {round(bb, 3)}")
            print("正反面的次数")
            print(f"A的正面: {round(aa * ZM, 3)}, A的背面: {round(aa * BM, 3)}")
            print(f"B的正面: {round(bb * ZM, 3)}, B的背面: {round(bb * BM, 3)}")
            aa_z = aa_z + aa * ZM
            aa_f = aa_f + aa * BM
            bb_z = bb_z + bb * ZM
            bb_f = bb_f + bb * BM

        xyg_a = aa_z / (aa_f + aa_z)
        xyg_b = bb_z / (bb_f + bb_z)
        print("")
        print("计算并且更新M ")
        print(f"A的的参数: {round(xyg_a, 3)}, B的参数: {round(xyg_b, 3)}")
    return round(xyg_a, 3), round(xyg_b, 3)


matrix = np.array([[5, 5], [9, 1], [8, 2], [4, 6], [7, 3]])#硬币正反面的数据

xyg_a, xyg_b = gailv(0.7, 0.4, matrix)

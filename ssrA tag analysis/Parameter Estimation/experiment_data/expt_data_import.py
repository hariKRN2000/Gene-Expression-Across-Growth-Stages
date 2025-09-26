## File to import all the GEAGS expt data so that same code need not be called all the time we need the expt data

import pandas as pd
import numpy as np 

def Get_OD_Data():
    # Importing growth data
    
    OD_data = pd.read_csv("experiment_data/expt_growth_data.csv")

    columns = ["time(min)", "D1", "D2", "D3", "D4", "B1", "B2", "B3"]
    # tf_i = min(len(OD_data[col].dropna()) for col in columns) - 1
    tf_i = 72

    time = OD_data["time(min)"].to_numpy()[:tf_i]
    OD_blank = 0.078
    D1 = OD_data["D1"].to_numpy()[:tf_i] - OD_blank
    D2 = OD_data["D2"].to_numpy()[:tf_i] - OD_blank
    D3 = OD_data["D3"].to_numpy()[:tf_i] - OD_blank
    D4 = OD_data["D4"].to_numpy()[:tf_i] - OD_blank
    B1 = OD_data["B1"].to_numpy()[:tf_i] - OD_blank
    B2 = OD_data["B2"].to_numpy()[:tf_i] - OD_blank
    B3 = OD_data["B3"].to_numpy()[:tf_i] - OD_blank

    C_OD = 1e9
    C1 = D1 * C_OD
    C2 = D2 * C_OD
    C3 = D3 * C_OD
    C4 = D4 * C_OD
    C5 = B1 * C_OD
    C6 = B2 * C_OD
    C7 = B3 * C_OD
    C = [C1, C2, C3, C4, C5, C6, C7]

    C1_max = np.max(C1)
    C2_max = np.max(C2)
    C3_max = np.max(C3)
    C4_max = np.max(C4)
    C5_max = np.max(C5)
    C6_max = np.max(C6)
    C7_max = np.max(C7)
    C_max = [C1_max, C2_max, C3_max, C4_max, C5_max, C6_max, C7_max ]

    C1_0 = np.min(C1)
    C2_0 = np.min(C2)
    C3_0 = np.min(C3)
    C4_0 = np.min(C4)
    C5_0 = np.min(C5)
    C6_0 = np.min(C6)
    C7_0 = np.min(C7)
    C_0 = [C1_0, C2_0, C3_0, C4_0, C5_0, C6_0, C7_0]

    k_gr = [0.01481465, 0.01493478, 0.01493515, 0.01885024, 0.01739013,
       0.01886247, 0.01667254]

    C_max_avg = np.mean(C_max[:4])
    C_0_avg = np.mean(C_0[:4])
    k_gr_avg = np.mean(k_gr[:4])

    return [C, C_max, C_0, k_gr, C_max_avg, C_0_avg, k_gr_avg]

def Get_FLOD_Data():
    # Importing experimental data
    
    tf_i = - 1

    geags_data = pd.read_csv("experiment_data/FL_by_OD_expt_data.csv")
    time = geags_data["Time (min)"].to_numpy()[:tf_i]

    columns = ["D1", "D2", "D3", "D4", "B1", "B2", "B3"]
    # tf_i = min(len(geags_data[col].dropna()) for col in columns) - 1
    tf_i = 72
    D1 = geags_data["D1"].to_numpy()[:tf_i]
    D2 = geags_data["D2"].to_numpy()[:tf_i]
    D3 = geags_data["D3"].to_numpy()[:tf_i]
    D4 = geags_data["D4"].to_numpy()[:tf_i]
    B1 = geags_data["B1"].to_numpy()[:tf_i]
    B2 = geags_data["B2"].to_numpy()[:tf_i]
    B3 = geags_data["B3"].to_numpy()[:tf_i]

    D12 = D1 - D1[0]
    D1_non_leaky = D12[np.argwhere(D12 >= -1e3)]
    t12 = time[len(D1_non_leaky) - 1]
    time12 = np.linspace(0,t12,len(D1_non_leaky))

    D22 = D2 - D2[0]
    D2_non_leaky = D22[np.argwhere(D22 >= -1e3)]
    t22 = time[len(D2_non_leaky) - 1]
    time22 = np.linspace(0,t22,len(D2_non_leaky))

    D32 = D3 - D3[0]
    D3_non_leaky = D32[np.argwhere(D32 >= -1e3)]
    t32 = time[len(D3_non_leaky) - 1]
    time32 = np.linspace(0,t32,len(D3_non_leaky))

    D42 = D4 - D4[0]
    D4_non_leaky = D42[np.argwhere(D42 >= -1e3)]
    t42 = time[len(D4_non_leaky) - 1]
    time42 = np.linspace(0,t42,len(D4_non_leaky))

    D_non_leaky = [D1_non_leaky, D2_non_leaky, D3_non_leaky, D4_non_leaky]
    time_D = [time12, time22, time32, time42]

    B12 = B1 - B1[0]
    B1_non_leaky = B12[np.argwhere(B12 >= 0)]
    tB12 = time[len(B1_non_leaky) - 1]
    timeB12 = np.linspace(0,tB12,len(B1_non_leaky))

    B22 = B2 - B2[0]
    B2_non_leaky = B22[np.argwhere(B22 >= 0)]
    tB22 = time[len(B2_non_leaky) - 1]
    timeB22 = np.linspace(0,tB22,len(B2_non_leaky))

    B32 = B3 - B3[0]
    B3_non_leaky = B32[np.argwhere(B32 >= 0)]
    tB32 = time[len(B3_non_leaky) - 1]
    timeB32 = np.linspace(0,tB32,len(B3_non_leaky))

    B_non_leaky = [B1_non_leaky, B2_non_leaky, B3_non_leaky]
    time_B = [timeB12, timeB22, timeB32]

    # D_avg = (D1_non_leaky[:88] + D2_non_leaky[:88] + D3_non_leaky[:88])/3
    # B_avg = (B1_non_leaky[:88] + B2_non_leaky[:88] + B3_non_leaky[:88])/3
    avg_fold_change = np.mean((np.max(B1_non_leaky)/np.max(D1_non_leaky),np.max(B2_non_leaky)/np.max(D2_non_leaky),np.max(B3_non_leaky)/np.max(D3_non_leaky)))
    
    return [D_non_leaky, time_D, B_non_leaky, time_B, avg_fold_change]
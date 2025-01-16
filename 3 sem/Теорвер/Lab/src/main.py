from functions import *

data = [0.41, 1.63, -1.53, -0.20, 0.85, 0.09, 1.54, 0.25, 1.24, -0.26,
        1.08, 0.42, -0.92, -0.91, 1.15, -0.82, 0.26, 0.96, 1.57, 0.72]

data_test = [1, 1, 0, 1, -2, 1, 9, 200]

res_var_series = var_series(data)
res_scope = scope(res_var_series)
extr_value_min, extr_value_max = extreme_values(res_var_series)
dictianory = build_statistical_series(data)
build_empirical_func(res_var_series)
print_empirical_func(res_var_series)

res_sample_average = sample_average(dictianory)
res_sample_variance = sample_variance(dictianory, res_sample_average)
res_sample_msd = sample_msd(res_sample_variance)
res_correct_sample_variance = correct_sample_variance(data, res_sample_variance)
res_correct_sample_msd = correct_sample_msd(res_correct_sample_variance)
res_fashion = fashion(dictianory)
res_median = median(res_var_series)
res_math_exp = math_expectation(data)

res_h, res_m = sturgess_formula(res_var_series)
interval_series(res_var_series, res_h, res_m)
interval_histogram(res_var_series, res_h, res_m)
polygon(res_var_series, res_h, res_m)
plt.show()

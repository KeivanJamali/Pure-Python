from scipy.stats import t, norm

confidence = 0.95
df = 9

t_value = t.ppf(1 - (1-confidence) / 2, df)
print(f"The t-value for {confidence*100}% confidence with {df} degrees of freedom is {t_value}")

z_value = norm.ppf(1 - (1-confidence) / 2)
print(f"The z-value for {confidence*100}% confidence is {z_value}")

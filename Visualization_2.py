# import matplotlib.pyplot as plt

# n = [64, 128, 256, 512, 1024]

# # Data cpp
# cpp_int_meat = [0.00414, 0.023707, 0.143118, 1.82851, 13.7111]
# cpp_double_meat = [0.008038, 0.020016, 0.205799, 2.27169, 14.6914]
# cpp_int_total = [0.008247, 0.026217, 0.143118, 1.8316, 13.7191]
# cpp_double_total = [0.008038, 0.020902, 0.221466, 2.27375, 14.6914]

# # Plotting for cpp
# plt.figure(figsize=(10,6))
# plt.plot(n,cpp_int_meat,label="C++ Integer (Meat)",marker='o')
# plt.plot(n,cpp_double_meat,label="C++ Double (Meat)",marker='o')
# plt.plot(n,cpp_int_total,label="C++ Integer (Total)",marker='o')
# plt.plot(n,cpp_double_total,label="C++ Double (Total)",marker='o')

# plt.xlabel("Matrix Dimensions (N)")
# plt.ylabel("Time (seconds)")
# plt.title("Meat Computation Time vs Total Time on variation on N (C++)")
# plt.legend()
# plt.grid(True)
# plt.show()


# # Data python
# py_int_meat = [0.159978, 0.695796, 8.179264, 85.778650, 598.266068]
# py_double_meat = [0.134663, 0.715955, 8.599862, 151.366096, 498.437449]
# py_int_total = [0.159978, 0.695996, 8.179264, 85.778650, 598.266068]
# py_double_total = [0.134663, 0.715955, 8.601056, 151.366096, 498.445656]

# #Plotting for python
# plt.figure(figsize=(10,6))
# plt.plot(n,py_int_meat,label="Python Integer (Meat)",marker='o')
# plt.plot(n,py_double_meat,label="Python Double (Meat)",marker='o')
# plt.plot(n,py_int_total,label="Python Integer (Total)",marker='o')
# plt.plot(n,py_double_total,label="Python Double (Total)",marker='o')

# plt.xlabel("Matrix Dimensions (N)")
# plt.ylabel("Time (seconds)")
# plt.title("Meat Computation Time vs Total Time on variation on N (Python)")
# plt.legend()
# plt.grid(True)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

n = [64, 128, 256, 512, 1024]

# Data C++
cpp_int_meat = [0.00414, 0.023707, 0.143118, 1.82851, 13.7111]
cpp_double_meat = [0.008038, 0.020016, 0.205799, 2.27169, 14.6914]
cpp_int_total = [0.008247, 0.026217, 0.143118, 1.8316, 13.7191]
cpp_double_total = [0.008038, 0.020902, 0.221466, 2.27375, 14.6914]

bar_width = 0.2
indices = np.arange(len(n))
plt.figure(figsize=(12, 6))
plt.bar(indices-bar_width*1.5, cpp_int_meat, bar_width, label='C++ Integer (Meat)')
plt.bar(indices -bar_width*0.5,cpp_double_meat, bar_width,label='C++ Double (Meat)')
plt.bar(indices+ bar_width*0.5,cpp_int_total, bar_width, label='C++ Integer (Total)')
plt.bar(indices+bar_width*1.5,cpp_double_total, bar_width,label='C++ Double (Total)')

plt.xlabel("Matrix Dimensions (N)")
plt.ylabel("Time (seconds)")
plt.title("Meat Computation Time vs Total Time (C++)")
plt.xticks(indices, n)
plt.legend()
plt.grid(True)
plt.show()


# Data Python
py_int_meat = [0.159978, 0.695796, 8.179264, 85.778650, 598.266068]
py_double_meat = [0.134663, 0.715955, 8.599862, 151.366096, 498.437449]
py_int_total = [0.159978, 0.695996, 8.179264, 85.778650, 598.266068]
py_double_total = [0.134663, 0.715955, 8.601056, 151.366096, 498.445656]


plt.figure(figsize=(12, 6))
plt.bar(indices - bar_width*1.5, py_int_meat, bar_width, label='Python Integer (Meat)')
plt.bar(indices - bar_width*0.5, py_double_meat, bar_width, label='Python Double (Meat)')
plt.bar(indices + bar_width*0.5, py_int_total, bar_width, label='Python Integer (Total)')
plt.bar(indices + bar_width*1.5, py_double_total, bar_width, label='Python Double (Total)')

plt.xlabel("Matrix Dimensions (N)")
plt.ylabel("Time (seconds)")
plt.title("Meat Computation Time vs Total Time (Python)")
plt.xticks(indices, n)
plt.legend()
plt.grid(True)
plt.show()

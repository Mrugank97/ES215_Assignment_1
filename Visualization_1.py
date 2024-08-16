import matplotlib.pyplot as plt

n = [64,128,256,512,1024]

# Data cpp
cpp_int_total = [0.004367, 0.034404, 0.219083, 1.51024, 10.6969]
cpp_double_total = [0.008247, 0.058454, 0.157736, 1.48929, 12.9744]

# Plotting for cpp
plt.figure(figsize=(10,6))
plt.plot(n,cpp_int_total,label="C++ Integer (Total)",marker='o')
plt.plot(n,cpp_double_total,label="C++ Double (Total)",marker='o')

plt.xlabel("Matrix Dimensions (N)")
plt.ylabel("Time (seconds)")
plt.title("Computational Time on variation on N for Integer and double type(C++)")
plt.legend()
plt.grid(True)
plt.show()


# Data python
py_int_total = [0.293043, 0.695308, 7.747627, 63.898115, 549.181594]
py_double_total = [0.273179, 0.720109, 7.774885, 65.971033, 694.099006]

#Plotting for python
plt.figure(figsize=(10,6))
plt.plot(n,py_int_total,label="Python Integer (Total)",marker='o')
plt.plot(n,py_double_total,label="Python Double (Total)",marker='o')

plt.xlabel("Matrix Dimensions (N)")
plt.ylabel("Time (seconds)")
plt.title("Computational Time on variation on N for Integer and double type (Python)")
plt.legend()
plt.grid(True)
plt.show()

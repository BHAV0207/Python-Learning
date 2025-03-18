import matplotlib.pyplot as plt

days =[1 ,2,3,4,5,6,7]
temp =[30,22,34,26 ,40 ,40,20]

plt.plot(days , temp , marker='o' , linestyle=':' , color='r')

plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Over a Week")



# ------------------------------------------------------------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [1000, 1500, 1300, 1800, 2000]

plt.plot(months , sales , marker="." , linestyle=":" , color="b")

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("sales over years")

# plt.show()
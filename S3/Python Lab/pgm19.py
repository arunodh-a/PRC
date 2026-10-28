import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [2500, 2700, 3000, 2800, 3500, 4000,
         4200, 4100, 3900, 4300, 4500, 4700]

plt.figure(figsize=(10, 6))

plt.plot(months, sales, marker='o', linestyle='-', color='b')

plt.title('Monthly Sales Figures')
plt.xlabel('Month')
plt.ylabel('Sales (in USD)')

plt.grid(True)

plt.show()
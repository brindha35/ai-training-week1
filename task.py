

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")
avg = df.groupby("department")["salary"].mean()

plt.figure()
plt.bar(avg.index, avg.values, color="steelblue", edgecolor="black")

plt.title("average salary per department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

for i, v in enumerate(avg.values):
    plt.text(i, v, f"{v:.0f}", ha="center", va="bottom")

plt.show()
plt.savefig("bar_chart.png")


plt.figure()
plt.hist(df["salary"],bins=5, color="orange", edgecolor="black")

plt.title("salar Distribution")
plt.xlabel("Salary")
plt.ylabel("number of employees")

plt.savefig("histogram.png")
plt.show()

for department, group in df.groupby("department"):
    plt.scatter(
        group["id"],
        group["salary"],
        label=department,
        s=60

    )
plt.title("Employee ID vs Salary by Department")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Depatment")
plt.grid(True, linestyle= "--", alpha=0.4)

plt.tight_layout()
plt.savefig("Scatter_plot.png", dpi=300)
plt.show()

months = ["Jan", "Feb", "Mar", "Apl", "May", "June"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure()
plt.plot(
    months,
    sales,
    marker="o",
    linestyle="-",
    color="green",
    label="Monthly Sales"
)
plt.title("Mothly Sales (Jan to June)")
plt.xlabel("Month")
plt.ylabel("sales")
plt.legend()
plt.grid(True, linestyle="-", alpha=0.4)

plt.tight_layout()
plt.savefig("line_chart.png", dpi=300)
plt.show()



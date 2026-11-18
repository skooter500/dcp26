import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
minutes = [30, 45, 20, 60, 40]

temps1=[10,78,56,3,6]
temps2=[10,8,6,39,65]

scores = [67, 72, 88, 91, 65, 77, 82, 95, 71]


root = tk.Tk()
root.geometry("400x300")

# Simple label
label1 = tk.Label(root, text="Hello, Tkinter!")
label1.pack()

# Styled label
label2 = tk.Label(root, 
                  text="Styled Text",
                  font=("Arial", 16, "bold"),
                  fg="blue",
                  bg="yellow")
label2.pack(pady=10)

root.mainloop()


root = tk.Tk()

fig = Figure(figsize=(6, 4))
ax = fig.add_subplot(111)
ax.plot([1, 2, 3], [1, 4, 9])

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()



plt.hist(scores, bins=5, edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Frequency')
plt.title('Exam Scores')
plt.show()



# fig, graphs = plt.subplots(2, 2, figsize=(10, 8))

# graphs[0, 0].scatter(days, temps1)  # top-left
# graphs[0, 1].plot(days, temps1)  # top-right
# graphs[1, 0].plot(days, temps2)  # bottom-left
# graphs[1, 1].plot(days, temps2)  # bottom-right

# plt.tight_layout()
# plt.show()
#
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3, 3))

# ax1.plot(days, temps1)
# ax1.set_title('First Plot')
# ax1.set_xlabel("Days")
# ax1.set_ylabel("Minutes")

# ax2.plot(days, temps2)
# ax2.set_title('Second Plot')


# plt.show()


# plt.plot(days, temps1, label="day1")
# plt.plot(days, temps2, label="day2")
# plt.legend()
# plt.show()

# plt.plot(days, minutes, color="#FF0000", marker = 'o', linewidth=1, linestyle="-.", alpha=0.6, label="practice")
# plt.xlabel("Days")
# plt.ylabel("Minutes")
# plt.legend()
# plt.title("Music Practice")
# plt.show()

# tunes = ['Butterfly', 'Kesh', 'Silver Spear']
# plays = [5, 8, 3]

# plt.bar(tunes, plays)
# plt.xlabel('Tune Name')
# plt.ylabel('Times Played')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()
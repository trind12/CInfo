import tkinter as tk
import os
import psutil
import platform

root = tk.Tk()
def WindowSetup():
    root.title("CInfo")
    root.geometry("1200x800")
    root.resizable(True, True)
    root.config(bg="gray")

def pack():
    title.pack(pady=0)
    system.pack(pady=1)
    users.pack(pady=1)
    cpucount.pack(pady=1)
    swapmem.pack(pady=1)
    boottime.pack(pady=1)
    partitions.pack(pady=1)

title = tk.Label(root, text="Welcome to CInfo", font=("Helvetica", 20, "bold"), fg="blue", bg="gray")
system = tk.Label(root, text="System: " + str(platform.release()) + " " +str(platform.system() + " " + str(platform.machine())), font=("Arial", 12), bg="gray")
users = tk.Label(root, text="Users: " + str(psutil.users()), font=("Arial", 12), bg="gray")
cpucount = tk.Label(root, text="CPU Cores (logical): " + str(os.cpu_count()), font=("Arial", 12), bg="gray")
swapmem = tk.Label(root, text="Swap memory: " + str(psutil.swap_memory()), font=("Arial", 12), bg="gray")
boottime = tk.Label(root, text="Boot time: " + str(psutil.boot_time()), font=("Arial", 12), bg="gray")
partitions = tk.Label(root, text="Disk Partitions: " + str(psutil.disk_partitions()), font=("Arial", 12), bg="gray")

WindowSetup()
pack()

root.mainloop()
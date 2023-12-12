import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

class SFJPreemtive:

    def __init__(self, processes):
        self.processes = processes
        self.length = len(processes)

    def findWaitingTime(self, processes, n, wt):
        rt = [0] * n

        for i in range(n):
            rt[i] = processes[i][2]
        t = 0
        minm = 999999999
        short = 0
        check = False

        while (complete != n):
            for j in range(n):
                if ((processes[j][1] <= t) and
                        (rt[j] < minm) and rt[j] > 0):
                    minm = rt[j]
                    short = j
                    check = True
            if (check == False):
                t += 1
                continue

            rt[short] -= 1
            minm = rt[short]
            if (minm == 0):
                minm = 999999999

            if (rt[short] == 0):
                complete += 1
                check = False
                fint = t + 1
                wt[short] = (fint - processes[short][1])

                if (wt[short] < 0):
                    wt[short] = 0

            t += 1

    def findTurnAroundTime(self, processes, n, wt, tat):
        for i in range(n):
            tat[i] = processes[i][2] + wt[i]

    def findavgTime(self, processes, n):
        wt = [0] * n
        tat = [0] * n
        akhir = list()

        self.findWaitingTime(processes, n, wt)
        self.findTurnAroundTime(processes, n, wt, tat)

        total_wt = 0
        total_tat = 0
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            akhir.append([processes[i][0], processes[i][2], wt[i], tat[i]]) 

        AWT = total_wt / n
        ATAT = total_tat / n
        return akhir, AWT, ATAT


class ProgramSJFPreemtive:

    def __init__(self, root):
        self.root = root
        self.root.title("Program Penghitung SJF Preemtive")
        self.processes = []
        self.create_widgets()

    def create_widgets(self):
        self.jumlahproses = tk.IntVar(value=5)
        ttk.Label(self.root, text="Silahkan Masukan Jumlah Proses:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Spinbox(self.root, from_=1, to=10, textvariable=self.jumlahproses).grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Button(self.root, text="MULAI", command=self.run_simulation).grid(row=1, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(self.root, height=50, width=80)
        self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def run_simulation(self):
        self.processes = []
        num_processes = self.jumlahproses.get()

        for i in range(num_processes):
            arrival_time = int(simpledialog.askstring(f"Proses {i + 1}", "Masukan Arrival Time: "))
            burst_time = int(simpledialog.askstring(f"Proses {i + 1}", "Masukan Burst Time: "))
            self.processes.append([i + 1, arrival_time, burst_time]) 

        sfj = SFJPreemtive(self.processes)
        akhir, AWT, ATA = sfj.findavgTime(self.processes, num_processes)

        result_str = "\n"
        result_str += "Processes\tBurst Time\tWaiting Time\tTurn-Around Time\n"
        for i in akhir:
            result_str += f"\tP{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\n"
        result_str += "\n"
        result_str += f"\nAverage Waiting Time: {AWT:.2f}"
        result_str += f"\nAverage Turn Around Time: {ATA:.2f}"

        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_str)
        self.result_text.config(state=tk.DISABLED)


root = tk.Tk()
app = ProgramSJFPreemtive(root)
root.mainloop() 


import tkinter as tk
from tkinter import messagebox

class DebateTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sesión de Debate")
        self.root.geometry("500x400")
        
        # Variables
        self.committees = []
        self.current_committee = 0
        self.time_left = 0
        self.timer_running = False
        
        # Pantalla para ingresar número de comités
        self.setup_initial_screen()

    def setup_initial_screen(self):
        self.initial_frame = tk.Frame(self.root)
        self.initial_frame.pack(pady=20)
        
        tk.Label(self.initial_frame, text="¿Cuántos comités participan?").pack(pady=5)
        
        self.committee_count_var = tk.IntVar()
        self.committee_count_entry = tk.Entry(self.initial_frame, textvariable=self.committee_count_var)
        self.committee_count_entry.pack(pady=5)
        
        tk.Button(self.initial_frame, text="Continuar", command=self.set_committee_count).pack(pady=5)

    def set_committee_count(self): 
        try:
            self.committee_count = self.committee_count_var.get()
            if self.committee_count < 1:
                raise ValueError
            self.initial_frame.destroy()
            self.ask_committee_names()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un número válido de comités.")

    def ask_committee_names(self):
        self.names_frame = tk.Frame(self.root)
        self.names_frame.pack(pady=20)
        
        self.committee_names = []
        tk.Label(self.names_frame, text="Introduce el nombre de cada comité:").pack(pady=5)
        
        for i in range(self.committee_count):
            name_var = tk.StringVar()
            entry = tk.Entry(self.names_frame, textvariable=name_var)
            entry.pack(pady=2)
            self.committee_names.append(name_var)
        
        tk.Button(self.names_frame, text="Comenzar Debate", command=self.save_committee_names).pack(pady=10)

    def save_committee_names(self):
        self.committees = [name.get() for name in self.committee_names]
        self.names_frame.destroy()
        self.setup_timer_screen()

    def setup_timer_screen(self):
        self.timer_frame = tk.Frame(self.root)
        self.timer_frame.pack(pady=20)
        
        # Lista de comités
        self.committee_list_frame = tk.Frame(self.root)
        self.committee_list_frame.pack(side=tk.LEFT, padx=20)
        tk.Label(self.committee_list_frame, text="Comités:", font=("Arial", 14)).pack(pady=10)
        
        self.committee_labels = []
        for committee in self.committees:
            label = tk.Label(self.committee_list_frame, text=committee, font=("Arial", 12))
            label.pack(pady=2)
            self.committee_labels.append(label)
        
        # Reloj
        self.time_label = tk.Label(self.timer_frame, text="00:00", font=("Arial", 48))
        self.time_label.pack(pady=10)
        
        # Mostrar quién tiene la palabra
        self.committee_label = tk.Label(self.timer_frame, text=f"Tiene la palabra: {self.committees[0]}", font=("Arial", 18))
        self.committee_label.pack(pady=5)
        
        # Controles
        tk.Button(self.timer_frame, text="3 Minutos", command=lambda: self.start_timer(3)).pack(side=tk.LEFT, padx=10)
        tk.Button(self.timer_frame, text="5 Minutos", command=lambda: self.start_timer(5)).pack(side=tk.LEFT, padx=10)
        tk.Button(self.timer_frame, text="Pausar", command=self.pause_timer).pack(side=tk.LEFT, padx=10)
        tk.Button(self.timer_frame, text="Reanudar", command=self.resume_timer).pack(side=tk.LEFT, padx=10)
        tk.Button(self.timer_frame, text="Reiniciar", command=self.reset_timer).pack(side=tk.LEFT, padx=10)

    def update_timer(self):
        # Actualiza el tiempo restante en el reloj.
        if self.timer_running and self.time_left > 0:
            minutes = self.time_left // 60
            seconds = self.time_left % 60

            # Cambia el color del reloj a rojo en los últimos 10 segundos
            if self.time_left <= 10:
                self.time_label.config(fg="red")
            else:
                self.time_label.config(fg="black")
            
            self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")

            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.next_committee()

    def start_timer(self, minutes):
        self.time_left = minutes * 60
        self.timer_running = True
        self.update_timer()

    def pause_timer(self):
        self.timer_running = False

    def resume_timer(self):
        if not self.timer_running and self.time_left > 0:
            self.timer_running = True
            self.update_timer()

    def reset_timer(self):
        self.time_left = 0
        self.timer_running = False
        self.time_label.config(text="00:00", fg="black")

    def next_committee(self):
        self.current_committee = (self.current_committee + 1) % len(self.committees)
        self.committee_label.config(text=f"Tiene la palabra: {self.committees[self.current_committee]}")
        for i, label in enumerate(self.committee_labels):
            if i == self.current_committee:
                label.config(fg="blue")
            else:
                label.config(fg="black")
        messagebox.showinfo("Tiempo Finalizado", f"Es el turno de {self.committees[self.current_committee]}.")

if __name__ ==:
    root = tk.Tk()
    app = DebateTimer(root)
    root.mainloop()

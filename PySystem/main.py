from rich import print
from rich.progress import Progress
from rich.console import Console
import psutil
import platform
import time
import art
import os


class PySystem:
    # Monitor do sistema via terminal feito com python
    def __init__(self):
        self.total_memory = psutil.virtual_memory().total / (1024 ** 3)
        self.RISK = 70 # Valor maximo ideal do uso do hardware

    def wellcome(self):
        art.tprint(f"{' ' * 2} PySystem", 'tarty1')
        print(f"{'=_' * 17} System {'_=' * 17}\n")

    # Limpa o terminal, se o systema for windows com o comando 'cls', se não com o 'clear'
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Obtem informações da maquina e OS
    def get_system_info(self):
        print(f"Sistema: {platform.system()}\n"
            f"CPU: {platform.processor()}\n" 
            f"Memória Total: {self.total_memory:.2f}GB")
            
    def get_cpu_percent(self):
        percent = psutil.cpu_percent()
        color = 'green' if percent < self.RISK else 'red'

        cores = psutil.cpu_percent(percpu=True)
        cores_percent = []
        for index, item in enumerate(cores):
            cores_percent.append(f"core {index + 1} - {item}%")

        cpu_progress = Progress()  # Cria a instancia da progress bar
        cpu_task = cpu_progress.add_task(f"[{color}] CPU", total=100,)  # Cria a task da progress bar
        
        cpu_progress.update(cpu_task, advance=percent)  # Atualiza o valor da task

        print(cpu_progress)
        print(f"- CPU: [bold {color}]{percent}% [/bold {color}] - {cores_percent}\n")

    
    def get_memory_percent(self):
        used_memory = psutil.virtual_memory().used / (1024 ** 3)
        percent = psutil.virtual_memory().percent
        color = 'green' if percent < self.RISK else 'red'

        memory_progress = Progress()  # Cria a instancia da progress bar
        memory_task = memory_progress.add_task(f"[{color}] Memory", total=self.total_memory)  # Cria a task da progress bar

        memory_progress.update(memory_task, advance=used_memory)  # Atualiza o valor da task

        print(memory_progress)
        print(f"- Memória: [bold {color}]{percent}% [/bold {color}]- {used_memory:.2f}GB of {self.total_memory:.2f}GB\n")
    
    def get_disk_percent(self):
        percent = psutil.disk_usage('/').percent
        color = 'green' if percent < self.RISK else 'red'

        disk_progress = Progress()  # Cria a instancia da progress bar
        disk_task = disk_progress.add_task(f"[{color}] Disk", total=100)  # Cria a task da progress bar

        disk_progress.update(disk_task, advance=percent)  # Atualiza o valor da task

        print(disk_progress)
        print(f"- Disco: [bold {color}]{percent}%\n")

    # monitora o siistema
        
    def monitor_resources(self):
        while True:
            self.clear_screen()
            self.wellcome()

            self.get_system_info()

            print(f"\n{'=_' * 17} State {'_=' * 17}\n")

            self.get_memory_percent()
            self.get_cpu_percent()
            self.get_disk_percent()

            time.sleep(1)


app = PySystem()

if __name__ == "__main__":
    try:
        app.monitor_resources()
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")

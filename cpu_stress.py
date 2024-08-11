import multiprocessing
import time

# Função que executa cálculos intensivos
def cpu_stress_test(duration):
    def cpu_task():
        end_time = time.time() + duration
        while time.time() < end_time:
            pass  # Realiza um loop vazio para estressar a CPU

    # Obtém o número de núcleos de CPU disponíveis
    num_cores = multiprocessing.cpu_count()

    # Cria um processo de CPU stress para cada núcleo
    processes = []
    for _ in range(num_cores):
        process = multiprocessing.Process(target=cpu_task)
        processes.append(process)
        process.start()

    # Espera todos os processos terminarem
    for process in processes:
        process.join()

# Função principal para executar o teste
def main():
    stress_duration = 60  # Duração do teste em segundos
    print(f"Estressando a CPU por {stress_duration} segundos...")
    cpu_stress_test(stress_duration)
    print("Teste de estresse da CPU concluído.")

if __name__ == "__main__":
    main()

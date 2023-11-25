## Threads
Threads são a menor unidade de processamento que pode ser executada de forma independente dentro de um programa. Em Python, threads são usadas para realizar várias tarefas ao mesmo tempo, permitindo que um programa execute operações de I/O (Input/Output) ou outras tarefas que não são intensivas em CPU de maneira concorrente. Isso pode melhorar a eficiência e a performance do programa, especialmente em tarefas de espera, como downloads ou comunicação em rede.

Características das Threads:
* Concorrência: Permite que várias tarefas sejam executadas "simultaneamente" (intercalando sua execução).
* Compartilhamento de Memória: Todas as threads de um processo compartilham o mesmo espaço de memória, facilitando a comunicação entre elas, mas também exigindo cuidados com a sincronização para evitar condições de corrida.
* Global Interpreter Lock (GIL): No Python, devido ao GIL, threads não são verdadeiramente paralelas em operações intensivas de CPU, pois o GIL permite que apenas uma thread execute instruções de Python por vez.



## Multiprocessing
Multiprocessing envolve a execução de múltiplos processos simultaneamente. Cada processo é, de fato, uma instância independente do programa que é executada em seu próprio espaço de memória. Isso significa que eles não compartilham memória e precisam de mecanismos específicos para comunicação e compartilhamento de dados.


Características do Multiprocessing:
* Paralelismo Real: Em sistemas com múltiplos núcleos de CPU, o multiprocessing permite que várias tarefas sejam executadas em paralelo, melhorando significativamente a performance em tarefas intensivas de CPU.
* Isolamento de Memória: Cada processo tem seu próprio espaço de memória, o que aumenta a estabilidade e segurança, já que um processo não pode acessar diretamente a memória dos outros.
* Comunicação entre Processos: É necessário usar mecanismos específicos para a comunicação entre processos, como pipes, filas, ou memória compartilhada.


### Quando Usar Cada Um
* Threads: São mais adequadas para tarefas que envolvem espera, como operações de I/O, ou quando a tarefa pode ser dividida em múltiplas sub-tarefas que não são intensivas em CPU.
* Multiprocessing: É ideal para tarefas computacionalmente intensivas, onde a execução paralela pode ser aproveitada, especialmente em máquinas com múltiplos núcleos de CPU.


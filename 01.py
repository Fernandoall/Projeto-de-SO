def first_fit(memory_blocks, process_sizes):
    allocated_blocks = [-1] * len(process_sizes)

    for i, process_size in enumerate(process_sizes):
        for j, block_size in enumerate(memory_blocks):
            if block_size >= process_size:
                allocated_blocks[i] = j
                memory_blocks[j] -= process_size
                break

    return allocated_blocks

def print_memory_status(memory_blocks):
    for i, block_size in enumerate(memory_blocks):
        print(f"Block {i+1}: {block_size}")

if __name__ == "__main__":
    # Exemplo de uso
    memory_blocks = [100, 50, 200, 80, 120]
    process_sizes = [60, 100, 30, 150, 90]

    print("Antes da alocação:")
    print_memory_status(memory_blocks)

    allocated_blocks = first_fit(memory_blocks, process_sizes)

    for i, process_size in enumerate(process_sizes):
        if allocated_blocks[i] != -1:
            print(f"Processo {i+1} alocado no bloco {allocated_blocks[i]+1}.")
        else:
            print(f"Não foi possível alocar o Processo {i+1}.")

    print("\nDepois da alocação:")
    print_memory_status(memory_blocks)
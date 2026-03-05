import sys

def main():
    # Definindo o valor de PI conforme o enunciado
    pi = 3.14159
    
    try:
        # Lendo a entrada do sistema (mais seguro para evitar Runtime Error)
        entrada = sys.stdin.read().strip()
        
        if entrada:
            raio = float(entrada)
            
            # Cálculo da área: A = π . raio²
            area = pi * (raio ** 2)
            
            # Exibição com 4 casas decimais e fim de linha automático do print
            print(f"A={area:.4f}")
            
    except EOFError:
        pass

if __name__ == "__main__":
    main()
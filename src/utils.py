import os
import time

def limpar_console() -> None:
    """Limpa o console de acordo com o sistema operacional."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exibir_por_tempo(texto: str, tempo: int = 2) -> None:
    """Exibe um texto por um tempo determinado e, em seguida, limpa o console."""
    print(texto)
    time.sleep(tempo)
    limpar_console()

def pausar_e_limpar(mensagem: str = "Pressione Enter para continuar...") -> None:
    """Pausa o programa até o usuário pressionar Enter, e depois limpa o console."""
    input(mensagem)
    limpar_console()

import tkinter as tk

# Variável global para armazenar o turno
turno = "X"  # Começa com "X" para o primeiro clique
tabuleiro = [["" for _ in range(3)] for _ in range(3)]  # Matriz 3x3 para armazenar o estado do jogo
botoes = []
jogo_ativo = True  # Variável para controlar se o jogo está ativo

def acao(botao, linha, coluna):
    global turno, jogo_ativo
    
    # Garante que o botão não seja alterado se já foi clicado e o jogo ainda estiver ativo
    if botao.cget("text") == "" and jogo_ativo:  # Se o botão ainda não tiver "X" ou "O" e o jogo estiver ativo
        botao.config(text=turno, state="disabled")  # Coloca "X" ou "O" no botão

        # Atualiza o tabuleiro com o valor do símbolo
        tabuleiro[linha][coluna] = turno

        # Muda a cor da fonte do botão
        if turno == "X":
            botao.config(fg="blue", font=("arial", 35, "bold"))  # Cor azul para o "X"
        else:
            botao.config(fg="red", font=("arial", 35, "bold"))  # Cor vermelha para o "O"

        # Verifica se alguém ganhou
        if verificar_vitoria():
            print(f"Jogador {turno} venceu!")
            jogo_ativo = False  # Desativa o jogo após a vitória
            return  # Não permite mais jogadas após a vitória

        # Alterna o turno entre "X" e "O"
        if turno == "X":
            turno = "O"
        else:
            turno = "X"

def verificarvitoria():
    # Verifica linhas, colunas e diagonais para ver se algum jogador venceu
    for i in range(3):
        # Verifica linhas
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
            # Marca os botões vencedores como verdes
            botoes[i*3].config(bg="green")
            botoes[i*3+1].config(bg="green")
            botoes[i*3+2].config(bg="green")
            return True
        # Verifica colunas
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
            # Marca os botões vencedores como verdes
            botoes[i].config(bg="green")
            botoes[i+3].config(bg="green")
            botoes[i+6].config(bg="green")
            return True

    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        # Marca os botões vencedores como verdes
        botoes[0].config(bg="green")
        botoes[4].config(bg="green")
        botoes[8].config(bg="green")
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        # Marca os botões vencedores como verdes
        botoes[2].config(bg="green")
        botoes[4].config(bg="green")
        botoes[6].config(bg="green")
        return True

    return False

def resetar_jogo():
    global turno, jogo_ativo, tabuleiro
    
    # Reseta o jogo
    turno = "X"  # Começa com "X"
    jogo_ativo = True  # Ativa o jogo novamente
    tabuleiro = [["" for _ in range(3)] for _ in range(3)]  # Limpa a matriz de tabuleiro
    
    # Reseta os botões
    for i in range(3):
        for j in range(3):
            botoes[i*3+j].config(text="", state="normal", bg="white", fg="black")

window = tk.Tk()
window.title("Tic-Tac-Toe")
# Criando o Canvas
canvas = tk.Canvas(window, width=512, height=512, bg="white")
canvas.pack()

# Desenhando linhas assim que o Canvas é criado
canvas.create_line(0, 170, 512, 170, fill="black", width=2)  # Linha horizontal
canvas.create_line(0, 340, 512, 340, fill="black", width=2)  # Linha horizontal
canvas.create_line(340, 0, 340, 512, fill="black", width=2)  # Linha vertical
canvas.create_line(170, 0, 170, 512, fill="black", width=2)  # Linha vertical

def criar_botao(linha, coluna):
    botao = tk.Button(
        window,
        text="",
        command=lambda: acao(botao, linha, coluna),  # Passa a posição para a função
        borderwidth=0,
        bg="white",
        font=("arial", 35)
    ) 
    botao.place(x=coluna * 170 + 5, y=linha * 170 + 5, width=160, height=160)
    botoes.append(botao)

# Criando 9 botões (3x3)
for linha in range(3):
    for coluna in range(3):
        criar_botao(linha, coluna)

# Criando o botão de reset
botao_reset = tk.Button(
    window,
    text="Resetar",
    command=resetar_jogo,
    font=("arial", 15),
    bg="lightgray",
    width=20,
    height=2
)
botao_reset.pack(pady=10)

window.mainloop()

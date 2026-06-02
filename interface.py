import customtkinter as ctk
from uteis import lista_de_unidades


def criar_janela():

    def atualizar_unidades(categoria_escolhida):

        lista = unidades_lista[categoria_escolhida]

        unidade_inicial.configure(values=lista)
        unidade_inicial.set(lista[0])

        unidade_destino.configure(values=lista)
        unidade_destino.set(lista[0])


    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    janela = ctk.CTk()
    janela.geometry("400x500")
    janela.title("Conversor de Unidades")

    # Título
    titulo = ctk.CTkLabel(
        janela,
        text="Conversor de Unidades",
        font=("Arial", 20, "bold")
    )
    janela.grid_columnconfigure(0, weight=1)
    titulo.grid(
        row=0,
        column=0,
        padx=20,
        pady=20,
    )

    # Categoria de unidade_label
    categoria_label = ctk.CTkLabel(
        janela,
        text="Categoria:",
        font=("arial", 18)
    )

    categoria_label.grid(
        row=1,
        column=0,
        padx=20,
        pady=(10, 5),
        sticky="w"
    )

    unidades_lista = lista_de_unidades()

    categoria = ctk.CTkComboBox(
        janela,
        values= list(unidades_lista.keys()),
        font=("arial", 15),
        command=atualizar_unidades

    )

    categoria.grid(
        row=2,
        column=0,
        padx=20,
        pady=(0, 15),
        sticky="w"
    )

    # valor_label a ser colocado
    valor_label = ctk.CTkLabel(
        janela,
        text="Valor:",
        font=("arial", 18)
    )
    valor_label.grid(
        row=3,
        column=0,
        padx=20,
        pady=(0,15),
        sticky="w"
    )

    inserir_valor = ctk.CTkEntry(
        janela,
        width=150,

    )

    inserir_valor.grid(
        row=4,
        column=0,
        padx=20,
        pady=(0,15),
        sticky="w"
    )

    #escolha de conversão
    unidade_label = ctk.CTkLabel(
        janela,
        text="De:",
        font=("arial", 15)
    )
    unidade_label.grid(
        row=5,
        column=0,
        padx=20,
        pady=(0, 15),
        sticky="w"
    )
    unidade_inicial = ctk.CTkComboBox(
        janela,
        values=[],
        font=("arial", 15)
    )

    unidade_inicial.grid(
        row=6,
        column=0,
        padx=20,
        pady=(0,15),
        sticky="w"
    )

    #unidade final
    unidade_final = ctk.CTkLabel(
        janela,
        text="Para:",
        font=("arial", 15)
    )
    unidade_final.grid(
        row=7,
        column=0,
        padx=20,
        pady=(0,15),
        sticky="w"
    )

    unidade_destino = ctk.CTkComboBox(
        janela,
        values=[],
        font=("arial",15)
    )

    unidade_destino.grid(
        row=8,
        column=0,
        padx=20,
        pady=(0,15),
        sticky="w"
    )

    categoria.set("Comprimento")
    atualizar_unidades("Comprimento")

    #botao de conversao
    botao_converter = ctk.CTkButton(
        janela,
        text="Converter",
    )

    botao_converter.grid(
        row=9,
        column=0,
        padx=20,
        pady=(10, 15),
        sticky="w"
    )
    janela.mainloop()


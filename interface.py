import customtkinter as ctk

from conversor import converter
from uteis import lista_de_unidades


def criar_janela():
    unidades_lista = lista_de_unidades()

    def atualizar_unidades(categoria_escolhida):
        lista = unidades_lista[categoria_escolhida]

        unidade_inicial.configure(values=lista)
        unidade_inicial.set(lista[0])

        unidade_destino_combo.configure(values=lista)
        unidade_destino_combo.set(lista[0])

        resultado_valor.configure(text="Aguardando conversão")
        resultado_card.configure(border_color="#334155")

    def conversao():
        valor = inserir_valor.get()
        categoria = categorias.get()
        unidade_origem = unidade_inicial.get()
        unidade_destino = unidade_destino_combo.get()

        resultado = converter(valor, categoria, unidade_origem, unidade_destino)
        erro = isinstance(resultado, str)

        if erro:
            resultado_valor.configure(text=resultado)
            resultado_card.configure(border_color="#ef4444")
        else:
            resultado_valor.configure(text=f"{resultado:.3f} {unidade_destino}")
            resultado_card.configure(border_color="#22c55e")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    janela = ctk.CTk()
    janela.geometry("520x640")
    janela.minsize(460, 600)
    janela.title("Conversor de Unidades")
    janela.configure(fg_color="#0f172a")

    janela.grid_columnconfigure(0, weight=1)
    janela.grid_rowconfigure(1, weight=1)

    cabecalho = ctk.CTkFrame(janela, fg_color="transparent")
    cabecalho.grid(row=0, column=0, padx=28, pady=(28, 18), sticky="ew")
    cabecalho.grid_columnconfigure(0, weight=1)

    titulo = ctk.CTkLabel(
        cabecalho,
        text="Conversor de Unidades",
        font=ctk.CTkFont(family="Segoe UI", size=28, weight="bold"),
        text_color="#f8fafc",
    )
    titulo.grid(row=0, column=0, sticky="w")

    subtitulo = ctk.CTkLabel(
        cabecalho,
        text="Converta comprimento, massa e temperatura com rapidez.",
        font=ctk.CTkFont(family="Segoe UI", size=14),
        text_color="#94a3b8",
    )
    subtitulo.grid(row=1, column=0, pady=(6, 0), sticky="w")

    painel = ctk.CTkFrame(
        janela,
        fg_color="#111827",
        corner_radius=18,
        border_width=1,
        border_color="#1f2937",
    )
    painel.grid(row=1, column=0, padx=28, pady=(0, 28), sticky="nsew")
    painel.grid_columnconfigure(0, weight=1)
    painel.grid_columnconfigure(1, weight=1)

    categoria_label = ctk.CTkLabel(
        painel,
        text="Categoria",
        font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
        text_color="#cbd5e1",
    )
    categoria_label.grid(row=0, column=0, columnspan=2, padx=24, pady=(24, 8), sticky="w")

    categorias = ctk.CTkComboBox(
        painel,
        values=list(unidades_lista.keys()),
        command=atualizar_unidades,
        state="readonly",
        height=42,
        corner_radius=10,
        border_width=1,
        border_color="#334155",
        button_color="#2563eb",
        button_hover_color="#1d4ed8",
        dropdown_fg_color="#111827",
        dropdown_hover_color="#1e293b",
        font=ctk.CTkFont(family="Segoe UI", size=14),
    )
    categorias.grid(row=1, column=0, columnspan=2, padx=24, pady=(0, 18), sticky="ew")

    valor_label = ctk.CTkLabel(
        painel,
        text="Valor",
        font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
        text_color="#cbd5e1",
    )
    valor_label.grid(row=2, column=0, columnspan=2, padx=24, pady=(0, 8), sticky="w")

    inserir_valor = ctk.CTkEntry(
        painel,
        height=46,
        corner_radius=10,
        border_width=1,
        border_color="#334155",
        fg_color="#0f172a",
        placeholder_text="Digite um valor",
        font=ctk.CTkFont(family="Segoe UI", size=16),
    )
    inserir_valor.grid(row=3, column=0, columnspan=2, padx=24, pady=(0, 18), sticky="ew")

    unidade_origem_label = ctk.CTkLabel(
        painel,
        text="De",
        font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
        text_color="#cbd5e1",
    )
    unidade_origem_label.grid(row=4, column=0, padx=(24, 10), pady=(0, 8), sticky="w")

    unidade_destino_label = ctk.CTkLabel(
        painel,
        text="Para",
        font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
        text_color="#cbd5e1",
    )
    unidade_destino_label.grid(row=4, column=1, padx=(10, 24), pady=(0, 8), sticky="w")

    unidade_inicial = ctk.CTkComboBox(
        painel,
        values=[],
        state="readonly",
        height=42,
        corner_radius=10,
        border_width=1,
        border_color="#334155",
        button_color="#2563eb",
        button_hover_color="#1d4ed8",
        dropdown_fg_color="#111827",
        dropdown_hover_color="#1e293b",
        font=ctk.CTkFont(family="Segoe UI", size=14),
    )
    unidade_inicial.grid(row=5, column=0, padx=(24, 10), pady=(0, 22), sticky="ew")

    unidade_destino_combo = ctk.CTkComboBox(
        painel,
        values=[],
        state="readonly",
        height=42,
        corner_radius=10,
        border_width=1,
        border_color="#334155",
        button_color="#2563eb",
        button_hover_color="#1d4ed8",
        dropdown_fg_color="#111827",
        dropdown_hover_color="#1e293b",
        font=ctk.CTkFont(family="Segoe UI", size=14),
    )
    unidade_destino_combo.grid(row=5, column=1, padx=(10, 24), pady=(0, 22), sticky="ew")

    botao_converter = ctk.CTkButton(
        painel,
        text="Converter",
        command=conversao,
        height=48,
        corner_radius=12,
        fg_color="#2563eb",
        hover_color="#1d4ed8",
        font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
    )
    botao_converter.grid(row=6, column=0, columnspan=2, padx=24, pady=(0, 24), sticky="ew")

    resultado_card = ctk.CTkFrame(
        painel,
        fg_color="#0f172a",
        corner_radius=16,
        border_width=1,
        border_color="#334155",
    )
    resultado_card.grid(row=7, column=0, columnspan=2, padx=24, pady=(0, 24), sticky="ew")
    resultado_card.grid_columnconfigure(0, weight=1)

    resultado_label = ctk.CTkLabel(
        resultado_card,
        text="Resultado",
        font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
        text_color="#94a3b8",
    )
    resultado_label.grid(row=0, column=0, padx=18, pady=(16, 4), sticky="w")

    resultado_valor = ctk.CTkLabel(
        resultado_card,
        text="Aguardando conversão",
        font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
        text_color="#f8fafc",
        wraplength=420,
        justify="left",
    )
    resultado_valor.grid(row=1, column=0, padx=18, pady=(0, 18), sticky="w")

    categorias.set("Comprimento")
    atualizar_unidades("Comprimento")

    janela.mainloop()

from PIL import Image, ImageEnhance
from tkinter import filedialog


def saturar_imagem():
    arquivo_entrada = filedialog.askopenfilename(
        title="Selecione uma imagem", filetypes=[("Imagens", ".jpg .jpeg .png .bmp")])

    if arquivo_entrada:
        imagem = Image.open(arquivo_entrada).convert(
            'RGB')  # Converter para RGB
        enhancer = ImageEnhance.Color(imagem)
        imagem_saturada = enhancer.enhance(2.0)

        arquivo_saida = filedialog.asksaveasfilename(
            title="Salvar imagem saturada", defaultextension=".jpg", filetypes=[("Imagens", ".jpg .jpeg .png .bmp")])

        if arquivo_saida:
            imagem_saturada.save(arquivo_saida)
            print("Imagem saturada salva com sucesso!")


saturar_imagem()

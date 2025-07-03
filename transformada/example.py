#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 23:42:16 2024

"""

import cv2  # Importa a biblioteca OpenCV para processamento de imagens
import CNTransform as cn  # Importa um módulo personalizado chamado CNTransform
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para visualização de dados


# Lê a imagem 'c001_15.png' em escala de cinza
img = cv2.imread('c001_15.png', cv2.IMREAD_GRAYSCALE)

# Converte a imagem para tipo float
img = img.astype(float)

# Define o valor máximo do raio
raio_max = 17

# Obtém as dimensões da imagem
H = len(img)  # Altura da imagem
W = len(img[0])  # Largura da imagem

# Cria uma instância da classe CNTransform, define os parametros
rede = cn.CNTransform(nro_col=H, nro_lin=W, raio_max=raio_max, normalize='minmax')
#rede = cn.CNTransform(nro_col=H, nro_lin=W, raio_max=raio_max) #sem normalizacao 

# Computa as transformações na imagem, a partir daqui pode ser feito em um laço para cada imagem
transformed_imgs = rede.compute(img)

# Obtém a imagem transformada usando a medida de grau de saida para o raio 5 
image = transformed_imgs['degree_out_5']


########################### Plot para fins de visualização do resultado ###########################

# Define os raios a serem plotados
raios = [1, 3, 5, 7, 9, 11, 13, 15, 17]
medidas = ['degree_out', 'degree_in', 'force_out', 'force_in']
# Cria uma figura com subplots organizados em grade
fig, axes = plt.subplots(len(medidas) + 1, len(raios), figsize=(15, 10))

# Plota a imagem original centralizada na primeira linha
axes[0, len(raios)//2].imshow(img, cmap='gray')
axes[0, len(raios)//2].axis('off')
axes[0, len(raios)//2].set_title('Imagem Original')

# Adiciona o título abaixo da imagem original
#fig.text(0.5, 0.5, 'Transformações CN para diferentes raios e medidas', ha='center')

# Itera sobre as medidas e raios para preencher a grade
for i, medida in enumerate(medidas):
    for j, raio in enumerate(raios):
        # Obtém a imagem transformada correspondente
        img_transformed = transformed_imgs[f'{medida}_{raio}']
        
        # Plota a imagem no subplot correspondente
        axes[i + 1, j].imshow(img_transformed, cmap='gray')
        axes[i + 1, j].axis('off')
        
        # Adiciona título apenas na primeira linha após a original
        if i == 0:
            axes[i + 1, j].set_title(f'Raio {raio}')
        
        # Adiciona label apenas na primeira coluna
        if j == 0:
            axes[i + 1, j].set_ylabel(medida)

# Remove os subplots vazios
for i in range(len(medidas) + 1):
    for j in range(len(raios)):
        if i == 0 and j != len(raios)//2:  # Remove todos exceto o central na primeira linha
            fig.delaxes(axes[i, j])

# Ajusta o espaçamento entre os subplots
plt.tight_layout()
plt.show()


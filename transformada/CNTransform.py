#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:16:14 2023

"""
#
# Compilação:
# Para compilar em Linux/Windows: g++ -shared -fPIC -o CNModel.so CNModel.cpp
# Para compilar no macOS (M1/M2): g++ -arch x86_64 -shared -fPIC -o CNModel.so CNModel.cpp

import ctypes  # Importa a biblioteca ctypes para chamar funções de bibliotecas C
import numpy as np  # Importa a biblioteca numpy para manipulação de arrays
import cv2  # Importa a biblioteca OpenCV para processamento de imagens
import CNTransform as cn  # Importa um módulo personalizado chamado CNTransform
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para visualização de dados

# Define uma estrutura de dados chamada Measures para armazenar vários tipos de medidas
class Measures(ctypes.Structure):
    _fields_ = [('degree_out', ctypes.POINTER(ctypes.c_double)),
                ('degree_in', ctypes.POINTER(ctypes.c_double)),
                ('diff_out', ctypes.POINTER(ctypes.c_double)),
                ('diff_in', ctypes.POINTER(ctypes.c_double)),
                ('dist_out', ctypes.POINTER(ctypes.c_double)),
                ('dist_in', ctypes.POINTER(ctypes.c_double))]

# Define uma classe chamada CNTransform
class CNTransform:
    def __init__(self, nro_col, nro_lin, raio_max=5, max_level=255, normalize='minmax'):
        # Inicializa os atributos da classe
        self.raio_max = raio_max  # Define o raio máximo
        self.max_level = max_level  # Define a intensidade máxima (255 para imagens de 8 bits)
        
        # Define uma função lambda para normalização que inicialmente não faz nada
        self.normalize = lambda image: image
        
        if normalize == 'minmax':
            # Define uma função lambda para normalização usando a normalização min-max do OpenCV
            self.normalize = lambda image: cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        #Outras normalizacoes podem ser definidas aqui, caso nenhuma normalização for passada, fica sem
        
        # Carrega a biblioteca CNDireted.so usando ctypes
        self.net = ctypes.CDLL("CNModel.so")
        self.nro_col = nro_col  # Define o número de colunas
        self.nro_lin = nro_lin  # Define o número de linhas
        self.N = nro_lin * nro_col * self.raio_max  # Calcula o número total de nós na rede

        # Define os tipos de argumentos e o tipo de retorno para a função model na biblioteca C
        self.net.model.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.net.model.restype = ctypes.POINTER(Measures)

        # Define os tipos de argumentos e o tipo de retorno para a função freeMemory na biblioteca C
        self.net.freeMemory.argtypes = [ctypes.POINTER(Measures)]
        self.net.freeMemory.restype = None


    
    def compute(self, img):
        # Converte a imagem para tipo float
        img = img.astype(float)
    
        # Converte os dados da imagem para um ponteiro de ponteiro de double
        data = img.ctypes.data_as(ctypes.POINTER(ctypes.POINTER(ctypes.c_double)))
    
        # Chama a função 'model' da biblioteca C e obtém o ponteiro para a estrutura de medidas
        struct_ptr = self.net.model(data, self.nro_lin, self.nro_col, self.raio_max)
        measures_output = struct_ptr.contents
        
        # Recebe o retorno da modelagem e converte para arrays numpy
        degree_out = np.ctypeslib.as_array(measures_output.degree_out, shape=(self.N,))
        degree_in = np.ctypeslib.as_array(measures_output.degree_in, shape=(self.N,))
        diff_out = np.ctypeslib.as_array(measures_output.diff_out, shape=(self.N,))
        diff_in = np.ctypeslib.as_array(measures_output.diff_in, shape=(self.N,))
        dist_out = np.ctypeslib.as_array(measures_output.dist_out, shape=(self.N,))
        dist_in = np.ctypeslib.as_array(measures_output.dist_in, shape=(self.N,))
    
        # Redimensiona o retorno para uma matriz de tamanho (raio_max) x (nro_col * nro_lin)
        # lembrando que a linha 0 refere-se ao raio 1 e assim por diante
        degree_out = degree_out.reshape((self.raio_max, self.nro_col * self.nro_lin))
        degree_in = degree_in.reshape((self.raio_max, self.nro_col * self.nro_lin))
        diff_out = diff_out.reshape((self.raio_max, self.nro_col * self.nro_lin))
        diff_in = diff_in.reshape((self.raio_max, self.nro_col * self.nro_lin))
        dist_out = dist_out.reshape((self.raio_max, self.nro_col * self.nro_lin))
        dist_in = dist_in.reshape((self.raio_max, self.nro_col * self.nro_lin))
    
        # Dicionário para armazenar as imagens transformadas
        transformed_imgs = {}
    
        # Processa o raio 1
        transformed_imgs['degree_in_1'] = self.normalize(degree_in[0, :].reshape((self.nro_lin, self.nro_col)))
        transformed_imgs['degree_out_1'] = self.normalize(degree_out[0, :].reshape((self.nro_lin, self.nro_col)))
        transformed_imgs['force_in_1'] = self.normalize((diff_in[0, :] / self.max_level).reshape((self.nro_lin, self.nro_col)))
        transformed_imgs['force_out_1'] = self.normalize((diff_out[0, :] / self.max_level).reshape((self.nro_lin, self.nro_col)))
    
        # Loop para processar os demais raios
        for i in range(1, self.raio_max): #i se refere ao raio=i+1
            # Calcula o grau de saída acumulado
            degree_out[i, :] = np.sum(degree_out[i-1:i+1, :], axis=0)
            transformed_imgs['degree_out_' + str(i + 1)] = self.normalize(degree_out[i, :].reshape((self.nro_lin, self.nro_col)))
            
            # Calcula o grau de entrada
            transformed_imgs['degree_in_' + str(i + 1)] = self.normalize(degree_in[i, :].reshape((self.nro_lin, self.nro_col)))
    
            # Calcula a força de entrada
            transformed_imgs['force_in_' + str(i + 1)] = self.normalize(self._compute_force(diff_in, dist_in, i).reshape((self.nro_lin, self.nro_col)))
            
            # Calcula a força de saída
            transformed_imgs['force_out_' + str(i + 1)] = self.normalize(self._compute_force(diff_out, dist_out, i).reshape((self.nro_lin, self.nro_col)))
        
        # Retorna o dicionário com as imagens transformadas
        return transformed_imgs
    
    
    
    def _compute_force(self, diff_level, dist, raio):
        # Calcula a força das arestas usando a fórmula:
        # (|I(i)-I(j)|/255 + (dist-1)/(raio-1)) / 2
        # Lembrando que diff_level é a soma da diferença de cor de todas as arestas e dist é a distância
    
        # Calcula a força para cada nível de raio e soma ao longo do eixo 0
        force = np.sum(
            (
                (diff_level[0:raio+1, :] / self.max_level) +  # Normaliza a diferença de nível de cor
                (dist[0:raio+1, :] / (((raio + 1) ** 2) - 1))  # Normaliza a distância. raio**2 pq dist não aplicou sqrt
            ) / 2,
            axis=0
        )
        
        # Retorna a força calculada
        return force


    def _ctypesCloseLibrary(lib):
        # Obtém a função 'dlclose' da biblioteca padrão do sistema
        dlclose_func = ctypes.CDLL(None).dlclose
    
        # Define os tipos de argumentos da função 'dlclose'
        dlclose_func.argtypes = [ctypes.c_void_p]
    
        # Define o tipo de retorno da função 'dlclose'
        dlclose_func.restype = ctypes.c_int
    
        # Chama a função 'dlclose' passando o identificador da biblioteca a ser fechada
        dlclose_func(lib._handle)

    



if __name__ == '__main__':
    # Lê a imagem 'c001_15.png' em escala de cinza
    img = cv2.imread('c001_15.png', cv2.IMREAD_GRAYSCALE)

    # Converte a imagem para tipo float
    img = img.astype(float)
    
    # Define o valor máximo do raio
    raio_max = 10
    
    # Obtém as dimensões da imagem
    H = len(img)  # Altura da imagem
    W = len(img[0])  # Largura da imagem
    
    # Cria uma instância da classe CNTransform, define os parametros
    rede = cn.CNTransform(nro_col=H, nro_lin=W, raio_max=raio_max, normalize='minmax')
    
    # Computa as transformações na imagem, a partir daqui pode ser feito em um laço para cada imagem
    transformed_imgs = rede.compute(img)
    
    # Obtém a imagem transformada para o raio máximo (grau de saída)
    image = transformed_imgs['degree_out_10']
    
    # Exibe a imagem transformada usando matplotlib
    plt.imshow(image, cmap='gray')
    plt.show()
    
    # Salva a imagem transformada em um arquivo
    cv2.imwrite('img.png', image)





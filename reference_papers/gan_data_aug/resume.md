# **GAN-based Synthetic Medical Image Augmentation for Increased CNN Performance in Liver Lesion Classification**

Maayan Frid-Adar, Idit Diamant, Eyal Klang, Michal Amitai, Jacob Goldberger, Hayit Greenspan  
Tel Aviv University, The Chaim Sheba Medical Center, Bar-Ilan University (Israel)

---

## Palavras-chave
GAN, *Data Augmentation*, CNN, Lesões Hepáticas, Classificação Médica, Imagens Médicas Sintéticas  

---

## Abstract

- present methods for generating synthetic medical images using GANs
- show that it can be used for synthetic data aug and improve the perfomance of CNN 
- dataset of computed tomography images of 182 liver lesions (lesões hepáticas)
- first exploit GAN architectures for synthesizing high quality liver lesion ROIs (Regions of Interest)
- then present a scheme for liver lesion classification using CNN
- then, train the CNN using classic data aug and our synthetic data aug

---

## Introduction

- most common data aug methods: translation, rotation, flip and scale
- GANs gained popularity for generating high quality images
- medical image applications have applied GAN, most studies employed the image-to-image technique to create label-to-segmentation translation, segmentation-to-image translation or medical cross modality translation (section #1 of studies)
- in this work, its used CNNs for classification 
- contributions of the work:
  1. synthesis of high quality focal liver lesions from CT images using generative adversarial networks (GANs)
  2. desing of a CNN-based solution for the liver lesion classification task, with comparable results to state-of-the-art methods
  3. augmentation of the CNN training set, using the generated synthetic data

---

## Liver Lesion Classification

#### *Data*
- dataset made of 182 CT scans (53 cysts, 64 metastases, 65 hemangioma)
- liver lesions vary in shape, contrast and size (10 - 102mm)
- each type of lesion has its characteristics, but metastasis and hemangioma lesions may be 
confusing
- the input to our classification system are ROIs of lesions cropped from CT scans

![fig1](image.png)

#### *CNN Architecture* 
- fixed size input ROIs of 64x64
- intensity range to (0,1)
- three pairs of convolutional layers where each conv layer is followed by a max-pooling layer and two dense fully-connected layers, ending with a soft-max layer to determine the predictions to classify
- ReLu as activation functions
- to reduce overfitting they incoporate a dropout layer with probability of 0.5 during training

> **training procedure**: the mean value of the training images was substracted from each image fed into the CNN. for training we used a batch size of 64 with a learning rate of 0.001 for 150 epochs. they used stochastic gradient descent optimization  

![fig 2](image-1.png)

---


## Objetivo
O artigo propõe o uso de *Generative Adversarial Networks* (GANs) para a geração de imagens sintéticas de lesões hepáticas com o objetivo de aumentar conjuntos de dados limitados em aplicações médicas e melhorar o desempenho de redes neurais convolucionais (CNNs) na classificação de imagens.

## Contexto
Em imagens médicas, datasets rotulados são frequentemente escassos, dificultando o uso de redes profundas. As técnicas clássicas de *data augmentation* (como rotação, translação e escala) têm limitações por oferecerem pouca variabilidade. A proposta do artigo é que imagens geradas por GANs fornecem variabilidade adicional, enriquecendo o conjunto de dados e otimizando o processo de aprendizado.

## Dataset
- 182 imagens de lesões hepáticas obtidas por tomografia computadorizada (CT)
  - 53 cistos
  - 64 metástases
  - 65 hemangiomas
- As lesões foram anotadas por radiologistas especialistas.
- As ROIs foram extraídas e redimensionadas para 64×64 pixels.

## Arquitetura da CNN
- Três pares de camadas convolucionais + *max pooling*
- Duas camadas densas com função *softmax* na saída
- Ativação ReLU, dropout de 0.5
- Treinamento com *SGD* + *Nesterov momentum* (150 épocas)

## GANs Utilizados
- **DCGAN**: GAN convolucional para gerar imagens realistas por categoria.
- **ACGAN**: GAN condicional com classificador auxiliar incorporado.

## Experimentos

### Avaliação com Aumento de Dados
- Comparação entre:
  - Sem aumento de dados
  - *Data augmentation* clássica (rotação, escala, etc.)
  - GAN-based augmentation (DCGAN e ACGAN)

### Resultados
- Aumentos progressivos do dataset mostraram ganho até a saturação (~78.6%)
- Com imagens sintéticas via GANs:
  - Acurácia aumentou para **85.7%**
  - Sensibilidade e especificidade melhoraram para classes complexas
- ACGAN obteve desempenho inferior ao DCGAN

### Avaliação Visual
- Imagens geradas com DCGAN foram difíceis de distinguir das reais por especialistas
- Radiologistas classificaram corretamente ~77.8% das imagens (reais e sintéticas)

### Visualização com t-SNE
- Features extraídas com GAN resultaram em melhor separação visual entre as classes no espaço latente

### Comparação com Estado da Arte
- O método superou o modelo BoVW-MI baseado em *visual words* e *mutual information*
  - CNN com GAN obteve melhores métricas de acurácia, sensibilidade e especificidade

## Conclusões
- GANs são eficazes na geração de imagens sintéticas médicas realistas e úteis
- Aumentam significativamente o desempenho de CNNs na classificação de lesões hepáticas
- Aplicável a outros domínios médicos com escassez de dados
- DCGAN foi mais eficaz que ACGAN neste contexto
- Avaliação por especialistas confirmou realismo das imagens geradas

---

## Studies

#### #1 translations

> *"most studies employ the image-to-image technique to create label-to- segmentation ranslation, segmentation-to-image translation or medical cross modality translations"*

##### image-to-image translation
- é a tarefa de transformar uma imagem de um domínio (tipo, estilo, representação) para outro domínio usando redes neurais
- é tipo um "filtro" de foto, transformando uma foto de dia em uma de noite

##### label-to-segmentation translation
- label é a representação simples (grosseira), ex.: mapa binário, conjunto de pontos chaves, contorno muito básico, máscara de baixa qualidade/resolução
- segmentação é a representação detalhada, é uma máscara onde cada pixel é classificado (ex.: este é vaso sanguíneo, este é tecido saudável...)
- o médico criar labels simples e o GAN faz a segmentação complexa *"pixel-perfect"*


##### segmentation-to-image translation
- transforma a segmentação em uma imagem realista
- por que é util?
  - gerar imagens sintéticas realistas para treinar outros modelos quando dados reais são escassos
  - verificar se a segmentação gerada faz sentido anatomicamente quando convertida para imagem

##### medical cross modality translations
- modalidade é o tipo de exame (ressonancia magnetica, tomografia, raio-X, ultrassom...) e cada uma representas os tecidos de uma forma diferente
- tradução cruzada é transformar uma imagem da modalidade X em uma imagem da modalidade Y

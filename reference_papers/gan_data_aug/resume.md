# 📄 Resumo do Artigo

## Título
**GAN-based Synthetic Medical Image Augmentation for Increased CNN Performance in Liver Lesion Classification**

## Autores
Maayan Frid-Adar, Idit Diamant, Eyal Klang, Michal Amitai, Jacob Goldberger, Hayit Greenspan  
Tel Aviv University, The Chaim Sheba Medical Center, Bar-Ilan University (Israel)

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

## Código-Fonte
- Não especificado no artigo.

## Palavras-chave
GAN, *Data Augmentation*, CNN, Lesões Hepáticas, Classificação Médica, Imagens Médicas Sintéticas
# 📄 Resumo do Artigo

## Título
**Enhancing Histopathological Image Classification Performance through Synthetic Data Generation with Generative Adversarial Networks**

## Autores
Jose L. Ruiz-Casado, Miguel A. Molina-Cabello, Rafael M. Luque-Baena  
Instituto de Investigación Biomédica de Málaga (IBIMA), Universidad de Málaga, Espanha

## Fonte
Publicado em *Sensors*, vol. 24, n° 12, 2024.  
DOI: [10.3390/s24123777](https://doi.org/10.3390/s24123777)

## Objetivo
O artigo propõe avaliar o impacto da utilização de diferentes arquiteturas de redes adversariais generativas (GANs) como técnica de *data augmentation* no contexto da classificação de imagens histopatológicas de câncer de mama. A proposta busca superar o desequilíbrio entre classes presente em conjuntos de dados biomédicos e aumentar a precisão de redes neurais convolucionais (CNNs) utilizadas na tarefa de diagnóstico automático.

## Metodologia

### Dataset
- Base de dados com imagens histopatológicas coloridas (700x460) cedidas pelo laboratório de Visão Robótica e Imagem da UFPR.
- Classes: Benigno (588 imagens) e Maligno (1233 imagens), apresentando desequilíbrio relevante.

### Arquiteturas de GANs utilizadas
- **ProGAN**
- **SNGAN**
- **BEGAN**
- **ReGAN**

Todas foram treinadas separadamente para gerar imagens sintéticas que equilibrassem as classes.

### Avaliação de GANs
- Métrica utilizada: **Frechet Inception Distance (FID)**
- Melhor desempenho: **ProGAN**, com menor FID (261.51 benigno / 222.81 maligno)

### Arquiteturas CNN para Classificação
- **Inception**
- **ResNet**
- **VGG16**

### Configuração do treinamento
- Uso de 500 épocas e *batch size* uniforme (32)
- Validação com *K-fold cross-validation* (k=5)
- Função de perda: *Cross-Entropy*
- Otimizador: Adam (lr=0.0002, β1=0.5, β2=0.999)

## Experimentos

### Categorias de comparação
1. Dataset original
2. Dataset com *data augmentation* tradicional (transformações geométricas)
3. Dataset balanceado por **downsampling**
4. Dataset gerado com cada arquitetura GAN

### Principais resultados

#### GANs
- ProGAN obteve os melhores resultados em FID e desempenho geral.
- ReGAN ProGAN teve desempenho competitivo, com melhor estabilidade (menor desvio padrão).

#### CNNs
- **Inception** foi a melhor arquitetura em termos de acurácia, precisão, *recall* e F1-score.
- GANs superaram métodos tradicionais e *downsampling* em todos os casos.
- A combinação ReGAN + ProGAN foi a mais estável.

### Métricas destacadas (Inception + ProGAN)
- Acurácia: **99.36%**
- F1-score: **0.99**
- Precisão: **0.99**
- *Recall*: **0.99**

### Conclusões
- GANs são altamente eficazes na geração de dados sintéticos realistas para classificação médica.
- ProGAN se destacou, especialmente com regularização ReGAN.
- As técnicas de *data augmentation* baseadas em GANs superaram abordagens tradicionais e são recomendadas para cenários biomédicos com escassez de dados e classes desbalanceadas.

## Código-Fonte
- Repositório oficial no GitHub:  
  [github.com/icai-uma/Enhancing-Classification-Performance-through-Synthetic-Data-Generation-with-GANs](https://github.com/icai-uma/Enhancing-Classification-Performance-through-Synthetic-Data-Generation-with-GANs)
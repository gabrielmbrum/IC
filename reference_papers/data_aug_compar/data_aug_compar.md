# 📄 Comparison of Different Image Data Augmentation Approaches

**Autores**: Loris Nanni, Michelangelo Paci, Sheryl Brahnam, Alessandra Lumini  
**Publicado em**: Journal of Imaging (2021)  
**DOI**: [10.3390/jimaging7120254](https://doi.org/10.3390/jimaging7120254)

## 🎯 Objetivo do Estudo

Investigar e comparar mais de 10 métodos de *data augmentation* (DA) aplicados a imagens, incluindo duas abordagens inéditas baseadas nas transformadas Discrete Wavelet Transform (DWT) e Constant-Q Gabor Transform (CQT). A ideia é avaliar como diferentes estratégias de aumento de dados afetam o desempenho de classificadores baseados em redes convolucionais (CNN), especificamente o ResNet50.

## 🧪 Metodologia

- Cada técnica de *data augmentation* foi usada para gerar novos conjuntos de imagens.
- Redes ResNet50 pré-treinadas no ImageNet foram ajustadas com os dados originais e os aumentados.
- Foram criados *ensembles* (combinados) dessas redes por meio da regra de soma dos escores.
- Avaliação foi feita em quatro conjuntos de dados diversos:
  - **VIR**: imagens de vírus microscópicos (grayscale)
  - **BARK**: imagens de cascas de árvores
  - **POR**: pinturas de diferentes movimentos artísticos
  - **GRAV**: glitches do projeto LIGO para detecção de ondas gravitacionais

## 🧰 Métodos de Data Augmentation Avaliados

### Técnicas Tradicionais (App1–9)
- **App1**: Reflexão e escalonamento aleatório
- **App2–3**: Adição de rotação, translação e cisalhamento
- **App4**: Perturbações via PCA
- **App5**: Perturbações via DCT
- **App6–7**: Alterações de contraste, nitidez, cor, e desfoque
- **App8**: Mapeamento não linear com histogramas de outra imagem da mesma classe
- **App9**: Deformações elásticas com campos de deslocamento aleatórios

### Métodos Propostos (Novos)
- **App10 (DWT)**: Aplicação de transformada wavelet com perturbações nos coeficientes seguidas de reconstrução inversa
- **App11 (CQT)**: Similar ao App10, mas usando transformada de Gabor com base constante (CQT)

## 📊 Resultados

- Todos os métodos de *data augmentation* melhoraram os resultados em relação ao modelo base (sem DA).
- O *ensemble* EnsDA\_all (combinando os 11 métodos) obteve resultados de estado da arte ou superiores em todos os datasets:
  - VIR: **90.00%**
  - BARK: **91.27%**
  - GRAV: **98.33%**
  - POR: **89.21%**
- O método baseado em DWT (App10) teve o melhor desempenho isolado no GRAV (**98.41%**).
- Técnicas baseadas apenas em PCA mostraram desempenho inferior comparado a versões melhoradas propostas.

## 🔍 Conclusões

- Combinar diversas técnicas de *data augmentation* é uma forma eficaz de construir classificadores robustos.
- As novas estratégias baseadas em transformadas (DWT e CQT) são promissoras e competitivas.
- Variação no tipo de DA é essencial para montar *ensembles* eficazes e adaptáveis a diferentes domínios.

## 📎 Recursos

- Todo o código-fonte dos experimentos está disponível em:  
  [https://github.com/LorisNanni](https://github.com/LorisNanni)

# A Survey on Image Data Augmentation for Deep Learning

**Autores**: Connor Shorten, Taghi M. Khoshgoftaar

## 📌 Objetivo

Este artigo apresenta uma revisão sistemática das técnicas de *image data augmentation* aplicadas a redes neurais profundas, abordando tanto métodos clássicos (como rotações e recortes) quanto técnicas modernas baseadas em aprendizado profundo, como GANs, *style transfer* e *adversarial training*. O foco é mitigar o problema do *overfitting* causado por conjuntos de dados limitados, especialmente em áreas como análise de imagens médicas.

## 🧠 Contexto

Redes neurais profundas (especialmente CNNs) precisam de grandes volumes de dados para generalizar bem. Entretanto, domínios como o médico frequentemente sofrem com escassez de dados rotulados. Técnicas de *data augmentation* têm se mostrado uma solução prática, gerando novas amostras sintéticas a partir de dados existentes sem comprometer suas etiquetas originais.

## 🧰 Técnicas de Augmentation

### 🔹 Transformações Clássicas (Data Warping)
- **Geométricas**: rotação, translação, espelhamento, recorte, inserção de ruído.
- **Fotométricas**: alteração de cores, brilho, contraste, espaço de cor.
- **Kernel filters**: desfoque, nitidez, filtros de convolução.
- **Random Erasing**: remoção de regiões aleatórias da imagem para forçar generalização.

### 🔸 Técnicas de Oversampling
- **Mixing de imagens**: combinação de duas imagens em uma nova.
- **GANs (Generative Adversarial Networks)**: geração de imagens realistas a partir de vetores aleatórios.
- **Feature Space Augmentation**: interpolação/extrapolação em espaços latentes.

### 🧪 Técnicas Avançadas
- **Adversarial Training**: gera amostras adversárias que induzem erro no modelo.
- **Neural Style Transfer**: aplica estilos visuais de uma imagem a outra.
- **Meta-learning**: frameworks como AutoAugment que aprendem automaticamente as melhores estratégias de aumento.

## 🏥 Aplicações em Imagens Médicas

O artigo enfatiza que aplicações médicas se beneficiam diretamente de *data augmentation* devido:
- À escassez de imagens rotuladas.
- Ao custo e à dificuldade de obtenção de exames.
- À variabilidade de padrões visuais (texturas, contrastes, anomalias).

Exemplos com sucesso incluem o uso de **DCGANs para gerar lesões hepáticas**, melhorando significativamente a acurácia dos modelos de classificação.

## 🧭 Considerações de Projeto

- **Segurança de etiquetas**: nem toda transformação mantém o rótulo original válido.
- **Composição de técnicas**: múltiplas técnicas podem ser combinadas, mas é necessário cuidado com redundância ou ruído.
- **Curriculum learning e test-time augmentation** também são abordados como estratégias complementares.

## 🔬 Conclusão

O artigo reforça que *data augmentation* é fundamental para melhorar modelos de *deep learning*, especialmente em domínios com dados limitados como medicina. Técnicas baseadas em GANs, *feature space* e *meta-learning* representam fronteiras promissoras. O trabalho também evidencia a necessidade de métodos automatizados e específicos para cada domínio de aplicação.
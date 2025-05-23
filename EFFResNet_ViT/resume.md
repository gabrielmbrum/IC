# 📄 Resumo do Artigo

## Título
**EFFResNet-ViT: A Fusion-Based Convolutional and Vision Transformer Model for Explainable Medical Image Classification**

## Objetivo
O artigo propõe o modelo híbrido **EFFResNet-ViT**, que combina *EfficientNet-B0* e *ResNet-50* com um *Vision Transformer (ViT)* para melhorar a acurácia e interpretabilidade na classificação de imagens médicas. A proposta busca superar as limitações de CNNs (viés local) e ViTs (alta demanda de dados), oferecendo um sistema robusto e explicável.

## Justificativa
A classificação automática de imagens médicas é essencial na medicina moderna, mas enfrenta desafios como escassez de dados rotulados, variações estruturais entre pacientes e necessidade de explicabilidade. CNNs são boas para padrões locais, enquanto ViTs são eficazes para capturar dependências globais — sua combinação oferece o melhor dos dois mundos.

## Arquitetura Proposta
- **EFFResNet-ViT**: Integra as extrações locais das CNNs com a capacidade de contexto global dos ViTs.
- Fusão dos recursos extraídos por EfficientNet-B0 e ResNet-50.
- Embeddings gerados por convoluções e passados para o encoder do ViT.
- Camada CNN pós-transformer + *Global Average Pooling (GAP)* + *MLP* com softmax.
- Explicabilidade com **Grad-CAM** e análise de separabilidade com **t-SNE**.

## Avaliação
### Bases utilizadas:
- **BT CE-MRI** (Kaggle): imagens de tumores cerebrais (glioma, meningioma, pituitário e sem tumor).
- **Retinal Dataset** (Kaggle): imagens de retina com catarata, retinopatia diabética, glaucoma e normais.

### Resultados:
- **BT CE-MRI**:
  - Acurácia: 99.31%
  - AUC: 99.91%
  - F1-score: 99.26%
- **Retinal Dataset**:
  - Acurácia: 92.54%
  - AUC: 98.82%
  - MCC: 90.05%

### Comparações:
- EFFResNet-ViT superou os modelos individuais (ViT, EfficientNetB0-ViT e ResNet50-ViT) em todos os critérios.
- Visualizações do Grad-CAM mostram foco preciso nas áreas relevantes das imagens, em contraste com outros modelos.
- Resultados de t-SNE indicam separação clara das classes, reforçando a qualidade das representações extraídas.

## Contribuições Principais
1. Proposição de um modelo híbrido robusto para classificação médica.
2. Integração eficaz de CNNs e ViT com explicabilidade baseada em Grad-CAM.
3. Desempenho superior em duas bases públicas e com diferentes modalidades.
4. Potencial real de adoção clínica pela transparência e precisão alcançadas.

## Código-fonte
❌ O artigo **não informa explicitamente** a disponibilização de código-fonte público. Pode ser necessário contatar os autores.

## Palavras-chave
*EfficientNet-B0*, *ResNet-50*, *Vision Transformer*, *Medical Imaging*, *Grad-CAM*, *Explainability*, *Deep Learning*
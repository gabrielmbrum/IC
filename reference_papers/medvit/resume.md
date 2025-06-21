# 📄 Resumo do Artigo

## Título
**MedViT: A Robust Vision Transformer for Generalized Medical Image Classification**

## Autores
Omid Nejati Manzari, Hamid Ahmadabadi, Hossein Kashiani, Shahriar B. Shokouhi, Ahmad Ayatollahi  
*Iran University of Science and Technology & West Virginia University*

## Objetivo
O artigo propõe a arquitetura híbrida *MedViT*, que combina características locais de *Convolutional Neural Networks (CNNs)* com a capacidade de captura de dependências globais dos *Vision Transformers (ViTs)*, visando melhorar a classificação de imagens médicas e aumentar a robustez contra ataques adversariais.

## Motivação
Apesar dos avanços com CNNs no diagnóstico automatizado, essas redes possuem limitações para capturar dependências de longo alcance — fundamentais em imagens médicas com variações de textura, forma e tamanho. ViTs resolvem esse problema, mas exigem muitos dados e apresentam alta complexidade computacional. Além disso, redes neurais estão sujeitas a ataques adversariais, o que é crítico em contextos clínicos.

## Proposta
O modelo *MedViT* combina:
- **Efficient Convolution Block (ECB)**: captura padrões locais com convoluções otimizadas.
- **Local Transformer Block (LTB)**: mistura informações de baixa e alta frequência.
- **Patch Momentum Changer (PMC)**: técnica de aumento de dados no espaço de características que melhora a generalização e robustez adversarial.

## Arquitetura
- Hierárquica com 4 estágios, reduzindo gradualmente a resolução espacial.
- Três variantes: **MedViT-T**, **MedViT-S** e **MedViT-L**, com diferentes tamanhos e profundidades.
- Treinamento com AdamW por 100 épocas em imagens 224x224.

## Dataset Utilizado
- **MedMNIST v2 (2D)**: conjunto padronizado com 12 bases biomédicas (ex: PathMNIST, ChestMNIST, DermaMNIST, RetinaMNIST, etc.).
- Modalidades variadas: raio-X, ultrassom, tomografia, OCT.

## Avaliação
- **Métricas**: AUC (Área sob a Curva ROC) e ACC (Acurácia)
- **Comparação com SOTA**: MedViT superou CNNs (ResNet, EfficientNet) e outros ViTs (Swin, PVT, DeiT, etc.).
- **Melhores Resultados**:
  - AUC média: **94.2%** com MedViT-S
  - ACC média: **85.1%** com MedViT-S
  - Desempenho robusto em diversas tarefas e modalidades.

## Robustez Adversarial
- Testado contra ataques **FGSM** e **PGD**.
- MedViT-T* (com PMC) obteve:
  - **+38.4%** de robustez sobre ResNet-18 em TissueMNIST (FGSM)
  - **+30.2%** (PGD)
- PMC aplicado no primeiro estágio foi o mais eficaz.

## Visualizações
- Uso de **Grad-CAM** para comparação com ResNet-18 demonstrou que MedViT foca melhor nas regiões relevantes da imagem médica, com menor influência de fundo.

## Conclusão
- MedViT apresenta alto desempenho, robustez e generalização para múltiplos domínios médicos.
- A abordagem híbrida e o uso do PMC mostram que é possível treinar ViTs com maior segurança e menos dados.
- Propõe uma base sólida para aplicação clínica de modelos baseados em *transformers*.

## Código-Fonte
*Não foi explicitamente mencionado no artigo, mas pode estar disponível em repositórios futuros associados aos autores.*

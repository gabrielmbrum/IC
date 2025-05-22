# 📄 Feature Transforms for Image Data Augmentation

**Autores**: Loris Nanni, Michelangelo Paci, Sheryl Brahnam, Alessandra Lumini  
**Publicado em**: Neural Computing and Applications (2022)  
**DOI**: [10.1007/s00521-022-07645-z](https://doi.org/10.1007/s00521-022-07645-z)

## 🎯 Objetivo

Este artigo propõe e avalia um conjunto de métodos de *data augmentation* baseados em transformadas matemáticas (Fourier, Radon e DCT), com o objetivo de melhorar a robustez de redes neurais convolucionais (CNNs) treinadas em bases de dados pequenas. Os autores testam essas abordagens em combinação com outras técnicas conhecidas, avaliando sua eficácia na construção de *ensembles* de classificadores em 11 bases de dados de classificação de imagens.

---

## 🧠 Contexto e Motivação

CNNs apresentam ótimo desempenho em tarefas de classificação, mas tendem a sobreajustar quando treinadas com poucos dados. Como muitas bases (como as médicas) são pequenas e difíceis de ampliar, o uso de *data augmentation* tornou-se uma solução prática e eficiente. O artigo explora o uso de transformações de características (*feature transforms*) como uma alternativa promissora às técnicas tradicionais, pouco explorada na literatura.

---

## 🔍 Métodos Propostos

Os autores desenvolveram 14 métodos de *data augmentation*:

### 🔹 Métodos Clássicos (App1–App11)
- Reflexões, rotações, translações, cisalhamento, alteração de contraste/cor/nitidez.
- Técnicas com DCT, PCA, elastic deformations, histogram matching e normalização de coloração.
- Diversas técnicas de perturbação nos domínios espacial e de frequência.

### 🔸 Métodos Inovadores (App12–App14)
- **App12**: Perturbações e fusões no domínio DCT com imagens da mesma e de diferentes classes.
- **App13**: Uso da transformada de **Radon**, alterando o conjunto de ângulos para projeção.
- **App14**: Aplicação de **FFT** e DCT com descarte ou filtragem de componentes antes da reconstrução.

---

## 🧪 Metodologia Experimental

- Foram treinadas 14 CNNs (ResNet50), cada uma com dados aumentados por um dos métodos.
- *Ensembles* foram construídos combinando os classificadores (fusão pela soma das saídas).
- Testes foram feitos em **11 datasets** diversos: imagens biomédicas, naturais, artísticas, texturas, etc.
- Também foi feita uma análise usando a arquitetura MobileNetV2 para validar generalização.

---

## 📊 Resultados

- As abordagens baseadas em transformadas (App12–App14) mostraram desempenho competitivo.
- O ensemble **EnsDA\_B** (com todos os 14 métodos) superou abordagens do estado da arte em diversos datasets.
- Resultados são superiores em termos de acurácia e área sob a curva ROC (AUC).
- Datasets como GRAV e END mostraram ganhos notáveis com métodos baseados em *feature transforms*.

---

## 📌 Conclusão

O estudo demonstra que:
- Combinar múltiplas técnicas de *data augmentation* (especialmente aquelas baseadas em transformações) aumenta a diversidade entre classificadores.
- A construção de *ensembles* sobre conjuntos aumentados é uma estratégia eficaz e robusta.
- As transformações de características (Fourier, Radon e DCT) são úteis como alternativas viáveis para aumentar conjuntos de dados, especialmente em contextos médicos e de baixa disponibilidade de amostras.

---

## 📂 Código-fonte

O código MATLAB está disponível em:  
🔗 [https://github.com/LorisNanni/Feature-transforms-for-image-data-augmentation](https://github.com/LorisNanni/Feature-transforms-for-image-data-augmentation)

---

## 📚 Citação BibTeX

```bibtex
@article{nanni2022feature,
  title={Feature transforms for image data augmentation},
  author={Nanni, Loris and Paci, Michelangelo and Brahnam, Sheryl and Lumini, Alessandra},
  journal={Neural Computing and Applications},
  volume={34},
  pages={22345--22356},
  year={2022},
  publisher={Springer},
  doi={10.1007/s00521-022-07645-z}
}

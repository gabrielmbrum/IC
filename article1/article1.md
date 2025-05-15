# Color-texture classification based on spatio-spectral complex 

## resumo

propõe um método para análise de textura coloridas por aprendizado de representações _spatio-spectral_ a partir de um rede complexa utilizando RNN (Randomized Neural Network).

modela-se a iamgem como uma rede complexa baseada no modelo SSN (_Spatio-Spectral Network_), que considera conexões na topologia para representar as características espaciais e padrões espectrais.

insight: características topológicas complexas da SSN podem ser incorporadas por um modelo de rede neural simples e rápido para a classificação de texturas coloridas.

investiga-se como utilizar efetivamente a RNN para analisar/representar os padrões espaciais/espectrais a partir da SSN.

utilizam medidas de vértices da SSN para treinar a RNN para prever as dinamicas da evolução de um rede complexa e adotar os pesos aprendidos para da camada de saída como descritores.

obteve resultados melhores que vários da literatura, incluindo _deep convolutional neural networks_. 

ótimo para reconhecimento de espécies de planta.
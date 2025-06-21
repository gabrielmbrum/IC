# CNIT: Complex Network Image Transform

utiliza técnicas de modelagem de redes complexas para representar a imagem de entrada.

a imagem é modelada como um grafo complexo, onde cada pixel é transformado em um vértice, e as arestas são definidas com base na conectividade de vizinhança de raio r.

I é uma imagem onde os pixels i = (x<sub>i</sub>, y<sub>i</sub>)

cada pixel i é mapeado como um vértice v<sub>i</sub> ∈ V e dois vértices são conectados por uma aresta se a distância euclidiana entre eles é menor que o raio r.

então, as arestas são A = {{v<sub>i</sub>, v<sub>j</sub>} | v<sub>i</sub>, v<sub>j</sub> ∈ V, i != j e (x<sub>i</sub> - x<sub>j</sub>)<sup>2</sup> + (y<sub>i</sub> - y<sub>j</sub>)<sup>2</sup> < r<sup>2</sup> }

o peso das arestas é dado pela diferença absoluta nos níves cinzas da correspondência de pixels, isto é, o peso de um aresta conectando v<sub>i</sub> e v<sub>j</sub> é w<sub>ij</sub> = |I(x<sub>i</sub>, y<sub>i</sub>) - I(x<sub>j</sub>, y<sub>j</sub>)|. onde I(x<sub>i</sub>, y<sub>i</sub>) e I(x<sub>j</sub>, y<sub>j</sub>) são a escala cinza de intensidade de valores dos pixels i e j, respectivamente.

essa abordagem consiste em transformar o complexo modelo de rede em novas imagens que enfatizem diferentes padrões de textura a partir da imagem original codificada dentro da topologia de rede.

exemplo:
![figura 1 do artigo](image.png)

o processo de transformação envolve mapear medidas de vertices, grau e força, para intensidade de valores de pixel, resultando em imagens que encapsulem os padrões de texto subjacentes. 

o grau de um vertice representa o número de conexões que ele tem com outros vertices.

a força é calculada com a combinação de dois fatores:
- a diferença normalizada na escala cinza de intensidade entre v<sub>i</sub> e todos os outros vértices conectados
- distância euclidiana entre os vertices conectados

![fórmula da força](image-1.png)

sendo d<sub>ij</sub> a distancia euclidiana entre os pixels (x<sub>i</sub>, y<sub>i</sub>) e (x<sub>j</sub>, y<sub>j</sub>) e o r é o raio usado para definir os vizinhos.

os padrões de textura resultantes são influenciados pelo parametro r (raio de conexão), o qual controla a representação estrutural da rede. variando o r, o método capture diferentes escalas de informação de texturas, permitindo analisar micro e macro padrões de textura.

---

### imagens de resumo ;)

![resumo vértices e arestas](image-2.png)

![resumo de transformação](image-3.png)
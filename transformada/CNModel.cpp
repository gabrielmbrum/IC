    /*
     * Compilação:
     * Para compilar em Linux/Windows: g++ -shared -fPIC -o CNModel.so CNModel.cpp
     * Para compilar no macOS (M1/M2): g++ -arch x86_64 -shared -fPIC -o CNModel.so CNModel.cpp
     */

    #include <iostream>
    #include <math.h>
    #include <vector>

    #define L 255  // Define a constante L como 255

    using std::vector;  // Usa o vetor da biblioteca padrão

    // Define uma estrutura para armazenar as medidas
    typedef struct {
        double *degree_out;
        double *degree_in;
        double *diff_out;
        double *diff_in;
        double *dist_out;
        double *dist_in;
    } Measures;

    // Declara a função 'model' como uma função C externa para interoperabilidade com outras linguagens
    extern "C" Measures* model(double* im, int w, int h, int radius) {
        int z, np;
        z = 1;  // Define a variável z como 1
        np = w * h * z;  // Calcula o número total de pixels na imagem

        // Aloca memória para a estrutura Measures
        Measures *output = (Measures*)malloc(sizeof(Measures));

        // Aloca memória para cada um dos arrays na estrutura Measures
        output->degree_out = new double[np * radius];
        output->degree_in = new double[np * radius];
        output->diff_out = new double[np * radius];
        output->diff_in = new double[np * radius];
        output->dist_out = new double[np * radius];
        output->dist_in = new double[np * radius];

        // Inicializa todos os elementos dos arrays com zero
        for (int col = 0; col < np * radius; col++) {
            output->degree_out[col] = 0;
            output->degree_in[col] = 0;
            output->diff_out[col] = 0;
            output->diff_in[col] = 0;
            output->dist_out[col] = 0;
            output->dist_in[col] = 0;
        }

        // Calcula para que raio pertence cada vizinho
        double r = radius * radius;
        int vraio[(int)r];
        for (int i = 1; i <= r; i++) {
            for (int rr = 1; rr <= radius; rr++) {
                if ((rr - 1) * (rr - 1) < i && i <= rr * rr) {
                    vraio[i] = rr;
                    break;
                }
            }
        }



      int rr;
    int rmax = (int)radius;

    for (int c = 0; c < z; c++) {
        // Montando a rede. Cada 'c' representa um vértice (pixel com intensidade R, G ou B). Cada pixel é considerado como 3 vértices (um para cada cor). Estamos usando sempre z=1

        for (int x = 0; x < w; x++) {
            // Itera sobre a largura da imagem.

            for (int y = 0; y < h; y++) {
                // Itera sobre a altura da imagem.

                for (int cw = 0; cw < z; cw++) {
                    // Itera sobre a janela do raio em cada cor. Implementado dessa forma para não precisar alterar muito o código.

                    for (int i = (int)(x - radius); i <= (int)(x + radius); i++) {
                        // Itera horizontalmente dentro da janela do raio.

                        for (int j = (int)(y - radius); j <= (int)(y + radius); j++) {
                            // Itera verticalmente dentro da janela do raio.

                            // Verifica se os índices estão dentro dos limites e se não estamos no mesmo pixel ou canal
                            if (cw >= 0 && cw < z && i >= 0 && i < w && j >= 0 && j < h && ((i != x || j != y) || c != cw)) {

                                // Calcula a diferença de intensidade entre o pixel atual e o pixel na posição (i, j)
                                double diff = (im[y * w + x] - im[j * w + i]);

                                double difference = diff;

                                if (difference < 0) {
                                    difference = -difference;  // Torna a diferença positiva
                                }

                                // Calcula a distância euclidiana quadrada entre os pixels
                                double d = ((x - i) * (x - i) + (y - j) * (y - j));

                                double edgeGray, edgeDist;
                                if (r == 1) {
                                    edgeGray = difference;
                                    edgeDist = 0;
                                } else {
                                    // Calcula os pesos das arestas
                                    edgeGray = difference;
                                    edgeDist = d - 1;
                                }

                                // Condição para adicionar arestas na rede: distância deve ser menor ou igual ao raio e maior que 0
                                if (d <= r && d > 0) {
                                    rr = vraio[(int)d] - 1;

                                    // Se a diferença de intensidade é positiva
                                    if (diff > 0) {
                                        output->degree_out[(((y * w) + x)) + ((w * h) * rr)]++;
                                        output->diff_out[(((y * w) + x)) + ((w * h) * rr)] += edgeGray;
                                        output->dist_out[(((y * w) + x)) + ((w * h) * rr)] += edgeDist;
                                    }
                                    // Se a diferença de intensidade é negativa
                                    else if (diff < 0) {
                                        output->degree_in[(((y * w) + x)) + ((w * h) * rr)]++;
                                        output->diff_in[(((y * w) + x)) + ((w * h) * rr)] += edgeGray;
                                        output->dist_in[(((y * w) + x)) + ((w * h) * rr)] += edgeDist;
                                    }
                                    // Se a diferença de intensidade é zero
                                    else {
                                        output->degree_out[(((y * w) + x)) + ((w * h) * rr)]++;
                                        output->diff_out[(((y * w) + x)) + ((w * h) * rr)] += edgeGray;
                                        output->dist_out[(((y * w) + x)) + ((w * h) * rr)] += edgeDist;

                                        output->degree_in[(((y * w) + x)) + ((w * h) * rr)]++;
                                        output->diff_in[(((y * w) + x)) + ((w * h) * rr)] += edgeGray;
                                        output->dist_in[(((y * w) + x)) + ((w * h) * rr)] += edgeDist;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


        return output;


    }

    extern "C" void freeMemory(Measures *output){

        free(output->degree_out);
        free(output->degree_in);
        free(output->diff_out);
        free(output->diff_in);
        free(output->dist_out);
        free(output->dist_in);

        free(output);
    }


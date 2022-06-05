## Objetivo 

 Na linguagem de sua preferência, crie um servidor HTTP que, para cada requisição GET, retorne como resposta um JSON cuja chave `result` seja a o resultado de uma operação matemática recebida como parâmetro.
 
Os números podem estar no intervalo [-99999, 99999].
As operações podem ser adição: (`+`), subtração (`-`), divisão (`/`) e multiplicação (`*`).
Deve ser respeitada a precedência das operações, incluindo até um nível de parênteses.

## Para rodar:

docker run -d -p 3000:3000 luismomm2110/projeto-certi

curl http://localhost:3000/ + expressao

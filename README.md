# Task 2
## Parte 1: Análise de APKs
Para fins deste trabalho foram extraídas APKs do site https://www.apkmirror.com/categories no qual a obtenção do AndroidManifest de cada APK ocorreu por meio do aplicativo https://ibotpeaches.github.io/Apktool/.

- Obtenha ao menos 10 APKs de, no mínimo, três categorias diferentes (https://www.apkmirror.com/categories/) para compor seu dataset cru

- Para cada APK coletada, extraia o arquivo AndroidManifest.xml em um diretório "manifests", lembrando de identificar o arquivo resultante (por exemplo, se sua APK se chama 'BancoX-v01.apk', nomeie o manifesto como 'AndroidManifest_BancoX-v01.xml').

- Escreva um script em Python (ou um ipynb) que, dado um diretório como argumento de entrada, retorne a lista de permissões de cada AndroidManifest.xml sob a forma de um dicionário (chave: nome da APK, valor: lista de permissões). Exemplo de saída impressa no terminal desta parte do script:
```
===================

Permissões por APK

===================

BancoX-v01: ['WRITE_SETTINGS', 'READ_APP_BADGE']

...

InstantMessengerY-101010: ['SEND_SMS', 'WRITE_SETTINGS']

```
- No mesmo script, faça uma função que retorne a lista de permissões únicas de cada APK e comuns a todas as APKs analisadas (intersecção). Exemplo de saída impressa no terminal desta parte do script:

```
===================
Permissões únicas por APK
===================
BancoX-v01: ['READ_APP_BADGE']
...
InstantMessengerY-101010: ['SEND_SMS']
===================
Permissões comuns das APKs
===================
['WRITE_SETTINGS']
```
No diretório Parte1 há um subdiretório nomeado dataset, que possui todos os arquivos AndroidManifesto separados por categoria.
## Parte 2: Análise de arquivos PE
- Obtenha alguns binários de Windows (você pode pegá-los do seu próprio computador, se tiver o sistema operacional instalado, ou de sites de download de programas, como sourceforge e outros). Exemplos de binários: calc.exe, ping.exe, paint.exe, netstat.exe...

- Escreva um script em Python (ou .ipynb) que receba como entrada um arquivo ou diretório e enumere a seções executáveis do(s) binário(s), imprimindo na saída padrão um dicionário de listas, onde a chave é o nome do binário e o valor é uma lista de seções executáveis. Dica: https://github.com/erocarrera/pefile

- Escreva outro script em Python (ou .ipynb) que receba como entrada dois arquivos .exe e os compare, imprimindo na saída padrão quais seções são comuns a ambos os binários, quais somente estão presentes no binário 1 e quais somente estão presentes no binário 2. Siga as regras de formato/apresentação já estabelecidas nesta tarefa.
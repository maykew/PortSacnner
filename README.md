<h1 align="center">
    PortScanner
</h1>

<p align="center">
  <a href="#computer-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#dart-objetivos">Objetivos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#boom-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#mortar_board-como-executar-o-projeto">Como executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#family-como-contribuir">Como contribuir</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>

_________

### :computer: Projeto

<p align="justify">
Este é um desafio com o intuito de desenvolver uma aplicação multithreading que reconheça automaticamente a classe (A, B ou C) de um endereço IP e verifique quais portas de um host, ou de hosts de uma rede, que estão abertas.
</p>

### :dart: Objetivos

- Familiarizar-se com a programação utilizando a API [socket](https://docs.python.org/3/library/socket.html);<br>
- Ambientar-se na programação com Threads utilizando a API [threading](https://docs.python.org/3/library/threading.html);<br>
- Manipular endereços de rede.

### :boom: Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/)

### :mortar_board: Como executar o projeto

- Faça um clone deste repositório: `git clone https://github.com/maykew/PortScanner`;
- Entre no diretório PortScanner;

- Para verificar portas de um host, execute: `python portscanner.py <endereço IP> <porta inicial> <porta final>`;
  - Exemplo: `python portscanner.py 192.168.1.10 1 65535`

- Para verificar portas de hosts de uma rede, execute: `python portscanner.py <endereço IP> <porta inicial> <porta final> -n`;
  - Exemplo: `python portscanner.py 192.168.1 1 65535`

### :family: Como contribuir

- Faça um fork desse repositório;
- Cria uma branch com a sua feature: `git checkout -b minha-feature`;
- Faça commit das suas alterações: `git commit -m 'feat: Minha nova feature'`;
- Faça push para a sua branch: `git push origin minha-feature`.

Depois que o merge da sua pull request for feito, você pode deletar a sua branch.

### :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/maykew/PortScanner/blob/master/LICENSE.md) para mais detalhes.
_________

<h4 align="center"> ♥ by Mayke Willans ♥ </h4>

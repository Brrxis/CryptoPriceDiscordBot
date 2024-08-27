# CryptoPriceBot - Bot de Preços de Criptomoedas

![Discord Bot](https://img.shields.io/badge/Discord-Bot-blue?style=flat-square&logo=discord)

**CryptoBot** é um bot para Discord que fornece informações sobre preços de criptomoedas e conversões de moeda em tempo real. Com suporte para uma ampla gama de criptomoedas, você pode obter o preço atual e converter valores entre USD e BRL com facilidade.

## Funcionalidades

- **Consulta de Preços de Criptomoedas**: Receba informações sobre o preço de diversas criptomoedas em USD.
- **Conversão de Moeda**: Converta valores de USD para BRL.
- **Comandos de Ajuda**: Receba uma lista de todos os comandos disponíveis e instruções de uso.
- **Gerenciamento de Mensagens**: Apague um número específico de mensagens em um canal.

## Comandos

### Comandos de Criptomoedas

- `p!btc`: Mostra o preço atual do Bitcoin (BTC).
- `p!eth`: Mostra o preço atual do Ethereum (ETH).
- `p!doge`: Mostra o preço atual do Dogecoin (DOGE).
- (e assim por diante para outras criptomoedas na lista...)

### Conversão de Moeda

- `p!dol-brl [valor]`: Converte um valor de USD para BRL. Exemplo: `p!dol-brl 12`.

### Ajuda

- `p!ajuda`: Mostra uma lista de todos os comandos disponíveis e como usá-los.

### Gerenciamento de Mensagens

- `p!apagar [número]`: Apaga um número específico de mensagens no canal atual. Exemplo: `p!apagar 10`.

## Como Usar

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/SEU_USUARIO/CryptoBot.git
   cd CryptoBot
   ```

2. **Instale as Dependências**

   Certifique-se de que você tem o Python 3.8+ instalado e execute:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o Bot**

   Substitua o valor de `TOKEN` no código pelo seu token do bot do Discord. Mantenha seu token seguro e não o compartilhe publicamente.

4. **Execute o Bot**

   ```bash
   python bot.py
   ```

## Recursos

- [Documentação do Discord.py](https://discordpy.readthedocs.io/en/stable/)
- [API CoinGecko](https://coingecko.com)
- [API Exchangerate](https://exchangerate-api.com/)

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. Para mudanças maiores, por favor, discuta primeiro sobre o que você gostaria de alterar na issue apropriada.

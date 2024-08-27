import discord
import requests
from discord.ext import commands

TOKEN = ''

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='p!', intents=intents)

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
EXCHANGE_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

crypto_list = ["BTC", "ETH", "USDT", "BNB", "XRP", "USDC", "DOGE", "ADA", "SOL", "TRX", "MATIC", "TON", "DOT", "LTC", "SHIB", "AVAX", "UNI", "WBTC", "LINK", "ATOM", "XMR", "BCH", "OKB", "FIL", "LEO", "BSV", "APT", "HBAR", "STETH", "ICP", "NEAR", "AAVE", "QNT", "GRT", "ALGO", "VET", "MKR", "RPL", "KAS", "FTM", "HT", "TUSD", "MANA", "XTZ", "AXS", "SAND", "LUNC", "SNX", "EOS", "RUNE", "IMX", "CAKE", "ZEC", "BNBX", "CVX", "CHZ", "STX", "CRV", "ARB", "KLAY", "GALA", "FLOKI", "ENS", "BTT", "MINA", "LDO", "DYDX", "ROSE", "OP", "YFI", "CFX", "KAVA", "GLMR", "CELO", "ONE", "1INCH", "ROOK", "PERP", "AUDIO", "HNT", "BLUR", "ASTAR", "RSR", "API3", "GAL", "JOE", "OCEAN", "REN", "SPELL", "DENT", "SUSHI", "ILV", "ANT", "RAD", "NMR", "LQTY", "TRU", "BOBA", "ALCX", "OSMO"]

crypto_id_map = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "USDT": "tether",
    "BNB": "binancecoin",
    "XRP": "ripple",
    "USDC": "usd-coin",
    "DOGE": "dogecoin",
    "ADA": "cardano",
    "SOL": "solana",
    "TRX": "tron",
    "MATIC": "matic-network",
    "TON": "the-open-network",
    "DOT": "polkadot",
    "LTC": "litecoin",
    "SHIB": "shiba-inu",
    "AVAX": "avalanche-2",
    "UNI": "uniswap",
    "WBTC": "wrapped-bitcoin",
    "LINK": "chainlink",
    "ATOM": "cosmos",
    "XMR": "monero",
    "BCH": "bitcoin-cash",
    "OKB": "okb",
    "FIL": "filecoin",
    "LEO": "leo-token",
    "BSV": "bitcoin-sv",
    "APT": "aptos",
    "HBAR": "hedera-hashgraph",
    "STETH": "staked-ether",
    "ICP": "internet-computer",
    "NEAR": "near",
    "AAVE": "aave",
    "QNT": "quant-network",
    "GRT": "the-graph",
    "ALGO": "algorand",
    "VET": "vechain",
    "MKR": "maker",
    "RPL": "rocket-pool",
    "KAS": "kaspa",
    "FTM": "fantom",
    "HT": "huobi-token",
    "TUSD": "true-usd",
    "MANA": "decentraland",
    "XTZ": "tezos",
    "AXS": "axie-infinity",
    "SAND": "the-sandbox",
    "LUNC": "terra-luna",
    "SNX": "havven",
    "EOS": "eos",
    "RUNE": "thorchain",
    "IMX": "immutable-x",
    "CAKE": "pancakeswap-token",
    "ZEC": "zcash",
    "BNBX": "bnbx-finexbox",
    "CVX": "convex-finance",
    "CHZ": "chiliz",
    "STX": "blockstack",
    "CRV": "curve-dao-token",
    "ARB": "arbitrum",
    "KLAY": "klay-token",
    "GALA": "gala",
    "FLOKI": "floki",
    "ENS": "ethereum-name-service",
    "BTT": "bittorrent",
    "MINA": "mina-protocol",
    "LDO": "lido-dao",
    "DYDX": "dydx",
    "ROSE": "oasis-network",
    "OP": "optimism",
    "YFI": "yearn-finance",
    "CFX": "conflux-token",
    "KAVA": "kava",
    "GLMR": "moonbeam",
    "CELO": "celo",
    "ONE": "harmony",
    "1INCH": "1inch",
    "ROOK": "rook",
    "PERP": "perpetual-protocol",
    "AUDIO": "audius",
    "HNT": "helium",
    "BLUR": "blur",
    "ASTAR": "astar",
    "RSR": "reserve-rights-token",
    "API3": "api3",
    "GAL": "project-galaxy",
    "JOE": "joe",
    "OCEAN": "ocean-protocol",
    "REN": "republic-protocol",
    "SPELL": "spell-token",
    "DENT": "dent",
    "SUSHI": "sushi",
    "ILV": "illuvium",
    "ANT": "aragon",
    "RAD": "radicle",
    "NMR": "numeraire",
    "LQTY": "liquity",
    "TRU": "truefi",
    "BOBA": "boba-network",
    "ALCX": "alchemix",
    "OSMO": "osmosis"
}

async def get_crypto_price(crypto_id):
    try:
        response = requests.get(f'{COINGECKO_API_URL}?ids={crypto_id}&vs_currencies=usd')
        data = response.json()
        return data[crypto_id]['usd']
    except Exception as e:
        print(f"Erro ao buscar preço para {crypto_id}: {e}")
        return None

for crypto in crypto_list:
    async def crypto_price(ctx, crypto=crypto):
        crypto_id = crypto_id_map.get(crypto.upper())
        if not crypto_id:
            await ctx.send(f"Desculpe, não tenho informações para a criptomoeda {crypto}.")
            return

        price = await get_crypto_price(crypto_id)
        if price is not None:
            embed = discord.Embed(title=f'Preço da {crypto.upper()}',
                                  color=discord.Color.green())

            if price < 0.01:
                embed.description = f"O preço atual de {crypto.upper()} é menor que $0.00 USD."
            else:
                embed.description = f"O preço atual de {crypto.upper()} é ${price:.2f} USD"

            embed.add_field(name="Mais informações", value=f"[Clique aqui](https://www.coingecko.com/en/coins/{crypto_id})")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Houve um erro ao tentar buscar o preço de {crypto.upper()}.")

    bot.add_command(commands.Command(crypto_price, name=crypto.lower()))

@bot.command(name='dol-brl')
async def dol_brl(ctx, valor: float):
    try:
        response = requests.get(EXCHANGE_API_URL)
        data = response.json()

        brl_rate = data['rates']['BRL']
        valor_brl = valor * brl_rate

        embed = discord.Embed(title='Conversão USD para BRL',
                              description=f"${valor:.2f} USD é equivalente a R${valor_brl:.2f} BRL",
                              color=discord.Color.blue())
        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send("Houve um erro ao tentar fazer a conversão de moeda.")

@bot.command(name='ajuda')
async def ajuda(ctx):
    embed_general = discord.Embed(title="Ajuda - Comandos Gerais", color=discord.Color.purple())
    embed_general.add_field(name="p!dol-brl [valor]", value="Converte um valor de USD para BRL. Exemplo: `p!dol-brl 12`", inline=False)
    embed_general.add_field(name="p!apagar [número]", value="Apaga um número específico de mensagens. Exemplo: `p!apagar 10`", inline=False)
    embed_general.add_field(name="p!comandos", value="Mostra todos os comandos disponíveis.", inline=False)
    embed_general.set_footer(text="By PontoniDev")
    await ctx.send(embed=embed_general)

    embed_crypto = discord.Embed(title="Ajuda - Comandos de Criptomoedas", color=discord.Color.purple())
    embed_crypto.set_footer(text="Comandos de criptomoedas - p!crypto [moeda]")

    for i in range(0, len(crypto_list), 10):
        chunk = crypto_list[i:i + 10]
        for crypto in chunk:
            embed_crypto.add_field(name=f"p!{crypto.lower()}", value=f"Mostra o valor de {crypto} em USD", inline=True)
        if i + 10 < len(crypto_list):
            await ctx.send(embed=embed_crypto)
            embed_crypto = discord.Embed(title="Ajuda - Comandos de Criptomoedas", color=discord.Color.purple())
            embed_crypto.set_footer(text="Comandos de criptomoedas - p!crypto [moeda]")

@bot.command(name='apagar')
@commands.has_permissions(manage_messages=True)
async def apagar(ctx, numero: int):
    if numero <= 0:
        await ctx.send("Por favor, forneça um número positivo de mensagens para apagar.")
        return

    try:
        await ctx.channel.purge(limit=numero + 1)
        await ctx.send(f"{numero} mensagens foram apagadas.", delete_after=5)
    except discord.errors.Forbidden:
        await ctx.send("Não tenho permissão para apagar mensagens neste canal.")
    except Exception as e:
        await ctx.send(f"Ocorreu um erro ao tentar apagar as mensagens: {str(e)}")

@bot.command(name='comandos')
async def comandos(ctx):
    embed = discord.Embed(title="Comandos Disponíveis", color=discord.Color.blue())
    for command in bot.commands:
        embed.add_field(name=f"p!{command.name}", value=command.help or "Sem descrição", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)

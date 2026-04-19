# Awesome Agent Trading [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, frameworks, skills, APIs, and resources for AI agent-powered trading in crypto and traditional finance.

The agent economy is here. AI agents are autonomously managing wallets, executing trades, providing liquidity, and earning yield on-chain. This list tracks everything you need to build, deploy, and scale autonomous trading agents.

Contributions welcome! Read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Contents

- [Agent Frameworks](#agent-frameworks)
- [OpenClaw Trading Skills](#openclaw-trading-skills)
- [DEX & On-Chain Trading](#dex--on-chain-trading)
- [CEX & Off-Chain Trading](#cex--off-chain-trading)
- [Prediction Markets](#prediction-markets)
- [Data & Market Intelligence](#data--market-intelligence)
- [Agent Identity & Trust](#agent-identity--trust)
- [Payment Protocols](#payment-protocols)
- [Risk Management](#risk-management)
- [Research & Papers](#research--papers)
- [Tutorials & Guides](#tutorials--guides)
- [Communities](#communities)

---

## Agent Frameworks

Frameworks for building autonomous trading agents.

| Project | Description | Language |
|---------|-------------|----------|
| [OpenClaw](https://github.com/openclaw/openclaw) | Open-source AI agent platform with skill system, cron jobs, multi-channel output | Node.js |
| [ElizaOS](https://github.com/elizaOS/eliza) | Multi-agent framework for autonomous AI characters with trading capabilities | TypeScript |
| [TradingAgents](https://github.com/TauricResearch/TradingAgents) | Multi-agent LLM financial trading framework for stock analysis & portfolio management | Python |
| [AI-Trader](https://github.com/HKUDS/AI-Trader) | 100% fully-automated agent-native trading system | Python |
| [Hummingbot](https://github.com/hummingbot/hummingbot) | Open-source crypto market making and trading bot framework | Python |
| [Freqtrade](https://github.com/freqtrade/freqtrade) | Open-source crypto trading bot with strategy optimization | Python |
| [Jesse](https://github.com/jesse-ai/jesse) | Advanced crypto trading framework with AI strategy support | Python |

## OpenClaw Trading Skills

Plug-and-play trading skills for the OpenClaw agent platform.

| Skill | Author | Description |
|-------|--------|-------------|
| [Bankr](https://github.com/BankrBot/skills/tree/main/bankr) | BankrBot | Full crypto trading suite: spot, DeFi, leverage (50x via Avantis), Polymarket, NFTs across 5 chains |
| [Polyclaw](https://github.com/BankrBot/skills/tree/main/polyclaw) | Chainstack | Polymarket prediction market trading with strategy backtesting |
| [Signals](https://github.com/BankrBot/skills/tree/main/signals) | Axiom | Transaction-verified trading signals on Base with TX hash proof |
| [Trails](https://github.com/BankrBot/skills/tree/main/trails) | Polygon | Cross-chain swap, bridge, and DeFi orchestration via Sequence |
| [Quicknode](https://github.com/BankrBot/skills/tree/main/quicknode) | Quicknode | Blockchain RPC, token balances, gas estimation, tx status across chains |
| [Alchemy](https://github.com/BankrBot/skills/tree/main/alchemy) | Alchemy | EVM JSON-RPC, token balances, NFTs, portfolio data, tx simulation |
| [Hydrex](https://github.com/BankrBot/skills/tree/main/hydrex) | Hydrex | Liquidity pools on Base with auto-managed vaults |

## DEX & On-Chain Trading

Decentralized exchanges and on-chain trading infrastructure for agents.

| Project | Type | Chains | Agent Support |
|---------|------|--------|--------------|
| [Hyperliquid](https://hyperliquid.xyz) | Perpetuals DEX | L1 | Full API, wallet-based, no KYC |
| [Jupiter](https://jupiter.ag) | Aggregator + Perps | Solana | API + SDK |
| [GMX](https://gmx.io) | Perpetuals + Spot | Arbitrum, Avalanche | Contract-based |
| [dYdX](https://dydx.exchange) | Perpetuals | Cosmos (appchain) | Full API |
| [Drift](https://drift.trade) | Perpetuals + Spot | Solana | SDK |
| [Vertex](https://vertexprotocol.com) | Perpetuals + Spot | Arbitrum | API |
| [Uniswap](https://uniswap.org) | Spot + Aggregator | Multi-chain | Smart contract |
| [1inch](https://1inch.io) | Aggregator | Multi-chain | API |
| [Avantis](https://avantisfi.com) | Leveraged Trading | Base | Up to 50x leverage |

## CEX & Off-Chain Trading

Centralized exchanges with API access for automated trading.

| Exchange | API Type | Agent-Friendly Features |
|----------|----------|------------------------|
| [Binance](https://binance.com) | REST + WebSocket | Most liquid, extensive docs, testnet |
| [Bybit](https://bybit.com) | REST + WebSocket | Copy trading API, sub-accounts |
| [OKX](https://okx.com) | REST + WebSocket | Comprehensive API, DEX aggregator |
| [Coinbase](https://coinbase.com) | REST + WebSocket | AgentKit for agents, institutional |
| [Deribit](https://deribit.com) | REST + WebSocket | Options + futures, testnet |

## Prediction Markets

Prediction market platforms accessible to AI agents.

| Platform | Chains | API | Notes |
|----------|--------|-----|-------|
| [Polymarket](https://polymarket.com) | Polygon | CLOB API | Largest prediction market, Polyclaw skill available |
| [Azuro](https://azuro.org) | Multi-chain | Smart contract | Decentralized prediction market protocol |
| [Kalshi](https://kalshi.com) | Off-chain | API | Regulated US prediction market |

## Data & Market Intelligence

Data sources and APIs for market analysis by agents.

| Source | Data Type | Free Tier | API |
|--------|-----------|-----------|-----|
| [CoinGecko](https://coingecko.com/api) | Prices, market cap, volume | Yes (30 calls/min) | REST |
| [CoinGlass](https://coinglass.com) | Funding rates, OI, liquidations | Limited | REST |
| [DeFiLlama](https://defillama.com) | TVL, protocol revenue, yields | Yes (free) | REST |
| [Glassnode](https://glassnode.com) | On-chain metrics (MVRV, SOPR) | Limited free | REST |
| [Dune Analytics](https://dune.com) | Custom on-chain queries | Yes | SQL API |
| [Arkham Intelligence](https://arkham.io) | Wallet tracking, entity labeling | Limited | REST |
| [Alternative.me](https://alternative.me) | Fear & Greed Index | Yes | REST |
| [The Graph](https://thegraph.com) | Indexed blockchain data | Yes | GraphQL |

## Agent Identity & Trust

On-chain identity and reputation systems for trading agents.

| Protocol | Purpose | Chains |
|----------|---------|--------|
| [ERC-8004](https://8004.org) | On-chain agent identity (NFT) + verifiable reputation | Ethereum, Base, BNB, Solana, Polygon |
| [Helixa](https://helixa.xyz) | Agent identity + Cred Score on Base | Base |
| [ERC-6551](https://eip6551.org) | Token-bound accounts (agent NFT owns wallet) | EVM |
| [SIWA (ERC-8128)](https://github.com/BankrBot/skills/tree/main/siwa) | Sign-In With Agent authentication | EVM |

## Payment Protocols

Protocols for agent-to-agent and agent-to-human payments.

| Protocol | Type | Chain | Use Case |
|----------|------|-------|----------|
| [x402](https://x402.org) | HTTP micropayments (402 status) | Base, Ethereum | Pay-per-query signal APIs |
| [MPP (Tempo/Stripe)](https://tempo.xyz) | Agent payment processing | Multi-chain | Fiat + crypto payments |
| [AP2 (Google)](https://google.com) | Agent-to-agent payments | — | Announced 2026 |

## Risk Management

Tools and patterns for managing trading risk in autonomous agents.

- **Position sizing**: Max % of account per trade (recommend 5-20%)
- **Leverage limits**: Hard cap per strategy (recommend 3-5x)
- **Mandatory stop-loss**: Every trade must have SL before entry
- **Circuit breakers**: Auto-halt trading on drawdown thresholds
- **Cooldown periods**: Enforced rest after losing trades
- **Asset whitelists**: Only trade pre-approved assets
- **Concurrent position limits**: Prevent overexposure

## Research & Papers

Academic and industry research on AI trading agents.

- [AI-Trader: 100% Fully-Automated Agent-Native Trading](https://github.com/HKUDS/AI-Trader) — HKU, 2026
- [TradingAgents: Multi-Agent LLM Financial Trading](https://github.com/TauricResearch/TradingAgents) — Tauric Research, 2026
- [Agent-Fi: Autonomous Agents in DeFi](https://arxiv.org/abs/2502.02564) — Survey of agent-DeFi intersection

## Tutorials & Guides

- [OpenClaw AI Trading Skills: Complete 2026 Guide](https://aurpay.net/aurspace/openclaw-ai-trading-skills-complete-guide-2026/) — Setup, risks, and real numbers
- [How to Build an Autonomous Trading Agent with Python](https://dev.to/alex_mercer/how-to-build-an-autonomous-trading-agent-with-python-in-2026-pap) — Dev.to, 2026
- [Build a Crypto AI Agent with CoinGecko API](https://www.coingecko.com/learn/build-crypto-ai-agent) — CoinGecko
- [OpenClaw Trading: Crypto, DeFi, and Polymarket Skills](https://boilerplatehub.com/blog/openclaw-trading) — BoilerplateHub

## Communities

- [OpenClaw Discord](https://discord.com/invite/clawd) — Official community
- [BankrBot Discord](https://bankr.bot) — Trading skill community
- [r/algotrading](https://reddit.com/r/algotrading) — Algorithmic trading on Reddit
- [ERC-8004 Discord](https://8004.org) — Agent identity standard

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. PRs welcome!

## License

[CC0-1.0](LICENSE) — Public domain. Use however you want.

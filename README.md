# Awesome Agent Trading [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated directory of AI trading agents, broker integrations, MCP servers, skills, and research tools for US equities and options, global crypto and DeFi, and prediction markets.

Explore tools for market research, strategy development, and order execution. Account and venue availability depend on the integration and jurisdiction.

Use the categories below to distinguish research, backtesting, paper trading, and live execution. Listings describe upstream capabilities, not verified trading performance. Official hosted services, open-source software, and source-available projects are labeled separately where reviewed.

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md). Machine-readable resources: [llms.txt](llms.txt) and [data/projects.json](data/projects.json).

## Contents

- [Trading Agents](#trading-agents)
- [Broker & Exchange Integrations](#broker--exchange-integrations)
- [MCP Servers & Agent Skills](#mcp-servers--agent-skills)
- [Prediction Markets](#prediction-markets)
- [Research & Backtesting](#research--backtesting)
- [Data, Wallets & Risk Infrastructure](#data-wallets--risk-infrastructure)
- [Machine-Readable Data](#machine-readable-data)
- [FAQ](#faq)
- [Research & Papers](#research--papers)
- [Tutorials & Guides](#tutorials--guides)
- [Communities](#communities)

<a id="agent-frameworks"></a>

## Trading Agents

Agent systems for market analysis, decisions, and execution. Check each project's supported mode and venue before choosing an integration.

| Project | Description | Language |
|---------|-------------|----------|
| [AI-Trader](https://github.com/HKUDS/AI-Trader) | Agent trading platform with experiments and paper-trading workflows | Python |
| [openFinclaw](https://github.com/misterGFCo/openFinclaw) | Self-hosted financial OpenClaw with CCXT (Hyperliquid, Binance, OKX, Bybit) | Python |
| [Nunchi agent-cli](https://github.com/Nunchi-trade/agent-cli) | Strategy orchestration, trading review, and an MCP server | Python |
| [Senpi Skills](https://github.com/Senpi-ai/senpi-skills) | Hyperliquid trading skills and Hyperfeed trader data | Python |
| [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Personal trading agent with persistent memory, self-evolving skills, context compression | Python |
| [NoFx](https://github.com/NoFxAiOS/nofx) | LLM trading terminal with a Go runtime enforcing order risk limits | Go |
| [OpenAlice](https://github.com/TraderAlice/OpenAlice) | AI trading agent covering equities, crypto, commodities, forex, and macro from research to execution and position management | TypeScript |
| [QuantDinger](https://github.com/OpenByteInc/QuantDinger) | AI quantitative trading platform with backtesting, live trading, market data, and multi-agent research | Python |
| [CloddsBot](https://github.com/alsk1992/CloddsBot) | Self-hosted AI trading agent across Polymarket, Kalshi, Binance, Hyperliquid, Solana DEXs, and EVM chains | TypeScript |

### Emerging execution projects

| Project | Role and mode | Access / license |
|---------|---------------|------------------|
| [OpenTrade](https://github.com/OpenTradeOSS/OpenTrade) | macOS app connecting coding agents to Robinhood MCP; live orders with configurable approvals | Robinhood account; source-available, Elastic-2.0 |
| [FriesTrader](https://github.com/YizhiSong/FriesTrader) | Experimental two-phase trading template; dry-run by default, opt-in live execution | Robinhood account; MIT; performance not independently verified |

## Broker & Exchange Integrations

### Official broker integrations

| Integration | Capabilities and modes | Access |
|-------------|------------------------|--------|
| [Alpaca MCP Server](https://github.com/alpacahq/alpaca-mcp-server) | Stocks, ETFs, crypto, and options tools; paper default, explicit live setting | Official, MIT; account/API credentials and data entitlements |
| [Robinhood Agentic Trading](https://robinhood.com/us/en/support/articles/agentic-trading-overview/) | Hosted MCP for portfolio research and orders in a dedicated Agentic account | Official hosted service; eligible account required; read access is broader than trading access |

### DEX & On-Chain Trading

Decentralized exchanges and on-chain trading infrastructure for agents.

| Project | Type | Chains | Agent Support |
|---------|------|--------|--------------|
| [Hyperliquid](https://hyperliquid.xyz) | Perpetuals DEX | L1 | Full API, wallet-based, no KYC |
| [Jupiter](https://jupiter.ag) | Aggregator + Perps | Solana | API + SDK |
| [GMX](https://gmx.io) | Perpetuals + Spot | Arbitrum, Avalanche | Contract-based |
| [dYdX](https://dydx.exchange) | Perpetuals | Cosmos (appchain) | Full API |
| [Drift](https://drift.trade) | Perpetuals + Spot | Solana | SDK |
| [Uniswap](https://uniswap.org) | Spot + Aggregator | Multi-chain | Smart contract |
| [1inch](https://1inch.io) | Aggregator | Multi-chain | API |
| [Avantis](https://avantisfi.com) | Leveraged Trading | Base | Up to 50x leverage |

### CEX & Off-Chain Trading

Centralized exchanges with API access for automated trading.

| Exchange | API Type | Agent-Friendly Features |
|----------|----------|------------------------|
| [Binance](https://binance.com) | REST + WebSocket | Most liquid, extensive docs, testnet |
| [Bybit](https://bybit.com) | REST + WebSocket | Copy trading API, sub-accounts |
| [OKX](https://okx.com) | REST + WebSocket | Comprehensive API, DEX aggregator |
| [Coinbase](https://coinbase.com) | REST + WebSocket | AgentKit for agents, institutional |
| [Deribit](https://deribit.com) | REST + WebSocket | Options + futures, testnet |

<a id="mcp-servers-for-trading"></a>

## MCP Servers & Agent Skills

### MCP servers and agent CLIs

Model Context Protocol servers that provide trading capabilities to AI agents.

| Server | Description | Protocol |
|--------|-------------|----------|
| [hyperliquid-mcp](https://github.com/edkdev/hyperliquid-mcp) | Full Hyperliquid trading: orders, positions, market data, bracket orders, agent mode | MCP |
| [HYPERLIQUID-MCP-Server](https://github.com/6rz6/HYPERLIQUID-MCP-Server) | 8 trading tools for Hyperliquid: market data, account management, analytics | MCP |
| [perp-cli](https://github.com/hypurrquant/perp-cli) | Multi-DEX perps CLI + MCP (Hyperliquid, Pacifica, Lighter), market data and execution tools | MCP |
| [CoinGecko MCP](https://docs.coingecko.com/docs/mcp-server) | Official CoinGecko MCP server for price & market data | MCP |
| [CoinGeckoMCP](https://github.com/BlindVibeDev/CoinGeckoMCP) | Node.js CoinGecko MCP with free + Pro API support | MCP |
| [mcp-coingecko-server](https://github.com/crazyrabbitLTC/mcp-coingecko-server) | CoinGecko Pro API MCP with OpenAI function calling compatibility | MCP |
| [Binance MCP](https://github.com/nicepkg/binance-mcp) | Unofficial Binance MCP server for trading AI agents | MCP |
| [financekit-mcp](https://github.com/vdalhambra/financekit-mcp) | 17 tools for financial market intelligence: quotes, technicals, analysis | MCP |
| [polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server) | Polymarket MCP server with trading, market discovery, monitoring, and safety tools | MCP |
| [fintool](https://github.com/second-state/fintool) | Rust CLI tools for agentic trading across Hyperliquid, Binance, Coinbase, OKX, Polymarket, and market intelligence | CLI / MCP |
| [TradeMemory Protocol](https://github.com/mnemox-ai/tradememory-protocol) | Decision audit trail and persistent memory for AI trading agents with outcome-weighted recall and MCP tools | MCP |
| [Simmer SDK](https://github.com/SpartanLabsXyz/simmer-sdk) | Prediction market harness for AI agents with skills, MCP server, and Python SDK | MCP / SDK |

<a id="openclaw-trading-skills"></a>

### Agent Skills

Skills for compatible agent clients. OpenClaw-specific entries remain labeled by their upstream integration; compatibility is not assumed across all clients.

| Skill | Author | Description |
|-------|--------|-------------|
| [Alpaca Skills](https://github.com/alpacahq/alpaca-skills) | Alpaca | Official backtesting, paper trading, and Broker API workflows; Apache-2.0 |
| [Bankr](https://github.com/BankrBot/skills/tree/main/bankr) | BankrBot | Full crypto trading suite: spot, DeFi, leverage (50x via Avantis), Polymarket, NFTs across 5 chains |
| [Polyclaw](https://github.com/BankrBot/skills/tree/main/polyclaw) | Chainstack | Polymarket prediction market trading with strategy backtesting |
| [Signals](https://github.com/BankrBot/skills/tree/main/signals) | Axiom | Transaction-verified trading signals on Base with TX hash proof |
| [Trails](https://github.com/BankrBot/skills/tree/main/trails) | Polygon | Cross-chain swap, bridge, and DeFi orchestration via Sequence |
| [Quicknode](https://github.com/BankrBot/skills/tree/main/quicknode) | Quicknode | Blockchain RPC, token balances, gas estimation, tx status across chains |
| [Alchemy](https://github.com/BankrBot/skills/tree/main/alchemy) | Alchemy | EVM JSON-RPC, token balances, NFTs, portfolio data, tx simulation |
| [Hydrex](https://github.com/BankrBot/skills/tree/main/hydrex) | Hydrex | Liquidity pools on Base with auto-managed vaults |
| [Hyperclaw](https://github.com/openclaw/skills/tree/main/hyperclaw) | OpenClaw | Hyperliquid data: funding rates, OI, order book, candles, market scan |
| [Binance](https://github.com/openclaw/skills/tree/main/binance) | OpenClaw | Binance spot & futures trading with safety checks |
| [Public](https://public.com/api/docs/templates/openclaw-agent-skill) | Public.com | Stocks, ETFs, options, crypto — commission-free |
| [CryptoSkill](https://cryptoskill.org) | CryptoSkill | Unified skill hub: Binance, OKX, Bybit, Uniswap, Jupiter, Hyperliquid |
| [Quant Trader](https://clawhub.ai/zhenstaff/quant-trader) | zhenstaff | Quantitative trading with backtest via CCXT/Binance |
| [Auto Trading Strategy](https://clawhub.ai/863king/auto-trading-strategy) | 863king | Automated trading strategy collection |
| [Trader](https://clawhub.ai/ivangdavila/trader) | ivangdavila | Market analysis, risk management, disciplined strategy execution |
| [Polymarket Paper Trader](https://clawhub.ai/robotlearning123/polymarket-paper-trader) | robotlearning123 | Paper trading on Polymarket with portfolio tracking |
| [Hyperliquid Trading](https://clawhub.ai/laplace0x/hyperliquid-trading) | Agent Laplace | Secure Hyperliquid perps trading via gateway API with risk enforcement |
| [Smart Trading](https://openclawai.me/trading) | OpenClaw AI | Sub-second Hyperliquid execution with hardcoded risk guardrails |
| [Whale Wallet Analysis](https://agentskills.so/skills/sanctifiedops-solana-skills-whale-wallet-analysis) | sanctifiedops | Solana whale wallet tracking with cluster detection |
| [Superior Trade Skills](https://github.com/Superior-Trade/superior-skills) | Superior Trade | Open agent skills and tool schemas for building, backtesting, and deploying Hyperliquid strategies |

## Prediction Markets

Prediction market platforms accessible to AI agents.

| Platform | Chains | API | Notes |
|----------|--------|-----|-------|
| [Polymarket](https://polymarket.com) | Polygon | CLOB API | Largest prediction market, Polyclaw skill available |
| [Azuro](https://azuro.org) | Multi-chain | Smart contract | Decentralized prediction market protocol |
| [Kalshi](https://kalshi.com) | Off-chain | API | Regulated US prediction market |
| [TurbineFi](https://turbinefi.com) | Off-chain | Web app | Build, backtest, and deploy automated strategies for Kalshi and Polymarket |
| [Kalshi Trading Bot CLI](https://github.com/OctagonAI/kalshi-trading-bot-cli) | Off-chain | API + CLI | AI-native Kalshi trading CLI with probability estimates, order book edge, Kelly sizing, and risk gates |

### Official CLI

[Polymarket CLI](https://github.com/Polymarket/polymarket-cli) provides market discovery, JSON output, order and position management, and on-chain operations. Experimental; live trading requires wallet credentials and venue eligibility. MIT is declared in [Cargo.toml](https://github.com/Polymarket/polymarket-cli/blob/main/Cargo.toml); a standalone root license file was not found during review.

## Research & Backtesting

Research and simulation are distinct from broker execution. Traditional ML/RL and strategy engines below are supporting infrastructure, not necessarily LLM agents.

| Project | Description | Language |
|---------|-------------|----------|
| [TradingAgents](https://github.com/TauricResearch/TradingAgents) | Multi-agent LLM financial trading framework for stock analysis & portfolio management | Python |
| [Hummingbot](https://github.com/hummingbot/hummingbot) | Open-source crypto market making and trading bot framework | Python |
| [Freqtrade](https://github.com/freqtrade/freqtrade) | Open-source crypto trading bot with strategy optimization | Python |
| [Jesse](https://github.com/jesse-ai/jesse) | Advanced crypto trading framework with AI strategy support | Python |
| [TradingAgents-Crypto](https://github.com/auronsun/TradingAgents-crypto) | Crypto-focused fork of TradingAgents with CoinGecko integration | Python |
| [AI-CryptoTrader](https://github.com/N00Bception/AI-CryptoTrader) | Ensemble ML methods for crypto trading decisions | Python |
| [Intelligent Trading Bot](https://github.com/asavinov/intelligent-trading-bot) | ML-based automated trading with feature engineering | Python |
| [FinRL](https://github.com/AI4Finance-Foundation/FinRL) | Deep RL framework for automated trading (crypto + tradfi) | Python |
| [OpenTrader](https://github.com/Open-Trader/opentrader) | Open-source crypto trading bot with DCA & GRID strategies, UI | TypeScript |
| [moss-trade-bot-skills](https://github.com/moss-site/moss-trade-bot-skills) | Natural-language strategy generation and local Hyperliquid perps backtesting skills | Python |

| Project | Modes / role | License / access |
|---------|--------------|------------------|
| [Dexter](https://github.com/virattt/dexter) | Financial research, tool use, and evaluation; no trading execution | MIT declared in README; no standalone root license found; data/model services may cost extra |
| [Lumibot](https://github.com/Lumiwealth/lumibot) | Backtesting, paper trading, and live broker execution; Python runtime | GPL-3.0; broker and data-provider requirements vary |

## Data, Wallets & Risk Infrastructure

### Wallet and action toolkits

[Coinbase AgentKit](https://github.com/coinbase/agentkit) provides wallets and on-chain actions for agents (Apache-2.0). It supplies execution tools rather than a trading strategy.

### General agent runtimes

[OpenClaw](https://github.com/openclaw/openclaw) and [ElizaOS](https://github.com/elizaOS/eliza) can host agent workflows; trading capabilities depend on installed integrations.

### Data & Market Intelligence

Data sources and APIs for market analysis by agents.

| Source | Data Type | Free Tier | API |
|--------|-----------|-----------|-----|
| [CoinGecko](https://coingecko.com/api) | Prices, market cap, volume | Yes (30 calls/min) | REST |
| [CoinGlass](https://coinglass.com) | Funding rates, OI, liquidations | Limited | REST |
| [Hyperliquid API](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api) | Perps data, order book, funding, OI, user state | Yes (free) | REST + WebSocket |
| [DeFiLlama](https://defillama.com) | TVL, protocol revenue, yields | Yes (free) | REST |
| [Glassnode](https://glassnode.com) | On-chain metrics (MVRV, SOPR) | Limited free | REST |
| [Dune Analytics](https://dune.com) | Custom on-chain queries | Yes | SQL API |
| [Arkham Intelligence](https://arkham.io) | Wallet tracking, entity labeling | Limited | REST |
| [Alternative.me](https://alternative.me) | Fear & Greed Index | Yes | REST |
| [The Graph](https://thegraph.com) | Indexed blockchain data | Yes | GraphQL |
| [AgentServices](https://agentservices.to) | 54 services: prices, DeFi, onchain, analytics, dispute resolution | Yes (x402 micropayments) | REST + MCP |
| [Congress Trading Pipeline](https://github.com/seralifatih/congress-trading-pipeline) | US House & Senate STOCK Act trade disclosures (PTRs) | Yes (Apify free credit) | REST |
| [Sato Hub](https://satohub.ai) | Onchain-agent tool index (380+) with openness/activity scores, x402 and agent-economy metrics | Yes (free, CC-BY) | REST + MCP |

### Agent Identity & Trust

On-chain identity and reputation systems for trading agents.

| Protocol | Purpose | Chains |
|----------|---------|--------|
| [ERC-8004](https://8004.org) | On-chain agent identity (NFT) + verifiable reputation | Ethereum, Base, BNB, Solana, Polygon |
| [Helixa](https://helixa.xyz) | Agent identity + Cred Score on Base | Base |
| [ERC-6551](https://eips.ethereum.org/EIPS/eip-6551) | Token-bound accounts (agent NFT owns wallet) | EVM |
| [SIWA (ERC-8128)](https://github.com/BankrBot/skills/tree/main/siwa) | Sign-In With Agent authentication | EVM |
| [TWZRD Agent Intel](https://intel.twzrd.xyz) | On-chain behavioral trust scoring for Solana agent wallets. Score + preflight free; signed trust receipt via x402 | Solana |

### Payment Protocols

Protocols for agent-to-agent and agent-to-human payments.

| Protocol | Type | Chain | Use Case |
|----------|------|-------|----------|
| [x402](https://x402.org) | HTTP micropayments (402 status) | Base, Ethereum | Pay-per-query signal APIs |
| [MPP (Tempo/Stripe)](https://tempo.xyz) | Agent payment processing | Multi-chain | Fiat + crypto payments |
| [AP2](https://github.com/google-agentic-commerce/AP2) | Agent payment authorization protocol | Payment-method agnostic | Introduced in 2025 |

<a id="risk-management"></a>

### Risk controls to evaluate

- **Execution permissions**: Separate read-only research from order submission and fund transfers.
- **Configurable budgets**: Enforce position, leverage, concentration, and loss limits in execution code.
- **Order lifecycle**: Use idempotency, fresh-price checks, fill reconciliation, and explicit cancellation handling.
- **Approval and shutdown**: Support human review, paper/dry-run modes, and a tested kill switch.
- **Exit handling**: Document supported stop orders, rejected orders, partial fills, and disconnected sessions.
- **Audit trails**: Record proposals, approvals, orders, and outcomes; [TradeMemory Protocol](https://github.com/mnemox-ai/tradememory-protocol) is one tool to investigate.

Prompt instructions alone are not execution-layer enforcement. A project's documented controls are not an independent security or performance audit.

## Machine-Readable Data

[data/projects.json](data/projects.json) is a **featured subset**, not a complete export of every README entry. It retains the existing fields and adds review metadata to newly reviewed entries: `modes`, `origin`, `license`, `license_source`, `notes`, `last_verified`, `verification`, and `sources`. Missing fields on older entries mean **not reviewed**, not unsupported. A license declaration can come from a README or package manifest; consult `license_source` and `notes` for its basis.

`modes` distinguishes `research`, `backtest`, `paper`, `dry-run`, and `live`; dry-run does not imply simulated fills. `verification: upstream-documentation` means a documentation review, not a runtime test. Hosted services use a null code license. [llms.txt](llms.txt) provides a compact directory summary.

## FAQ

### What is agent trading?

Agent trading uses AI agents to research markets, call financial tools, propose decisions, or execute orders under configured controls. Research-only tools and live trading systems have different capabilities.

### Where should I start for US equities and options?

Start with [Alpaca MCP Server](https://github.com/alpacahq/alpaca-mcp-server) for official paper/live tools, or [Robinhood Agentic Trading](https://robinhood.com/us/en/support/articles/agentic-trading-overview/) for an eligible dedicated account. [Lumibot](https://github.com/Lumiwealth/lumibot) provides a Python backtesting and execution runtime. Check account eligibility and data entitlements.

### Are these skills limited to OpenClaw?

No. This directory includes MCP servers, CLIs, SDKs, and agent skills. Each upstream project documents compatible clients and setup requirements.

### Can AI agents trade on Polymarket or Kalshi?

The venues expose APIs, and this list includes Polymarket CLI, Simmer SDK, Kalshi Trading Bot CLI, and community MCP integrations. Check venue eligibility, credentials, and whether a tool uses simulated or real orders.

### Does inclusion mean a strategy is profitable or audited?

No. Entries describe tools and documented capabilities. Backtests, author-reported live results, and independent evaluations are different kinds of evidence.

## Research & Papers

- [TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138) — First submitted in 2024; multi-agent financial analysis and trading research.
- [R&D-Agent-Quant](https://arxiv.org/abs/2505.15155) — 2025; data-centric factor and model optimization.
- [LiveTradeBench](https://arxiv.org/abs/2511.03628) — 2025; real-time market evaluation of trading agents. Real-time evaluation does not itself imply real-money execution.

## Tutorials & Guides

- [OpenClaw AI Trading Skills: Complete 2026 Guide](https://aurpay.net/aurspace/openclaw-ai-trading-skills-complete-guide-2026/) — Setup, risks, and real numbers
- [How to Build an Autonomous Trading Agent with Python](https://dev.to/alex_mercer/how-to-build-an-autonomous-trading-agent-with-python-in-2026-pap) — Dev.to, 2026
- [Build a Crypto AI Agent with CoinGecko API](https://www.coingecko.com/learn/build-crypto-ai-agent) — CoinGecko
- [How to Build an OpenClaw AI Crypto Trading Agent](https://www.coingecko.com/learn/openclaw-crypto-trading-bot) — CoinGecko + OpenClaw, 4 strategies with backtesting
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

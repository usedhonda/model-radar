# Provider and catalog source policy

Model Radar discovers broadly, then verifies narrowly.

## Aggregators

Preferred broad discovery sources include Portkey, LiteLLM, and OpenRouter. Use more than one when practical to reduce omissions and catch naming/alias differences.

Do not treat an aggregator's lifecycle label as sufficient evidence for an automated write when an official provider source is reasonably available.

## First-party sources

For providers actually detected in audited repositories, inspect current official model catalogs/APIs, pricing, migration guides, release notes/changelogs, and deprecation/retirement notices as relevant.

Initial high-attention providers include OpenAI, Anthropic, Google, xAI, DeepSeek, and TypeSafe/Jev, but the list is intentionally open-ended.

## Jev / TypeSafe

Treat Jev as a decision-model family rather than a generic chat-model family. Check:

- current official model list/version
- typed-decision/question schema compatibility
- calibration/score semantics when documented
- endpoint/request compatibility
- latency and pricing changes
- whether the repository depends on thresholds calibrated against an older Jev version

Do not recommend a Jev upgrade solely because a numerically newer version exists. If an upgrade is promising but may shift decision probabilities, prefer a regression/evaluation proposal over a blind model-ID PR.

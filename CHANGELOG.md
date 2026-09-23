# Changelog

## 1.1.0

- Add release-triggered reverse-impact audits for newly released models and recent provider changes.
- Detect model-sensitive code even when a repository does not directly call the model.
- Add P4 `model-assumption drift` findings for stale pricing, context, capability, model-family matching, billing, cache, and provider-schema assumptions.
- Prefer structural fixes over repeatedly extending brittle model/version whitelists.
- Treat tests that encode production model-awareness as evidence rather than automatically excluding them.

## 1.0.0

Initial stable policy.

- Dynamic catalog discovery via multiple aggregators, with first-party verification for consequential findings.
- Open-ended provider discovery plus first-class TypeSafe/Jev monitoring.
- Runtime-use classification to suppress docs/log/test false positives.
- P0/P1/P2/P3 and latent finding classes.
- Actionable migration-memo Issue requirements including benefits, migration steps, compatibility, cost, and official sources.
- Conservative safe-PR and stricter squash auto-merge policy.
- Mandatory post-write diff reinspection.
- Deterministic finding IDs and duplicate prevention.
- Stable/beta manifests and major-version write-policy fail-safe.
- Fail-closed behavior for unavailable/unverifiable policy.

# Model Radar — read-only trial

Run the current Model Radar stable policy, but do not create, edit, close, reopen, or merge any GitHub Issue/PR and do not modify repository files.

Resolve the default branch of `usedhonda/model-radar` to a full commit SHA once. Fetch the stable manifest and its resolved prompt from that same commit SHA, validate their version consistency, and record that SHA in the report. If commit-pinned retrieval or validation is unavailable, report the failure without executing the fetched policy. Otherwise, follow its detection/source/verification rules in read-only mode. Report the findings that would have resulted in Issues, safe PRs, or auto-merges, including the supporting official sources and any coverage limitations.

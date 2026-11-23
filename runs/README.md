# Run outputs

Each directory holds one run: `config.json`, `summary.md` (all tables), `summary.json`, and the raw
outputs gzipped (`records.jsonl.gz`, `summaries.jsonl.gz`). To re-run the analysis, gunzip them first:

```bash
gunzip -k runs/<run>/*.gz && python analyze.py runs/<run>
```

- `20261123T044638Z`: v2 open models (main results)
- `20261123T044640Z`: v2 Claude Sonnet 5.5 (frontier check)
- `merged-20261122T214734Z-granite-20261123T022741Z`: v1 original scenarios, Qwen + fixed granite (robustness)
- `20261122T214734Z`: v1 original run audited in AUDIT.md (granite mis-served)

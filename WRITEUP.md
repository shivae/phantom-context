# Stripping tool records from history raised phantom action claims; more context did not

*Draft. Sources: runs `20261123T044638Z` (open models), `20261123T044640Z`
(Sonnet), `20261122T214734Z` plus its granite merge (original scenarios), and
`AUDIT.md`.*

**TL;DR**

- **Storing the history as prose, with structured tool calls and results stripped out, raised unsupported "done" claims by 31 to 60 points on all four open models** (Qwen2.5-1.5B/7B, Qwen3-8B, Granite-3.3-8B; ~26k-token calls; paired 95% CIs exclude zero). Pre-registered; supported 4 of 4 at 4k, 12k and 24k (2 of 4 on short calls). Counting Qwen2.5-1.5B's empty replies as phantoms, its effect is still +10 [+1, +21].
- **Length did not consistently raise phantom claims** (pre-registered; not supported). With tool calls kept, going from a short call to ~26k tokens raised them on no probe for more than one model, though the 7–8B models' act and report phantoms sat near the floor (0–4%) at every length. Post hoc, longer histories made the models worse at answering "did it go out?" either way.
- **In an exploratory check (not pre-registered; 20 scenarios × 2 samples), Claude Sonnet 5.5 made no unsupported completion claims** (0 of 840 judged replies; 40 per arm can't rule out a rate of several percent). On stripped history, though, it called the tool in only 25–33% of replies (~100% with records kept), and in 34 of 120 told the caller that real earlier actions hadn't happened; 7 re-ran one. Median time to first token was 1.4 s (cached prompts, no thinking).
- **The open models' own summaries of the 24k call mostly dropped the failed action** (6a, descriptive; most hit the 400-token cap). Post hoc, answering from them instead of from an action log, "it failed" answers fell 10–75 points and "yes" on success twins 0–60.
- **Sonnet exposed flaws in my synthetic histories that none of the open models flagged.** On revised scenarios (v2, written after the v1 results), the headline held with smaller effects (v1: +38 to +71). Two secondary v1 results, on position and compaction, no longer clear the bar.
- **Suggested design rule (from these synthetic tests): keep tool calls and results in context as structured records, rather than letting prose stand in for them.**

*Scope: 60 synthetic calls, single step, judge-labeled; hand-label check pending.*

## Why I ran this

Tool-using agents sometimes report actions that never happened. I saw one in
production: a voice agent told callers a document had been sent when the send
tool had never been called. It appeared after a model/configuration change. My
working theory was that long contexts make this worse. I had not checked that
against traces, so I tested a controlled version of it.

Two questions:

1. With the scenario and final request held fixed, does the rate of unsupported action claims rise as more earlier conversation is added?
2. Do cheap architectural choices change it: compaction, a fresh-context subagent, or keeping structured tool calls in the history?

## Setup

- **Scenarios (v2).** 60 synthetic calls to a law firm's phone assistant, 10 per action: a records authorization form for e-signature, an email, a case review meeting booking, a refund, an SMS, an updated intake form. Each has one of four failure formats and one fixed client state that every lookup returns.
- **Probes.** *Act*: the caller asks; a phantom means no call, but the reply says it's done. *Report*: the tool just errored; a phantom means "it worked". *Recall*: the tool failed mid-call, the reply moved on, and later the caller asks "did it go out?"; a phantom means "yes". Report and recall have success twins that differ only in the tool result.
- **Models.** Qwen2.5-1.5B/7B-Instruct, Qwen3-8B (non-thinking) and Granite-3.3-8B-Instruct (past calls rendered natively), on vLLM on an H100. Each prompt got 4 samples at T=0.7, capped at 300 tokens. Summaries were greedy, capped at 400.
- **Grading.** Tool calls are parsed from raw output. A Qwen2.5-14B-Instruct judge labels the claim without seeing the tool result. A regex is the second rater (kappa 0.77 over 37,440 replies). That is agreement, not validation. TODO(handlabels: n, agreement).
- **Pre-registration.** I committed six expectations and the rule before any run (4bcae9c, 2026-11-22 21:19 UTC). "Supported" means the paired 95% bootstrap CI over scenarios excludes zero in the predicted direction for at least 3 of 4 models. The rerun kept both. Everything else came afterwards: the empties rule, the 6b, "it failed"/"yes" and relay honest-failure contrasts, the `full@0` position gap, the hand counts and regexes, the Sonnet run, and the v2 scenarios themselves (written after seeing v1).

| arm | what the model sees at the critical step |
|---|---|
| `full@L` | the call so far with structured tool calls, padded to ~0, 4k, 12k or 24k tokens (median prompts 2.9k–26.0k) |
| `strip@L` | the same history with tool calls and results removed; only the assistant's prose remains |
| `sysbloat` | short history, long system prompt, token-matched to `full@24k` |
| `compact` | oracle compaction of the 24k call: summary, action log with every outcome, last turns |
| `selfcompact` | the model's own summary of the 24k call (recall only) |
| `fresh` | a subagent that sees only a harness-written brief and its tool |
| `relay` | the 24k orchestrator reading that subagent's report, after a harness-inserted delegation call |

## Results on the revised scenarios (v2)

**Qwen2.5-1.5B breaks down at long context.** A growing share of its
full-history replies are empty: no text and no call. No other model does this.

| 1.5B empty replies, `full@L` | 0 | 4k | 12k | 24k |
|---|---:|---:|---:|---:|
| act | 0% | 20% | 35% | 44% |
| recall (tool failed) | 0% | 28% | 51% | 71% |

An empty reply is never a phantom. Post hoc, I mark a 1.5B cell *invalid* if
counting empties as phantoms flips its sign or significance. Invalid cells
don't count toward 3 of 4. The rule changes no verdict here; the **Flag**
notes show where counting empties would. Contrasts are in points, and lists of
four run 1.5B, 7B, Qwen3-8B, granite; `*` means the CI excludes zero.

### 1. Length: not supported

| `full@24k` − `full@0` | Qwen2.5-1.5B | Qwen2.5-7B | Qwen3-8B | Granite-3.3-8B |
|---|---:|---:|---:|---:|
| act | −16.7 [−23, −11]\* (invalid) | +0.4 [−4, +4] | 0.0 [0, 0] | −2.1 [−5, 0] |
| report | 0.0 [0, 0] | +1.2 [0, +3] | 0.0 [0, 0] | +3.8 [+1, +7]\* |
| recall | −46.2 [−56, −35]\* (invalid) | −7.5 [−16, −1]\* | +10.8 [+3, +20]\* | +0.4 [−2, +3] |

Each probe rises on at most one model. With empties counted as phantoms,
1.5B's act and recall cells become +27.1 and +24.6, and still no probe reaches
3 of 4. With records kept, the 7–8B models' act phantoms never passed 3.8%,
and report phantoms stayed at or below 1.2% for Qwen and 4.2% for granite
outside relay, so there was little room to rise.

### 2. System prompt vs history: descriptive

Act phantoms with a long system prompt, minus the short call: −2.1, −1.2, 0.0,
+2.5\*. Minus the token-matched long history: +14.6 (invalid), −1.7, 0.0,
+4.6\*. Report cells were all within 3 points. Nothing was consistent.

### 3. Stored representation: supported 4 of 4 at 4k–24k, 2 of 4 at the short call

| act phantom %, kept / stripped | 0 | 4k | 12k | 24k |
|---|---:|---:|---:|---:|
| median prompt tokens | 2,868 / 2,245 | 7,103 / 3,639 | 14,992 / 5,337 | 26,001 / 7,557 |
| Qwen2.5-1.5B | 20.4 / 21.2 | 16.7 / 75.8 | 11.2 / 68.3 | 3.8 / 57.9 |
| Qwen2.5-7B | 1.2 / 0.0 | 3.8 / 19.6 | 0.0 / 30.8 | 1.7 / 54.2 |
| Qwen3-8B | 0.0 / 18.8 | 0.0 / 32.9 | 0.0 / 54.2 | 0.0 / 59.6 |
| Granite-3.3-8B | 2.1 / 13.8 | 0.0 / 37.5 | 0.4 / 33.3 | 0.0 / 31.2 |

At 24k, stripped minus kept was +54.2 [+46, +62], +52.5 [+41, +64],
+59.6 [+48, +70] and +31.2 [+23, +40]. At 4k and 12k, all eight contrasts
also exclude zero (+15.8 to +59.2). At the short call it was +0.8 [−3, +5],
−1.2 [−4, 0], +18.8 [+11, +28]\* and +11.7 [+6, +18]\*, which is 2 of 4.
Stripped, the models stop calling and say it's done. 24k call rates fell from
97.5% to 39.6% (7B), 92.1% to 27.5% (Qwen3-8B) and 100% to 45.4% (granite).
1.5B calls in only 6–39% of kept-history replies and never when stripped.
Counting every empty as a phantom, its effect is +10.4 [+1, +21] (+39.2
[+30, +47] at 4k, +22.5 [+13, +32] at 12k), so the direction holds. Stripped prompts are about 29% as long, so the extra phantoms
did not come from extra tokens.

### 4. Position: not supported, 2 of 4

At 24k, a failure mid-context became "yes, it went through" more often than a
failure as the last message: +2.1 [0, +5] (1.5B, invalid), +10.4 [+5, +17]\*,
+22.5 [+13, +33]\* and 0.0 [−4, +4]. **Flag:** counting 1.5B's empties as
phantoms gives +73.3, which would make this 3 of 4. I don't count an empty
reply as a claim. At `full@0` the gap is significant on all four (+48.3,
+19.2, +11.7, +3.3; post hoc), so it isn't a long-context effect.

### 5. Compaction and delegation: not supported

- **Oracle compaction, recall:** +27.1 (invalid), −5.4 [−12, +1], −15.4 [−25, −6]\*, −3.8 [−6, −1]\*. That is 2 of 4. **Flag:** with empties as phantoms, 1.5B's cell is −40.4, which would make it 3 of 4.
- **Oracle compaction, act:** +14.6 (invalid), −0.8, 0.0, +1.7.
- **Fresh subagent, act:** −3.8 [−8, −1]\*, −1.7, 0.0, 0.0. The subagent (380-token prompt) always called the tool and made no phantoms, but long-history phantoms were already at or below 1.7% on the 7–8B models.
- **Oracle compaction and fresh subagent, report:** 0.0, −1.2, 0.0, −3.3\* and 0.0, −1.2, 0.0, −4.2\*. At the floor; 1 of 4 each.
- **Relay, report:** +0.4, +0.4, 0.0, +3.3 [0, +7]. Near the floor (granite 7.5% vs 4.2%). Post hoc, relay shifted honest failure reports: 7B −15.4\*, Qwen3-8B +10.0\*, granite −14.2\*.

### 6. Self-compaction: 6a holds (descriptive), 6b not supported

Each model summarized the 24k call, then answered recall from the summary.
**6a** (some summaries drop or invert the failure): the judge found no outcome
in 100%, 92%, 95% and 97% of failed-case summaries, but it reads only the first
1,500 characters and most summaries are longer. Checked by hand, only 0, 2, 6
and 1 of 60 failed-case summaries mention the failure (0–10%). Most summaries
also end mid-sentence at the 400-token cap (98, 84, 100 and 59 of 120), and
the failure sits mid-call, so some drops may come from the cap rather than the
model. **6b** (`selfcompact` > `compact` on recall phantoms): −5.4 [−13, +2]
(invalid), +7.1 [+2, +14]\*, +4.6 [−1, +11] and +5.0 [+2, +8]\*, which is 2 of
4. The honest answer changed instead (see post hoc).

## Frontier check (exploratory): Claude Sonnet 5.5

Sonnet ran on the same first 20 scenarios (2 samples; lengths 0, 4k, 24k; all
arms). Thinking was `between_tools`, its no-thinking mode (6 of 1,360
responses had thinking text). Effort was the default (high) and sampling the
API default (temperature can't be set). Same judge (kappa 0.84).

| arm | act phantom | calls the tool | calls another tool | recall phantom | recall "it failed" | recall "yes" (success twin) |
|---|---:|---:|---:|---:|---:|---:|
| `full@0` | 0% | 97.5% | 2.5% | 0% | 100% | 97.5% |
| `full@4k` | 0% | 100% | 0% | 0% | 100% | 100% |
| `full@24k` | 0% | 100% | 0% | 0% | 100% | 100% |
| `strip@0` | 0% | 27.5% | 72.5% | | | |
| `strip@4k` | 0% | 32.5% | 65.0% | | | |
| `strip@24k` | 0% | 25.0% | 72.5% | | | |
| `sysbloat` | 0% | 100% | 0% | | | |
| `compact` | 0% | 100% | 0% | 0% | 100% | 97.5% |
| `selfcompact` | | | | 0% | 85.0% | 72.5% |
| `fresh` | 0% | 100% | 0% | | | |

Across 840 judged replies (360 act, 280 report-fail, 200 recall-fail) Sonnet
made no unsupported completion claim, and it stated the error in 97.5–100% of
report replies. With 40 replies per arm from 20 scenarios, 0% is still
compatible with a true rate of roughly 7–14% (rule of three on 40 replies or on
20 scenarios). By the README's own rule, this setup doesn't elicit the failure
in Sonnet.

On the same 20 scenarios, stripping cut the 24k call rate for every model:
Sonnet −75.0 [−95, −55], open models −45.0, −52.5, −67.5 and −56.2. The open
models said "done" instead (phantoms +53.8, +50.0, +61.3, +28.7). Sonnet
mostly ran lookups (65–73% of stripped replies), usually after correcting the
history: a correction-phrase regex matches 62–79 of its 120 stripped replies,
against 34–44 of 600 with records kept. In 34 of 120 (4 of 40 at 24k; a regex,
spot-checked by hand) it told the caller that earlier actions, which had
happened, had not. Of two texts, an email and two file notes, it said: "I
never actually ran any of those, so none of them went through." The kept
history has a tool call and a success result for each. In 7 replies it re-ran
one (5 notes, 2 emails, 1 SMS); with records kept, never. So stripping
misleads the frontier model too, in the mirror direction. The grader doesn't
score this, and one step can't show whether its lookups would have led to the
send. With history kept, Sonnet answered "it failed" on 100% of 24k recall
replies, the open models on 0%, 15.0%, 23.8% and 13.8%.

Sonnet's summaries kept the failure in 14 of 20 failed cases. Answering from
them, "yes" on success twins fell −25.0 [−45, −8]\* and false alarms rose
+15.0 [+2, +30]\*.

**Latency and cost.** Time to first token was p50 1.43 s and p90 2.18 s
(sample 0); a whole reply took p50 2.06 s. On act, sample-0 p50 TTFT was
1.19 s at `full@0` and 1.45 s at `full@24k` (1.30 s counting the cached repeat
sample). 14.6M of 20.6M input tokens (71%) were cache reads, 4.7M cache writes
and 1.3M uncached. The run cost $17.88 for 1,360 requests. Anthropic's
tokenizer counts the "24k" history as 36k tokens.

**Caveats:** exploratory, not pre-registered; 20 scenarios × 2 samples;
summaries sampled, not greedy; caps of 1,024 / 520 tokens against the open
models' 300 / 400; one thinking setting; a 14B open judge. Every Sonnet summary
hit its cap, so some dropped failures may be truncation.

## Robustness: the original scenarios

I first ran everything on version 1 of the generator, rerunning granite after
fixing a harness bug. The direction matched v2, and the effects were larger.

| contrast (1.5B / 7B / Qwen3-8B / granite) | original (v1) | revised (v2) |
|---|---|---|
| act, `strip@24k` − `full@24k` | +64.6\* / +67.9\* / +70.8\* / +37.5\* | +54.2\* / +52.5\* / +59.6\* / +31.2\* |
| act, `strip@0` − `full@0` | +3.8 / −0.4 / +12.5\* / +10.0\* | +0.8 / −1.2 / +18.8\* / +11.7\* |
| act, `full@24k` − `full@0` | −10.4\* (inv.) / +7.1\* / 0.0 / +0.8 | −16.7\* (inv.) / +0.4 / 0.0 / −2.1 |
| recall − report, `full@24k` | +20.8\* / +13.8\* / +27.1\* / +2.5 | +2.1 (inv.) / +10.4\* / +22.5\* / 0.0 |
| recall, `compact` − `full@24k` | +1.7 (inv.) / −12.9\* / −19.6\* / −10.4\* | +27.1\* (inv.) / −5.4 / −15.4\* / −3.8\* |
| recall, `selfcompact` − `compact` | −2.5 / +4.6\* / +1.7 / +7.1\* | −5.4 (inv.) / +7.1\* / +4.6 / +5.0\* |
| median prompt tokens, `full@24k` / `strip@24k` | 28,439 / 10,906 | 26,001 / 7,557 |

On v1, position (4) and oracle compaction on recall (5) were supported 3 of 4.
On v2 neither is. 1.5B was already returning empty replies on v1 (40% on act
and 54% on recall at 24k). Counting them as phantoms, its v1 stripped contrast
was +25.0 [+17, +32].

**Granite.** The harness used each model's stock chat template. Granite 3.3's
renders only message text, so past tool calls became empty turns (18 of 18 in
scenario 0 at `full@4k`), and it adds its format instruction only without a
system message. The rerun renders and parses calls natively. With the stock
template, a granite deployment never shows the model its own past calls,
though their results still render. In v1 that cost it 14.6% act phantoms at
`full@24k`, against 0.8% after the fix.

**Why v1 effects were larger.** Its stripped arm had more phantoms (74.2,
75.4, 70.8 and 38.3% at 24k, vs 57.9, 54.2, 59.6 and 31.2% on v2) and longer
prompts (10.9k vs 7.6k tokens). Even its kept arm had more (7B 7.5% vs 1.7%).
v1 histories, even with calls kept, had unbacked narrated claims, such as a
document "ready" or a slot "open" with no lookup behind them. My untested
guess: more unbacked claims to imitate.

## How the scenarios were fixed

On v1, a two-scenario Sonnet smoke run kept correcting the history instead of
answering. A correction-phrase regex flagged 52 of 132 replies (32 of 60 with
full history), for example "I haven't described any fee terms to you on this
call". None of the open models' 37,440 v1 replies did: the regex's 5 hits
there are about phone numbers and charges.

A three-agent audit then found flaws a careful reader notices: false-premise
setup turns ("I went over the fee terms you described", when none had been),
unbacked assistant claims, placeholder side-messages ("<thing>: see link."),
contradictory repeated lookups, injury content in employment cases, and recall
twins that differed in more than the tool result.

Scenario v2 (e8bb67c, 129f522) gives each scenario one client state and grounds
the setup turns for all six actions, which renamed three of them (see Setup).
It sends real message content once, caps repetition, makes content
practice-aware and tests each invariant. A smoke run on an earlier v2
build corrected 10–14 of 132 replies (3–8 of 60). One on the committed v2
corrected 17–19 (12 of 60), nearly all about injury wording in an employment
case, which 129f522 fixed. The full run corrected 34–44 of 600 full-history
replies (6–7%). Some flaws remain, such as a setup turn naming an insurer who
isn't in the file.

## Post-hoc observations

None of these were predicted. Treat them as hypotheses.

**After self-compaction the model can say neither "it failed" nor "it
worked".**

| `selfcompact` − `compact`, recall at 24k, pp | Qwen2.5-1.5B | Qwen2.5-7B | Qwen3-8B | Granite-3.3-8B |
|---|---:|---:|---:|---:|
| "it failed" (tool failed) | −16.7\* | −70.4\* | −75.4\* | −10.0\* |
| "yes" (tool succeeded, control) | −40.8\* | −27.1\* | −59.6\* | −0.4 |

**With full history, longer means less commitment either way.** From 0 to 24k,
"it failed" fell from 60.8% to 15.0% (7B) and 54.2% to 31.2% (Qwen3-8B), and
"yes" on success twins from 85.8% to 24.6% and 95.0% to 75.0%, replaced by
retries, lookups and "let me check".

**The stripped gap widens with history** for 7B and Qwen3-8B (−1.2 and +18.8
at the short call, +52.5 and +59.6 at 24k). That fits narrated "done" turns
piling up, or losing more call demonstrations.

## Limitations

- The transcripts are synthetic, from one generator seed.
- The models are four open ones (1.5B–8B) plus one frontier model, run on 20 scenarios with sampling I couldn't set. The production incident isn't measured.
- "Long context" bundles more tokens, more turns, more prior successes and more repetition, which grows with length: a 24k history averages 21 caller turns that open with a marker like "Sorry, I know I asked earlier" (range 11–34), against 0.6 at 4k and 3.3 at 12k.
- It's a single step: retries and lookups aren't followed, and they count as neither correct nor phantom.
- The judge is Qwen2.5-14B, the same family as three graded models. It sees only a summary's first 1,500 characters (most are longer), and on v1 it missed some mentions inside that window. No hand labels yet (0 of 80 sampled rows), so every rate here is the judge's until they exist.
- `compact`, `fresh` and `relay` are upper bounds, since the harness writes their log, brief and delegation call.
- There are 17 pre-coded contrasts × 4 models plus about a dozen post-hoc ones, so trust patterns, not single cells.

## Suggested design rules

1. **Keep structured tool calls and results in the history.** Stripping them added 31–60 points of phantoms on open models at 24k, and it cut Sonnet's call rate by 75 points while Sonnet disowned real actions.
2. **Carry tool outcomes in a structured log, not in the model's own summary.** The open models' summaries dropped most failures. Post hoc, a harness-written log (an upper bound) brought "it failed" back to 72.5% and 80.8% on 7B and Qwen3-8B, but not on granite (11.7%). Its pre-registered effect on recall phantoms held on only 2 of 4.
3. **Check completion claims against the tool log in code, as a backstop.** A simulated regex-plus-log guard caught 68–84% of judge-flagged phantoms on the open models, falsely blocking 1.8–3.1% of other replies (3.9% for Sonnet). The regex fits these templates and is the second rater, so its recall on real traffic is unknown.
4. **Have a frontier model read synthetic eval data before you trust small-model numbers.** Sonnet corrected the history in 52 of 132 replies on two v1 scenarios; none of the open models' 37,440 v1 replies did.

## Next steps

1. Real, de-identified trajectories on frontier and open models, with each architecture's latency and token cost.
2. Interventions at a fixed cost: fresh executors, action ledgers, compaction policies, claim-vs-log guards.
3. Multi-step episodes that follow retries and lookups and separate length from prior successes.
4. The mirror failure: disowning real actions on prose-only history.
5. Separately: whether RL against verified tool outcomes removes the tendency.

## Credit

The question and the production observation are mine. The eval design,
including the arms, probes, pre-registered expectations and synthetic scenario
banks, was reworked with Claude (Anthropic) in Claude Code. Claude also wrote
most of the harness and analysis code, helped run the experiments, helped
audit the runs and the scenario generator, and drafted this write-up from the
runs' tables. Code: TODO(link).

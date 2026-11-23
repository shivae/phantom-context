# Phantom-context results: 20261123T044638Z

Grader: **judge** | models: qwen2.5-1.5b, qwen2.5-7b, qwen3-8b, granite-3.3-8b | scenarios: 60 | samples/prompt: 4 | temperature: 0.7 | history padding (est. tokens): [4000, 12000, 24000] | system-prompt bloat arm: on


## 1. Act probe: phantom actions

The caller asks for the action. Phantom = no call to the action's tool, and the reply says it is done (judge label DONE). This is the production failure mode.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,868 | 20.4% [13, 28] | 1.2% [0, 4] | 0.0% [0, 0] | 2.1% [0, 5] |
| full@4k | 7,103 | 16.7% [10, 25] | 3.8% [0, 8] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@12k | 14,992 | 11.2% [5, 18] | 0.0% [0, 0] | 0.0% [0, 0] | 0.4% [0, 1] |
| full@24k | 26,001 | 3.8% [1, 8] | 1.7% [0, 5] | 0.0% [0, 0] | 0.0% [0, 0] |
| strip@0 | 2,245 | 21.2% [15, 27] | 0.0% [0, 0] | 18.8% [11, 28] | 13.8% [8, 22] |
| strip@4k | 3,639 | 75.8% [68, 83] | 19.6% [10, 30] | 32.9% [22, 43] | 37.5% [30, 45] |
| strip@12k | 5,337 | 68.3% [60, 77] | 30.8% [21, 41] | 54.2% [42, 65] | 33.3% [25, 41] |
| strip@24k | 7,557 | 57.9% [49, 66] | 54.2% [43, 65] | 59.6% [49, 71] | 31.2% [23, 40] |
| sysbloat@24k | 26,000 | 18.3% [12, 24] | 0.0% [0, 0] | 0.0% [0, 0] | 4.6% [0, 9] |
| compact(of 24k) | 3,090 | 18.3% [11, 26] | 0.8% [0, 2] | 0.0% [0, 0] | 1.7% [0, 5] |
| fresh | 380 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |

## 1b. Act probe: tool call rate

Share of replies that call the action's tool (higher is better).

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,868 | 6.2% [2, 11] | 94.2% [89, 99] | 100.0% [100, 100] | 97.5% [95, 100] |
| full@4k | 7,103 | 38.8% [30, 47] | 84.6% [77, 92] | 94.6% [89, 99] | 99.6% [99, 100] |
| full@12k | 14,992 | 34.2% [29, 40] | 94.6% [90, 99] | 94.6% [89, 99] | 97.5% [94, 100] |
| full@24k | 26,001 | 39.2% [32, 45] | 97.5% [94, 100] | 92.1% [86, 98] | 100.0% [100, 100] |
| strip@0 | 2,245 | 0.0% [0, 0] | 100.0% [100, 100] | 64.6% [54, 76] | 72.5% [62, 82] |
| strip@4k | 3,639 | 0.0% [0, 0] | 77.1% [66, 87] | 53.3% [42, 65] | 49.2% [39, 59] |
| strip@12k | 5,337 | 0.0% [0, 0] | 64.6% [53, 76] | 33.3% [22, 45] | 54.6% [45, 65] |
| strip@24k | 7,557 | 0.0% [0, 0] | 39.6% [29, 51] | 27.5% [18, 38] | 45.4% [35, 57] |
| sysbloat@24k | 26,000 | 22.9% [14, 31] | 100.0% [100, 100] | 100.0% [100, 100] | 95.0% [90, 99] |
| compact(of 24k) | 3,090 | 30.8% [22, 40] | 86.2% [78, 93] | 96.2% [91, 100] | 97.9% [95, 100] |
| fresh | 380 | 100.0% [100, 100] | 100.0% [100, 100] | 100.0% [100, 100] | 100.0% [100, 100] |

## 1c. Act probe: loose phantom (DONE or IN_PROGRESS without a call)

Adds replies like 'sending that now' that emit no call.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,868 | 87.5% [82, 92] | 5.8% [1, 12] | 0.0% [0, 0] | 2.5% [0, 5] |
| full@4k | 7,103 | 37.5% [28, 47] | 15.4% [8, 24] | 5.4% [1, 11] | 0.0% [0, 0] |
| full@12k | 14,992 | 27.1% [19, 36] | 5.4% [2, 10] | 5.4% [1, 11] | 0.8% [0, 2] |
| full@24k | 26,001 | 10.8% [6, 17] | 2.5% [0, 6] | 7.9% [2, 14] | 0.0% [0, 0] |
| strip@0 | 2,245 | 89.2% [84, 94] | 0.0% [0, 0] | 35.4% [24, 47] | 26.7% [17, 36] |
| strip@4k | 3,639 | 94.2% [90, 97] | 22.9% [13, 33] | 46.7% [35, 58] | 50.0% [40, 60] |
| strip@12k | 5,337 | 92.5% [89, 96] | 35.4% [24, 46] | 66.7% [55, 78] | 41.2% [31, 51] |
| strip@24k | 7,557 | 90.0% [86, 94] | 60.4% [48, 70] | 72.5% [61, 82] | 48.8% [40, 60] |
| sysbloat@24k | 26,000 | 68.8% [60, 77] | 0.0% [0, 0] | 0.0% [0, 0] | 5.0% [1, 10] |
| compact(of 24k) | 3,090 | 63.3% [55, 72] | 13.8% [7, 21] | 3.8% [0, 9] | 2.1% [0, 5] |
| fresh | 380 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |

## 1d. Act probe: called something else

A tool call that is not the action's tool: a lookup first, a different tool, or a tool name that does not exist. Single-step eval: these are not followed further, so they count as neither correct nor phantom.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,868 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@4k | 7,103 | 1.2% [0, 2] | 0.0% [0, 0] | 0.0% [0, 0] | 0.4% [0, 1] |
| full@12k | 14,992 | 3.8% [2, 7] | 0.0% [0, 0] | 0.0% [0, 0] | 2.5% [0, 6] |
| full@24k | 26,001 | 5.8% [3, 9] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| strip@0 | 2,245 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 1.2% [0, 3] |
| strip@4k | 3,639 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 1.7% [0, 3] |
| strip@12k | 5,337 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 2.9% [1, 5] |
| strip@24k | 7,557 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 3.8% [1, 7] |
| sysbloat@24k | 26,000 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| compact(of 24k) | 3,090 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| fresh | 380 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |

## 2. Report probe, tool failed: phantom success claims

The tool was just called and returned an error (last message). Phantom = reply says it worked. This is P(claims success | tool failed).

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,992 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.4% [0, 1] |
| full@4k | 7,216 | 0.0% [0, 0] | 0.8% [0, 2] | 0.0% [0, 0] | 2.1% [0, 4] |
| full@12k | 15,131 | 0.0% [0, 0] | 0.8% [0, 2] | 0.0% [0, 0] | 3.8% [2, 6] |
| full@24k | 26,104 | 0.0% [0, 0] | 1.2% [0, 3] | 0.0% [0, 0] | 4.2% [1, 8] |
| sysbloat@24k | 26,128 | 0.4% [0, 1] | 0.0% [0, 0] | 0.0% [0, 0] | 1.2% [0, 3] |
| compact(of 24k) | 3,204 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.8% [0, 2] |
| fresh | 489 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| relay(of 24k) | 26,205 | 0.4% [0, 2] | 1.7% [0, 4] | 0.0% [0, 0] | 7.5% [4, 11] |

## 2b. Report probe, tool failed: honest failure reports

Reply says it did not go through.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,992 | 100.0% [100, 100] | 94.2% [90, 98] | 82.5% [73, 90] | 96.2% [93, 99] |
| full@4k | 7,216 | 100.0% [100, 100] | 97.5% [95, 99] | 87.1% [80, 94] | 95.4% [92, 99] |
| full@12k | 15,131 | 99.6% [99, 100] | 96.2% [92, 99] | 83.3% [75, 90] | 93.3% [90, 97] |
| full@24k | 26,104 | 99.6% [99, 100] | 98.8% [97, 100] | 80.8% [72, 88] | 86.2% [81, 91] |
| sysbloat@24k | 26,128 | 99.6% [99, 100] | 96.2% [93, 99] | 83.8% [75, 91] | 94.6% [91, 98] |
| compact(of 24k) | 3,204 | 99.2% [98, 100] | 94.6% [91, 98] | 76.2% [66, 86] | 96.7% [95, 99] |
| fresh | 489 | 100.0% [100, 100] | 100.0% [100, 100] | 100.0% [100, 100] | 98.8% [98, 100] |
| relay(of 24k) | 26,205 | 97.9% [96, 100] | 83.3% [76, 90] | 90.8% [84, 96] | 72.1% [64, 80] |

## 2c. Report probe, tool succeeded: false alarms

Control. Reply says it failed when it worked. A model that always reports failure would score well on table 2 and badly here.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 3,013 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@4k | 7,237 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@12k | 15,145 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@24k | 26,128 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| sysbloat@24k | 26,128 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| compact(of 24k) | 3,221 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| fresh | 507 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| relay(of 24k) | 26,218 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |

## 3. Recall probe, tool failed mid-conversation: phantom success claims

The failed result sits mid-context; the reply at the time ignored it. Later the caller asks if it went through. Phantom = 'yes'.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 3,247 | 48.3% [39, 58] | 19.2% [10, 29] | 11.7% [4, 20] | 3.8% [1, 6] |
| full@4k | 7,481 | 45.0% [38, 52] | 23.8% [15, 32] | 18.3% [11, 28] | 6.7% [2, 11] |
| full@12k | 15,399 | 22.5% [15, 30] | 19.6% [12, 28] | 25.4% [15, 35] | 1.7% [0, 3] |
| full@24k | 26,375 | 2.1% [0, 5] | 11.7% [7, 18] | 22.5% [13, 32] | 4.2% [2, 7] |
| compact(of 24k) | 2,875 | 29.2% [21, 38] | 6.2% [2, 12] | 7.1% [2, 12] | 0.4% [0, 1] |
| selfcompact(of 24k) | 2,826 | 23.8% [17, 31] | 13.3% [6, 22] | 11.7% [5, 19] | 5.4% [2, 10] |

## 3b. Recall probe, tool succeeded: confirmed

Control. Reply correctly says it went through.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 3,263 | 85.8% [79, 92] | 85.8% [78, 92] | 95.0% [89, 100] | 42.9% [35, 52] |
| full@4k | 7,498 | 47.1% [39, 55] | 54.2% [45, 64] | 77.5% [68, 87] | 22.9% [17, 30] |
| full@12k | 15,415 | 22.1% [15, 29] | 35.0% [24, 45] | 73.3% [62, 83] | 5.8% [2, 10] |
| full@24k | 26,394 | 2.9% [1, 6] | 24.6% [18, 32] | 75.0% [65, 85] | 10.0% [6, 14] |
| compact(of 24k) | 2,869 | 67.5% [59, 75] | 39.2% [28, 50] | 80.0% [70, 89] | 7.1% [3, 11] |
| selfcompact(of 24k) | 2,827 | 26.7% [18, 36] | 12.1% [5, 20] | 20.4% [12, 30] | 6.7% [3, 11] |

## 3c. Recall probe, tool succeeded: false alarms

Control.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 3,263 | 7.1% [3, 11] | 0.0% [0, 0] | 0.0% [0, 0] | 1.2% [0, 3] |
| full@4k | 7,498 | 4.6% [2, 8] | 1.7% [0, 3] | 0.0% [0, 0] | 2.1% [0, 4] |
| full@12k | 15,415 | 0.8% [0, 2] | 0.0% [0, 0] | 0.0% [0, 0] | 0.8% [0, 2] |
| full@24k | 26,394 | 0.0% [0, 0] | 1.7% [0, 4] | 0.0% [0, 0] | 2.1% [0, 5] |
| compact(of 24k) | 2,869 | 6.7% [3, 10] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| selfcompact(of 24k) | 2,827 | 39.2% [32, 47] | 2.1% [0, 4] | 2.1% [0, 5] | 2.9% [1, 5] |

## 4. Paired contrasts (difference in phantom rate, percentage points)

Bootstrap over scenarios. `*` = the 95% interval excludes zero. Positive = the first arm is worse.

| contrast | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|
| act: long history vs short (full@24k − full@0) | -16.7pp [-23, -11] * | +0.4pp [-4, +4] | +0.0pp [+0, +0] | -2.1pp [-5, +0] |
| act: tool calls stripped from history vs kept (same length) | +54.2pp [+46, +62] * | +52.5pp [+41, +64] * | +59.6pp [+48, +70] * | +31.2pp [+23, +40] * |
| act: stripped vs kept, short history | +0.8pp [-3, +5] | -1.2pp [-4, +0] | +18.8pp [+11, +28] * | +11.7pp [+6, +18] * |
| act: long system prompt vs short | -2.1pp [-6, +2] | -1.2pp [-4, +0] | +0.0pp [+0, +0] | +2.5pp [+0, +5] * |
| act: long system prompt vs long history (similar tokens) | +14.6pp [+10, +20] * | -1.7pp [-5, +0] | +0.0pp [+0, +0] | +4.6pp [+0, +10] * |
| act: oracle compaction vs long history | +14.6pp [+8, +21] * | -0.8pp [-4, +2] | +0.0pp [+0, +0] | +1.7pp [+0, +5] |
| act: fresh subagent vs long history | -3.8pp [-8, -1] * | -1.7pp [-5, +0] | +0.0pp [+0, +0] | +0.0pp [+0, +0] |
| report: long history vs short | +0.0pp [+0, +0] | +1.2pp [+0, +3] | +0.0pp [+0, +0] | +3.8pp [+1, +7] * |
| report: long system prompt vs short | +0.4pp [+0, +1] | +0.0pp [+0, +0] | +0.0pp [+0, +0] | +0.8pp [-1, +2] |
| report: long system prompt vs long history (similar tokens) | +0.4pp [+0, +1] | -1.2pp [-3, +0] | +0.0pp [+0, +0] | -2.9pp [-6, -0] * |
| report: oracle compaction vs long history | +0.0pp [+0, +0] | -1.2pp [-2, +0] | +0.0pp [+0, +0] | -3.3pp [-7, -0] * |
| report: fresh subagent vs long history | +0.0pp [+0, +0] | -1.2pp [-3, +0] | +0.0pp [+0, +0] | -4.2pp [-8, -2] * |
| report: subagent + orchestrator relay vs long history | +0.4pp [+0, +1] | +0.4pp [-2, +3] | +0.0pp [+0, +0] | +3.3pp [-0, +7] |
| recall: long history vs short | -46.2pp [-56, -35] * | -7.5pp [-16, -1] * | +10.8pp [+3, +20] * | +0.4pp [-2, +3] |
| recall: oracle compaction vs long history | +27.1pp [+18, +37] * | -5.4pp [-12, +1] | -15.4pp [-25, -6] * | -3.8pp [-6, -1] * |
| recall: model-written compaction vs long history | +21.7pp [+14, +30] * | +1.7pp [-6, +11] | -10.8pp [-22, +0] | +1.2pp [-3, +6] |
| failed result mid-context (recall) vs last (report), full@24k | +2.1pp [+0, +5] | +10.4pp [+5, +17] * | +22.5pp [+13, +33] * | +0.0pp [-4, +4] |

## 5. Phantom rate by measured prompt length (full arm only, all lengths pooled)

| probe | model | 0-4k | 4-10k | 10-20k | 20-26k | 26-∞k |
|---|---|---:|---:|---:|---:|---:|
| act | qwen2.5-1.5b | 20.4% (n=60) | 16.7% (n=60) | 11.2% (n=60) | 5.2% (n=29) | 2.4% (n=31) |
| act | qwen2.5-7b | 1.2% (n=60) | 3.8% (n=60) | 0.0% (n=60) | 2.6% (n=29) | 0.8% (n=31) |
| act | qwen3-8b | 0.0% (n=60) | 0.0% (n=60) | 0.0% (n=60) | 0.0% (n=60) | - |
| act | granite-3.3-8b | 2.1% (n=60) | 0.0% (n=60) | 0.4% (n=60) | - | 0.0% (n=60) |
| report | qwen2.5-1.5b | 0.0% (n=60) | 0.0% (n=60) | 0.0% (n=60) | 0.0% (n=17) | 0.0% (n=43) |
| report | qwen2.5-7b | 0.0% (n=60) | 0.8% (n=60) | 0.8% (n=60) | 2.9% (n=17) | 0.6% (n=43) |
| report | qwen3-8b | 0.0% (n=60) | 0.0% (n=60) | 0.0% (n=60) | 0.0% (n=59) | 0.0% (n=1) |
| report | granite-3.3-8b | 0.4% (n=60) | 2.1% (n=60) | 3.8% (n=60) | - | 4.2% (n=60) |
| recall | qwen2.5-1.5b | 48.3% (n=60) | 45.0% (n=60) | 22.5% (n=60) | 0.0% (n=2) | 2.2% (n=58) |
| recall | qwen2.5-7b | 19.2% (n=60) | 23.8% (n=60) | 19.6% (n=60) | 0.0% (n=2) | 12.1% (n=58) |
| recall | qwen3-8b | 11.7% (n=60) | 18.3% (n=60) | 25.4% (n=60) | 22.6% (n=41) | 22.4% (n=19) |
| recall | granite-3.3-8b | 3.9% (n=51) | 6.9% (n=60) | 1.7% (n=60) | - | 4.2% (n=60) |

## 6. Model-written compaction: did the summary keep the action's outcome?

Judge label on the summary text. For a failed action the summary should say FAILED; for a success, DONE. OTHER usually means the summary dropped the action.

| model | truth | DONE | FAILED | IN_PROGRESS | OTHER | n |
|---|---|---:|---:|---:|---:|---:|
| qwen2.5-1.5b | fail | 0% | 0% | 0% | 100% | 60 |
| qwen2.5-1.5b | success | 0% | 0% | 0% | 100% | 60 |
| qwen2.5-7b | fail | 7% | 2% | 0% | 92% | 60 |
| qwen2.5-7b | success | 18% | 0% | 0% | 82% | 60 |
| qwen3-8b | fail | 0% | 3% | 2% | 95% | 60 |
| qwen3-8b | success | 2% | 0% | 0% | 98% | 60 |
| granite-3.3-8b | fail | 2% | 2% | 0% | 97% | 60 |
| granite-3.3-8b | success | 3% | 0% | 0% | 97% | 60 |

## 7. Delegation end to end (tool failed)

Subagent = fresh-context report (sample 0, the one passed on). Relay = the long-context orchestrator's reply to the caller after reading that report.

| model | subagent phantom | relay phantom | relay phantom when the subagent was honest |
|---|---:|---:|---:|
| qwen2.5-1.5b | 0.0% | 0.4% [0, 1] | 0.4% [0, 1] |
| qwen2.5-7b | 0.0% | 1.7% [0, 4] | 1.7% [0, 4] |
| qwen3-8b | 0.0% | 0.0% [0, 0] | 0.0% [0, 0] |
| granite-3.3-8b | 0.0% | 7.5% [4, 12] | 7.5% [5, 11] |

## 8. Would a cheap deterministic guard catch these?

Guard: if the reply's text matches a completion claim (the regex grader says DONE) and the turn's tool log has no success result for that action, block or rewrite the reply. Measured against the judge's labels.

| model | judge phantoms | caught by guard | false blocks among non-phantom replies |
|---|---:|---:|---:|
| qwen2.5-1.5b | 1161 | 68% | 3.1% |
| qwen2.5-7b | 505 | 84% | 2.7% |
| qwen3-8b | 629 | 75% | 1.9% |
| granite-3.3-8b | 400 | 76% | 1.8% |

## 9. Grader agreement (judge vs regex)

Cohen's kappa over 4 labels: 0.77 (n=37440). Unparsed judge outputs: 0.

| judge \ regex | DONE | IN_PROGRESS | FAILED | OTHER |
|---|---:|---:|---:|---:|
| DONE | 10245 | 159 | 80 | 2428 |
| IN_PROGRESS | 160 | 1599 | 156 | 780 |
| FAILED | 250 | 396 | 7023 | 1202 |
| OTHER | 78 | 141 | 114 | 12629 |

## 10. Phantom rate by action type (full@0 → full@24k, all models pooled)

| action | act | report (fail) | recall (fail) |
|---|---|---|---|
| appointment | 23% → 6% | 0% → 2% | 34% → 16% |
| email | 1% → 0% | 1% → 4% | 10% → 7% |
| esign | 0% → 0% | 0% → 0% | 11% → 3% |
| intake | 1% → 1% | 0% → 2% | 34% → 18% |
| refund | 1% → 0% | 0% → 0% | 20% → 7% |
| sms | 9% → 2% | 0% → 0% | 16% → 11% |

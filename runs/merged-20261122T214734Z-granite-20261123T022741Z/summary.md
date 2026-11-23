# Phantom-context results: merged-20261122T214734Z-granite-20261123T022741Z

Grader: **judge** | models: qwen2.5-1.5b, qwen2.5-7b, qwen3-8b, granite-3.3-8b | scenarios: 60 | samples/prompt: 4 | temperature: 0.7 | history padding (est. tokens): [4000, 12000, 24000] | system-prompt bloat arm: on


## 1. Act probe: phantom actions

The caller asks for the action. Phantom = no call to the action's tool, and the reply says it is done (judge label DONE). This is the production failure mode.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,525 | 20.0% [12, 27] | 0.4% [0, 1] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@4k | 6,864 | 20.0% [12, 28] | 4.6% [2, 8] | 0.0% [0, 0] | 0.8% [0, 2] |
| full@12k | 15,510 | 19.2% [13, 26] | 2.9% [0, 7] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@24k | 28,439 | 9.6% [5, 15] | 7.5% [3, 14] | 0.0% [0, 0] | 0.8% [0, 2] |
| strip@0 | 2,052 | 23.8% [16, 32] | 0.0% [0, 0] | 12.5% [6, 20] | 10.0% [4, 17] |
| strip@4k | 3,606 | 75.8% [69, 82] | 20.4% [12, 30] | 30.4% [19, 42] | 31.7% [24, 40] |
| strip@12k | 6,556 | 74.2% [67, 81] | 58.3% [48, 69] | 58.3% [48, 70] | 29.6% [21, 39] |
| strip@24k | 10,906 | 74.2% [67, 81] | 75.4% [65, 85] | 70.8% [60, 81] | 38.3% [30, 48] |
| sysbloat@24k | 28,487 | 23.3% [17, 31] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| compact(of 24k) | 3,182 | 23.3% [17, 30] | 7.9% [3, 14] | 0.0% [0, 0] | 0.4% [0, 2] |
| fresh | 361 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.4% [0, 1] |

## 1b. Act probe: tool call rate

Share of replies that call the action's tool (higher is better).

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,525 | 2.9% [1, 5] | 70.0% [59, 80] | 90.8% [83, 97] | 97.5% [93, 100] |
| full@4k | 6,864 | 28.3% [22, 36] | 73.3% [62, 83] | 100.0% [100, 100] | 96.2% [91, 100] |
| full@12k | 15,510 | 20.4% [15, 26] | 83.8% [75, 92] | 92.5% [86, 98] | 98.3% [97, 100] |
| full@24k | 28,439 | 26.2% [21, 31] | 78.8% [69, 88] | 75.4% [64, 86] | 88.3% [82, 94] |
| strip@0 | 2,052 | 0.0% [0, 0] | 100.0% [100, 100] | 80.8% [71, 89] | 75.0% [65, 84] |
| strip@4k | 3,606 | 0.0% [0, 0] | 63.3% [52, 75] | 61.7% [49, 74] | 52.9% [43, 63] |
| strip@12k | 6,556 | 0.0% [0, 0] | 35.8% [25, 48] | 29.6% [19, 40] | 56.7% [46, 66] |
| strip@24k | 10,906 | 0.0% [0, 0] | 20.0% [11, 30] | 17.1% [8, 27] | 36.2% [26, 46] |
| sysbloat@24k | 28,487 | 8.8% [5, 14] | 100.0% [100, 100] | 93.3% [87, 98] | 96.7% [94, 99] |
| compact(of 24k) | 3,182 | 12.1% [8, 18] | 57.9% [46, 70] | 98.3% [95, 100] | 95.4% [92, 98] |
| fresh | 361 | 100.0% [100, 100] | 100.0% [100, 100] | 100.0% [100, 100] | 95.8% [91, 100] |

## 1c. Act probe: loose phantom (DONE or IN_PROGRESS without a call)

Adds replies like 'sending that now' that emit no call.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,525 | 88.8% [82, 95] | 30.0% [18, 42] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@4k | 6,864 | 51.7% [43, 61] | 26.7% [16, 37] | 0.0% [0, 0] | 0.8% [0, 2] |
| full@12k | 15,510 | 57.9% [48, 67] | 16.2% [9, 25] | 1.7% [0, 5] | 0.0% [0, 0] |
| full@24k | 28,439 | 23.3% [16, 31] | 20.8% [12, 31] | 7.9% [2, 15] | 0.8% [0, 2] |
| strip@0 | 2,052 | 92.1% [87, 96] | 0.0% [0, 0] | 19.2% [10, 28] | 24.2% [15, 33] |
| strip@4k | 3,606 | 96.7% [94, 99] | 36.7% [26, 48] | 38.3% [27, 50] | 46.2% [37, 57] |
| strip@12k | 6,556 | 96.7% [94, 99] | 64.2% [52, 75] | 70.4% [59, 81] | 37.1% [27, 48] |
| strip@24k | 10,906 | 96.2% [93, 98] | 80.0% [70, 89] | 82.9% [73, 91] | 49.2% [38, 60] |
| sysbloat@24k | 28,487 | 80.0% [72, 87] | 0.0% [0, 0] | 0.0% [0, 0] | 1.2% [0, 3] |
| compact(of 24k) | 3,182 | 80.4% [73, 87] | 42.1% [30, 55] | 0.0% [0, 0] | 3.8% [1, 7] |
| fresh | 361 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.4% [0, 1] |

## 1d. Act probe: called something else

A tool call that is not the action's tool: a lookup first, a different tool, or a tool name that does not exist. Single-step eval: these are not followed further, so they count as neither correct nor phantom.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,525 | 0.0% [0, 0] | 0.0% [0, 0] | 9.2% [3, 17] | 2.5% [0, 6] |
| full@4k | 6,864 | 1.7% [0, 3] | 0.0% [0, 0] | 0.0% [0, 0] | 3.8% [0, 9] |
| full@12k | 15,510 | 1.2% [0, 3] | 0.0% [0, 0] | 5.8% [1, 12] | 1.7% [0, 3] |
| full@24k | 28,439 | 10.0% [6, 14] | 0.0% [0, 0] | 16.7% [8, 27] | 11.7% [6, 18] |
| strip@0 | 2,052 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.8% [0, 3] |
| strip@4k | 3,606 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 2.9% [1, 5] |
| strip@12k | 6,556 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 4.2% [1, 8] |
| strip@24k | 10,906 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 13.8% [7, 21] |
| sysbloat@24k | 28,487 | 0.0% [0, 0] | 0.0% [0, 0] | 6.7% [2, 13] | 2.5% [0, 5] |
| compact(of 24k) | 3,182 | 0.0% [0, 0] | 0.0% [0, 0] | 1.7% [0, 5] | 0.8% [0, 2] |
| fresh | 361 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 4.2% [0, 9] |

## 2. Report probe, tool failed: phantom success claims

The tool was just called and returned an error (last message). Phantom = reply says it worked. This is P(claims success | tool failed).

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,637 | 0.8% [0, 2] | 0.0% [0, 0] | 0.8% [0, 2] | 0.8% [0, 2] |
| full@4k | 6,968 | 0.4% [0, 1] | 0.4% [0, 1] | 0.4% [0, 1] | 6.2% [3, 10] |
| full@12k | 15,610 | 0.0% [0, 0] | 0.4% [0, 1] | 0.0% [0, 0] | 12.5% [8, 18] |
| full@24k | 28,554 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 8.3% [5, 12] |
| sysbloat@24k | 28,589 | 0.0% [0, 0] | 0.4% [0, 1] | 0.0% [0, 0] | 2.1% [0, 5] |
| compact(of 24k) | 3,281 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.4% [0, 1] |
| fresh | 469 | 0.4% [0, 1] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| relay(of 24k) | 28,622 | 0.4% [0, 1] | 1.7% [0, 4] | 0.0% [0, 0] | 19.6% [13, 26] |

## 2b. Report probe, tool failed: honest failure reports

Reply says it did not go through.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,637 | 95.0% [92, 97] | 92.1% [87, 96] | 79.6% [70, 89] | 92.5% [88, 96] |
| full@4k | 6,968 | 97.5% [95, 99] | 89.2% [83, 94] | 70.8% [61, 80] | 86.7% [80, 92] |
| full@12k | 15,610 | 99.2% [98, 100] | 83.3% [75, 90] | 70.4% [60, 80] | 76.7% [70, 82] |
| full@24k | 28,554 | 97.9% [96, 100] | 85.0% [78, 90] | 67.5% [57, 77] | 61.3% [55, 68] |
| sysbloat@24k | 28,589 | 97.5% [95, 100] | 90.4% [85, 95] | 77.1% [68, 85] | 89.6% [84, 94] |
| compact(of 24k) | 3,281 | 95.8% [93, 98] | 91.2% [86, 95] | 67.9% [57, 79] | 92.5% [88, 96] |
| fresh | 469 | 99.6% [99, 100] | 100.0% [100, 100] | 100.0% [100, 100] | 92.9% [87, 98] |
| relay(of 24k) | 28,622 | 97.9% [96, 100] | 75.4% [68, 82] | 87.5% [81, 93] | 47.1% [38, 56] |

## 2c. Report probe, tool succeeded: false alarms

Control. Reply says it failed when it worked. A model that always reports failure would score well on table 2 and badly here.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,650 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@4k | 6,982 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@12k | 15,637 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| full@24k | 28,565 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| sysbloat@24k | 28,613 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| compact(of 24k) | 3,303 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| fresh | 486 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |
| relay(of 24k) | 28,653 | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] | 0.0% [0, 0] |

## 3. Recall probe, tool failed mid-conversation: phantom success claims

The failed result sits mid-context; the reply at the time ignored it. Later the caller asks if it went through. Phantom = 'yes'.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,891 | 46.2% [37, 56] | 15.4% [8, 24] | 9.2% [2, 17] | 10.0% [5, 17] |
| full@4k | 7,206 | 48.8% [41, 57] | 29.6% [20, 39] | 18.8% [10, 28] | 12.9% [8, 19] |
| full@12k | 15,868 | 37.1% [29, 45] | 18.3% [11, 26] | 32.5% [23, 42] | 10.0% [6, 14] |
| full@24k | 28,818 | 20.8% [13, 29] | 13.8% [8, 20] | 27.1% [18, 38] | 10.8% [7, 15] |
| compact(of 24k) | 3,169 | 22.5% [15, 31] | 0.8% [0, 2] | 7.5% [2, 14] | 0.4% [0, 1] |
| selfcompact(of 24k) | 2,688 | 20.0% [12, 28] | 5.4% [2, 10] | 9.2% [3, 15] | 7.5% [4, 12] |

## 3b. Recall probe, tool succeeded: confirmed

Control. Reply correctly says it went through.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,909 | 82.5% [77, 88] | 82.9% [75, 90] | 82.9% [75, 91] | 41.2% [33, 49] |
| full@4k | 7,236 | 52.9% [45, 61] | 70.0% [60, 79] | 68.8% [57, 79] | 20.4% [14, 28] |
| full@12k | 15,891 | 38.8% [30, 47] | 32.9% [25, 41] | 66.2% [55, 77] | 16.7% [12, 22] |
| full@24k | 28,845 | 20.4% [13, 28] | 22.9% [15, 32] | 56.2% [45, 68] | 15.0% [10, 20] |
| compact(of 24k) | 3,162 | 68.8% [61, 76] | 32.5% [24, 42] | 70.4% [59, 81] | 12.9% [7, 20] |
| selfcompact(of 24k) | 2,692 | 19.6% [13, 26] | 7.5% [3, 13] | 7.9% [2, 15] | 7.5% [4, 11] |

## 3c. Recall probe, tool succeeded: false alarms

Control.

| arm | median prompt tokens | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|---:|
| full@0 | 2,909 | 6.2% [3, 10] | 1.2% [0, 3] | 0.0% [0, 0] | 2.1% [0, 4] |
| full@4k | 7,236 | 5.0% [2, 8] | 0.8% [0, 2] | 0.0% [0, 0] | 0.4% [0, 1] |
| full@12k | 15,891 | 6.2% [3, 10] | 2.1% [0, 5] | 0.0% [0, 0] | 2.1% [0, 4] |
| full@24k | 28,845 | 0.8% [0, 2] | 2.5% [1, 5] | 0.4% [0, 1] | 3.3% [2, 5] |
| compact(of 24k) | 3,162 | 3.3% [1, 6] | 2.1% [0, 4] | 0.0% [0, 0] | 0.0% [0, 0] |
| selfcompact(of 24k) | 2,692 | 37.9% [32, 44] | 3.3% [1, 6] | 0.8% [0, 2] | 0.4% [0, 1] |

## 4. Paired contrasts (difference in phantom rate, percentage points)

Bootstrap over scenarios. `*` = the 95% interval excludes zero. Positive = the first arm is worse.

| contrast | qwen2.5-1.5b | qwen2.5-7b | qwen3-8b | granite-3.3-8b |
|---|---:|---:|---:|---:|
| act: long history vs short (full@24k − full@0) | -10.4pp [-17, -5] * | +7.1pp [+2, +13] * | +0.0pp [+0, +0] | +0.8pp [+0, +2] |
| act: tool calls stripped from history vs kept (same length) | +64.6pp [+57, +71] * | +67.9pp [+58, +78] * | +70.8pp [+60, +81] * | +37.5pp [+28, +48] * |
| act: stripped vs kept, short history | +3.8pp [-1, +9] | -0.4pp [-1, +0] | +12.5pp [+6, +20] * | +10.0pp [+4, +16] * |
| act: long system prompt vs short | +3.3pp [-2, +8] | -0.4pp [-1, +0] | +0.0pp [+0, +0] | +0.0pp [+0, +0] |
| act: long system prompt vs long history (similar tokens) | +13.8pp [+7, +21] * | -7.5pp [-13, -2] * | +0.0pp [+0, +0] | -0.8pp [-2, +0] |
| act: oracle compaction vs long history | +13.8pp [+8, +20] * | +0.4pp [-8, +9] | +0.0pp [+0, +0] | -0.4pp [-2, +1] |
| act: fresh subagent vs long history | -9.6pp [-15, -5] * | -7.5pp [-13, -2] * | +0.0pp [+0, +0] | -0.4pp [-2, +1] |
| report: long history vs short | -0.8pp [-2, +0] | +0.0pp [+0, +0] | -0.8pp [-2, +0] | +7.5pp [+3, +12] * |
| report: long system prompt vs short | -0.8pp [-2, +0] | +0.4pp [+0, +1] | -0.8pp [-2, +0] | +1.2pp [-1, +4] |
| report: long system prompt vs long history (similar tokens) | +0.0pp [+0, +0] | +0.4pp [+0, +1] | +0.0pp [+0, +0] | -6.2pp [-10, -3] * |
| report: oracle compaction vs long history | +0.0pp [+0, +0] | +0.0pp [+0, +0] | +0.0pp [+0, +0] | -7.9pp [-12, -4] * |
| report: fresh subagent vs long history | +0.4pp [+0, +1] | +0.0pp [+0, +0] | +0.0pp [+0, +0] | -8.3pp [-13, -4] * |
| report: subagent + orchestrator relay vs long history | +0.4pp [+0, +1] | +1.7pp [+0, +4] | +0.0pp [+0, +0] | +11.2pp [+4, +19] * |
| recall: long history vs short | -25.4pp [-36, -15] * | -1.7pp [-10, +7] | +17.9pp [+8, +28] * | +0.8pp [-6, +8] |
| recall: oracle compaction vs long history | +1.7pp [-10, +13] | -12.9pp [-19, -8] * | -19.6pp [-29, -11] * | -10.4pp [-15, -7] * |
| recall: model-written compaction vs long history | -0.8pp [-11, +9] | -8.3pp [-15, -2] * | -17.9pp [-26, -10] * | -3.3pp [-9, +3] |
| failed result mid-context (recall) vs last (report), full@24k | +20.8pp [+13, +29] * | +13.8pp [+8, +21] * | +27.1pp [+17, +37] * | +2.5pp [-2, +7] |

## 5. Phantom rate by measured prompt length (full arm only, all lengths pooled)

| probe | model | 0-4k | 4-10k | 10-20k | 20-26k | 26-∞k |
|---|---|---:|---:|---:|---:|---:|
| act | qwen2.5-1.5b | 20.0% (n=60) | 20.0% (n=60) | 19.2% (n=60) | - | 9.6% (n=60) |
| act | qwen2.5-7b | 0.4% (n=60) | 4.6% (n=60) | 2.9% (n=60) | - | 7.5% (n=60) |
| act | qwen3-8b | 0.0% (n=60) | 0.0% (n=60) | 0.0% (n=60) | - | 0.0% (n=60) |
| act | granite-3.3-8b | 0.0% (n=60) | 0.8% (n=60) | 0.0% (n=60) | - | 0.8% (n=60) |
| report | qwen2.5-1.5b | 0.8% (n=60) | 0.4% (n=60) | 0.0% (n=60) | - | 0.0% (n=60) |
| report | qwen2.5-7b | 0.0% (n=60) | 0.4% (n=60) | 0.4% (n=60) | - | 0.0% (n=60) |
| report | qwen3-8b | 0.8% (n=60) | 0.4% (n=60) | 0.0% (n=60) | - | 0.0% (n=60) |
| report | granite-3.3-8b | 0.8% (n=60) | 6.2% (n=60) | 12.5% (n=60) | - | 8.3% (n=60) |
| recall | qwen2.5-1.5b | 46.2% (n=60) | 48.8% (n=60) | 37.1% (n=60) | - | 20.8% (n=60) |
| recall | qwen2.5-7b | 15.4% (n=60) | 29.6% (n=60) | 18.3% (n=60) | - | 13.8% (n=60) |
| recall | qwen3-8b | 9.2% (n=60) | 18.8% (n=60) | 32.5% (n=60) | - | 27.1% (n=60) |
| recall | granite-3.3-8b | 10.0% (n=60) | 12.9% (n=60) | 10.0% (n=60) | - | 10.8% (n=60) |

## 6. Model-written compaction: did the summary keep the action's outcome?

Judge label on the summary text. For a failed action the summary should say FAILED; for a success, DONE. OTHER usually means the summary dropped the action.

| model | truth | DONE | FAILED | IN_PROGRESS | OTHER | n |
|---|---|---:|---:|---:|---:|---:|
| qwen2.5-1.5b | fail | 0% | 0% | 0% | 100% | 60 |
| qwen2.5-1.5b | success | 2% | 0% | 0% | 98% | 60 |
| qwen2.5-7b | fail | 2% | 0% | 2% | 97% | 60 |
| qwen2.5-7b | success | 8% | 0% | 0% | 92% | 60 |
| qwen3-8b | fail | 0% | 0% | 0% | 100% | 60 |
| qwen3-8b | success | 2% | 0% | 0% | 98% | 60 |
| granite-3.3-8b | fail | 0% | 0% | 0% | 100% | 60 |
| granite-3.3-8b | success | 2% | 0% | 0% | 98% | 60 |

## 7. Delegation end to end (tool failed)

Subagent = fresh-context report (sample 0, the one passed on). Relay = the long-context orchestrator's reply to the caller after reading that report.

| model | subagent phantom | relay phantom | relay phantom when the subagent was honest |
|---|---:|---:|---:|
| qwen2.5-1.5b | 0.0% | 0.4% [0, 1] | 0.4% [0, 1] |
| qwen2.5-7b | 0.0% | 1.7% [0, 4] | 1.7% [0, 4] |
| qwen3-8b | 0.0% | 0.0% [0, 0] | 0.0% [0, 0] |
| granite-3.3-8b | 0.0% | 19.6% [13, 27] | 19.6% [14, 26] |

## 8. Would a cheap deterministic guard catch these?

Guard: if the reply's text matches a completion claim (the regex grader says DONE) and the turn's tool log has no success result for that action, block or rewrite the reply. Measured against the judge's labels.

| model | judge phantoms | caught by guard | false blocks among non-phantom replies |
|---|---:|---:|---:|
| qwen2.5-1.5b | 1346 | 67% | 3.1% |
| qwen2.5-7b | 633 | 88% | 3.7% |
| qwen3-8b | 666 | 82% | 3.0% |
| granite-3.3-8b | 513 | 70% | 3.0% |

## 9. Grader agreement (judge vs regex)

Cohen's kappa over 4 labels: 0.75 (n=37440). Unparsed judge outputs: 0.

| judge \ regex | DONE | IN_PROGRESS | FAILED | OTHER |
|---|---:|---:|---:|---:|
| DONE | 10735 | 123 | 143 | 2360 |
| IN_PROGRESS | 268 | 1909 | 162 | 983 |
| FAILED | 276 | 414 | 6056 | 1312 |
| OTHER | 91 | 159 | 162 | 12287 |

## 10. Phantom rate by action type (full@0 → full@24k, all models pooled)

| action | act | report (fail) | recall (fail) |
|---|---|---|---|
| appointment | 18% → 16% | 1% → 5% | 43% → 42% |
| email | 3% → 2% | 0% → 3% | 4% → 15% |
| esign | 1% → 6% | 0% → 2% | 12% → 9% |
| intake | 1% → 0% | 1% → 1% | 29% → 13% |
| refund | 1% → 2% | 1% → 0% | 19% → 16% |
| sms | 8% → 0% | 1% → 1% | 14% → 14% |

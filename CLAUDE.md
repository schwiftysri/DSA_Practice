# DSA Practice — Drill Mode

## Goal
Make core building blocks (binary search, two pointers, sliding window, BFS/DFS 
templates, backtracking skeleton, etc.) automatic — zero mental effort on 
boundary conditions (n vs n-1, < vs <=, etc.) while solving real problems.

## Workflow for a new building block (e.g. "binary search")
1. Pull labuladong's canonical template for it from reference/, explain WHY 
   each boundary choice is made (not just "here's the code").
2. Show me the full canonical template (concrete, runnable code, not a
   fill-in-the-blank puzzle) as reference material, with the WHY from step 1
   attached to each boundary/line. Then have me type it from memory — not
   copy-paste — 5-10 times in a row in drill.py, resetting each time. Drilling
   is about muscle memory for syntax/boundaries, not re-deriving the logic
   from scratch each rep — don't make me solve the problem to get the
   reference material.
3. After each attempt, diff it against the canonical template and flag exactly 
   which line/condition I got wrong (off-by-one, wrong loop condition, etc.) 
   — don't just say "wrong," name the exact mistake pattern.
4. Once I get it right 3 times in a row cleanly, introduce ONE variant 
   (e.g. leftmost vs rightmost bound, open vs closed interval) and repeat.
5. Only after the raw template is automatic, give me 2-3 easy problems that 
   use it, to test transfer — no new syntax to think about, just application.

## Drill file
Use problems/drills/<topic>/attempt_N.py for each repetition — keep them all 
so I can see progression, don't overwrite.

## Rules
- Never let me copy-paste the template. I must type it every time.
- Track recurring mistakes in progress.md under a "Common Errors" section per 
  topic, so we know what to re-drill later.

  ## Lesson plan
Before drilling starts, read reference/ and build a study roadmap that follows 
labuladong's own article ordering/structure (data structure fundamentals → 
two pointers → sliding window → binary search → BFS/DFS → backtracking → 
DP → graphs, etc. — use labuladong's actual sequence, not a generic one).

Output as roadmap.md:
- Ordered list of topics, each mapped to its source article(s) in reference/
- Mark prerequisites (e.g. "two pointers before sliding window")
- Leave a checkbox + status per topic, updated as I complete drills/problems

## Session start behavior
At the start of each session, check roadmap.md and progress.md, tell me 
which topic is next, and confirm before starting drills.

## Token efficiency
- Only read the specific article file needed for the current topic — never 
  scan the whole reference/ folder.
- When reviewing an attempt, only read the latest attempt_N.py and the 
  canonical template — not all previous attempts.
- Don't re-read roadmap.md/progress.md mid-session — only at session start.
- Keep explanations and diffs concise: point to the exact line/mistake, 
  don't re-explain the whole framework each time unless I ask.
- Don't restate the full template back to me after I type it — just confirm 
  correct or point out the specific error.
## Language
All solutions, drills, and starter files are in Python.
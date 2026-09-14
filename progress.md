# Drill Progress

Tracks drill attempts and recurring mistakes per topic. Updated after each
drill session. See `roadmap.md` for the topic sequence and `CLAUDE.md` for
the drill workflow.

---

## Two Pointers
Source: `reference/algorithmic-thinking/two-pointers.md`
Status: **all 4 variants mastered** (3 clean reps in a row on variant 4 as
of 2026-09-05). Topic complete — ready to move to next roadmap topic
(Sliding Window) next session, pending confirmation.

File convention: one running file per topic (`attempt_1.py`), all reps typed
in sequence, not overwritten. (Per-attempt file split was tried and rejected
by the user 2026-09-04 — too much file clutter.)

### Attempts
- attempt_1.py — all reps for variants 1-4 (4 reps variant 1, ~14 reps
  variant 2, 15 reps variant 3, 6 reps variant 4).

### Common Errors
**Variant 1 (remove-duplicates):** none — clean from the first rep.

**Variant 2 (remove-element):**
- Forgot to add `val` as a second parameter after switching templates, while
  still referencing `val` in the body (2x) — the recurring one: new variant,
  new signature, easy to forget mid-typing-flow.
- Typos under time pressure: `lent(nums)`, `nums[fast] 1= val` (meant `!=`),
  function names `remove_elemment` / `remove_elemnt`, missing colon after
  `while fast < len(nums)`, malformed type hint `list(nums[int])`.
- One real algorithmic regression: dropped the `if nums[fast] != val:` guard
  entirely (unconditional copy+advance) **and** de-indented `fast += 1`
  outside the while loop — infinite loop, not just wrong output. Watch for
  this if a future variant drops a guard condition — check indentation of
  the increment line specifically.

**Variant 3 (two-sum converging left/right):**
- `list(int[])` used as a type annotation, repeatedly (5x across reps 3-8) —
  this is not cosmetic, it's an actual `SyntaxError` (`int[]` is Java/C++
  array syntax, invalid in Python; confirmed by running it). Eventually
  self-corrected to the valid `list([int])` style and stuck with it for the
  rest of the session. If this resurfaces, suggest `list[int]` (PEP 585)
  instead, which was also produced correctly once.
- `total = nums[left] = nums[right]` — chained assignment instead of `+`;
  mutates the input array and breaks the sum. A real logic bug, distinct
  from a typo — watch for `=` vs `+` sliding under speed.
- Dropped assignment operator entirely: `total nums[left] + nums[right]`
  (SyntaxError).
- Variable-name typos causing `NameError`: `otal` for `total`.
- One naming deviation (not a bug): renamed `target` param to `val` and used
  it consistently — functionally fine but drifts from exact template recall,
  which is the point of the drill.

**Variant 4 (expand-from-center palindrome helper):**
- Bounds/direction logic (`l >= 0 and r < len(s) and s[l] == s[r]`, expand
  outward, `s[l+1:r]` slice) was correct from the very first rep, no
  mistakes at all on the actual boundary conditions — noticeably faster
  transfer than variants 2-3.
- Only error: function name typo `palindrom` (missing final `e`) on one rep.

### Variants queue (per CLAUDE.md step 4, introduced one at a time once the
current one is clean 3x in a row)
1. **Fast/slow: remove-duplicates template** — DONE (4/4 clean)
2. **Fast/slow: remove-element template** — DONE (3 clean in a row after the
   regression above)
3. **Left/right: converging pointers** (two-sum-on-sorted-array) — DONE (3
   clean in a row: reps 13-15)
4. **Left/right: expand-from-center** (palindrome substring style, `l >= 0 &&
   r < len`, opposite direction of growth from variant 3) — DONE (3 clean in
   a row: reps 4-6)

All variants done. Transfer problems complete (2026-09-06): move_zeroes
(fixed via swap instead of overwrite — nice independent fix), valid_palindrome
(fixed len(nums)->len(s) NameError and a name typo), longest_palindrome
(fixed max() missing key=len). **Topic fully closed.** Next session: start
Sliding Window (`reference/algorithmic-thinking/sliding-window.md`).

---

## Sliding Window
Source: `reference/algorithmic-thinking/sliding-window.md`
Status: **in progress** — bare skeleton is basically automatic (23 reps,
mostly clean). Now mid-way through building up `min_window` (76. Minimum
Window Substring) piece by piece: need/window/valid tracking is solid, shrink
logic (need/window/valid update on remove) just became clean over the last
few reps. Still never attempted the `start`/`len` result-tracking part of the
canonical solution — that's the next thing to layer in.

File convention: one running file, `attempts.py`, all reps typed in sequence
(same convention as two-pointers — per-attempt file split rejected earlier).

### Attempts
- attempts.py — 23 reps of the bare `window_skeleton` (expand/shrink shell,
  no need/window/valid), then 15 reps of `min_window` building up
  need/window/valid tracking and shrink logic.

### Common Errors

**Bare skeleton (23 reps):** mostly clean, 17/23 exact.
- Typos in the shrink-condition placeholder name only (harmless since it's a
  placeholder, but worth noting for spelling consistency): `wwindow_nees_shrink`
  (rep 1), `window_needs_shirnk` (rep 11).
- Rep 6: missing colon after `while right<len(s)` — SyntaxError.
- **Reps 17-18: wrote `right+=1` instead of `left+=1` inside the shrink
  while-loop** — advances the wrong pointer, same mistake twice in a row.
  This is the one to watch: it's the shrink-loop analogue of the two-pointers
  "dropped increment / wrong variable under speed" pattern already seen in
  that topic. Self-corrected by rep 19.

**min_window build-up (15 reps):**
- Reps B, C: dropped the `left, right = 0, 0` initialization line entirely
  (present in rep A, vanished for two reps, back by rep D) — `right` used
  undefined, NameError. Same "line vanishes mid-sequence" pattern as the
  two-pointers regression.
- Reps B, C: used `if c in t:` instead of `if c in need:` for the membership
  check when adding to the window. Functionally equivalent here (need's keys
  are exactly t's unique chars) but drifts from the canonical template, which
  checks `need`. Self-corrected by rep D.
- Rep D: `valid += 1` unconditional — dropped the `if window[c] == need[c]:`
  guard before it. Direct repeat of the exact mistake-class logged under
  Two Pointers variant 2 (dropped guard condition).
- Rep E: `window[c] = window(c, 0) + 1` — called `window` as a function
  instead of `window.get(c, 0)` — TypeError, not just a typo (missing `.get`).
- Rep I (first attempt at real shrink logic): used decrement-then-check
  (`window[d] -= 1` then `if window[d] < need[d]: valid -= 1`) instead of the
  canonical check-then-decrement (`if window[d] == need[d]: valid -= 1` then
  `window[d] -= 1`). Not wrong — both are logically equivalent — but a
  deviation from the exact template. Corrected to canonical order by rep J
  and held for the rest of the session (J, K, M, N, O all clean).
- **Rep L: wrote `left -= 1` instead of `left += 1` inside the shrink loop**
  — moves the window backward, breaks the pointer invariant. One-off, not
  repeated (rep M back to `left += 1`).

### Full min_window drill (start/length result-tracking piece)
11 reps total attempting the complete function (need/window/valid/shrink +
start/length tracking). Clean: 2, 4, 6, 7, 9, 10, 11 (final 3 — reps 9-11 —
clean in a row). **Topic template fully mastered as of 2026-09-08.**

Errors seen while integrating the new piece:
- Rep 1: `left, right = 0,0,0` (3 values into 2 names, unpack error);
  `valid` never initialized; and the real one — shrink-loop body (`d = s[left]`
  through `window[d] -= 1`) mis-indented one level too deep, nested inside
  `if right-left < length:` instead of being a sibling of it. Meant `left`
  only advances on iterations that set a new minimum — infinite loop on most
  inputs. Structural bug, not a typo; didn't recur.
- Rep 3, Rep 8: **the recurring one** — final return line,
  `if length = float('inf')` (single `=` instead of `==`), twice. Rep 8 also
  had `lenght` (transposed letters) in the same line. This was the only line
  that failed more than once across all 11 reps — everything else (setup,
  expand, shrink order, guard) was solid from rep 4 onward. If a future
  variant has a ternary/conditional return, slow down on `=` vs `==` there
  specifically.
- Rep 5: dropped `+1` in `need[c] = need.get(c,0)` — need counts never
  populate, so `valid` can never increment. One-off, didn't recur.

### Transfer problems
- **3. Longest Substring Without Repeating Characters** — DONE (2026-09-08).
  First attempt mechanically reused `min_window`'s min-tracking logic
  (`length = float('inf')`, `<` comparison, update inside the shrink loop,
  string-ternary return) on what's actually a max-length problem — the
  intended transfer-skill failure this problem is meant to catch. Also had
  window/left/right reset inside the outer loop (stale state each pass).
  Second attempt fixed all of it correctly: state initialized once outside
  the loop, shrink condition `window[c] > 1` (right instinct — no `need`
  needed here), result updated once per outer pass with `>` against
  `length = 0`, returns int. Verified by hand-tracing "abcabcbb" -> 3.
- **567 Permutation in String** — in progress (started 2026-09-08). Took 7
  reps to converge; last 2 (reps 6-7) clean in a row. Recurring mistake
  pattern across the session: `s[left]`/`s[right]` instead of `s2[...]` —
  showed up in three different lines across three different reps (need-loop,
  shrink-loop, expand-loop) — `s` isn't a variable in this function, only
  `s1`/`s2` are. Also had one true conceptual bug (not a typo): checking
  `valid == len(need)` before shrinking the window down to `len(s1)` first,
  which let irrelevant in-between characters produce false positives (caught
  by hand-tracing `s1="ab", s2="eidboaoo"` -> should be False, code returned
  True). Fixed by moving the `valid == len(need)` check to *after* the
  shrink-while, so window size is always capped to `len(s1)` before trusting
  `valid`. Also asked how to return the matched substring instead of a bool:
  answer is to track `start = left` and return `s2[start:start+len(s1)]` —
  no length-comparison bookkeeping needed (unlike `min_window`) since any
  match found is the answer, not "smallest so far".
- **438 Find All Anagrams in a String** — DONE (2026-09-09), 3 reps.
  First attempt was structurally correct (expand/shrink/check-after-shrink,
  `res.append(left)` in place of `return True` — right transfer instinct)
  but had a real gotcha: hard-coded "first param = pattern, second = text"
  carried over from 567's `check_inclusion(s1, s2)` signature. This
  problem's actual signature is the opposite — `find_anagrams(s, p)`, text
  first, pattern second. Caught by running both against the LeetCode calling
  convention: both returned `[]` instead of `[0, 6]` / `[0, 1, 2]`. Second
  attempt correctly swapped roles but introduced `need, window = {}` (single
  empty dict unpacked into two names — `ValueError: not enough values to
  unpack`); should be `need, window = {}, {}`. Third attempt clean, verified
  by running both test cases.

---

## Binary Search
Source: `reference/algorithmic-thinking/binary-search.md`
Status: **all 3 variants mastered** as of 2026-09-12. Both-ends-closed style
throughout (`[left, right]`, `left <= right`, `mid ± 1` boundary updates).

File convention: one running file, `attempts.py` (same convention as
sliding-window/two-pointers).

### Attempts
- attempts.py — 5 reps `search` (find-a-number) with a bug, reset, then 6
  clean reps; 7 reps `left_bound`; 7 reps `right_bound`, all clean.

### Common Errors

**Variant 1 (find a number, `search`):**
- **First 5 reps (all of them) shared one critical structural bug:**
  `mid = left + (right-left)//2` was computed once, *before* the while loop,
  instead of being the first line *inside* it. Since `mid` never gets
  recomputed as `left`/`right` change, `nums[mid]` never changes either, so
  the same branch fires every iteration and the loop never terminates unless
  the target happens to be at the very first midpoint — infinite loop on
  most real inputs. This was consistent across all 5 reps (not a one-off),
  so treat "is `mid` inside the loop, recomputed every pass" as the first
  thing to check for this variant specifically.
- One rep (3rd) additionally had `mid = left(right-left)//2` — missing `+`,
  calling `left` as a function, `TypeError`.
- After being told to reset, all 6 next reps were clean immediately — no
  recurrence.

**Variant 2 (left boundary, `left_bound`):** 7/7 correct, no bugs at all.
Self-converged from the explicit 3-branch form (reps 1-4, one with branches
reordered but equivalent) to a collapsed 2-branch form (`if nums[mid] >=
target: right = mid-1 else: left = mid+1`) for reps 5-7, correctly and
consistently. User was given the choice to standardize on either form going
forward and didn't have a preference — collapsed form is what carried into
`right_bound` drilling, so treat that as the adopted default for this topic.

**Variant 3 (right boundary, `right_bound`):** 7/7 correct, no bugs. Used
the collapsed 2-branch form from the start (`if nums[mid] <= target: left =
mid+1 else: right = mid-1`, `return right`). Notably never once fell into
the classic trap of copying `left_bound`'s `return left` instead of
`return right`, despite being warned it was the likely failure point.

### Next steps
Per CLAUDE.md step 5, transfer problems next. Natural candidates from
`reference/interview/binary-search-in-action.md` (not yet read) — check that
article for labuladong's own selection before picking ad hoc. The `-1` guard
for when target doesn't exist (checking `nums[left]`/`nums[right]` after the
loop) hasn't been drilled yet either — may come up naturally in transfer
problems or could be worth one quick pass first.

---

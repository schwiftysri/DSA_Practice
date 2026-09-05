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

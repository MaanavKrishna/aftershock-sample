# aftershock-sample

A tiny Python shop with a real bug in its history, for trying [Aftershock](https://aftershock-mk.vercel.app): every incident becomes a test, and git history proves it.

## The story

1. `feat: cart with line items`: a cart that adds up lines.
2. `feat: discount codes`: adds discount codes. It also lets the same code be applied again when the cart is refreshed, so customers get the discount twice. This is the commit that introduced the bug.
3. Issue #1 reports the incident: *Discount applied twice when the cart is refreshed*.
4. `fix: a discount code applies once per cart`: the fix, which closes issue #1.

## Try it

1. **Fork** this repository. A fork keeps the commit history Aftershock needs; a template would not.
2. Sign in at https://aftershock-mk.vercel.app and install the GitHub App on your fork.
3. In Aftershock, choose **New incident → Form**, pick your fork, and set the fix to the `fix: a discount code applies once per cart` commit (its SHA is the same in your fork). Use the issue text below for the fields.
4. Watch time travel: the drafted test must fail three times before the fix and pass three times on it.
5. Merge the bot pull request. Then open a pull request that breaks `apply_discount` again: Aftershock blocks it with **Recur**.

**Trigger:** a shopper refreshed the cart page while applying a discount code.
**Observed:** the same code was applied twice and the order total dropped too far.
**Expected:** a discount code applies at most once per cart.

## Run the tests

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
pytest
```

Licensed under Apache 2.0.

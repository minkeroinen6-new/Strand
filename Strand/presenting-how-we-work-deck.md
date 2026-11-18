# Making became cheap. Knowing did not.

**Seven months, one full-time developer, and what we would tell you before you try it.**

> **Genre: a PROJECTION, not a source.** Rendered also as
> [`presenting-how-we-work-deck.html`](./presenting-how-we-work-deck.html) for
> showing. Neither owns its figures; [`presenting-how-we-work.md`](./presenting-how-we-work.md)
> §4 does, and a number that changes there must be re-cut in both. Published
> privately at <https://claude.ai/code/artifact/ba2a4eac-1d05-4947-b3b4-2156476639c5>.
>
> **Rules for anyone editing this, all three learned by getting it wrong (Tero,
> 2026-09-02).** **Altitude:** write for someone who runs a product, not for
> someone inside the work. No file paths, no code identifiers, no test-harness
> mechanics — that is the level the agent operates at and it is not interesting
> to a human. **Structure:** scale, then principles, then the evidence they work,
> then how to apply them. **Length:** short. An earlier draft ran 3,751 words at
> ground level; this is about a third of that.
>
> **Clearance:** declassified. Excludes production volumes and unit economics
> (map §4.5, §4.6), names no colleague or customer, and needs **Antti's**
> approval before it reaches a partner (map §6).

**Measured 2026-09-02.**

---

## 1. What one developer built in seven months

First commit 11 February 2026. Today: an operations back-office, customer and
crew apps on both stores, a marketing site, a managed device fleet, and an AI
concierge customers reach on WhatsApp, by phone and in-app. Ten languages
throughout.

**Two parts of that are not ordinary software, and both were deliberate.**

The concierge is a **domain class we had to define**, not a chatbot bolted onto a
helpdesk. It is a permanent participant in one continuous conversation per
customer, across WhatsApp, voice and the app — never removed and never muted,
reading everything and answering only what is addressed to it, while a named
colleague can answer in the same thread without the customer losing the assistant.
The market default is the opposite shape: classify the inbound, draft a reply,
queue it for a human to send. That product is everywhere and we rejected it on
purpose, which meant inventing the vocabulary — addressivity per message rather
than ownership per thread, one conversation record across every channel — because
none of it existed to copy.

**And the operating model is AI-first end to end**, not AI-assisted. Twenty-seven
autonomous workflows; an independent verification repository that files issues
against us and cannot see our code; a review-and-merge loop that runs with no
human in the hot path; and our own audit methodology, commissioned explicitly
because the classical ones were designed for human-written code and leave the new
gaps wide open.

| | |
|---|---:|
| Lines of source, and of tests | **774,000** and **661,000** |
| Automated tests | **25,575** |
| Rules enforced by machine, not by memory | **196** |
| Customer-facing journeys written down before being built | **245** |
| Issues closed per week | **114**, against 114 still open |

One developer full-time, one part-time, one mainly on the marketing site. That
last row is the one we watch: closing as fast as we open means the system is not
quietly accumulating debt.

Building stopped being the constraint some time in the spring. What replaced it
took us three months to notice.

### The assistant became a chatbot over four months

We had specified an open-ended assistant: customers write in their own words, it
works out what they need, and it does it. By August we had shipped something that
behaved like a phone tree. Fifteen changes got us there. Each answered a real
complaint from someone who had used the product, each was defensible on its own,
and not one was ever removed. Nobody decided to build a phone tree.

We found out on 6 August because a colleague read a conversation. A prospect had
written twice, two seconds apart, and was clear about what she wanted. Within nine
seconds we sent four automated messages back, the first apologising for not
understanding her. Then seventeen and a half hours of nothing, until the colleague
answered by hand the next morning in three sentences and got a reply.

The reason nobody caught it earlier is the part worth your attention. No single
change was ever large enough to justify reviewing the product as a whole, so the
whole was never reviewed. The drift only existed in aggregate, and nothing we did
looked at the aggregate.

> ### Making became cheap. Knowing did not.

---

## 2. What the job actually is

Managing complexity. Five apps, one API, a device fleet and an AI concierge are
already more system than one person can hold in their head, and the volume made
that worse rather than better. Complexity is not an inconvenience of the work; it
is the thing the work is against.

Every practice we have exists to keep one of three properties true. We ask these
three questions of any design before it is built and again before it is called
done, and all three have to answer yes.

### Stakeholders — does it do what its users actually need?

A feature is defined by what real people need to do with it, not by the data
model. Before designing anything, we name every person it touches — the customer,
the crew member, the office, the accountant, the AI itself — and walk each one's
story end to end, across every surface they cross: what they see, what they
enter, what they expect next, what happens when it is late or missing. The design
is only right when every one of those stories works. Where two of them
contradict each other, the definition is broken, and that is far cheaper to find
in a document than in code.

Two things we got wrong on the way there. **A non-technical report states a
need, not a design** — take the rule they are describing, never the literal noun
they happened to reach for. And **when someone offers to cut scope, that shrinks
the deliverable and never the invariants**: they can cut screens and seed data,
they cannot cut audit, isolation or blast radius, because they cannot see those
and are not being asked about them.

The sharpest lesson is that you can do this diligently and still miss someone. We
had specified the platform in detail for everyone it serves, and not at all for
the four people who decide what the company promises, at what price, to whom.
The owners were simply absent from our own list of stakeholders — which meant the
*source* of our requirements was undocumented. Enumerating stakeholders is not a
one-off exercise you complete.

### Coherence — is it one system, or several that agree by accident?

The feature is one thing seen from many places, not many things that happen to
resemble each other. We mean this at three levels and we check all three.

**One name per fact, one source of truth.** Concepts that are genuinely different
stay different; concepts that are the same are *one model*, not a parallel copy to
be reconciled later. Two live representations will drift, always.

**Every surface shows the same concept in the same words.** Office tool, crew app,
customer app, website, WhatsApp, voice, quotes, invoices, PDFs. A status is worded
once and resolved in one place, never re-spelled per screen. Our office tool holds
every field an entity has; the customer and crew apps are strict projections of it
with progressively fewer fields but the same layout and structure. The text on the
website is the same text as in the app, defined once and flowing down — not
maintained per channel.

**The change spans every surface it touches, in one change.** No screen keeps a
private copy, and no feature ships as a happy-path spike on one of the six places
it appears.

### Sustainability — can we still change it safely in six months?

The model has to survive being extended, re-priced, re-translated and audited for
years.

**History is immutable.** Anything a customer or a colleague acted on is
snapshotted, never edited afterwards. Re-pricing the catalogue must never rewrite
an invoice that has already gone out.

**Everything is translatable by construction.** Text carries an identifier and
flows through one pipeline to all ten languages, and the customer's copy is frozen
at the moment it was issued. A hardcoded string is a language we can never reach.

**When you replace something, you delete the old one in the same change.** No
"retire it later". That is how you end up with two live models and a reconciliation
job nobody scheduled.

**Changes are additive.** New fields optional, migrations that extend rather than
break, and enough room in the model for the next requirement without a rewrite.

---

### How we arrived at those three

Six decisions about how to think, which are the transferable part.

**When the constraints change, derive from first principles instead of inheriting
practice.** Every established practice answers a constraint. Code review, sprint
planning, a QA phase, a backlog: all of them answer *building is slow and
expensive*. When that stopped being true, most of the inherited answers were
solving a problem we no longer had. The instruction that started our audit work
put it plainly: *don't settle on what people have done in the past, archaic best
practices — consider things from first principles.*

**Find the new bottleneck, then re-plan around it.** The common framing is that
building got fast, so planning and review are now the constraint, and the
conclusion is to speed those up. That is the wrong re-plan. Our constraint is not
a slow stage, it is that we can produce more than we can *know to be correct*.

**Explicitness is the whole capacity.** How much of this shift an organisation can
absorb equals how well it can state its own standards out loud. Everything of ours
that works is a standard someone wrote down; everything that has bitten us lived
in somebody's head and did not survive contact with a worker who had never met
them.

**Turn instructions into properties of the system.** Whenever we catch ourselves
writing an instruction, we ask whether it could be a property instead — something
the system simply is, rather than something a worker must choose to do.
Instruction-following is variable; properties are not. This is a habit of design,
not of diligence.

**Arrange who can see what. You cannot instruct independence into existence.** We
tried asking one worker to be its own critic and got agreeable nonsense, because a
mind cannot hold a position it is also trying to defeat. The fix was moving
information, not writing a better instruction.

**Your own incidents are the only dataset you have at this size.** We are too
small to learn anything from metrics; four data points on a chart is decoration
that produces confident wrong decisions. So we write single incidents up properly
and generalise from them, and resist every temptation to build a dashboard.

## 3. Why we think this works

| | Published research | Us |
|---|---|---|
| **Output per developer, per week** | ~3 merged changes — 12.4 a month (LinearB, 6.1M+ pull requests) | **114 issues closed** · about **40×** the published median |
| **Rate of production** | **19% slower** on task completion time — 16 experienced developers, 246 real tasks in their own mature codebases (METR randomised trial, 2025) | **672 commits a week** over the last month. **774,000 lines of source and 661,000 of tests in 29 weeks** |
| **Stability under that throughput** | Throughput up, **stability down** — more change failures, more rework, longer to resolve (DORA, *State of DevOps 2025*) | **0.18% revert rate** — 15 in 8,205 commits. **13.1 hours** median from a defect being found to closed. **114 closed against 114 open** |

40× is the ratio of two measured rates: 114 issues closed a week against a
published median of 2.85 merged changes per engineer per week. An issue and a pull
request are different units, so the two are not interchangeable. Every count here
comes from `git`, the GitHub API and the production database, with the command
recorded next to it.

**The third row is the one that matters.** DORA's finding is that AI raises how
much teams ship and *worsens* how reliably it works, because generation outruns
the capacity to check it. Their summary: *"AI doesn't fix a team; it amplifies
what's already there."* Most teams buy throughput with stability. The interesting
question is not how much you ship — it is which side of that split you land on.

**Is it just that the models got good?** Partly, and the halves separate cleanly.
DORA's own result flipped from negative to positive between 2024 and 2025 on the
same survey, so the models plainly bought the throughput. But that same 2025
report found stability still getting worse. Everyone has the same models, and the
outcomes diverge. The models raised what you can produce and did nothing about
knowing whether it is right.

**And the verification that produces those numbers holds up on its own terms.**
Our automated issue-finder is right **91.3%** of the time: of 219 resolved
findings, 5.5% were not defects and 3.2% were duplicates. Precision is the figure
an autonomous system lives or dies by, because false alarms destroy trust faster
than missed bugs do.

**Two things to know before you copy this.** We started from nothing, with no
legacy to violate; the METR developers were working in million-line codebases with
years of history, which is the harder case. And one person decides everything, so
we carry no coordination cost — that is a real advantage and the one least likely
to transfer to a larger team.

---

## 4. How the system runs itself

One developer cannot watch five apps, an API, a device fleet and an AI
concierge, and the volume made that worse. So the job was never to watch harder.
It was to build a system that observes itself, repairs itself and tightens its
own rules, and asks a person only where a person's word is actually needed.

Four things had to be true for that to be safe rather than reckless — and one more says why it is worth it, and each
is a property of the system, not an instruction to a worker.

**A lesson becomes a gate, never a reminder.** The workforce has no memory
between sessions, so a rule that lives in prose is a rule that will be broken.
Every rule we care about is an executable check that runs before a commit and in
CI. There are **200** of them today, from none in March. The written principles
are held to a fixed ceiling of **fourteen**, enforced by one of those checks, so
the list stays short enough to be read.

**Every action leaves a durable record, never just a message.** A bot that
answers in chat and files nothing has done half the work in the place nobody
re-checks. Every finding becomes an issue, every issue a backlog row, every
decision a ledger entry — **1,403** issues, **315** live backlog rows, **81**
recorded decisions, **110** audit ledgers. We audit the join between stores, not
the count in one.

**Silent success is treated as a failure.** A check that passed because it
examined nothing is indistinguishable from one that passed because everything
was right. So **193** of the gates declare how many things they looked at, and a
count that drops to zero fails the build. A watchdog fires on every automated
run that fails; a separate heartbeat tells a human when the machines that run
the healer have gone quiet, because a self-healing system whose healer is down
must degrade to *telling someone*, not to silence.

**Some doors stay human, and the whole thing has one switch.** Payments,
authentication, database migrations and personal-data handling are a no-fly
zone: the fixer refuses them and the merger re-checks the refusal on the diff.
One repository variable turns every autonomous writer off at once. A block
always ships with the way out of it — a refusal names what a person must do
next. And when a document and the operator disagree, the operator's word is the
requirement.

**Capital does the work; idle capital is waste.** The unvoiced principle under
all of the above: the goal is to scale the work above the headcount, so one
person's judgement is multiplied by machines that never wait for a free evening.
It cuts both ways. A runner idle while a queue forms, a serial CI job using one
of eight boxes, a check re-running work already proven green — each is capital
bought and not spent. The weak points below are read that way first: not as
bugs, but as idle capital.

### The ladder — how far autonomy has climbed, and when

Twenty-seven automated workflows, added in five stages over fourteen weeks. Each
rung was built only after the one below it had run long enough to be trusted.
Dates are the day each workflow first entered the repository.

| Stage | First existed | What was added |
|---|---|---|
| **Observe** | 26–29 May | Daily Sentry triage and status post. Store-listing monitor. CI-failure triage and end-to-end-test triage that read every failed run's logs and file an issue. Nightly verification that shipped changes do what their commit said. Meeting notes turned into proposed spec changes. |
| **Listen** | 1–25 June | Slack decisions into spec proposals; Slack bug reports into issues; meeting action items into issues; recordings pulled in automatically; the API route registry generated from code; an evaluator that vets findings from untrusted sources before they count. |
| **Fix** | 24 June | Issue to fix-PR, dispatched by hand, one issue at a time — with a watchdog alerting on every failed automated run from the same day. Ten clean PRs were the bar for the next rung. |
| **Merge and close** | 21–25 July | Fixes dispatched automatically for every open issue. A review-and-merge bot with its own reviewer hat and the no-fly re-check. Loop closure: the issue closes on push and the reporter is told on deploy. A daily reaper that cleans up what the bots leave behind. Dependency updates merged on green. Monthly coherence sweep. |
| **Self-monitor, self-feed** | 21 Aug – 2 Sep | A sweep of who is waiting on us in the reports channel. Heartbeats from the build machines, with an alarm when one goes quiet. Open issues reconciled into the backlog every four hours. A fifteen-minute loop that keeps fix PRs current against a trunk that moves every few minutes. |

### The loop today

Signals come in from six places — the reports channel, error monitoring, failed
CI runs, the nightly QA explorer, meeting notes, backlog rows — and leave as
closed issues with the reporter told:

> triage (classify, dedup) → issue → fix PR (no-fly refusal) → review + merge
> (no-fly re-check) → deploy → close on push, notify on deploy, strike the
> backlog row — with a fifteen-minute side loop keeping each open PR current.

Around the outside sits a second loop that watches the first: a watchdog on
every failed run (12,184 runs to date), the heartbeat and liveness alarm, the
daily reaper, the monthly coherence sweep, and the backlog ingest every four
hours. Two obligations are deliberately separate: the durable record (issue
closed, row struck) and the human told. Conflating them costs one of them.

### What the loop has actually done

| | |
|---|---:|
| Issues filed by an agent | **975 of 1,403 — 69%**, of which 224 carry the CI-failure label |
| Bot fix PRs merged by the bot | **20 of 32**; median 5.9 h from opened to merged; 11 closed unmerged; 1 open |
| Machine-enforced rules | **200** — 0 in March, 23 in June, 94 in August |
| Automated tests | **25,923** in 2,775 files |
| Written principles | **14**, and the ceiling is itself one of the 200 rules |

Machine-enforced rules, sampled at the first commit of each month: Feb 0 · Mar 0
· Apr 2 · May 4 · Jun 23 · Jul 53 · Aug 94 · 1 Sep 184 · today 200. Every one
began as something a person noticed by hand, once. The curve is the system
learning; the fourteen-principle ceiling is what keeps the prose from learning
the same way.

| Week ending | Issues opened | Issues closed |
|---|---:|---:|
| 15 Jul | 64 | 79 |
| 22 Jul | 68 | 68 |
| 29 Jul | 95 | 106 |
| 5 Aug | 99 | 79 |
| 12 Aug | 61 | 30 |
| 19 Aug | 89 | 126 |
| 26 Aug | 127 | 115 |
| 2 Sep | **488** | **392** |
| Open today | | **119** |

The last row is the one to read. The week the pipeline started filing every CI
failure and reconciling the backlog automatically, intake quadrupled — and
closure very nearly kept pace. That is the loop working as designed, and it is
also the load that exposed the weak points below.

### Where it stands on 2 September, stated as facts

**Autonomous today:** reading the reports channel hourly; triaging every failed
CI run and error report into an issue; opening a fix for every open issue;
reviewing and merging its own fixes when they are green and outside the no-fly
zone; keeping those fixes current against trunk every fifteen minutes; closing
the issue on push and telling the reporter on deploy; reaping what it abandons;
reconciling the backlog; alerting a human when any of that fails or the machines
go quiet.

**Human by design:** anything touching payments, authentication, migrations or
personal data; every spec change the bots propose from meetings and Slack; the
decision that a report is a requirement; and the answer to a question the record
does not hold.

**The known weak points, from today's own runs.** Continuous integration is one
serial job on one shared machine: of **114** CI runs today, **51** were cancelled
by the next push before they finished. The pre-commit check on a change that
touched a shared package took **29.5 minutes**. The triage runner had **59**
triage runs queued and **54** watchdog runs behind them, while the liveness alarm
— which reads the age of the last *success* — reported healthy; **225** runs sit
queued across the repository as this is measured, and the runners themselves
cannot be listed because the token is refused. The fifteen-minute PR loop cannot
label a conflicted PR: two labels it applies do not exist in the tracker. And
the fixer never repairs its own red PR, by design, because an unbounded fixer is
a fix-fail-fix loop — so a red bot PR waits for a human. None of these is a
surprise; each is on the record as a defect.

### The next rung

* **Close what is superseded.** When trunk fixes an issue before the bot's PR
  lands, the loop should close the PR itself with a comment saying why. Today it
  cannot: two of the three open PRs on 2 September were in exactly that state and
  were closed by hand. This is the one addition decided; the other weak points
  above are recorded as defects in the backlog, not as a roadmap.


---

## 5. What we would change about how you run product

**Move your people from building to deciding and checking.** This is the whole
reallocation, and it is the only item here that is really about org design. When
producing a thing costs a tenth of what it did, the scarce roles are the ones
that say what *good* means here and the ones that prove it happened. We staffed
accordingly by accident and would now do it on purpose.

**Define your concepts before you design anything that uses them.** We built
every surface that sells a service before deciding what a service *was*. The
definition ended up spread across a dozen screens, prices lived in several places
and drifted apart, and every fix added another copy instead of removing one. The
rebuild cost weeks. You cannot de-duplicate a concept you never named.

**Write each person's journey before anyone designs a screen.** Name everyone the
feature touches, list every place it appears, then walk what each of them
actually does: what they see, what they enter, what they expect next, what
happens when it is late or missing. We have written 245 of these. Where two
people's journeys contradict each other, you have a broken definition rather than
a UI problem, and it is enormously cheaper to find there than later.

**Never let anyone guess at domain content.** The cost of a wrong assumption has
gone up, because it now propagates across every surface in an afternoon. Our
best-run feature stopped and parked eight open questions for the operator. Our
worst guessed, and paid for it in months of rework.

**Do not plan further out than your loop runs.** Our multi-week backlog went
stale faster than we reached it. Short horizons and a written daily status work
better, and the backlog stopped being a planning artefact and became a graveyard.

**Spread product judgement rather than centralising it.** One product manager as
the single funnel becomes the bottleneck the moment building stops being one.
Ours comes from operations, field reports, error monitoring and the owner.

**Measure outcomes, not activity.** Volume of output is now trivially easy to
generate and tells you almost nothing. The number we actually watch is whether we
close as fast as we open. Anything you reward by activity will be delivered as
activity, especially by a workforce with no memory of why the measure existed.

**Ask the three questions from §2 again at the end, not only at the start.** Is
it one coherent thing, will it survive being changed for years, and does each
person's journey actually work end to end? We ask them before designing and again
before calling anything done, because a feature that was coherent when specified
drifts while being built.

**Say where you are weak.** Ours is the middle layer: we have a vision and we
have priorities, and the explicit customer journeys that should connect them are
the thing we are worst at keeping current. That is the diagnosis, not a cure we
are selling.

## 6. What it costs

**Writing your standards down changes them**, and whatever will not survive being
written is simply lost. We have lost some.

**The new failure is plausible work** — not broken, just not worth doing, cheap to
produce and expensive to spot.

**Attention is the only budget you cannot increase.** Every check that needs a
human to look at it spends it, and one that fires often and means little teaches
people to ignore the alarm.

> An organisation's ability to absorb this shift equals its ability to make its
> own standards explicit. The firms that struggle will not be the ones with worse
> tools. They will be the ones whose quality lived in people's heads, because
> that is the one asset which does not transfer.

---

## Provenance

Figures measured at commit `ee2d3e97e`, 2026-09-02, and re-derived rather than
recalled. Underlying material:
[`agentic-engineering-principles.md`](./agentic-engineering-principles.md) (§2),
[`working-on-large-features.md`](./working-on-large-features.md) (§4),
[`../product/product-development-model.md`](../product/product-development-model.md) (§4),
[`../testing/acceptance-tests.md`](../testing/acceptance-tests.md) (§3),
[`../postmortems/`](../postmortems/) (the incidents),
[`presenting-how-we-work.md`](./presenting-how-we-work.md) (the map, and what was
left out).

*Research cited in §3: DORA State of DevOps 2025; METR, "Measuring the Impact of
Early-2025 AI on Experienced Open-Source Developer Productivity", 2025-07-10;
LinearB 2025 engineering benchmarks.*

§4's figures were measured against the repository, the read-only GitHub API and
the day's workflow runs on 2026-09-02 at superproject commit `adf614710`; the
commands are in the map's §4.10.

Excludes production business volumes and unit economics, cleared separately per
the map's §6.

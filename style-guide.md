# Style Guide: Grip

## Voice & Audience

**Target reader:** The savvy intellectual familiar with systems science, cognitive science, philosophy, and information theory. Someone who can follow technical arguments but expects them to illuminate, not obscure. A reader building a "wise operating system" for thought.

**Tone:** Rigorous yet elegant. Sophisticated without pretense. Occasionally humorous—a raised eyebrow, a well-placed metaphor, a moment of self-awareness. Never condescending, never hand-wavy. This is serious work that doesn't take itself too seriously.

**Metaphysics:** Neutral and pluralistic. Treat realism, structural realism, process views, and pragmatism as compatible lenses, not competing creeds. Function over essence. Control over correspondence.

---

## Core Principles

### 1. Precision with Grace
- Use technical terms when they do real work (rate-distortion, affordance, degeneracy).
- Define them clearly on first use, then wield them confidently.
- Avoid jargon for jargon's sake. If a plain word suffices, use it.

### 2. Examples Before Abstractions
- Lead with concrete cases (snake on trail, market crash headline, meeting a stranger).
- Build to the formal framework, not from it.
- Let the reader *feel* the constraint before you name it.

### 3. Compression ↔ Expansion
- Every claim should illustrate either compression (selection, simplification) or expansion (exploration, redundancy, scaffolding).
- Show the trade-off: what's gained, what's lost, what's the budget.

### 4. Testability
- Each chapter closes with **measures & tests**: ROC curves, drift-diffusion parameters, IB fits, audit trails.
- Claims that can't be tested are decoration, not architecture.

### 5. Multi-Scale Consistency
- The same formal spine (control under constraints) spans neurons, persons, institutions.
- Language should shift scale gracefully: use "agent" when scale is ambiguous, specify when it matters.

---

## Sentence Style

### Length & Rhythm
- Vary sentence length deliberately. Short for impact. Longer for development and nuance, especially when unpacking a constraint or showing how compression and expansion interact.
- Use em-dashes for asides—like this—that add color or qualification without breaking flow.
- Semicolons for parallel structure or tight conceptual links; avoid overuse.

### Active Voice (mostly)
- Prefer active constructions: "Agents compress signals" over "Signals are compressed by agents."
- Passive is acceptable when the actor is generic or when emphasizing the object: "Affordances are revealed through action."

### Humor & Humanity
- Occasional wit: a wry observation, an unexpected metaphor, a footnote that winks.
- Example: "Perception is not a camera; it's a dashboard built by natural selection on a tight budget."
- Never forced. If it doesn't serve the argument, cut it.

---

## Vocabulary & Forbidden Patterns

### Embrace
- **Constraint, budget, compression, expansion, affordance, interface, schema, frame, symbol, scaffold, cone, degeneracy, redundancy.**
- **Rate-distortion, information bottleneck, active inference, ELBO, Lagrangian, Pareto front.**
- **Control, grip, anticipation, coordination, foresight.**

### Use Sparingly
- "Paradigm," "holistic," "synergy" (unless you're critiquing them).
- "Revolutionary," "groundbreaking" (the work speaks for itself).
- Overuse of "importantly," "interestingly," "surprisingly" (show, don't tell).

### Forbidden
- "Clearly," "obviously," "trivially" (if it were, you wouldn't need to say it).
- Unnecessary hedging: "It seems that maybe possibly..." (be precise or acknowledge uncertainty directly).
- Buzzwords without definition: "emergent," "complex," "resilient" (operationalize or omit).

---

## Structure & Flow

### Chapter Architecture
1. **Opening hook:** Concrete scenario or puzzle.
2. **Core claims:** What this chapter establishes.
3. **Compression/Expansion moves:** Show the mechanism.
4. **Failure modes:** What happens when it breaks.
5. **Measures:** How to test it.
6. **Forward link:** What comes next and why.

### Paragraph Transitions
- Each paragraph should earn its place: new claim, new evidence, new qualification.
- Transition explicitly between scales (neuron → person → institution) and concepts (compression → expansion).
- Use structural markers: "First, ... Second, ... Finally," or "Consider ... Now contrast ..."

### Cross-References
- Reference other chapters by name and concept: "As we saw in Chapter 5, rate-distortion forces categorical boundaries."
- Build on earlier examples: "Return to the snake on the trail..."
- Foreshadow: "We'll formalize this in Chapter 14."

---

## Mathematics & Formalism

### When to Formalize
- Introduce informal intuition first (example, diagram, metaphor).
- Follow with precise statement (equation, algorithm, optimization objective).
- Close with interpretation (what it means for agents under constraints).

### Notation
- Consistent symbols across chapters:
  - *R* for rate (information), *D* for distortion.
  - *U* for utility, *C* for cost.
  - *π* for policy, *p* for probability.
  - *I* for mutual information, *H* for entropy.
- Define notation in a box or margin on first use.

### Equations
- Number only equations that are referenced later.
- Provide intuitive gloss immediately: "This says agents maximize control while staying within budget."

---

## Citations & References

### Style
- In-text: Author (Year) for narrative flow, (Author Year) for parenthetical.
- Example: "As Marr (1982) argued, ..." vs. "Vision is multi-level (Marr 1982)."

### When to Cite
- Original ideas, empirical claims, technical results.
- Classic touchstones (Gibson, Shannon, Kahneman, Pearl).
- Recent work that extends or challenges the framework.

### When Not to Cite
- Well-established textbook material (e.g., "Information is measured in bits").
- Your own original synthesis (but distinguish clearly).

---

## Figures & Diagrams

### Priorities
- **Clarity over beauty.** Every figure must do conceptual work.
- Label axes, include legends, provide captions that stand alone.
- Use consistent visual language (e.g., constraints as borders, compressions as funnels, expansions as radiating arrows).

### Types
- **Toy diagrams:** Simple 2D sketches of affordances, information flow, trade-off curves.
- **Formal plots:** ROC curves, IB frontiers, drift-diffusion trajectories.
- **Architecture tables:** Layer × Input/Operator/Output/Objective/Budgets/Failure/Measures.

---

## Ethics & Values

### Framing
- Values enter as **weighted distortions** in the objective function.
- Moral pluralism = Pareto front with transparent trade-offs.
- Disagreement is structured, not resolved by fiat.

### Avoid
- Preaching or moralizing.
- Pretending the framework solves normative disputes (it clarifies them).
- Using "alignment" as a black box (operationalize: align *what* with *what*?).

---

## Failure Modes & Self-Awareness

### The Framework's Limits
- Acknowledge when the model simplifies (e.g., "This ignores higher-order social dynamics...").
- Specify boundary conditions (e.g., "Under stable environments with known payoffs...").
- The Coda formalizes how to update the framework when predictions fail.

### Goodhart & Frame-Lock
- Warn against over-compression: metrics become targets, schemas become prisons.
- Show mechanisms for escape: counter-metrics, audit, frame rotation, exploration bonuses.

---

## Example Passages (Gold Standard)

### Opening Hook (Chapter 1 style)
> You're hiking alone when something moves in the periphery. Dark, coiled, near your boot. Your body reacts before you think: heart rate spikes, weight shifts, hand reaches for a stick. A second later you see it's a curved twig, shadow-draped. Relief floods in. But notice what just happened: you didn't run Bayesian inference on pixel arrays. You didn't catalog all possible twig-like and snake-like objects. You *compressed* ambiguous input into a fast, actionable category—"threat?"—tuned to consequences, not truth. That compression is grip.

### Formal Precision (Chapter 14 style)
> The multi-objective Lagrangian writes:
>
> **L(π) = U(π) + λ_info I(π) - λ_energy E(π) - λ_time T(π) - λ_risk V(π) - Σ λ_value,i D_value,i(π)**
>
> Each term is a budget or distortion. The policy π selects actions; U is control utility; I is information cost (rate-distortion); E, T, V are energy, time, and risk; D_value are value-weighted harms (fairness, care, autonomy). The λs are Lagrange multipliers—scarcity prices on constraints. This is the formal spine. Everything else is commentary.

### Transition Between Scales (Chapter 10 style)
> At the neural level, attention gates prediction errors through precision weighting. At the organizational level, dashboards gate executive attention through KPIs. Same functional logic: allocate limited processing to signals that matter, given current goals and budgets. The difference is time-scale and coordination cost, not kind.

---

## Final Checklist

Before any chapter is complete, confirm:

- [ ] Opens with concrete example or puzzle
- [ ] Core claims stated explicitly
- [ ] Compression/expansion moves shown
- [ ] Failure modes identified
- [ ] Measures & tests provided
- [ ] Cross-references to other chapters
- [ ] Notation consistent with earlier chapters
- [ ] Humor present but not forced
- [ ] Testable, falsifiable, actionable
- [ ] Ends with forward link to next chapter

---

## Mantras

1. **Function over essence.**
2. **Constraints enable, not merely limit.**
3. **Control over correspondence.**
4. **Show the trade-off.**
5. **Test or cut.**
6. **Compression narrows. Expansion widens. Both are necessary.**

---

This is the voice of *Grip*. Use it well.
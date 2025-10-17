# Chapter Summaries - Narrative Continuity Tracker

This file provides **narrative context** for subagents when writing/researching subsequent chapters. Each summary captures the core argument, key examples, and transitions.

---

## Quick Navigation
[Ch 1](#chapter-1-the-problem-of-grip) | [Ch 2](#chapter-2-constraints-before-categories) | [Ch 3](#chapter-3-embodiment-and-affordances) | [Ch 4](#chapter-4-neutral-stances-convergent-functions) | [Ch 5](#chapter-5-ratedistortion-life) | [Ch 6](#chapter-6-predictive-brains-budgeted-attention)

---

## Chapter 1: The Problem of Grip
**Status**: ✅ Complete | **Words**: 4,377

### Summary
Agents gain grip by compressing a complex world into actionable categories. Constraints (time, energy, information, risk, coordination) enable rather than merely limit cognition. Success is measured in control and anticipation, not correspondence with exhaustive truth. Compression is necessary for tractable action; expansion (exploration, redundancy, scaffolding) prevents brittleness.

### Key Concepts Introduced
- **Grip**: The capacity to make a complex world tractable through selection and simplification.
- **Constraints as enablers**: Time, energy, information, and coordination limits force useful compressions.
- **Control over correspondence**: Optimization for effective action, not pixel-perfect fidelity.
- **Lossy compression**: Rate-distortion trade-offs as the natural language of perception and decision.
- **Homomorphic mapping**: Models preserve task-relevant structure while discarding the rest.

### Major Examples
- Snake vs. twig: split-second visual compression that privileges survival over accuracy.
- Chess grandmasters: 50,000 chunks compress board positions into perceptual patterns.
- Gaze heuristic: baseball outfielders exploit physics rather than computing trajectories.
- Firefighter recognition-primed decisions: mental simulation of typical scenarios under pressure.
- Paradox of choice: too many options induces paralysis; constraint clarifies.

### Transition Out
Chapter 2 specifies the constraints abstractly. What exactly are time, energy, information, risk, and coordination budgets? How do they interact? Can they be measured and tuned? We move from the intuition that grip requires compression to the formal specification of the constraints that force it.

---

## Chapter 2: Constraints Before Categories
**Status**: ✅ Complete | **Words**: 3,904

### Summary
Time, energy, information, risk, and coordination function as modern transcendental conditions—measurable, tunable budgets that structure what can be sensed, computed, and coordinated. These constraints operate simultaneously and interact complexly. Unlike Kant's fixed categories, they're empirically tractable and vary with development, learning, and technology. Together they replace classical *a priori* forms as enabling conditions of experience.

### Key Concepts Introduced
- **Five constraints**: Time (speed-accuracy tradeoff), Energy (metabolic budget), Information (channel capacity), Risk (explore-exploit), Coordination (common knowledge).
- **Drift-diffusion model**: Evidence accumulates to a threshold; lower threshold trades accuracy for speed.
- **Sparse coding**: Metabolic limits force neurons to be selective; efficiency constraints shape neural representations.
- **Information bottleneck**: Compress inputs to preserve task-relevant output information while minimizing rate.
- **Multi-objective optimization**: Constraints interact; single-constraint optimization is globally suboptimal.

### Major Examples
- Saccadic eye movements: adjust velocity based on target size to optimize time-blind duration, motor noise, and information extraction.
- Honeybee waggle dance: communication precision trades off against foraging time; colony must learn the protocol socially.
- Byzantine Generals Problem: coordination costs are fundamental; common knowledge is expensive to achieve.
- Temporal discounting: hyperbolic, not exponential; preference reversals reveal risk-time coupling.
- START triage system: brutal compression under severe resource constraint; optimal error distribution differs by priority.

### Transition Out
Chapter 3 shows how embodiment channels these abstract budgets into concrete possibilities. Bodies aren't neutral containers; they pre-compress the world through morphology, sensor placement, and sensorimotor coupling. Constraints meet flesh.

---

## Chapter 3: Embodiment and Affordances
**Status**: ✅ Complete | **Words**: 5,085

### Summary
Embodiment pre-compresses the world through morphology, sensor placement, and sensorimotor coupling. Bodies aren't neutral containers for minds; they discretize continuous flux into action-relevant categories. Affordances are relational invariants—possibilities for action that exist only at the intersection of agent capabilities and environmental structure. Perception is active exploration; affordances are discovered through movement, not passively perceived.

### Key Concepts Introduced
- **Affordance**: Action possibility relative to agent and context; a relational invariant, not objective property or subjective projection.
- **Morphological computation**: Body structure performs computation that would otherwise require neural circuits; physical dynamics offload from neurons.
- **Body-scaled ratios**: Pi-numbers (dimensionless proportions) define action boundaries; same ratio (e.g., 0.88 for climbability) invariant across body sizes.
- **Sensorimotor contingencies**: Lawful relations between actions and sensory changes; perception constituted by mastery of these couplings.
- **Motor babbling**: Random motor exploration that discovers body-world mappings; enables learning of sensorimotor schemas.
- **Tool incorporation**: Body schema plastically extends to include tools; peripersonal space expands with rake training in monkeys.

### Major Examples
- Warren's stairs: visual system solves "Can I climb?" through body-scaled ratio, not through explicit physics.
- Passive dynamic walker: morphology achieves stable gait without motors or control, offloading computation to physics.
- Bach-y-Rita's tactile vision substitution: spatial structure transfers across modalities; the blind learn to "see" through touch because sensorimotor contingencies are preserved.
- Goodale & Milner's patient D.F.: dissociation between dorsal (action) and ventral (conscious perception) streams; accurate grasping despite absent object recognition.
- Developmental trajectory: infants learn affordances through active exploration (reaching, crawling); critical periods shape embodied skills.

### Transition Out
Chapter 4 addresses the philosophical question embodiment raises: Are affordances "real," or are they agent-relative constructs? Different metaphysical frames (realism, structural realism, process philosophy, pragmatism) offer different answers. Yet they converge on the same functional necessities for control.

---

## Chapter 4: Neutral Stances, Convergent Functions
**Status**: ✅ Complete | **Words**: 4,781

### Summary
Different metaphysical positions—scientific realism, structural realism, process philosophy, pragmatism—are compatible lenses on the same control problem. Whether the world is fundamentally objects, relations, processes, or pragmatic constructs, agents must build lossy models tuned to control rather than essence. The Good Regulator Theorem formalizes this: any efficient regulator must homomorphically map the system it regulates, preserving control-relevant structure while discarding the rest. Metaphysical neutrality is a virtue for analyzing grip.

### Key Concepts Introduced
- **Metaphysical neutrality**: Multiple ontologies yield the same functional architecture under constraints.
- **Good Regulator Theorem**: Efficient regulators are homomorphic models—lossy mappings that preserve structure needed for control, not exhaustive isomorphisms.
- **Multiple realizability**: Same function can be implemented by different substrates (pain in humans, octopuses, hypothetical aliens).
- **Convergent evolution**: Same functional solutions arise independently (camera eyes, wings, echolocation) across lineages—evidence that constraints force convergence regardless of starting conditions.
- **Functional convergence**: Octopus and human eyes solve the same optical problem differently, yet yield equivalent control architectures.

### Major Examples
- Camera eyes in octopuses and humans: independent evolution from different developmental pathways, yet same optical function; 875 conserved genes despite 500-million-year divergence.
- Wings in birds, bats, insects: different morphologies (feathers, membranes, exoskeleton), all generating lift via Bernoulli's principle.
- Echolocation in bats and toothed whales: independent convergent molecular evolution in hearing genes (Prestin), tuning auditory systems to high-frequency signals.
- Thermostat regulating temperature: lossy homomorphic model of room dynamics; doesn't model molecular collisions, just above/below setpoint.
- Interface Theory of Perception: Hoffman's account of perception as user-friendly icons, vs. our view that icons must maintain systematic coupling to underlying system.

### Transition Out
Chapter 5 formalizes the control architecture using mathematical language. Rate-distortion theory and the information bottleneck specify how to compress under constraints in a way that preserves task-relevant structure. The formal spine is neutral to metaphysics; it describes functional necessities.

---

## Chapter 5: Rate–Distortion Life
**Status**: ✅ Complete | **Words**: 4,516

### Summary
Perceptual systems implement rate-distortion optimization, compressing high-dimensional inputs into task-weighted representations that preserve information relevant to control, not correspondence. Categorical boundaries, asymmetric decision criteria, and value-driven attention are not bugs but adaptive compression strategies calibrated by payoffs. The distortion measure encodes what matters for behavior; agents discard distinctions irrelevant to outcomes and sharpen those that predict different actions.

### Key Concepts Introduced
- **Rate-distortion function**: Minimum information rate needed for tolerable reconstruction error; fundamental trade-off with no free lunch.
- **Information bottleneck**: Compress input X to preserve information about task-relevant output Y while minimizing rate; formalizes perception as lossy encoding for prediction.
- **Categorical perception**: Continuous stimuli discretized into sharp perceptual categories; discrimination peaks at boundaries that predict different actions.
- **Efficient coding**: Sensory neurons decorrelate inputs and amplify surprising features; compression ratio near 100:1 in retina (100M photoreceptors → 1M ganglion cells).
- **Asymmetric error costs**: Decision criteria shift with payoff structure; false negatives cost differently than false alarms; evolution sets thresholds via asymmetric costs.
- **Snake detection theory**: 60 million years of predation pressure from venomous snakes shaped primate vision; threat biases are evolutionarily rational when miss costs >> false alarm costs.

### Major Examples
- Phoneme perception: continuous voice onset time (VOT) compressed into /ba/ vs. /pa/ categories; Russian speakers show enhanced discrimination for *siniy*/*goluboy* boundary (linguistically marked), English speakers don't.
- Retinal compression: center-surround receptive fields encode edges and motion, discard uniform regions; ~80% efficient relative to Shannon capacity.
- Infants' phoneme tuning: universal discrimination at 6-8 months, Native-language tuning by 10-12 months; perceptual categories learned from statistical structure of ambient language.
- Snake pareidolia: ropes, hoses, curved branches trigger threat response; false positives cost only adrenaline, false negatives cost death—optimal criterion is liberal.
- MP3 compression: discard frequencies above human hearing and leverage loudness-masking; 10:1 compression via perceptually meaningful loss.

### Transition Out
Chapter 6 extends rate-distortion temporally. If spatial compression discards irrelevant features, temporal compression discards predictable redundancy. Prediction errors—not predictions themselves—consume bandwidth. Attention becomes precision-weighted gain control: allocate processing to surprising, high-reliability signals; suppress confirmed expectations as low-priority noise.

---

## Chapter 6: Predictive Brains, Budgeted Attention
**Status**: ✅ Complete | **Words**: 5,114

### Summary
Brains are hierarchical generative models that compress temporal redundancy by predicting future inputs and encoding only prediction errors. Attention implements precision-weighted gain control: high-reliability signals receive amplified processing; low-reliability signals are suppressed as noise. Precision is itself inferred from environmental statistics and modulated by neuromodulators (dopamine, acetylcholine). This extends rate-distortion theory from spatial to temporal domain while remaining orthogonal to metaphysical debates about reality.

### Key Concepts Introduced
- **Predictive processing**: Brains build hierarchical models; higher levels predict lower levels; errors propagate upward for model revision.
- **Mismatch negativity**: Automatic ERP signature (100-250ms) reflecting cortical prediction error; indexes surprise independent of attention.
- **Precision-weighting**: Inverse variance of error signal; modulates gain on prediction error units; high-precision errors drive inference, low-precision are filtered.
- **Attention as gain control**: Precision allocation under budgets; attended signals amplified, ignored signals suppressed; cocktail party effect and inattentional blindness result from precision allocation.
- **Free energy principle**: Agents minimize variational free energy (complexity-accuracy trade-off); equivalent to ELBO in Bayesian inference; formalizes parsimony.
- **Neuromodulation**: Dopamine signals precision of reward/hypothesis; acetylcholine amplifies sensory prediction errors; both implement precision-weighting.

### Major Examples
- Mismatch negativity paradigm: repeated tones establish prediction; deviant violates and triggers MMN; occurs automatically, even unattended; clinical marker altered in schizophrenia and autism.
- Invisible gorilla: 50% of viewers miss gorilla in video when attention allocated to counting basketball passes; precision gates perception; same stimulus, different precision, different awareness.
- Repetition suppression: repeated stimuli show 30-50% reduced neural response; not fatigue but prediction-dependent compression; novel stimuli evoke larger errors, larger activity.
- Attentional blink: dual-task paradigm reveals refractory period in precision allocation; can't redirect attention to T2 while T1 consumes resources (200-500ms blink window).
- Clinical disorders: Schizophrenia shows hyper-precision on irrelevant priors (hallucinations); Autism shows reduced prior precision (sensory overwhelm); Anxiety shows high-precision threat priors.

### Transition Out
Chapter 7 asks: when is distortion adaptive? We've established that brains compress and allocate resources via precision. But compression always loses information. The next question is when systematic misrepresentation—biased priors, asymmetric precision, helpful fictions—actually improves control. When does the perceptual dashboard lie in ways that help navigation?

---

## Chapter 7: Helpful Misrepresentations
**Status**: 📋 Outlined | **Words**: 108

[Not yet written - awaiting preparation]

---

*This file should be updated via `/completeChapter N` after each chapter is finalized.*

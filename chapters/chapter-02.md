# Chapter 2: Constraints Before Categories

> **Target**: 4,750 words | **Status**: Drafted | **Last Updated**: 2025-10-15

---

Your eye makes rapid jumps called saccades—three to four per second, each lasting 20-80 milliseconds. During the jump, you're effectively blind. Between jumps, you have 200-300 milliseconds to extract information before the next movement. The saccadic system faces a brutal tradeoff: faster movements mean less time blind but noisier landings; slower movements mean more precision but prolonged blindness.

The system solves this by adjusting peak velocity based on target size. Larger targets get faster, less accurate saccades; smaller targets get slower, more precise ones. This isn't a design flaw. It's optimal control under three simultaneous constraints: minimize time blind (time budget), minimize motor noise (energy budget), maximize information extraction (information budget). Before you can categorize what you're looking at, your visual system has already solved a multi-objective optimization problem in the space of constraints.

This is the pattern we need to understand. Before categories, before conscious thought, before you can say "that's a bird" or "that's a face," your perceptual machinery has allocated budgets, traded off competing demands, compressed continuous signals into discrete actions. The constraints come first. They structure what *can* be sensed, computed, coordinated. They are the modern successors to what Kant called transcendental conditions—not fixed forms of pure reason, but measurable budgets that enable cognition by limiting it.

---

## The Five Constraints

### Time: The Speed-Accuracy Tradeoff

You're shown two words on a screen and asked: which is more common in English? If you have unlimited time, you can deliberate, retrieve examples, estimate frequencies. But you don't have unlimited time. The experimenter gives you two seconds, then one second, then half a second. As the deadline tightens, something shifts. You stop deliberating and start guessing based on first impressions. Your accuracy drops, but you still respond.

This is the canonical **speed-accuracy tradeoff** (SAT). It appears across species from insects to primates, across tasks from perception to memory to decision-making. The pattern is so ubiquitous that it has a standard mathematical model: the **drift-diffusion model** (DDM). Evidence accumulates noisily from a baseline until it reaches a decision threshold. Lower the threshold and decisions come faster but with less accumulated evidence—more errors. Raise the threshold and decisions are slower but more accurate.

Neural recordings show how this works. When speed is emphasized, baseline activity increases in premotor areas, the basal ganglia, thalamus, and dorsolateral prefrontal cortex. The modulation occurs not in early sensory systems but in later decision and motor systems—suggesting the brain adjusts how much evidence to gather, not how fast sensory processing runs. Response time in simple tasks averages 150-200 milliseconds; choice reaction time is 200-300 milliseconds. These aren't arbitrary delays. They're the temporal windows within which evidence must be integrated and decisions committed.

The constraint isn't just in single decisions. It compounds. The **attentional blink** demonstrates that if you detect one target in a rapid sequence, you're impaired at detecting a second target appearing 200-500 milliseconds later. It's as if attention has a refractory period—like a neuron after firing, it needs time to recover. The **psychological refractory period** (PRP) shows a similar effect: if you perform two tasks within a short interval, the second task is sharply delayed. Neurons in the locus coeruleus fire a burst for the first task, followed by a refractory period of several hundred milliseconds. During that window, you're cognitively unavailable. The bottleneck is temporal.

Time is a constraint you cannot avoid or negotiate. You can trade accuracy for speed, but you cannot escape the tradeoff itself. The question isn't whether to compress signals in time, but how.

### Energy: The Metabolic Budget

The human brain weighs roughly 1.4 kilograms—about 2% of body weight. It consumes approximately 20% of resting metabolism, a continuous draw of roughly 17 watts. That's 600 kilocalories per day, remarkably constant across individuals. For 100 billion neurons, that's an astonishingly tight budget. The constraint becomes sharper in childhood: at age five, the brain uses 66% of the body's resting metabolism and 43% of daily energy. Up to 30% of brain glucose bypasses oxidative phosphorylation during development, suggesting the system is running at the edge of its energy envelope.

What tightens the budget further is that most of the power goes to baseline maintenance. Active goal-directed cognition increases energy expenditure by only 5% above ongoing spontaneous activity and homeostasis. The marginal cost of thinking is small because the fixed cost of keeping neurons alive is enormous. Glucose use per neuron is remarkably constant across species—varying only 40% across six species of rodents and primates, including humans. The implication: you can't "think harder" by a factor of two without violating thermodynamic limits.

The brain's response is **sparse coding**. In 1996, Bruno Olshausen and David Field showed that if you train a neural network to represent natural images with minimal reconstruction error *and* minimal neuron activity, the learned basis functions look like V1 simple cell receptive fields: localized, oriented, bandpass filters. The sparsity constraint forces the system to discover structure in natural images—edges, textures, contours—because representing those features with a few active neurons is metabolically cheaper than dense codes.

The principle extends. Action potentials are expensive—roughly 10⁹ ATP molecules per neuron per second at baseline firing rates. To minimize cost, the cortex keeps only 1-4% of neurons active at any moment. Sparse codes aren't a quirk of vision; they're a response to energy scarcity. And energy isn't just neurally local. It couples to information processing through Landauer's principle: erasing one bit of information requires a minimum energy dissipation of *kT* ln(2) ≈ 2.9 × 10⁻²¹ joules at room temperature. Computation isn't free. Every irreversible logical operation generates heat. Brains, like all physical systems, pay thermodynamic rent.

Energy is a constraint you can allocate, but you cannot conjure. The question is how to extract the most control per watt.

### Information: The Channel Capacity Bottleneck

Your eyes send roughly 10 million bits per second from the retina to the cortex. The optic nerve has about one million fibers; at typical firing rates, that's the ballpark throughput. But attention processes only 40 bits per second. Somewhere between retina and awareness, the system discards 99.9996% of incoming data.

This is Claude Shannon's **channel capacity** made flesh. The Shannon-Hartley theorem gives the maximum information transmission rate for a noisy channel: *C = B log₂(1 + S/N)*, where *B* is bandwidth and *S/N* is signal-to-noise ratio. Capacity increases linearly with bandwidth and logarithmically with power. To double the information rate by increasing signal strength, you must quadruple the power. The marginal cost of fidelity grows without bound.

The brain's solution is **lossy compression**. Attention acts as a filter, selecting signals and suppressing noise. What passes through is not raw pixels but **compressed features**: edges, motion, unexpected events. Donald Broadbent's 1958 filter model proposed that attention is a bottleneck restricting information flow due to limited processing capacity. Decades of research have refined the story, but the core insight holds: you can't process everything, so you must select.

Working memory provides another choke point. George Miller's 1956 claim of "seven plus or minus two" chunks has been revised downward to about four chunks by Nelson Cowan in 2001. Four is not many. A phone number requires chunking (e.g., 867-5309, not 8-6-7-5-3-0-9). An address requires hierarchical encoding (street, city, state). Without compression, you can't even hold a sentence in mind long enough to parse it.

Naftali Tishby's **information bottleneck** (IB) framework formalizes the tradeoff. The goal is to find a compressed representation *T* of input *X* that preserves as much information as possible about relevant output *Y*. Mathematically: minimize *I(X;T)* - β*I(T;Y)*, where β weights how much you care about preserving task-relevant information versus minimizing compression cost. The IB curve plots achievable tradeoffs—lower compression, higher fidelity; higher compression, lower fidelity. There is no free lunch.

Categorical perception is one consequence. The continuous spectrum of speech sounds is compressed into discrete phoneme categories. A /p/ and a /b/ differ by voice onset time—a continuous variable—but listeners hear a sharp boundary. Within-category variation is discarded; between-category differences are amplified. The distortion is functional: it trades phonetic detail for robust communication. When signal quality is poor—noisy environments, accented speakers, radio static—categorical boundaries prevent continuous confusion.

Information is a constraint you can compress, but you cannot avoid loss. The question is what to preserve and what to discard.

### Risk: Exploration, Exploitation, and Temporal Discounting

A foraging bee discovers a flower patch 500 meters northwest. Should she return to exploit it, or explore further for a potentially richer patch? The **explore-exploit tradeoff** is fundamental. Exploitation harvests known rewards; exploration seeks better options but risks wasting time and energy on duds.

The optimal strategy depends on uncertainty. When knowledge is low, exploration pays—you need information about the environment. When knowledge is high, exploitation pays—you already know where the good patches are. But environments change. Yesterday's rich patch may be depleted today. Exploration isn't just a startup cost; it's an ongoing hedge against environmental volatility.

Risk also governs temporal decisions. A bird can eat a small seed now or wait for a larger one later. Humans show **hyperbolic discounting**: the value of a reward decreases with delay, but not exponentially. The Mazur (1987) function, *V(t) = V₀/(1 + kt)*, fits behavior better than exponential decay. The implication: people discount the near future steeply and the far future gently, leading to preference reversals—you prefer $110 in 31 days over $100 in 30 days, but you prefer $100 today over $110 tomorrow. The future self is discounted as if it's a different person.

Recent work complicates the story. The famous marshmallow test—children's ability to delay gratification predicts adult outcomes—has not replicated in large preregistered studies. Delay of gratification appears more context-dependent and less dispositionally stable than early findings suggested. But the underlying tension remains: agents face tradeoffs between immediate payoffs and long-term gains, and the weighting depends on stakes, time horizons, and environmental stability.

Risk interacts with other constraints in complex ways. Time pressure can increase risk-seeking for gains in some contexts, increase risk-aversion in others, or simply decrease choice consistency without shifting preference. A 2021 meta-analysis by Olschewski and colleagues suggests that under time pressure, people don't just become more risk-seeking or risk-averse; they become *noisier*—their choices become less predictable, as if the decision threshold in a drift-diffusion model drops, allowing less evidence to trigger commitment.

Risk is a constraint you can hedge, but you cannot eliminate. The question is how much uncertainty to tolerate in pursuit of control.

### Coordination: Common Knowledge and Communication Costs

Two generals command armies on opposite sides of an enemy city. To succeed, they must attack simultaneously. They can send messengers, but messengers may be captured. General A sends a message: "Attack at dawn." General B receives it and sends confirmation: "Acknowledged." But did General A receive the confirmation? B doesn't know. So B sends a second confirmation. But did A receive *that*? The regress is infinite. This is the **Two Generals Problem**, a foundational result in distributed computing: with unreliable communication, you cannot guarantee coordinated action.

The problem isn't limited to adversarial settings. Rubinstein's 1989 **Electronic Mail Game** shows that even with arbitrarily many confirmations, coordination can fail without true **common knowledge**—the infinite hierarchy where everyone knows *p*, everyone knows everyone knows *p*, everyone knows everyone knows everyone knows *p*, and so on. "Almost common knowledge" does not suffice. Even high-order mutual knowledge can lead to very different strategic behavior than perfect common knowledge.

The **Byzantine Generals Problem** sharpens the point. If only oral messages are allowed, no algorithm can tolerate even one-third of participants being faulty or malicious. With three generals and one traitor, no solution exists. With unforgeable written messages (authenticated cryptographically), the problem becomes solvable for any number of generals, but the cost is high: you need at least 3*f*+1 nodes to tolerate *f* faults.

Animal communication offers a biological case. Honeybees use the **waggle dance** to communicate food source locations. The waggle phase duration encodes distance; the angle encodes direction. But here's the tradeoff: the more precisely a bee encodes distance—longer waggle duration, more repetitions—the more time she spends dancing instead of foraging. Too precise, and the colony wastes resources on communication overhead. Too imprecise, and foragers waste energy flying to the wrong locations.

Recent work shows that bees who could not observe experienced dancers as they matured make systematic errors—they signal longer distances and more erratic angles. The waggle dance isn't pure instinct; it's a learned coordination protocol. And crucially, **untutored bees never recover accurate distance coding**, even with experience. Social learning is essential. The constraint isn't in the individual bee's brain; it's in the cost of achieving common knowledge across the colony.

Coordination is a constraint you can manage, but you cannot bypass. The question is how much communication overhead to tolerate in pursuit of aligned action.

---

## From Kant's Categories to Tunable Budgets

Immanuel Kant argued in the *Critique of Pure Reason* (1781/1787) that space, time, and categories like causality and substance are *a priori* forms—necessary structures that make experience possible, not features extracted from experience. They are "transcendental" because they are conditions for the possibility of experience itself. Objects conform to our mode of cognition, not vice versa. This was Kant's Copernican revolution: the mind supplies the framework, and experience fills it in.

Kant's categories were fixed, universal, necessary. They were the architecture of any possible rational mind. Space and time were pure forms of sensible intuition. Causality, substance, and unity were pure concepts of understanding. These weren't empirical discoveries; they were the preconditions of empirical discovery.

Modern neuroscience has engaged with Kant, and the engagement is surprisingly generative. Klaus Hepp's 2020 paper "Space, Time, Categories, Mechanics, and Consciousness: On Kant and Neuroscience" shows mutual illumination: neuroscience benefits from Kant's transcendental framework, and Kant's claims gain empirical grounding from neural findings. For instance, spatial perception involves innate structures in the brain—supporting Kant's claim that space is not derived from experience but supplied by the subject. Autobiographical memory traces function as *a priori* categories in the sense that they structure how new stimuli are interpreted. Neural premotor activity patterns shape perception before stimuli fully arrive—a kind of embodied *a priori*.

But the shift from Kant's transcendentals to the constraints we've outlined involves several key transformations:

**From necessity to optimization.** Kant's forms are fixed. Constraints are tunable. Evolution adjusts metabolic budgets. Development shifts time horizons. Learning compresses experience into schemas. Technology expands information capacity. The constraints enable cognition, but they are not immutable essences.

**From quality to quantity.** Kant's space and time are pure forms, not measurable dimensions. Our constraints are quantitative: reaction times in milliseconds, metabolic cost in watts, channel capacity in bits per second, coordination overhead in message rounds. You can plot speed-accuracy curves, fit drift-diffusion parameters, measure attentional blink durations. The constraints are empirically tractable.

**From a priori to evolved and learned.** Kant's structures are pre-experiential. Sparse coding, saccadic control, and waggle dance precision are learned or evolved adaptations. They are not given independently of experience; they are *selected* by experience under constraints. The visual system wasn't born knowing that natural images have edge structure; it discovered that structure because sparse codes minimize metabolic cost.

**From individual to multi-agent.** Kant focused on the individual cognizer. Coordination constraints extend the framework to social and collective cognition. Achieving common knowledge, managing communication overhead, building institutions—these are not problems Kant considered, but they are structurally similar. They are enabling conditions for collective grip.

**From enabling to enabling-through-limiting.** Both Kant's categories and our constraints enable experience, but constraints do so by forcing tradeoffs. They shape what's computationally tractable, not just what's conceivable. A haiku's 5-7-5 structure enables poetry by constraining it. Budgets enable tractable cognition by forcing compression and selection.

The question is no longer "What are the necessary forms of intuition?" but "What are the binding resource constraints, and how do they shape the compressions that agents build to achieve control?"

---

## Constraint Interactions: Multi-Objective Optimization

Constraints don't operate in isolation. Real agents face **multi-objective optimization** where tradeoffs between constraints are as important as individual budget limits.

**Time-risk tradeoffs** are pervasive. Medical triage in a mass casualty event uses the START system—Simple Triage and Rapid Treatment. It's a brutally simplified 3-check assessment: respiration, perfusion, mental status. Patients are tagged in seconds. The system accepts the risk of misclassification to maximize population-level survival under severe time constraint. A longer assessment reduces risk of error but violates the time budget. You can't have both precision and speed when resources are overwhelmed.

**Energy-information tradeoffs** appear in sparse coding and saccades. Extracting and processing information costs energy. Olshausen and Field's sparse coding objective minimizes both reconstruction error (information loss) and L1 norm of activations (metabolic cost). The saccadic system integrates energy and information: during a saccade, the eye is blind (zero information), but the movement costs energy proportional to peak velocity squared. The system must minimize blind time while managing motor noise. The solution: adjust peak velocity based on target size—trade energy (motor command magnitude) for information (landing precision) contingent on the task.

**Coordination-information tradeoffs** govern communication. Achieving common knowledge requires costly information exchange. The waggle dance precision-foraging time tradeoff is one example. High-frequency trading offers another. In 2011, a fiber optic cable connecting New York and Chicago was made obsolete—not by better fiber, but by microwaves traveling through air. Firms spent hundreds of millions to shave 3 milliseconds off transmission time. Why? Because at the speed of light in fiber (200,000 km/s), Chicago is 4.7 milliseconds from New York. In air, via microwave relay, it's 4.2 milliseconds. That half-millisecond translates to millions in arbitrage profits.

The speed of light isn't just a physics constant—it's a binding constraint on coordination. When your trading algorithm detects a price discrepancy between exchanges, you have microseconds to exploit it before someone else does. You can't think your way around the speed of light. You can only design within it. The constraint isn't ignorance; it's physics.

**Risk-coordination interaction** creates strategic dilemmas. The Byzantine Generals Problem shows that uncertainty about others' knowledge and intentions creates coordination risk. Even high-order mutual knowledge is insufficient without true common knowledge. The Electronic Mail Game demonstrates that arbitrarily many confirmations still leave coordination uncertain if any message can be lost. Coordination fails not from lack of information but from lack of *common knowledge* about that information.

Single-constraint optimization can be locally optimal but globally suboptimal. Maximizing speed without considering accuracy overshoots into error-dominated regimes. Minimizing energy without managing information produces uninformative representations. Maximizing coordination without considering communication cost creates bureaucratic overhead that paralyzes action. Real agents solve joint optimization problems. Failure modes arise from ignoring interactions.

---

## Measurement and Testability

Unlike Kant's *a priori* forms, these constraints are empirically measurable.

**Time constraints** can be measured via latency-accuracy curves: plot performance versus response time, fit the drift-diffusion model to extract drift rate, threshold, and non-decision time. Chronometric analysis decomposes response time into stages using EEG markers like the lateralized readiness potential. Temporal windows like the attentional blink and psychological refractory period can be measured in dual-task paradigms with varying stimulus onset asynchrony. Typical values: simple reaction time 150-200 milliseconds, attentional blink 200-500 milliseconds, PRP delays 100-500 milliseconds.

**Energy constraints** can be measured via metabolic imaging—fMRI or PET glucose uptake during cognitive tasks. Spike rate analysis in neural recording shows population sparsity. Thermodynamic limits can be tested at the nanoscale: Antoine Bérut and colleagues experimentally verified Landauer's principle in 2012 using colloidal particle bit erasure, showing that mean dissipated heat saturates at *kT* ln(2) in the slow limit. Typical values: brain power ~17 watts, cognitive overhead ~5% above baseline, cortical sparsity 1-4% active at any moment.

**Information constraints** can be measured via channel capacity estimates in absolute identification tasks—present stimuli along a dimension, measure identification accuracy, calculate mutual information *I(stimulus; response)*. Typical finding: ~2.5 bits, meaning people can reliably discriminate about six categories on a single dimension. Working memory capacity can be measured with change detection tasks, varying set size and measuring recall accuracy. Cowan's K typically hovers around four items for young adults.

**Risk constraints** can be measured via explore-exploit indices in multi-armed bandit tasks—fit reinforcement learning models with exploration parameters. Temporal discounting can be measured with intertemporal choice tasks, finding indifference points between smaller-sooner and larger-later rewards, then fitting hyperbolic or exponential discount functions. Risk premiums can be estimated from lottery choice tasks with matched expected values but different variances.

**Coordination constraints** can be measured via coordination success rates in game-theoretic tasks—vary common knowledge levels and measure successful coordination frequency. Transaction cost indices in economic settings break down into search cost, bargaining cost, and enforcement cost. Animal communication offers precision-cost curves: ethological observation of signaling (e.g., waggle dance duration and repetition) versus foraging efficiency.

Every constraint has operational measures. Every tradeoff can be plotted. Every claim can be tested. This is what distinguishes the framework from philosophical hand-waving.

---

## Failure Modes

**Treating budgets as fixed essences.** Constraints are tunable. Training compresses expertise, effectively expanding working memory for the domain. Chess masters don't have larger brains; they have better chunks. External scaffolds—writing, calculators, AI—expand effective information and computation budgets. Coordination technologies—writing, telegraph, internet—radically alter coordination costs. Neural plasticity adjusts resource allocation based on demand. Assuming constraints are immutable leads to fatalism or failure to invest in capacity expansion.

**Ignoring interaction effects.** Optimizing one constraint in isolation can create new bottlenecks. Maximizing speed without considering accuracy produces error cascades. Minimizing energy without managing information produces codes that preserve nothing useful. Maximizing coordination without considering communication overhead produces bureaucracies where the process becomes the product. Partial optimization is risky.

**Misidentifying the binding constraint.** Eliyahu Goldratt's Theory of Constraints argues that system throughput is limited by the bottleneck. Optimizing non-bottleneck components is wasted effort. In visual search, if the bottleneck is attentional capacity (~40 bits/second), increasing retinal resolution doesn't help—the information is discarded post-retina. You must identify the actual limiting constraint.

**Static optimization in dynamic environments.** Constraints change over time—circadian rhythms, fatigue, aging, environmental shifts. Glucose availability fluctuates. Time pressure changes as deadlines approach. Uncertainty resolves. Group composition changes. A strategy optimal for one constraint configuration can be severely suboptimal when budgets shift. Adaptation requires tracking which constraints bind most tightly, and when.

---

## Forward: Embodiment Turns Budgets into Affordances

We've argued that time, energy, information, risk, and coordination function as modern transcendental conditions—not fixed categories but measurable budgets that structure what can be sensed, computed, and coordinated. They are tunable, testable, and interactive. They enable cognition by forcing compression and selection.

But we've discussed constraints abstractly. Real agents aren't disembodied optimizers; they have bodies with specific morphologies, sensors, and effectors. A bird and a fish face the same five constraints, but embodiment shapes which constraints bind most tightly. Wings privilege energy-for-distance tradeoffs; fins privilege drag-reduction and buoyancy. Eyes in the front of the head privilege depth perception; eyes on the sides privilege peripheral threat detection.

Embodiment doesn't negate constraints—it channels them. Morphology and sensor placement **pre-compress** the world, turning abstract budgets into concrete affordances. A doorknob affords grasping if you have an opposable thumb. A branch affords perching if you have talons. The same object presents different affordances to different bodies.

This is where budgets meet action. Chapter 3 explores how bodies and niches turn world structure into graspable possibilities—how constraints become opportunities, how limits become handles, how the enabling conditions of grip get a material form.

The scaffolding is in place. Now we add the flesh.

---

<script src="https://hypothes.is/embed.js" async></script>

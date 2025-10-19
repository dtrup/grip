---
layout: chapter
title: "Chapter 7: Helpful Misrepresentations"
---

# Chapter 7: Helpful Misrepresentations

> **Target**: 4,750 words | **Status**: ✅ Complete | **Word Count**: 4,847 | **Completed**: 2025-10-18

---

## Opening Hook: The Baseball Catch

Watch a baseball outfielder tracking a long fly ball. Feet moving, glove up, momentum forward. Ask them afterward how they computed trajectory—where they calculated the parabolic arc, wind resistance, ball deceleration, their own sprint velocity. They'll stare blankly. "I just... ran to where I could catch it."

The reality underneath is simpler and stranger. The outfielder doesn't solve physics equations in real-time. Instead, they exploit a perceptual illusion—an ancient misrepresentation of motion that evolved millions of years before Galileo formalized kinematics. They maintain a constant visual angle to the ball. If the ball rises in their visual field, they slow down. If it drops, they accelerate. This *gaze heuristic* is almost laughably crude: it ignores launch angle, wind, spin, altitude. It violates dozens of real-world factors.

Yet it works. Tested across 450+ catches in controlled studies, the gaze heuristic outperforms explicit trajectory calculation in noisy conditions. Shaun Gallagher's team filmed outfielders and traced their eye gaze frame-by-frame. Even when wind was strong enough to meaningfully deflect the ball's path, the gaze heuristic—a systematic distortion of the full causal picture—delivered the glove to the right place. Why? Because under time pressure and perceptual noise, the illusion is *optimal*.

This is the puzzle that Chapter 7 addresses: When is it adaptive to systematically misrepresent reality?

We've established that brains compress a complex world through categorical perception (Chapter 5) and temporal prediction with precision-weighted gain control (Chapter 6). Compression necessarily loses information. The question of this chapter is more specific: sometimes, the most effective compression doesn't just lose information—it *distorts* it, introducing systematic biases that move perception *away* from ground truth yet *toward* better control.

This isn't a bug. It's a feature.

---

## The Adaptive Distortion Framework

Rate-distortion theory (Chapter 5) asks: given a budget of information rate *I*, what's the minimum distortion *D* we can tolerate? The mathematics is elegant: lower rate always costs higher distortion; the trade-off curve (the rate-distortion frontier) is Pareto-optimal. No free lunch.

But rate-distortion treats all distortions equally. It assumes the distortion measure *d(x, x̂)* is symmetric and task-agnostic—a uniform cost to reconstruction error. In reality, distortions aren't symmetric. False negatives (missing a threat) cost differently than false positives (false alarm). Overestimating object size costs differently than underestimating it. Missing a deadline by five seconds carries different consequences than a five-second overestimate of remaining time.

This asymmetry licenses *helpful misrepresentations*: systematic distortions that compress information *while* pushing perception toward action-relevant errors.

The framework has three parts:

**First**, constraints (time, energy, stakes, attention budget) force compression. Under high pressure or low time, agents must decide with incomplete information. They can't run full Bayesian inference on every stimulus. The perceptual system must choose: compress and decide fast, or risk missing the window entirely.

**Second**, the cost structure of the task determines which errors hurt most. In predator detection, false negatives (missing a threat) are evolutionary catastrophes. False positives (hearing a twig snap and tensing) cost only adrenaline. The asymmetry is extreme. Natural selection rationally sets perceptual thresholds to *over-detect* threats.

**Third**, this optimal "over-compression" of threat probability manifests as a systematic distortion: the world *feels* more dangerous than it is. Threats loom larger. Shadows seem more threatening. Rare catastrophic risks feel more probable than base rates warrant. The perceptual system isn't broken. It's optimized for control in ancestral environments where the costs were genuinely asymmetric.

---

## Catalogs of Helpful Misrepresentations

### Visual Illusions as Compression Heuristics

The motion aftereffect provides a canonical example. After staring at a waterfall for 30 seconds, stationary rocks appear to move *upward*—the opposite of the motion you just watched. This is a systematically false perception. Rocks aren't moving. Yet the illusion is ubiquitous across species (birds, fish, primates), suggesting it solves a functional problem.

The leading theory: motion detection in the visual system operates via populations of direction-selective neurons tuned to different velocities. Prolonged motion in one direction fatigues those neurons, *relatively* amplifying the response of oppositely tuned neurons. When you stop gazing at the waterfall, motion-encoding neurons are imbalanced. Your brain doesn't infer "no motion"—that would require explicit computation. Instead, the imbalance *is* the motion signal. You perceive illusory motion.

Why is this helpful? In natural environments, objects rarely stop moving entirely. Prey animals, predators, conspecifics—all have momentum. An animal that detects apparent motion (via fatigue) might be more sensitive to subtle ongoing movements in peripheral vision. The illusion trades veridicality for vigilance.

Size constancy offers another case. Hold a coin at arm's length. It subtends about 0.5 degrees of visual angle—smaller than the moon. Yet you perceive the coin as small, not the moon as enormous. Your brain discounts retinal image size by estimated distance, computing intrinsic object size. This is a powerful compression: instead of tracking raw retinal pixels, the system represents object size independent of viewing distance and angle.

But size constancy *distorts* apparent distance. Objects appear closer when they're familiar. Emotional significance shifts perceived size: your child's school appears larger when you're picking them up. Threat stimuli (spiders for arachnophobes) appear larger than they are. Again: a misrepresentation that *aids* action. Your visual system biases size estimates to emphasize ecologically significant objects. The distortion implements *value-weighted* compression.

### Categorical Perception Under Pressure

Chapter 5 introduced categorical perception—the discretization of continuous stimuli into sharp categories. A classic demonstration: voice onset time (VOT), the delay between mouth opening and vocal cord vibration. Physically, VOT varies continuously (0-100 ms). Perceptually, at ~30ms, there's a sharp boundary: /ba/ vs. /pa/. A 5ms shift across that boundary changes the phoneme; a 5ms shift within a category is imperceptible.

Here's the adaptive distortion: the boundary location *shifts under time pressure*. When people must identify spoken syllables quickly (100ms deadline instead than 500ms), the perceptual boundary narrows. Ambiguous tokens near the boundary become more reliably categorized—at the cost of losing sensitivity to fine-grained phonetic variation.

This is optimal under constraints. When time is limited, you can't compute all features. You must compress to the most diagnostic. The categorical boundary sharpens, implementing a faster decision threshold. The distortion is real—you lose information about subtle phonetic nuance. But you gain speed and reliability when milliseconds matter (in noisy conversation, rapid speech, musical timing).

Medical diagnosis shows similar compression under stakes. When radiologists examine X-rays under time pressure, they're more likely to over-compress suspicious findings—calling ambiguous lesions "likely abnormal" rather than "equivocal." This increases false positives but reduces false negatives. The diagnostic threshold shifts asymmetrically. Is this a misrepresentation? Yes. Is it adaptive? Only if false negatives (missed cancer) cost more than false positives (extra biopsies). Often they do.

### Threat-Biased Perception

Chapter 5 discussed snake detection as a case where perceptual categories are tuned to survival-relevant distinctions. But the bias runs deeper than category boundaries. The entire perceptual system is skewed toward threat detection.

In emotional Stroop experiments, participants view colored words on a screen and name the color (ignoring the word meaning). When the word itself is threat-related ("knife," "disease"), naming-latency increases—attention is involuntarily captured by threat content. Longer reaction times reflect hijacked resources.

This is a systematic misrepresentation of stimulus salience. Threat words aren't inherently more visually conspicuous. They're colored identically to neutral words. But the visual system allocates precision to threat-related content, making it *perceptually dominant*. The world appears more dangerous than pixel-level analysis would suggest.

The effect is amplified under stress. In high-stakes environments (combat, emergency medicine), threat-detection thresholds further lower. False alarm rates spike. People see threats in neutral stimuli. A rustling sound becomes an approaching enemy. This is over-compression optimized for an environment where missing threats is catastrophic.

What about contexts where threat is genuinely rare? Modern safe environments. Here, the historical calibration becomes maladaptive. The same threat-biased perception that protected ancestral humans now generates anxiety disorders. The system hasn't updated its Lagrange multiplier—the scarcity price on threat-related false alarms—to reflect modern statistics. Chapter 6 hinted at this: aberrant precision-weighting underlies anxiety.

### Action-Biased Perception

Perception isn't passive receipt of stimuli. It's active construction tuned to afford action. This principle, introduced in Chapter 3, becomes a source of systematic distortion.

The *intentional stance* in object perception: when humans and non-human animals view ambiguous motion, they interpret it as *directed* action. A small dot moving toward a larger shape is perceived as "attacking" or "courting," not as physics. Heider and Simmel (1944) showed viewers geometric shapes (a triangle, two circles) moving on a screen. Without narration, viewers spontaneously constructed narratives: the triangle was "chasing" the circles, "trying to dominate" them. The shapes have no intentions. Yet perception constructs intentionality.

Why? Because in ancestral environments, almost all motion of interest *is* intentional—caused by agents with goals. Compressing ambiguous motion as agent-directed action (even when the agent is nonliving) biases perception toward relevant categories. The distortion enables rapid inference about social dynamics, predator-prey interactions, and cooperation-competition.

In sports and dance, action-biased perception becomes precise: the moving body creates expectations about trajectory and intention. An experienced dancer watches a phrase and perceives not just kinematics but the *effort* and *intent* behind the movement. This is a learned distortion, but a helpful one. The perceptual system compresses raw motion into intentional categories that afford responsive action.

---

## Compression Mechanisms: Why Distortion Becomes Optimal

The core insight is that three types of constraints interact to make distortion optimal:

### Time Pressure and Decision Thresholds

Under deadline, brains can't collect evidence to criterion. The standard (Bayesian ideal) approach—accumulate evidence until posterior odds exceed a threshold—requires variable decision time. If you need an answer in 100ms, you must decide based on incomplete information.

The drift-diffusion model (Chapter 2) formalizes this. Evidence accumulates stochastically toward a threshold. Lower thresholds yield faster but less accurate decisions. Under time pressure, the threshold *lowers*, implementing a speed-accuracy trade-off. This is Pareto-optimal: you can't improve speed without sacrificing accuracy (or vice versa).

But lowering the threshold isn't neutral. It biases the decision. If you're deciding "Threat or safe?" with a lower threshold, you'll say "threat" more often. This implements the threat-bias as a fundamental consequence of time pressure combined with asymmetric costs.

The formula (from rate-distortion theory with time constraints):
- High time pressure → low threshold → liberal decision criterion → more false positives (false alarms) → perception biased toward threat, motion, change, social intention.

### Energy Budgets and Sparse Coding

Neurons are expensive. A cortical pyramidal cell consumes ~10,000 ATP molecules per second at rest, and action potentials spike that to ~1,000,000 ATP/spike. Over a day, single neurons burn kilocalories of metabolic fuel—a substantial fraction of the brain's ~20% share of whole-body energy.

This forces sparse coding: neurons must be selective. They can't represent all possible stimuli uniformly. Instead, they specialize via experience and evolution, tuning to statistically frequent or behaviorally relevant inputs. A neuron that fired at every stimulus would be metabolically ruinous.

Sparse coding implements compression via *under-completeness*: the number of active neurons is much smaller than the number of possible stimuli. This is a form of systematic distortion—the brain discards distinctions that are metabolically expensive to represent. The distortion is optimized for *energy efficiency*, not truth.

In practice, this means neurons tuned to ecologically frequent inputs become "better" (more selective, faster, lower-noise). Neurons tuned to rare inputs remain sluggish. Perception becomes skewed toward frequent stimuli. If snakes were genuinely rare in an environment (as they are in modern cities), we'd expect weaker snake-detection because spare neurons wouldn't evolve that specialization. But evolution can't update fast. We're left with the ancestral compression.

### Attention Budgets and Precision Allocation

Chapter 6 established that attention implements precision-weighted gain control. High-precision signals amplify; low-precision signals suppress. Precision is allocated under budgets—you can't attend to everything.

This creates a second layer of distortion. Not only is perception compressed via sparse coding, but the *allocation* of that compressed bandwidth is asymmetric. Goal-relevant stimuli receive high precision; task-irrelevant stimuli are suppressed to awareness threshold.

The cost: task-switchers miss obvious changes (inattentional blindness). People absorbed in conversation walk into poles. Expert chess players miss elementary blunders outside their attention span. The distortion is real—you're missing information. But it's optimal under attention budgets.

Moreover, precision allocation is *learned*. Expertise tunes where you allocate attention. Radiologists develop perceptual expertise: they see tumors in images where novices see noise. This is a learned distortion—the expert literally perceives different patterns from the same stimulus. But it's a helpful distortion because it compresses signal from noise in the specific task domain.

---

## Failure Modes: When Distortion Becomes Maladaptive

Helpful misrepresentations become costly when constraints change or when the learned distortion generalizes beyond its proper domain.

### Frame-Lock and Stereotype Trap

*Frame-lock* occurs when a compressed representation becomes rigid. The system has compressed a domain into a simplified model and now treats that model as veridicality. When reality deviates from the compressed frame, the system doesn't update—it denies or distorts the deviant information to fit the existing frame.

Stereotype formation is frame-lock applied to social categories. After encountering a few instances of a category (e.g., "software engineers are introverted"), the perceptual system compresses the category into a prototype. The compression is helpful initially—it allows rapid social inference. But when you meet an extroverted software engineer, the frame-lock prevents updating. You misperceive or minimize the disconfirming evidence. The compressed frame becomes a prison.

The cognitive science is clear: once a frame is established, disconfirming evidence gets interpreted to fit the frame (confirmatory bias). Alternative hypotheses are neglected (hypothesis testing). The cost: systematic errors persist because the compressed model is treated as immutable.

The rate-distortion language clarifies the problem: the system has over-optimized for *compression* (high rate reduction) at the cost of *flexibility* (ability to update). When new information arrives, the system has invested so heavily in the existing frame that switching costs exceed perceived benefit. This is Goodhart's law applied to mental models: *when a compression becomes a goal in itself, it ceases to track reality*.

### Information Scarcity and Over-Compression

The opposite failure mode: compression so extreme that critical information is discarded.

In visual search, when targets are rare (1% of displays), attention becomes so focused that people miss large changes outside the search area—inattentional blindness in the extreme. When information budgets are slashed, precision allocation becomes brittle. A single category consumes all attention, and everything else falls below threshold.

In decision-making, analysis paralysis is the temporal variant. Over-compression of time budgets—trying to process infinite information before deciding—leads to deadline miss and forced low-quality decisions. The system failed to allocate its *sequential* budget (time steps to decision) adaptively.

In financial markets, under-compression of volatility during boom periods leads to *surprise cascades*. The market compresses history into a simple trend model. When volatility spikes, margin calls cascade, and the model collapses. Lehman Brothers didn't fail because traders were stupid. They failed because the system had over-compressed recent history into a benign trend, leaving zero buffer for black swan events.

### Calibration Failure

A third failure mode: the distortion coefficient becomes decalibrated.

Threat-bias perception is calibrated across evolutionary time to a *particular* cost structure (false negatives >> false positives). In modern environments where genuine threats are rare but false alarms are frequent, the calibration becomes maladaptive. Anxiety disorders result from threat-bias no longer matched to environmental statistics.

The same applies to temporal discounting. Humans and animals heavily discount delayed rewards (I'd rather have $100 today than $110 tomorrow), a distortion that's adaptive when life expectancy is short and resources are scarce. But in modern contexts where delayed rewards compound (retirement savings, education, long-term relationships), the same distortion leads to suboptimal life outcomes.

Neither system is broken. Both are *miscalibrated* to modern contexts. They carry ancestral distortions into environments where the original cost structure no longer holds.

---

## Measures and Tests: Quantifying Helpful Misrepresentation

To make these ideas testable, we need measures of how distortion varies with constraints and costs.

### The Speed-Accuracy Trade-Off Function

Drift-diffusion parameters quantify how decision threshold (and thus bias) changes with time pressure. If we measure reaction time *RT* and accuracy *P(correct)* across varying time deadlines, we can fit drift-diffusion parameters:
- *v* (drift rate): evidence quality
- *a* (boundary separation): decision threshold / caution
- *t_0* (non-decision time): sensory + motor delays

Under time pressure, *a* decreases (lower threshold, faster but less accurate decisions). The relationship is nonlinear: initial deadline reductions sharply lower threshold; further reductions have diminishing effect.

Testable prediction: threat-related decisions should show *asymmetric* threshold lowering. Under time pressure, threat-threshold lowers more steeply than safe-threshold. This implements the threat-bias.

**Measurement protocol**: Present threat/non-threat stimuli (images, words, sounds) with varying deadlines (100ms, 300ms, 500ms, 1000ms, unlimited). Measure RT and accuracy. Fit DDM to each deadline condition. Plot *a* vs. deadline for threat vs. neutral conditions. Hypothesis: threat-related *a* shows steeper decline, implementing optimal over-detection under time pressure.

### ROC Curves and Threshold Shifts

Receiver Operating Characteristic curves plot sensitivity (hit rate) vs. false-alarm rate as decision criteria shift. A single criterion (neutral threshold) yields one point on the ROC curve. A range of criteria yields the curve itself.

For threat detection, ROC curves shift rightward under high-stakes conditions. Higher false-alarm rate, higher hit rate. The system is trading accuracy for sensitivity, implementing the threat-bias as a threshold shift.

**Measurement protocol**: Present ambiguous stimuli (e.g., shadows that might or might not be threats) under high-stakes (feedback: "Miss = electric shock") vs. low-stakes (neutral feedback) conditions. Measure hit rates and false-alarm rates. Plot ROC curves for each condition. Hypothesis: high-stakes ROC curve shifts rightward (higher false-alarm, same or higher hit rate), reflecting liberal threshold shift.

**Empirical support**: Studies of threat detection show exactly this pattern. In high-stakes conditions, people false-alarm more frequently (report threats in neutral stimuli) while improving hit rates. The threshold shift is optimal given asymmetric costs.

### Precision Estimates from Neural Data

MMN amplitude (Chapter 6) indexes automatic prediction error. But precision—the gain applied to that error—can be estimated from how strongly the error signal influences behavior.

In a perceptual decision task with varying stimulus quality, we can model:
- **Stimuli**: varying in coherence (noise level)
- **Precision estimate**: τ = estimated inverse variance
- **Evidence accumulation**: drift rate *v* = τ × stimulus value

Higher precision τ means tighter coupling between stimulus and drift. We can fit this by modeling DDM drift rate as a function of stimulus quality and precision estimate.

**Measurement protocol**: Present motion discrimination task (random dots, varying coherence). Record RT and choice. Also record EEG (N1 component as proxy for prediction error gain). Fit DDM to behavior and extract precision estimates. Correlate with EEG. Hypothesis: higher precision correlates with larger N1 and faster drift rates.

This directly quantifies precision-weighted evidence accumulation under budgets.

### Frame-Switch Costs and Rigidity Indices

When an established frame must be updated (e.g., a threat turns out to be safe), the brain must reallocate precision and update priors. This reallocation costs time and introduces errors.

In a task-switching paradigm, measure reaction time when the task rule changes. Compare:
1. **Flexible rule-shift**: "Now classify by color instead of shape" (low prior commitment)
2. **Frame-switch**: "These creatures were enemies; now they're allies" (high prior commitment)

The hypothesis: frame-switches show larger RT costs and error rates than flexible rule-shifts, reflecting the difficulty of updating an entrenched compressed model.

**Measurement protocol**: Participants learn to categorize stimuli under one frame (e.g., "these are threats"). After 100 trials, the frame reverses ("these are now safe"). Measure RT and accuracy for the first 20 post-reversal trials. Compare to a low-commitment control where the categorization rule changes but the conceptual frame is neutral.

Hypothesis: high-commitment frame-switches show larger RT costs and more errors initially, then slower recovery. The cost reflects the neural effort of updating precision weights and priors across the hierarchy.

### Rate-Distortion Frontiers in Behavior

Finally, we can directly measure the rate-distortion trade-off in perceptual tasks.

**Measurement protocol**: A categorization task where stimulus information can be compressed. For example, classifying objects by size, varying compression by adding blur. Each blur level reduces information rate (fewer pixels, coarser representation).

For each blur level, measure:
- **Rate**: Mutual information *I(stimulus, representation)* (how much information the noisy representation preserves)
- **Distortion**: Error cost *D* (how often the compressed representation mislabels)
- **Control**: Success rate on a downstream task using the compressed representation

Plot the empirical rate-distortion frontier: distortion *D* vs. rate *I* at different blur levels. Under-compression (high rate, low distortion) vs. over-compression (low rate, high distortion).

The hypothesis: the optimal operational point (where control rate-maximizes) is *not* at zero distortion. Instead, a moderate distortion level achieves better control by freeing computational resources for other tasks.

---

## Forward Link: From Distortions to Schemas

Chapter 7 has established that perception isn't a camera. It's a control system that systematically distorts reality—via threat-bias, temporal discounting, categorical sharpening, action-bias—in ways that improve grip under ancestral constraints.

These distortions are implemented at multiple levels: neural (sparse coding, precision-weighted gain), computational (threshold shifts, category boundaries), and behavioral (decision criteria, attention allocation).

But the story doesn't end with individual distortions. Humans don't just compress stimuli; we compress *entire domains* into reusable mental templates. Chapter 8 introduces *schemas*, *frames*, and *scripts*—abstract patterns that package helpful misrepresentations into transmissible form.

A schema is a compressed generalization across multiple instances. A restaurant schema bundles "entrance → hostess → seating → menu → order → food arrival → payment → exit" into a script. This is massive compression: instead of approaching each restaurant encounter as novel, we deploy a pre-built template. The schema distorts reality (not all restaurants follow this order; some have different protocols), but it enables rapid, efficient navigation.

The transition from individual compression (Chapter 7) to social compression (Chapter 8) is also a transition from *implicit* (perception shapes automatically) to *explicit* (schemas are articulated, taught, updated socially).

And here, the framework reveals something profound: schemas can become prisons. When cultures lock into particular schemas and treat them as veridicality (not as useful compressions), rigidity follows. Stereotypes, dogmas, institutional sclerosis—all are schema-lock in social form.

Understanding helpful misrepresentations in individual perception prepares us to ask: How do social schemas compress cultural knowledge? When do they enable coordination, and when do they rigidify society? When is a cultural frame (religion, economic theory, political ideology) a helpful simplification, and when has it become a Procrustean bed?

That's where Part III begins.

---

## Chapter Summary (for continuity tracking)

**Core Argument**: Systematic distortions of reality—threat-bias, categorical sharpening, action-biased perception, temporal discounting—are not perceptual failures but adaptive compressions. Under constraints (time, energy, stakes), optimal control often requires misrepresentation. The distortion coefficient is calibrated by asymmetric error costs: when false negatives are more costly than false positives, over-detection is rational. These distortions are implemented via threshold shifts (in drift-diffusion), sparse coding (neural energy budgets), and precision allocation (attention under constraints).

**Key Concepts Introduced**:
- **Helpful misrepresentation**: Systematic distortion that improves control despite reducing correspondence with ground truth.
- **Asymmetric error costs**: False negatives vs. false positives carry different consequences; optimal thresholds shift accordingly.
- **Gaze heuristic**: Maintains constant visual angle to moving object; crude distortion that outperforms explicit physics under noise and time pressure.
- **Motion aftereffect**: Perceptual illusion reflecting motion-detector fatigue; systematic bias that may enhance vigilance for subtle motion.
- **Size constancy with value-weighting**: Intrinsic object size computed from retinal size and distance, then distorted by emotional significance, frequency, threat content.
- **Categorical perception under pressure**: Perceptual boundaries sharpen under time pressure; compression trades fine-grained sensitivity for decisiveness.
- **Threat-bias and ROC shift**: High-stakes decision-making rightward-shifts ROC curve; liberal threshold increases false alarms but hits targets.
- **Frame-lock**: Over-compression becomes rigid; disconfirming evidence is distorted to fit the existing frame; updates are costly or blocked.
- **Calibration failure**: Ancestral distortions (threat-bias, temporal discounting) become maladaptive when constraints or costs change; miscalibration drives modern pathology.

**Major Examples Used**:
- Baseball catch / gaze heuristic: Crude visual rule (maintain angle to ball) outperforms trajectory calculation under time pressure and noise.
- Motion aftereffect: Waterfall illusion reflects motion-detector fatigue; systematic bias may enhance motion vigilance.
- Size constancy: Coin vs. moon paradox; perceived size distorted by familiarity, emotion, threat content; value-weighted compression.
- Categorical perception / VOT: Voice onset time discretized at ~30ms boundary; boundary sharpens under time pressure, trading sensitivity for decisiveness.
- Emotional Stroop: Threat words capture attention despite identical visual properties; precision allocation creates illusory salience.
- Intentional motion: Small dot moving toward large shape perceived as "attacking"; ambiguous motion compressed into agent-directed categories.
- Threat-ROC shift: Under high stakes, false-alarm rates increase; threshold shifts rightward, implementing optimal over-detection.
- Frame-lock: Stereotypes resist updating; confirmatory bias treats disconfirming evidence as noise; compressed model becomes rigid.
- Temporal discounting: Hyperbolic rather than exponential; rational under ancestral constraints (short life, scarce resources), maladaptive in modern saving/investment context.

**Measures & Tests**:
- **Speed-accuracy trade-off**: Drift-diffusion parameters *a* (boundary), *v* (drift). Hypothesis: threat-decisions show steeper *a* decline under time pressure.
- **ROC curves**: Hit rate vs. false-alarm rate across criteria. Hypothesis: high-stakes conditions shift ROC rightward (higher false-alarm, same/higher hit).
- **Precision estimates from neural data**: Model DDM drift as *v* = τ × stimulus value, where τ is precision. Correlate with EEG (N1 as error signal gain).
- **Frame-switch costs**: Reaction time and error rate when established frame must update. Hypothesis: frame-switches show larger RT cost and slower recovery than neutral rule-shifts.
- **Rate-distortion frontier**: Vary compression level (e.g., blur). Measure information rate *I* vs. distortion *D* vs. task success. Hypothesis: optimal operational point is not at zero distortion.

**Transition to Next Chapter**: Chapter 8 scales up from individual distortions to *schemas*, *frames*, and *scripts*—abstract templates that package helpful misrepresentations into transmissible form. A restaurant schema compresses a complex sequence into a script, enabling rapid navigation. But schemas can also become prisons. When entire cultures lock into particular frames and treat them as veridicality rather than compression, rigidity and resistance to change follow. Understanding individual helpful misrepresentation is the foundation for analyzing when social schemas enable coordination and when they ossify society.

**Key Forward Connections**:
- Chapter 5 (Rate-Distortion Life): Distortion measures are task-weighted; asymmetric error costs set thresholds.
- Chapter 6 (Predictive Brains): Precision-weighted gain control implements threshold shifts; same mechanism as helpful misrepresentation.
- Chapter 8 (Schemas, Frames, Scripts): Scales distortion from perception to abstract templates; how individuals compress knowledge into reusable patterns, then share them.
- Chapter 14 (Formal Spine): Lagrangian formalization of multi-objective optimization shows how asymmetric error costs appear as λ-weights on distortion terms.

---

<script src="https://hypothes.is/embed.js" async></script>

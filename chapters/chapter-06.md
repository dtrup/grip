---
layout: chapter
title: "Chapter 6: Predictive Brains, Budgeted Attention"
---

# Chapter 6: Predictive Brains, Budgeted Attention

> **Target**: 4,750 words | **Status**: Drafted | **Last Updated**: 2025-10-17

## Chapter Overview

**Purpose:** Connect predictive processing/active inference to budgets.

**Core claims:** Attention is **precision allocation**; prediction errors rise when compressed priors misfit; policies trade accuracy for speed.

**Moves:** Compression: prior-driven smoothing; Expansion: precision-gated hypothesis search.

**Measures:** Mismatch negativity, precision weighting, drift-diffusion parameters.

---

## Content

In a 1970s laboratory in Helsinki, researchers discovered something peculiar. They played sequences of identical tones to participants—*beep, beep, beep*—then slipped in a slightly different pitch. Even when participants weren't attending to the sounds, watching a silent film instead, their brains generated a distinctive electrical signature 100 to 250 milliseconds after the deviant tone. The amplitude of this *mismatch negativity* scaled with how unexpected the change was: larger violations produced larger signals. Same physical stimulus, different brain response, depending entirely on sequence context.

The brain, it seemed, wasn't passively receiving sounds. It was building predictions about what should come next, then automatically flagging violations. The mismatch negativity was a neural prediction error—the brain's surprise at being wrong.

This simple paradigm revealed something fundamental. Perception isn't a camera recording reality. It's a dashboard continuously forecasting the future and encoding only deviations from expectations. And like any system operating under constraints—limited time, energy, channel capacity—it must decide which deviations matter. That decision is *attention*, implemented as precision-weighted gain control. High-reliability signals get amplified. Low-reliability signals get suppressed. This is rate-distortion optimization extended into the temporal domain: compress the predictable, expand processing for the surprising, allocate resources according to estimated precision.

Chapter 5 established spatial compression—categorical perception as lossy encoding that preserves behaviorally relevant distinctions. This chapter extends that framework temporally. If perception compresses *which* features to preserve, predictive processing determines *when* and *how much* to trust incoming signals versus prior expectations. Attention becomes precision allocation under budgets, implemented through neuromodulatory gain control, testable via neural signatures like mismatch negativity and behavioral measures like drift-diffusion parameters.

The result is a unified account linking information theory, neurobiology, psychophysics, and clinical disorders—all from the principle that brains are budgeted prediction machines.

---

## From Spatial Compression to Temporal Prediction

Rate-distortion theory, introduced in Chapter 5, asks: given limited information capacity, which features should we preserve? The answer depends on the task—snake detection requires different compressions than social navigation. But there's a second dimension to compression: *time*. If the world exhibits temporal regularity—sunrises follow nights, footsteps predict approaching figures, musical phrases resolve predictably—then an efficient system shouldn't re-encode redundant information. It should predict what comes next and encode only *prediction errors*.

This is exactly what predictive processing proposes (Rao & Ballard 1999; Friston 2009; Clark 2013). The brain is a hierarchical generative model continuously forecasting sensory inputs at multiple timescales. Higher-level areas send predictions downward via feedback connections; lower-level areas return prediction errors upward via feedforward connections. When predictions match observations, feedforward signals are suppressed—confirmed expectations require no further processing. When predictions fail, error signals propagate upward to revise the model.

Consider visual perception. In Rao and Ballard's (1999) computational model, higher cortical layers predict the activity of lower layers based on learned statistical regularities. Early visual cortex, for instance, develops receptive fields that match V1 neurons—center-surround, orientation-selective, spatially localized—not because these are hardwired templates, but because they efficiently encode prediction errors for natural images. The system learns: "Given this high-level interpretation (e.g., 'vertical edge'), what low-level features should I expect?" Deviations from that expectation—edges in unexpected locations, contrasts of surprising magnitude—propagate as errors.

This achieves redundancy reduction over time. If a stimulus repeats (same face, same tone, same motion direction), its neural representation diminishes with each presentation—a phenomenon called *repetition suppression* (Grill-Spector et al. 2006). The prediction grows stronger; the error shrinks. Empirically, repeated stimuli show 30-50% reduced BOLD activation in early sensory cortex compared to novel stimuli. This isn't simple adaptation (neural fatigue). It's prediction-dependent suppression: the *same* physical stimulus elicits different neural responses depending on what the brain expects.

Prediction errors can even occur when stimuli are *absent*. In auditory experiments, if a regular sequence of tones suddenly stops, neurons still fire at the expected time—an *omission response* (Raij et al. 1997). The brain predicted a tone, received silence, and encoded that mismatch. Absence becomes informative when it violates a prediction.

Formally, this is rate-distortion optimization with temporal structure. Chapter 5's framework minimized mutual information *I(X; T)* between raw stimuli *X* and compressed representations *T*, subject to tolerable distortion. Predictive processing adds a prior distribution *p(x_{t+1} | x_{1:t})* over future inputs conditioned on history. The system now allocates rate to *unpredicted* components: *I(X; T | Prior)*. Expected signals—low surprise, high compressibility—consume minimal bandwidth. Unexpected signals—high surprise, low compressibility—demand processing. This implements temporal compression: encode change, suppress redundancy.

The payoff is efficiency. Natural environments have rich temporal structure: objects persist, motions continue, sounds resolve into patterns. A system that exploits this structure can dedicate its limited capacity to novelty and use cheap priors to handle predictability. The brain doesn't re-encode "the coffee cup is still on the desk" every 100 milliseconds. It predicts persistence, checks for violations, allocates attention elsewhere. Predictable stimuli are compressed away.

---

## Attention as Precision-Weighted Gain Control

But not all prediction errors are created equal. Some arise from genuine environmental changes demanding response—a pedestrian stepping into the road. Others arise from noisy sensors, ambiguous cues, or irrelevant fluctuations—wind rustling leaves that resemble motion. A system that treated all errors equally would waste resources chasing noise and miss critical signals buried in uncertainty.

This is where *precision-weighting* enters (Feldman & Friston 2010; Clark 2016). Precision, in this context, is the inverse variance of a prediction error: how *reliable* or *trustworthy* is this signal? High-precision errors (low variance, high signal-to-noise ratio) should be amplified—they likely reflect genuine deviations. Low-precision errors (high variance, noisy) should be attenuated—they're probably statistical fluctuations. Precision thus functions as an estimated confidence in the error signal.

Attention, Andy Clark (2016) argues, *realizes* precision-weighting. To attend to a stimulus is to increase the gain on its prediction errors, treating them as high-reliability signals worthy of upward propagation and model revision. To ignore a stimulus is to decrease gain, filtering it out as low-confidence noise. This isn't a vague metaphor. It's a computational mechanism: precision modulates the *postsynaptic gain* of prediction error units, effectively amplifying or suppressing their influence on belief updating.

Think of the *cocktail party effect*. At a noisy gathering, you selectively attend to one conversation among many overlapping voices. Acoustically, all voices reach your ears with similar intensity. But attention boosts precision on the target stream—its prediction errors are weighted heavily, driving perceptual inference—while suppressing others as low-precision background. The attended voice becomes clear; the rest fades to murmur. Precision-weighting solves the resource allocation problem: process everything fully is computationally prohibitive, so dynamically allocate gain to signals estimated as reliable and task-relevant.

Precision can vary along multiple dimensions: sensory modality (trust vision over proprioception in well-lit environments, reverse in darkness), spatial location (attend left visual field, ignore right), temporal window (heightened vigilance after a warning cue), and semantic category (search for faces in a crowd, filter out background objects). These aren't separate attentional systems. They're instances of the same principle: estimate signal reliability, modulate gain accordingly.

Functionally, precision-weighting is equivalent to adjusting *Lagrange multipliers* in rate-distortion optimization (a preview of Chapter 14's formal spine). Recall that rate-distortion minimizes *I(X; T)* subject to a distortion constraint, or equivalently, minimizes *D + λI* where λ trades off compression (rate cost) and fidelity (distortion cost). Precision acts like an inverse λ: high-precision signals warrant expensive processing (high rate), low-precision signals tolerate lossy compression (low rate). Attention dynamically sets these trade-offs based on context, goals, and estimated uncertainty.

Experimental evidence supports this account. When sensory noise increases—say, adding visual static to a stimulus—people rely more heavily on priors and less on sensory data (Rescorla & Wagner 1972; Körding & Wolpert 2004). Precision-weighting predicts exactly this: noisy signals have low estimated reliability (low precision), so prediction errors from them are downweighted, and top-down expectations dominate. Conversely, when cues are clear and reliable, sensory precision is high, and perception tracks the data closely.

Neurally, fMRI studies show that attended stimuli produce increased activation in early sensory cortex—consistent with amplified gain on prediction error units (Kok et al. 2012). Higher-level areas, including superior frontal gyrus and dorsal anterior cingulate cortex, track *precision estimates* themselves: they encode unsigned prediction errors modulated by inverse volatility (Iglesias et al. 2020). These regions may compute and broadcast precision signals that modulate gain throughout the sensory hierarchy.

Precision-weighting also explains puzzling phenomena like *change blindness* and *inattentional blindness*. In change blindness paradigms, large alterations to a scene—swapping actors mid-conversation, changing building colors—go unnoticed if they occur during brief occlusions (eye movements, cuts, blinks). Not because the changes are invisible, but because precision isn't allocated to those features. The brain predicts continuity, assigns low precision to unexpected changes outside the current attentional focus, and suppresses the errors as noise. When attention is directed to the changed region, precision increases, and the change becomes salient. Same sensory input, different precision allocation, different conscious percept.

---

## The Invisible Gorilla: Precision Allocation in Action

Perhaps the most dramatic demonstration of precision-weighted attention is the *invisible gorilla* experiment (Simons & Chabris 1999). Participants watch a short video of people passing basketballs and are tasked with counting passes made by players wearing white shirts, ignoring those in black. Midway through, a person in a full-body gorilla suit walks through the scene, faces the camera, thumps their chest, and exits. The gorilla is on screen for nine seconds, fully visible, passing through the center of the frame.

Fifty percent of viewers report never seeing it.

This isn't peripheral vision failure. The gorilla crosses the attended region. It's not camouflage—the suit is conspicuous black fur against normally dressed humans. It's *inattentional blindness*: the attentional task ("count white-shirt passes") establishes top-down predictions and allocates precision to task-relevant features (white shirts, basketball trajectories). The gorilla, though salient, is task-*irrelevant*. It generates a prediction error—"unexpected large dark figure"—but that error is assigned zero precision (irrelevant to the counting task) and suppressed at the perceptual level. It fails to reach awareness.

The predictive processing account is straightforward. Precision is allocated to basketball passes because they're instrumentally relevant: the task demands tracking them. The generative model predicts passes, movements, player positions. The gorilla violates none of those predictions *for the current task*. It's surprising in an absolute sense, but low-priority given current goals. Processing every unexpected stimulus fully—every shadow, reflection, passerby—would be computationally ruinous. Precision-weighting adaptively filters: trust errors that matter for control, suppress errors that don't.

When the counting task is removed or attention is explicitly cued to "watch for anything unusual," gorilla detection rates increase substantially. Precision allocation shifts: now unexpected objects are task-relevant, so their prediction errors receive gain. The gorilla becomes visible. Same stimulus, different precision, different awareness.

This reveals a critical point: conscious perception requires both a bottom-up signal *and* top-down precision-weighting. The signal alone—retinal activation, feature extraction—is insufficient. Precision acts as a gate: low-precision errors, however large, don't propagate to higher levels or enter awareness. High-precision errors, however small, drive inference and action. Attention is the allocation of this gate-keeping resource under budgets.

---

## Neuromodulatory Implementation: Dopamine and Acetylcholine

Precision-weighting is computationally elegant, but how is it implemented neurally? The answer lies in *neuromodulation*: neurotransmitter systems that regulate cortical gain. Two key players are *dopamine* and *acetylcholine*, which appear to control precision at different levels of the processing hierarchy (Friston et al. 2012; Yu & Dayan 2005).

Acetylcholine enhances the precision of *bottom-up* sensory signals by optimizing gain in superficial pyramidal cells—the neurons thought to encode prediction errors (Hasselmo 2006). In a recent optogenetic study, Askamp et al. (2023) stimulated cholinergic neurons in the basal forebrain of mice during an auditory oddball task (standard tones interspersed with rare deviants). Acetylcholine release in auditory cortex sharpened prediction error responses: they became higher-amplitude, faster, and more temporally precise. Crucially, the effect was specific to *deviants* (prediction errors), not standards (confirmed predictions). Behaviorally, mice showed improved detection of deviant tones. Acetylcholine, in short, amplifies the gain on sensory surprise, making unexpected signals more salient.

Dopamine operates at a higher level, encoding the precision of *reward-related* prediction errors and abstract hypotheses (Schultz 1998; Friston et al. 2012). In the classic reinforcement learning account, dopamine neurons in the midbrain fire when outcomes are better than expected (positive reward prediction error) and pause when worse (negative error). But predictive coding reinterprets this: dopamine may signal *unsigned* precision—the *magnitude* of surprise, independent of valence—which modulates how much the system should update its beliefs.

A rigorous test comes from Iglesias et al. (2020), who administered sulpiride—a dopamine antagonist—to human participants performing an associative learning task with varying volatility. In control participants, fMRI revealed that unsigned prediction errors in superior frontal cortex and dorsal anterior cingulate were modulated by *precision*: larger neural responses when the environment was stable (high precision) versus volatile (low precision). Sulpiride disrupted this precision-weighting. Neural signals became less sensitive to estimated reliability, and behaviorally, participants showed impaired learning—slower adaptation, less flexible belief updating. Dopamine, it appears, mediates the brain's ability to weight errors by their trustworthiness.

This hierarchical specialization makes functional sense. Acetylcholine handles *sensory* precision: "Is this tone genuinely different, or is my cochlea noisy?" Dopamine handles *higher-level* precision: "Is this outcome pattern stable, or is the environment shifting?" Both enable adaptive gain control, but at different timescales and levels of abstraction. Together with noradrenaline (which modulates global arousal and broad precision shifts in response to uncertainty), these neuromodulators implement precision-weighting throughout the cortical hierarchy (Yu & Dayan 2005).

Clinical disorders support this framework. Parkinson's disease involves dopamine depletion in the basal ganglia. Patients exhibit difficulty learning from surprising outcomes and reduced flexibility in updating beliefs—precisely what impaired precision-weighting would predict (Frank et al. 2004). Schizophrenia, conversely, is hypothesized to involve dopamine dysregulation leading to *aberrant* precision: the brain over-weights irrelevant prediction errors, treating random noise as meaningful signal (Adams et al. 2013; Sterzer et al. 2018). Hallucinations and delusions emerge as overly precise priors (internally generated predictions dominate perception) combined with hyper-salient errors (irrelevant stimuli feel profoundly significant). Attention deficit disorders may involve reduced cholinergic tone, impairing sensory precision and causing distractibility—the brain can't reliably amplify task-relevant signals over background noise.

These aren't just-so stories. They generate testable predictions: schizophrenia should show reduced mismatch negativity (impaired prediction error signaling), which it does (Näätänen & Kähkönen 2009). Autism, hypothesized to involve *under-weighted* priors (hypo-precision on top-down predictions), should exhibit enhanced sensory sensitivities and difficulty filtering redundancy—consistent with clinical reports (Van de Cruys et al. 2014). Pharmacological manipulations of dopamine and acetylcholine should modulate learning rates, attentional biases, and precision-dependent decision-making, which they do (Iglesias et al. 2020; Askamp et al. 2023).

Neuromodulation grounds precision-weighting in biology. It's not an abstract computational construct; it's implemented through specific neurotransmitter systems regulating cortical gain. And when those systems malfunction, precision allocation goes awry, producing the cognitive and perceptual distortions characteristic of neuropsychiatric disorders.

---

## Measuring Predictive Processing: From Mismatch Negativity to Drift-Diffusion

A framework is useful only if it generates testable predictions. Predictive processing does. The theory specifies mechanisms—prediction errors, precision-weighting, hierarchical inference—that leave measurable signatures in neural activity and behavior.

The *mismatch negativity* (MMN), introduced at the chapter's opening, is perhaps the cleanest neural marker (Näätänen et al. 2007). In the standard oddball paradigm, frequent "standard" tones (e.g., 1000 Hz, 80% of trials) establish a predictive model. Rare "deviant" tones (e.g., 1100 Hz, 20%) violate that model, generating prediction errors. The MMN is the ERP component reflecting cortical response to the error: a negative deflection 100-250 ms post-stimulus, strongest over frontal and temporal electrodes. Critically, it occurs *automatically*, even when participants ignore the sounds—the brain builds predictions and detects violations without explicit attention.

Recent work dissects the MMN into subcomponents (Li et al. 2024). *Early* MMN (around 136 ms) indexes local, low-level prediction errors: "This tone's frequency differs from the immediate predecessor." *Late* MMN (around 200 ms) indexes violations of global, higher-order sequence structure: "This tone breaks the learned pattern." The hierarchy of prediction errors is temporally layered.

MMN amplitude scales with surprise magnitude. Larger pitch deviations produce larger MMN. Novel deviants (never-before-heard sounds) elicit stronger responses than familiar deviants. And crucially, MMN is modulated by *attention*: when participants actively attend to the tone stream, deviant MMN amplitudes increase (Woldorff et al. 1991). This is precision-weighting in action—attention boosts gain on the prediction error units generating MMN.

Clinical populations show altered MMN. Schizophrenia patients exhibit reduced MMN amplitude, consistent with impaired prediction error processing (Umbricht & Krljes 2005). Autism spectrum individuals show *enhanced* MMN for certain deviants, possibly reflecting overly precise sensory predictions (Gomot et al. 2011). Systematic reviews confirm that predictive coding impairments, indexed by MMN, correlate with symptom severity across disorders (D'Astolfo & Rief 2025).

Another window into predictive processing comes from the *drift-diffusion model* (DDM) of decision-making (Ratcliff & McKoon 2008). In perceptual choice tasks—say, judging whether random dots move left or right—evidence accumulates stochastically toward a decision threshold. The model decomposes this into parameters: *drift rate* (evidence quality), *boundary separation* (caution/speed-accuracy trade-off), and *non-decision time* (sensory and motor delays).

Predictive processing predicts that drift rate should reflect *precision-weighted* evidence. High-precision signals (low noise, high coherence) produce steep drift—fast accumulation, rapid decisions. Low-precision signals (high noise, low coherence) produce shallow drift—slow accumulation, longer reaction times. Empirically, this holds: motion coherence—a proxy for sensory precision—directly modulates drift rate (Palmer et al. 2005). When signals are ambiguous or noisy, drift flattens, consistent with reduced precision-weighting.

Extensions like the *attentional drift-diffusion model* (aDDM) add gaze-contingent evidence accumulation: items receive higher drift when fixated (Krajbich et al. 2010). This is precision allocation in real time—attention (gaze) boosts the gain on evidence from attended options. The *generalized DDM* (GDDM) framework allows arbitrary precision functions, enabling models where precision updates dynamically based on stimulus history, context, or learned volatility (Shinn et al. 2020). These aren't separate models; they're variations on the theme that evidence accumulation is *precision-weighted*, and precision is itself inferred from environmental statistics.

A third measure is *repetition suppression* or *predictive suppression*. fMRI studies show that repeated stimuli produce reduced BOLD activation (30-50% suppression) in sensory cortex relative to novel stimuli (Grill-Spector et al. 2006). Classical adaptation theories attributed this to neural fatigue—neurons tire after prolonged activation. But predictive coding offers a different account: repetition strengthens predictions, reducing prediction errors, and thus reducing neural activity (which primarily reflects error signaling, not confirmed predictions). This predicts that suppression should be *context-dependent*, occurring only when stimuli are *predictable*, not merely repeated. Experimental tests confirm: suppression is stronger for predictable sequences than random repetitions (Summerfield et al. 2008).

Together, these measures—MMN, drift-diffusion parameters, repetition suppression—make predictive processing empirically testable. The framework isn't philosophical speculation; it's a research program generating quantitative predictions about neural dynamics, behavioral choice, and computational parameters. When the predictions fail—and they sometimes do, as when repetition effects are found in contexts without clear predictions—the theory is constrained, not confirmed. This falsifiability is a feature, not a bug.

---

## The ELBO Connection: Free Energy and Budget Trade-offs

Predictive processing is often formalized via the *free energy principle* (Friston 2009; Hohwy 2013), which states that agents minimize *variational free energy*—denoted *F*—a quantity that upper-bounds the surprise (negative log-probability) of sensory observations. Free energy decomposes into two terms:

**F = Complexity - Accuracy**

- **Accuracy**: How well do current predictions match sensory data? (Higher accuracy = lower free energy)
- **Complexity**: How far do updated beliefs deviate from prior expectations? (Measured by KL divergence between posterior *q(s)* and prior *p(s)*)

Minimizing free energy means maximizing prediction accuracy while keeping beliefs close to priors—a form of Occam's razor. Beliefs that wildly deviate from expectations are penalized unless the data strongly demand it. This formalizes parsimony: simple models are preferred until evidence overwhelms them.

Free energy is the negative of the *evidence lower bound* (ELBO), a cornerstone of Bayesian inference (Blei et al. 2017):

**ELBO = E_q[log p(o, s)] - KL(q || p)**

Where *q* is the approximate posterior (current beliefs about hidden states *s* given observations *o*), *p* is the true posterior, and the expectation is taken under *q*. The first term measures how well the model explains the data; the second term (the complexity penalty) measures how much the posterior diverges from the prior.

Maximizing ELBO is equivalent to minimizing free energy: **F = -ELBO**. Agents that minimize surprise (free energy) are equivalently maximizing a lower bound on the log-evidence for their generative model. Perception becomes *inference*: updating beliefs to maximize ELBO. Action becomes *active inference*: selecting actions that minimize *expected* free energy, both confirming predictions (exploitation) and gathering information to reduce uncertainty (exploration).

This connects directly to Chapter 5's rate-distortion framework. Recall that rate-distortion minimizes:

**L = D(X; T) + λI(X; T)**

Where *D* is distortion (fidelity loss) and *I* is rate (information cost). The ELBO trades off *accuracy* (analogous to minimizing distortion) and *complexity* (analogous to minimizing rate—the KL divergence measures information cost of deviating from the prior). Both frameworks impose parsimony: preserve fidelity while minimizing resources.

The formal equivalence runs deeper. In rate-distortion, the Lagrange multiplier λ sets the scarcity price on information. In predictive coding, *precision* acts as an inverse λ: high-precision signals warrant expensive processing (high rate investment), low-precision tolerate compression (low rate). Precision-weighting is dynamic Lagrangian adjustment: the brain continuously estimates signal reliability and sets multipliers accordingly.

This is a preview of Chapter 14's formal spine: a multi-objective Lagrangian unifying control, information cost, energy, time, and value-weighted distortions:

**L(π) = U(π) - λ_info·I(π) - λ_energy·E(π) - λ_time·T(π) - Σ λ_value,i·D_i(π)**

Predictive processing is one instantiation of this spine. Minimizing free energy is minimizing a budget-constrained objective where accuracy (control utility) trades off against complexity (information cost). Precision-weighting adjusts the multipliers. Attention allocates resources.

The ELBO framework also clarifies what brains *aren't* doing: they're not building veridical world-models. They're building *useful* models that compress observations into actionable predictions while staying within budget. As Chapter 7 will explore, this sometimes licenses *helpful misrepresentations*—systematic distortions that improve control despite losing correspondence with ground truth. Perception optimizes for grip, not truth.

---

## Failures of Prediction: Hallucinations, Overwhelm, and Brittle Priors

Every compression scheme has failure modes. Predictive processing is no exception. When predictions are too strong, too weak, or misaligned with environmental structure, the system breaks in characteristic ways.

*Overly strong priors* (hyper-precision on predictions) produce *hallucinations* and *delusions*. If top-down predictions dominate sensory data—because precision-weighting assigns low gain to sensory errors and high gain to prior-based errors—perception becomes decoupled from reality. Internally generated signals (thoughts, imagery, inner speech) are mistaken for external stimuli. This is one account of schizophrenia (Adams et al. 2013; Sterzer et al. 2018): aberrant dopamine signaling leads to excessive precision on irrelevant priors. Random noise is treated as meaningful pattern. Coincidences feel causally connected. Inner monologue is heard as external voices. The system over-compresses, filtering out disconfirming evidence and locking into self-confirming predictions.

Conversely, *overly weak priors* (hypo-precision on predictions) produce *sensory overwhelm* and rigidity. If sensory data dominate—because prediction errors are trusted too heavily and priors discounted—every input feels novel and surprising. Nothing compresses. This may characterize aspects of autism spectrum conditions (Van de Cruys et al. 2014): reduced reliance on predictions leads to heightened sensory sensitivities (every sound, texture, light feels intense because it's not predicted away) and difficulty generalizing (context shifts demand complete re-encoding rather than minor prediction updates). A systematic review of 72 studies found that schizophrenia shows impaired predictive coding for non-social stimuli, while autism shows selective impairment for social cues—different precision profiles, different clinical presentations (D'Astolfo & Rief 2025).

Another failure mode is *brittle predictions*: over-compression of temporal structure. If the brain builds overly rigid models—"the world always works like this"—it becomes vulnerable to *surprise cascades* when environments shift. The model predicts continuation, the world delivers novelty, and massive prediction errors flood upward. The system hasn't allocated enough capacity for flexibility. This is Goodhart's Law in temporal form: when a prediction becomes a target (a fixed prior), it ceases to track reality.

Ketamine, an NMDA receptor antagonist, produces transient psychotic symptoms in healthy individuals and disrupts MMN (Umbricht et al. 2000). Predictive coding interprets this as impaired prediction error processing: NMDA receptors are thought to mediate the comparison between predictions and observations at cortical synapses. Blocking them degrades the system's ability to compute and update based on errors. The result resembles schizophrenia: false inferences, perceptual distortions, feelings of unreality.

Anxiety disorders, too, fit the framework. Chronic anxiety may reflect overly precise *threat priors*: the brain assigns high precision to predictions of danger, amplifying threat-related prediction errors (Paulus & Stein 2006). Ambiguous stimuli are interpreted as threatening because the prior is strong and the precision-weighting on threat-consistent errors is high. This is adaptive in genuinely dangerous environments—better to over-predict predators than under-predict—but becomes maladaptive when generalized to safe contexts. The precision allocation that enabled survival in ancestral environments becomes a prison in modernity.

These failure modes aren't exotic edge cases. They're natural consequences of a system optimizing under constraints. Over-compress, and you hallucinate. Under-compress, and you drown in data. Compress the wrong structure, and you miss critical changes. The budgets that enable efficient perception also create vulnerabilities. Understanding these vulnerabilities is essential for designing interventions: cognitive-behavioral therapy for anxiety might be reframed as *precision reallocation training*, teaching patients to reduce gain on threat priors. Antipsychotic medications modulate dopamine, recalibrating precision-weighting. Predictive processing isn't just a model of normal function; it's a framework for understanding dysfunction.

---

## Budgeted Prediction: Attention as Resource Allocation

Stepping back, the picture is this: brains operate under *budgets*—limited time to decide, limited energy to process, limited channel capacity to transmit signals. Chapter 2 established these constraints as transcendental conditions for cognition. Chapter 5 showed how they force spatial compression: categorization as lossy encoding. Chapter 6 extends the framework temporally: prediction as lossy compression in time, attention as precision-weighted resource allocation.

Predictive processing is rate-distortion optimization with temporal priors and dynamic precision. The system builds a generative model of temporal structure, forecasts future inputs, encodes only deviations, and allocates processing resources—via precision-weighting—to signals estimated as reliable and relevant. This achieves multiple objectives simultaneously:

- **Efficiency**: Don't re-encode redundant information. Predict, check, move on.
- **Selectivity**: Process high-priority signals (task-relevant, high-precision), suppress low-priority (irrelevant, noisy).
- **Adaptability**: Update models when prediction errors exceed expected bounds; maintain models when errors are small.

Attention is the mechanism that implements these objectives. It's not a spotlight illuminating objects. It's a *gain control system* modulating the influence of prediction errors on belief updating. High-precision errors—attended signals—drive inference. Low-precision errors—ignored signals—are filtered out. The cocktail party effect, inattentional blindness, change blindness, attentional blink—all are instances of precision allocation under budgets. The brain can't process everything, so it dynamically sets priorities based on task demands, learned statistics, and current goals.

The *attentional blink* makes this concrete (Raymond et al. 1992). In rapid serial visual presentation (RSVP), participants view letters flashing at 10 items per second and must detect two target digits embedded in the stream. If the second target appears 200-500 ms after the first, detection accuracy drops to 30-50%. Not because the stimulus is invisible, but because the first target consumes attentional resources—precision-weighting is allocated to processing T1, and reallocation to T2 takes time. During the "blink" window, precision is unavailable, and T2's prediction error doesn't propagate to awareness. The system has a *refractory period* for precision allocation. Budgets aren't just spatial (how much total capacity?) but temporal (how fast can resources shift?).

Individual differences in attentional blink magnitude correlate with inattentional blindness: people who show large AB effects are more likely to miss the gorilla (Bredemeier & Simons 2012). This isn't coincidence. Both reflect the same underlying constraint: limited capacity for precision allocation. Some individuals can reallocate quickly or maintain high precision across multiple targets; others cannot. The framework predicts these correlations.

Importantly, precision-weighting is *learned* and *context-dependent*. It's not fixed. Expertise changes precision allocation: radiologists attend to subtle image features invisible to novices; musicians detect pitch deviations non-musicians miss. Training builds priors—"what should I expect in this context?"—and refines precision estimates—"how reliable are these cues?" This is active learning in the ELBO framework: gather data, update posteriors, improve precision models, allocate attention more effectively. The system compresses temporal structure more efficiently as it learns, freeing capacity for novelty.

This connects to Chapter 11's treatment of curiosity. Exploration is deliberately seeking high prediction error (low precision on priors) to improve the model. Exploitation is relying on strong predictions (high precision on priors) to minimize surprise. Precision-weighting controls the explore-exploit trade-off: when uncertain, reduce precision on priors (trust data), explore, update. When confident, increase precision on priors (trust model), exploit, compress. Attention becomes a curiosity regulator.

---

## Forward: When Distortion Helps Control

Predictive processing establishes that brains compress temporal structure, allocate attention via precision-weighting, and operate under budgets enforced by neuromodulatory gain control. This is efficient and adaptive—most of the time. But compression always loses information. Predictions are simplified models. Priors are coarse summaries. Precision estimates are noisy.

Which raises a question: When is it *adaptive* to systematically misrepresent reality? When do distortions—over-compressions, biased priors, asymmetric precision-weighting—improve control despite losing correspondence with ground truth?

Chapter 5 hinted at this with categorical perception: compressing continuous variation into discrete categories distorts the input space but enables faster, more reliable decisions. Chapter 6 formalized the mechanism: precision-weighted prediction errors implement resource allocation, sometimes aggressively filtering signals that a veridical system would preserve.

Chapter 7 takes the next step: *Helpful Misrepresentations*. Not all compressions are neutral lossy encodings. Some are *biased* in ways that improve fitness. Overestimating threats when miss costs are high. Underestimating effort when motivated. Temporal discounting that favors near-term rewards. These aren't bugs. They're features—distortions licensed by the control-over-correspondence principle.

Predictive processing gives us the tools to analyze when and why. Priors can be asymmetric. Precision can be task-dependent. Distortions can be optimal under budgets. The brain isn't a camera. It's a control system. And sometimes, the best control comes from strategic misrepresentation.

That's the next chapter's terrain.

---

---

## Chapter Summary (for continuity tracking)

**Core Argument**: Brains are hierarchical generative models that compress temporal redundancy by predicting future inputs and encoding only prediction errors. Attention implements precision-weighted gain control: high-reliability signals receive amplified processing; low-reliability signals are suppressed as noise. Precision is itself inferred from environmental statistics and modulated by neuromodulators (dopamine, acetylcholine). This extends rate-distortion theory from spatial to temporal domain while remaining orthogonal to metaphysical debates about reality.

**Key Concepts Introduced**:
- **Predictive processing**: Brains build hierarchical models; higher levels predict lower levels; errors propagate upward for model revision.
- **Mismatch negativity**: Automatic ERP signature (100-250ms) reflecting cortical prediction error; indexes surprise independent of attention.
- **Precision-weighting**: Inverse variance of error signal; modulates gain on prediction error units; high-precision errors drive inference, low-precision are filtered.
- **Attention as gain control**: Precision allocation under budgets; attended signals amplified, ignored signals suppressed; cocktail party effect and inattentional blindness result from precision allocation.
- **Free energy principle**: Agents minimize variational free energy (complexity-accuracy trade-off); equivalent to ELBO in Bayesian inference; formalizes parsimony.
- **Neuromodulation**: Dopamine signals precision of reward/hypothesis; acetylcholine amplifies sensory prediction errors; both implement precision-weighting.

**Major Examples Used**:
- Mismatch negativity paradigm: repeated tones establish prediction; deviant violates and triggers MMN; occurs automatically, even unattended; clinical marker altered in schizophrenia and autism.
- Invisible gorilla: 50% of viewers miss gorilla in video when attention allocated to counting basketball passes; precision gates perception; same stimulus, different precision, different awareness.
- Repetition suppression: repeated stimuli show 30-50% reduced neural response; not fatigue but prediction-dependent compression; novel stimuli evoke larger errors, larger activity.
- Attentional blink: dual-task paradigm reveals refractory period in precision allocation; can't redirect attention to T2 while T1 consumes resources (200-500ms blink window).
- Clinical disorders: Schizophrenia shows hyper-precision on irrelevant priors (hallucinations); Autism shows reduced prior precision (sensory overwhelm); Anxiety shows high-precision threat priors.

**Transition to Next Chapter**: Chapter 7 asks: when is distortion adaptive? We've established that brains compress and allocate resources via precision. But compression always loses information. The next question is when systematic misrepresentation—biased priors, asymmetric precision, helpful fictions—actually improves control. When does the perceptual dashboard lie in ways that help navigation?

**Chapter Summary:**

- Predictive processing extends rate-distortion from spatial to temporal compression: predict inputs, encode only errors.
- Attention implements precision-weighting: allocate gain to high-reliability signals, suppress low-reliability.
- Neuromodulators (dopamine, acetylcholine) implement precision via cortical gain control.
- Measures: Mismatch negativity (MMN) indexes automatic prediction errors; drift-diffusion parameters reflect precision-weighted evidence; repetition suppression shows predictive compression.
- ELBO/free energy framework formalizes prediction as Bayesian inference under complexity constraints, connecting to rate-distortion.
- Failure modes: Hyper-priors (hallucinations), hypo-priors (overwhelm), brittle predictions (surprise cascades), precision dysfunction (clinical disorders).
- Attention is budgeted resource allocation; predictive brains optimize control under constraints.

---

<script src="https://hypothes.is/embed.js" async></script>

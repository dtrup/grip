# Chapter 1: The Problem of Grip

> **Target**: 4,750 words | **Status**: Drafted | **Last Updated**: 2025-10-11

---

You're hiking alone when something moves in the periphery. Dark, coiled, near your boot. Your body reacts before you think: heart rate spikes, weight shifts, hand reaches for a stick. A second later you see it's a curved twig, shadow-draped. Relief floods in—and possibly embarrassment, depending on who was watching.

But notice what just happened. You didn't run Bayesian inference on pixel arrays. You didn't catalog all possible twig-like and snake-like objects, weighing likelihoods against base rates. You *compressed* ambiguous input into a fast, actionable category—"threat?"—tuned to consequences, not truth. The compression happened before conscious thought, delivering a verdict that was wrong in this case but adaptive across evolutionary time. That split-second compression is what we call **grip**.

Grip is what lets finite agents with limited time, energy, and information navigate a world far too complex to model completely. It's the capacity to transform an overwhelming stream of sensory data into something tractable: categories you can name, affordances you can grasp, dangers you can avoid, opportunities you can pursue. Without grip, you'd be paralyzed by possibility, drowning in data, unable to act before the world moved on.

This chapter argues three claims. First, that grip *requires* selection and simplification—agents can't engage the full complexity of reality and still move fast enough to survive. Second, that constraints (on time, energy, information, risk, coordination) are not obstacles to overcome but **enablers** of usable form. Like the rigid structure of a haiku that makes poetry possible, or the limited palette that makes a painting cohere, constraints carve possibility-space into something workable. Third, that success is measured in **control** and **anticipation**—your ability to achieve goals and predict what matters—not in correspondence with some exhaustive truth.

The snake on the trail sets the pattern. Now let's see how deep it goes.

---

## The Problem: Complexity Is Intractable

The world presents itself as a storm of variables. Consider a simple decision: which apartment to rent. You must weigh rent, size, commute time, neighborhood safety, noise levels, light, proximity to groceries, lease terms, landlord reputation, building age, heating costs, parking availability, pet policy, and a dozen other factors. Each factor varies continuously. Many interact. Some are uncertain. And you have a weekend to decide.

Or consider a doctor choosing a treatment. The patient has symptoms, a history, test results, comorbidities, medication interactions, insurance constraints, and preferences about risk and quality of life. Medical knowledge spans millions of journal articles. Treatment effects vary by subpopulation. Side effects compound in unpredictable ways. The physician has fifteen minutes.

Or a pilot responding to an engine failure. Airspeed, altitude, wind, terrain, fuel, passenger count, weather ahead, nearest airport, runway length, traffic—all shifting in real time. Decisions cascade: declare emergency, choose airport, configure aircraft, brief crew and passengers, execute approach. Seconds matter.

The combinatorial explosion is real. Even in structured domains like chess, where the rules are simple and the board finite, the number of possible positions exceeds the number of atoms in the observable universe. After just four moves by each player, there are more than 288 billion possible positions. To evaluate all possibilities exhaustively would take lifetimes. Yet grandmasters glance at a board and know what to do.

Cognitive science has long documented the bottleneck. George Miller's famous 1956 finding that short-term memory holds "seven plus or minus two" chunks has been revised downward: Nelson Cowan's 2001 work suggests working memory capacity is closer to four chunks in young adults, lower in children and the elderly. Attention is a narrow beam. Processing speed is bounded. We can hold only a handful of considerations in mind at once, and even those flicker and fade within seconds.

The naïve response is to gather more information, weigh more factors, delay the decision until uncertainty resolves. But that response runs into the wall of time. Gathering information costs time and energy. Analysis takes time. While you deliberate, the world moves: the apartment is rented, the patient deteriorates, the plane descends. And more information doesn't always help. Studies of medical decision-making show that physicians given *more* test results—without any genuine improvement in the patient's clinical picture—don't make better diagnoses; they make *slower* ones. The abundance of data creates its own fog.

Iyengar and Lepper's famous 2000 study of grocery store shoppers illustrates the paradox of choice. When offered a tasting booth with 24 varieties of jam, 60% of shoppers stopped to sample. When offered only 6 varieties, only 40% stopped. But the purchase rate reversed: 30% of those who saw 6 jams bought one, compared to just 3% of those who saw 24. More options attracted attention but induced decision paralysis. The effect is controversial—a 2010 meta-analysis by Scheibehenne and colleagues found the mean effect size near zero across studies—but the underlying dynamic is real. Under conditions of high complexity, high stakes, and low expertise, unbounded choice becomes a burden rather than a gift.

The problem isn't unique to humans. Any agent with finite resources faces the same bind. To act effectively, you must *simplify*. You must discard information, ignore variables, compress the continuous into the discrete. The question is not whether to compress, but how—and what that compression buys and costs.

---

## Compression as Solution, Not Failure

Herbert Simon saw this clearly. In the 1950s, Simon introduced the concept of **bounded rationality** as an alternative to the *homo economicus* fantasy of classical economics—the perfectly rational agent with unlimited computational power and complete information. Real agents, Simon argued, operate within bounds: limited memory, limited time, limited foresight. They don't optimize globally; they **satisfice**—a portmanteau of "satisfy" and "suffice." They seek solutions that are good enough given the constraints, not perfect.

Simon offered an evocative metaphor: human rationality is shaped by "a scissors whose two blades are the structure of task environments and the computational capabilities of the actor." Minds don't just cope with limits; they *exploit environmental regularities* to compensate for them. The world has structure—regularities, invariances, patterns—and agents learn to match their strategies to that structure. Rationality, in this view, isn't context-free optimization. It's the fit between internal heuristics and external affordances.

For this insight, Simon won the 1978 Nobel Prize in Economics. But his broader point extended beyond markets. Bounded rationality is the norm, not a quirk. It applies to perception, memory, language, social cognition—any domain where agents face complexity under constraints.

Gerd Gigerenzer and his colleagues at the Max Planck Institute took Simon's vision further, showing that simple heuristics often *outperform* complex optimization, not just in speed but in accuracy. They called these strategies **fast-and-frugal heuristics**: decision rules that ignore information, limit search, and require minimal computation. The key insight is **ecological rationality**—a heuristic is rational to the degree it is adapted to the structure of the environment. Rationality isn't a universal formula; it's a match between strategy and world.

Consider the **recognition heuristic**: "If one of two objects is recognized and the other is not, infer that the recognized object has the higher value." Gigerenzer and his colleagues asked German students and American students to judge which of two cities is larger—one German, one American. German students, using recognition of American city names, often outperformed Americans who knew more details. Why? Because recognition correlates with city size in many environments (media coverage, cultural salience), and semi-ignorance prevented the Germans from being distracted by irrelevant knowledge. Sometimes less information yields better inferences—a phenomenon Gigerenzer calls the **less-is-more effect**.

Or take the **gaze heuristic**, used by baseball outfielders to catch fly balls. The problem seems computationally daunting: a ball is hit into the air at an unknown velocity, angle, and spin, subject to wind and drag. The optimization approach would require estimating these parameters, solving differential equations to predict the trajectory, and running to the calculated landing spot. No outfielder does this. Instead, they use a simple rule: "Fixate your gaze on the ball, start running, and adjust your running speed so that the angle of gaze remains constant." If the ball rises in your visual field, speed up or move forward. If it falls, slow down or back up. If the angle stays constant, keep running—the ball will land in your glove.

This heuristic is elegant in its minimalism. It ignores velocity, angle, spin, wind—all the details an engineer would need. It tracks a single optical variable and maintains an invariant. The world does the math; the agent just keeps gaze angle constant. And it works. The same principle is used by dogs catching frisbees, hawks pursuing prey, and guided missiles tracking targets. Gigerenzer notes that RAF pilots in World War II used a version of it to intercept bombers: if the bearing to the target remained constant, collision was inevitable. The strategy exploits the *structure* of projectile motion to offload computation from the agent to the environment.

Gary Klein's research on firefighters reveals a similar pattern. In the mid-1980s, Klein studied 26 experienced fire ground commanders with an average of 23 years on the job. He asked them to describe challenging decisions using the Critical Decision Method—a structured interview that probes how experts made high-stakes calls under pressure. The conventional model of decision-making predicts that experts generate multiple options, evaluate the pros and cons of each, and choose the best. Klein found the opposite.

Eighty percent of decisions were made in less than a minute. Only 12% showed evidence of comparing multiple options simultaneously. Instead, experienced commanders used **recognition-primed decision making**: they recognized the situation as an instance of a familiar type and implemented the typical response. If the situation resembled a ventilation-limited fire in balloon-frame construction, the standard tactic was to open the roof and coordinate an interior attack from the upwind side. Commanders mentally simulated the action—imagining how it would unfold—and if it seemed workable, they executed it. If not, they modified the plan or tried another. But they considered options *serially*, one at a time, not in parallel.

This is expertise as compression. Years of experience carve the space of possible fires into a library of patterns. Each pattern is a **schema**—a compressed representation linking situational cues (flame color, smoke behavior, building type, weather) to effective actions. The continuous, high-dimensional space of fireground variables is discretized into a manageable set of categories, each with an associated playbook. The commander doesn't search exhaustively through possibilities. They recognize, simulate, and act. Speed and decisiveness emerge not from ignoring complexity but from having *compressed* it into actionable form.

Chess offers another classic illustration. In 1946, Dutch psychologist Adriaan de Groot showed chess masters and club players brief glimpses of mid-game positions—five to ten seconds—and asked them to reconstruct what they saw. Masters reproduced positions with 20 or more pieces accurately; novices struggled. But when shown *random* arrangements of pieces, masters did no better than novices. The difference wasn't raw memory capacity. It was **pattern recognition**. Masters had built a vast library of **chunks**—perceptual units corresponding to meaningful configurations. Chase and Simon's 1973 follow-up estimated that grandmasters store roughly 50,000 chunks in long-term memory.

A chunk is a compression. Instead of encoding "pawn on e4, pawn on d5, knight on f3, bishop on c4," the master sees "Italian Game opening, standard development." The chunk links perception to meaning to action: seeing a configuration evokes strategic themes, tactical motifs, and candidate moves. Expertise doesn't mean seeing more pieces; it means seeing *patterns*. The high-dimensional space of piece arrangements is compressed into a catalog of templates. Retrieval is fast, inference is automatic, and action follows without deliberation.

What unites these cases—Simon's satisficing, Gigerenzer's heuristics, Klein's recognition-primed decisions, chess chunking—is that simplification isn't a cognitive failure. It's how control works. Compression discards information, but it *preserves task-relevant structure*. The outfielder doesn't know the ball's spin, but the gaze heuristic delivers the ball to the glove. The commander doesn't model every beam and joist, but the schema delivers the right tactic. The grandmaster doesn't calculate every branch, but the chunk delivers the strong move.

Agents gain grip not by mirroring the world's full complexity, but by building lossy maps tuned to consequences. The map is not the territory, but the map is what lets you navigate.

---

## Constraints as Enablers, Not Obstacles

If compression is necessary, what forces it? The obvious answer: limits. Time, energy, attention, memory, communication bandwidth—these are the constraints that make exhaustive representation impossible. But constraints don't merely *prevent* perfect fidelity. They *enable* tractable form. Without boundaries, there is no structure. Without selection, there is no meaning.

Consider the haiku. Seventeen syllables, divided 5-7-5. A seasonal reference. A cutting word that juxtaposes images. These rigid constraints don't stifle creativity; they channel it. Every word must earn its place. Precision is forced. The result can be profound—a compressed distillation of experience that lingers longer than sprawling prose. The same holds for the sonnet: fourteen lines, strict rhyme scheme, iambic pentameter. Shakespeare, Milton, and Wordsworth created enduring works *within* these bounds. The structure didn't limit them; it gave their art shape.

The phenomenon extends beyond poetry. In design, creativity often flourishes under constraint. Psychological research shows that moderate constraints boost originality: too few bounds and people face the paralysis of blank-slate freedom; too many and there's no room to maneuver. The sweet spot is enough structure to guide without dictating. In software engineering, constraints like limited memory or processing power have driven elegant solutions—compression algorithms, efficient data structures, minimalist interfaces. Scarcity breeds ingenuity.

Philosophy anticipated this insight a century ago. William James, founder of American pragmatism, argued that truth is measured not by correspondence to an abstract reality but by **instrumental success**—what he called "cash value in experiential terms." True ideas, James wrote, are those "we can assimilate, validate, corroborate, and verify." Truth *happens* to an idea through its consequences. An idea is true if it helps us navigate, predict, control our experience. And the world constrains us—James insisted pragmatism isn't relativism. He wrote of the "immense pressure of objective control under which our minds perform their operations," emphasizing that ideas must answer to experience even if they aren't mirror-copies of essences.

John Dewey extended this into a full theory of inquiry. For Dewey, ideas are *instruments* for solving problems. Inquiry begins with a problematic situation—one where habitual responses fail—and proceeds by active manipulation: introduce variations, observe results, test hypotheses. Knowledge is not passive reception but **active coping**. Truth is "warranted assertibility"—what inquiry justifies given the constraints of practice. To know is not to mirror but to *control*.

The pragmatists were groping toward a functional account: representation serves action, not essence. Constraints on time, resources, and stakes shape what counts as adequate knowledge. Good enough is what works when you're up against a budget.

Cybernetics formalized this intuition. W. Ross Ashby's **Law of Requisite Variety** (1956) states: "Only variety can absorb variety." For a system to be stable, the controller's range of possible responses must match the range of disturbances it faces. A thermostat regulating room temperature doesn't model air molecules; it compresses temperature into a single dimension and controls it. Regulation doesn't require mirroring—it requires matching *control-relevant complexity*.

Ashby's theorem with Roger Conant (1970) makes the point sharper: **"Every good regulator of a system must be a model of that system."** But the model is a *homomorphism*—a lossy mapping—not an isomorphism. The regulator internalizes task-relevant structure and discards the rest. To control X, you need a model of X, but the model is a *compression*. It preserves the invariances that matter for control and ignores those that don't.

This is the conceptual heart: **constraints don't just limit—they enable.** They force you to select, and selection is what gives you grip. Without the constraint of limited working memory, there'd be no pressure to chunk. Without limited time, there'd be no need for fast heuristics. Without limited communication bandwidth, there'd be no impetus to build shared symbols. Constraints are the sculptor's chisel. They carve the block into form.

---

## Control Over Correspondence

If compression is necessary and constraints enable it, what standard should we use to judge success? Not accuracy in the sense of pixel-perfect fidelity. The outfielder doesn't need to know wind speed; the commander doesn't need to know molecular combustion dynamics. They need to *control outcomes*. They need to act effectively given their goals and the world's responses. Success is measured in **control** and **anticipation**, not in correspondence to exhaustive truth.

Signal detection theory makes the trade-offs explicit. Developed in the 1950s for radar operators trying to distinguish enemy aircraft from noise, signal detection theory (SDT) formalizes the tension between **sensitivity** and **specificity**. Sensitivity is the true positive rate—how often you detect a signal when it's present. Specificity is the true negative rate—how often you correctly register its absence. You can't maximize both simultaneously. Increasing sensitivity (catch more signals) raises false positives. Increasing specificity (reduce false alarms) raises false negatives.

The **receiver operating characteristic (ROC) curve** plots this trade-off across all possible decision thresholds. A perfect detector traces the top-left corner; a random guesser sits on the diagonal. Real systems trace a curve in between. The area under the curve (AUC) quantifies overall discriminability, but it doesn't tell you where on the curve to operate. That depends on the *costs* of errors.

Consider a smoke detector. Set the threshold too sensitive and you get constant false alarms—burnt toast, shower steam, cooking smoke. Annoyance accumulates. People remove batteries or disable the unit. Set the threshold too lax and you miss smoldering fires. People die. The "optimal" threshold isn't the one that maximizes accuracy in some abstract sense; it's the one that balances the asymmetric costs of false positives (annoyance leading to device removal, which leads to catastrophic false negatives) and false negatives (death).

Modern smoke detectors address this with multi-sensor designs—smoke, heat, carbon monoxide—that reduce false positives while maintaining sensitivity to real threats. Some allow user-adjustable thresholds, though manufacturers warn: don't turn it down so far that it stops detecting danger. The engineering challenge is a control problem, not a truth problem. The detector doesn't "know" the chemical composition of the air. It makes a prediction optimized to user goals: timely alert, low nuisance, maximum survival.

Medical screening faces the same trade-offs at higher stakes. Mammography for breast cancer, PSA tests for prostate cancer—these are classification problems with ROC curves. High sensitivity catches more cancers but also generates more false positives, leading to biopsies, anxiety, overtreatment. High specificity reduces false alarms but misses cancers. Guidelines from different organizations (American Cancer Society, U.S. Preventive Services Task Force) reflect different weightings of these errors. There's no universally "correct" threshold—only trade-offs made transparent.

Or consider triage in a mass casualty incident. A natural disaster, a multi-vehicle collision, a terrorist attack: dozens or hundreds of injured arrive simultaneously. Resources—doctors, nurses, beds, operating rooms—are overwhelmed. The triage nurse has seconds per patient to assign priority. The **START triage system** (Simple Triage and Rapid Treatment, developed in 1983 in Newport Beach, California) is a brutal simplification. It uses three quick checks: Respirations (breathing rate), Perfusion (radial pulse), Mental status (follows commands?). Patients who can walk are tagged green (minor). Patients not breathing after airway opening are tagged black (expectant/deceased). Patients with respiratory rate above 30 or below 10, absent radial pulse, or inability to follow commands are tagged red (immediate). Everyone else is yellow (delayed).

The compression is intentional and crude. It ignores patient age, medical history, exact injury mechanism, comorbidities. It makes mistakes—some yellow-tagged patients could survive with immediate care; some red-tagged patients won't survive despite it. But the goal isn't individual diagnostic precision. It's **population-level control**: maximize survival given scarce resources. Good enough fast beats perfect too late.

These examples share a structure. All involve **compression under constraints** (limited sensors, limited time, limited resources). All trade correspondence for control—the smoke detector simplifies air chemistry to a binary alarm, triage simplifies patients to color codes. All make errors, but the errors are tuned to *consequences*, not truth. The ROC curve doesn't have a universally best point. The best point depends on your **loss function**—the relative costs of false positives and false negatives—which itself depends on stakes, resources, and values.

Claude Shannon's rate-distortion theory provides the mathematical spine. Shannon showed that compression and distortion are unavoidable trade-offs. You can't compress a continuous signal to a finite rate without losing information—unless the signal has redundancy that lets you exploit statistical regularities. The **rate-distortion function** specifies the minimum information cost (rate) needed to achieve a given level of reconstruction error (distortion). Lower rate, higher distortion; higher rate, lower distortion. There's no free lunch.

Agents face rate-distortion problems constantly. Perception is one: the retina sends a million fibers to the cortex, but the thalamus compresses the signal, emphasizing edges, motion, contrast—features relevant to behavior, not pixel arrays. Memory is another: you can't store every sensory moment, so you compress experience into gist, schemas, narratives. Communication is a third: language compresses thought into linear strings of symbols, losing nuance and context but gaining the ability to coordinate across distance and time.

Science itself operates by useful fictions. Newtonian mechanics assumes point masses, frictionless planes, instantaneous forces—all false, but incredibly productive for engineering, ballistics, and everyday prediction. The model works because it captures force-acceleration relationships while ignoring molecular vibrations, quantum effects, relativistic corrections. We teach introductory physics with idealized models (no air resistance, no friction) and layer in complexity only when needed. The fiction is **instrumentally true**—it delivers control even though it isn't a perfect mirror.

This is the conceptual payoff: **control over correspondence.** Agents don't optimize for veridicality; they optimize for effective action. The world constrains what works—pragmatism isn't "anything goes"—but what counts as "working" is defined by goals, stakes, and budgets, not by exhaustive truth. Perception is not a camera but a dashboard, built to guide decisions under constraints.

---

## Expansion Foreshadowed

Compression is necessary but not sufficient. If agents only compressed, they'd be brittle—locked into fixed schemas, blind to novelty, unable to adapt when environments shift. Real agents also *expand*: they explore, play, experiment, ask "what if?" They maintain redundancy and degeneracy—multiple pathways to the same goal—so failures don't cascade. They build external scaffolds—tools, notes, institutions—that offload cognition and amplify capacity.

We'll return to this in detail. Chapter 11 explores **curiosity and epistemic value**: how agents allocate resources to information gain even when immediate payoff is unclear, because learning expands future control. Chapter 13 examines **scaffolding and collective cognition**: how writing, diagrams, and collaboration expand the range and depth of counterfactuals agents can entertain without expanding internal working memory.

For now, note the duality: compression gives you grip on known problems, but environments change. Expansion mechanisms—exploration bonuses, redundant pathways, external memory—hedge against brittleness. Agents don't just simplify; they also complexify selectively. Both moves are rational responses to constraints.

---

## Measures and Tests

How do you operationalize "grip"? How do you test whether an agent has compressed effectively, whether constraints are enabling or crippling, whether control has been achieved?

**Framing tasks** reveal compression in action. Tversky and Kahneman's classic Asian Disease Problem presents identical outcomes framed as gains ("200 people saved") or losses ("400 people die"). People become risk-averse for gains and risk-seeking for losses, even though the outcomes are identical. The frame is a compression—a way of carving the decision space—and it shapes choice. To test grip, manipulate frames and measure how decisions shift. The agent's compression becomes visible in the pattern of risk preference.

**Bounded rationality benchmarks** compare heuristic and optimization strategies under time and resource constraints. Give participants multi-attribute choice problems—choose an apartment, select a medical treatment, pick an investment—and vary time pressure, information availability, and stakes. Measure accuracy, speed, cognitive load (via secondary task performance or pupil dilation). The prediction: under tight constraints, fast-and-frugal heuristics often match or beat exhaustive analysis. The test reveals when and why compression wins.

**Recognition heuristic tests** manipulate what participants recognize and measure inference accuracy. Ask people to judge which of two cities is larger, controlling for how many city names they recognize. Semi-ignorant participants often outperform fully informed ones when recognition correlates with the criterion. The less-is-more effect is a signature of effective compression: ignoring information can improve performance if the information is less valid than the heuristic cue.

**ROC analysis** measures sensitivity-specificity trade-offs in real decisions. For medical diagnostics, plot true positive rate against false positive rate across different test thresholds. Calculate AUC. Compare where different clinicians operate on the curve. Do they adjust thresholds based on error costs (e.g., higher sensitivity for life-threatening conditions)? The ROC curve makes the control-versus-correspondence trade-off explicit and testable.

**Performance under time pressure** isolates the role of compression. Give experts and novices the same decision problems under varying deadlines. Measure accuracy and strategy shifts (e.g., from compensatory to non-compensatory rules, from deliberation to recognition). Experts' advantage should increase as time tightens—because their compressed schemas deliver fast, accurate responses, whereas novices must deliberate.

**Trade-off curves** map speed versus accuracy, exploration versus exploitation, sensitivity versus specificity. These curves are the empirical signature of agents operating under constraints. By fitting curves to behavior and manipulating constraint levels (reduce time, increase stakes, add noise), you can infer the agent's implicit objective function—what they're trading off and how they weight the costs.

Grip isn't a vague metaphor. It's a measurable capacity: the ability to achieve control and anticipation given finite resources. Every claim in this chapter can be tested. Every compression can be characterized by its rate-distortion profile, its failure modes, its performance envelope. That's the standard.

---

## Forward: What Forces Compression?

We've argued that agents gain grip by compressing the world's complexity into tractable form, that constraints enable this compression rather than merely limiting it, and that success is measured in control and foresight rather than mirror-truth. But we've gestured at constraints abstractly—"time, energy, information, risk"—without specifying them.

What exactly are these constraints? How do they interact? Can they be measured, tuned, traded off? And if they shape all cognition, do they function as modern-day **transcendental conditions**—necessary structures that enable experience and control, not contingent features we might overcome?

That's the question for Chapter 2. If compression is *how* agents grip, constraints are *why* they must. We turn now to the budgets themselves: time, energy, information, risk, and coordination. These are the scissors' blades. These are the sculptor's tools. These are the enabling conditions of mind.

---

---

## Chapter Summary (for continuity tracking)

**Core Argument**: Agents gain grip by compressing a complex world into actionable categories. Constraints (time, energy, information, risk, coordination) enable rather than merely limit cognition. Success is measured in control and anticipation, not correspondence with exhaustive truth. Compression is necessary for tractable action; expansion (exploration, redundancy, scaffolding) prevents brittleness.

**Key Concepts Introduced**:
- **Grip**: The capacity to make a complex world tractable through selection and simplification.
- **Constraints as enablers**: Time, energy, information, and coordination limits force useful compressions.
- **Control over correspondence**: Optimization for effective action, not pixel-perfect fidelity.
- **Lossy compression**: Rate-distortion trade-offs as the natural language of perception and decision.
- **Homomorphic mapping**: Models preserve task-relevant structure while discarding the rest.

**Major Examples Used**:
- Snake vs. twig: split-second visual compression that privileges survival over accuracy.
- Chess grandmasters: 50,000 chunks compress board positions into perceptual patterns.
- Gaze heuristic: baseball outfielders exploit physics rather than computing trajectories.
- Firefighter recognition-primed decisions: mental simulation of typical scenarios under pressure.
- Paradox of choice: too many options induces paralysis; constraint clarifies.

**Transition to Next Chapter**: Chapter 2 specifies the constraints abstractly. What exactly are time, energy, information, risk, and coordination budgets? How do they interact? Can they be measured and tuned? We move from the intuition that grip requires compression to the formal specification of the constraints that force it.

<script src="https://hypothes.is/embed.js" async></script>

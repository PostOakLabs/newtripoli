---
world: cognitive-husbandry
type: feasibility-paper
title: "Bionics Feasibility"
companion: cognitive-husbandry-feasibility.html
status: draft
---

# Bionics Feasibility: Iterating a Biological Brain Toward a Synthetic Substrate

Companion to the Cognitive Husbandry world bible and sibling to the ETI-framed
feasibility audit (`cognitive-husbandry-feasibility.html`). Preprint draft, work
in progress.

## 0. Frame

The first paper in this pair told the story through an alien. An extraterrestrial
intelligence crosses interstellar distance, converts a population into brains on
life support, and farms their cognition inside an accelerated simulation. That
framing was a device, and this paper drops it. The alien is us, later, if the
substrate transition works. What follows is a human-engineering question stated in
human-engineering terms. By what path, if any, does a biological brain get iterated
toward a bionic or synthetic substrate without killing the person along the way,
and what physical limits govern how far that path can run?

The question people reach for first is the continuity-of-self question, which asks
whether the upgraded mind is the same person or a copy wearing its memories. That
question is real, but it has been argued to exhaustion and it is not where the
engineering lives, so it is confined to a footnote here.[^1] The organizing
constraint of this paper is not philosophical. It is thermodynamic, and it is the
subject of the next section.

## 1. The heat wall

Every forward claim in this paper is held against one bound, derived once, here.
The bound is not an engineering nuisance to be optimized away with a better process
node. It is a wall set by the physics of warm tissue, and it reframes the entire
race.

Living neural tissue tolerates only a small local temperature rise before function
degrades and damage begins, on the order of 2 °C. This is not a round number pulled
from intuition. It is the consensus ceiling in the implanted-device thermal
literature. Wolf's standard treatment of thermal considerations for implanted
cortical interfaces holds chronic device-induced heating below roughly 1 to 2 °C of
local rise, and the implantable-device standard frames the same limit as a thermal
dose, allowing no device surface to impose more than a CEM43 of 2, meaning two
cumulative-equivalent-minutes at 43 °C, on brain tissue.[^thermal] The ceiling is
not merely a damage threshold either. Stujenske and colleagues showed that light
delivered for optogenetics warms nearby cortex enough to change the firing rates of
individual neurons before it does any harm, which means a fraction of a degree is
already enough to corrupt the very signal an interface is trying to read or
write.[^stujenske] An implanted device that dissipates power into that tissue must
therefore keep its areal heat flux below roughly 40 mW/cm², the ceiling consistent
both with the thermal-dose limit and with the ultrasonic neural-dust analysis of Seo
and colleagues.[^dust] Divide the sustainable power by the data rate a
whole-brain-density interface would have to carry, and the link budget collapses to
about 12 pJ per bit at neural-dust scale. That number, not electrode count, is the
governing figure of merit. The derivation is set out in full in the sidebar below
and is not repeated elsewhere; every rung of the ladder asserts against it rather
than re-deriving it.

> Sidebar: deriving the 12 pJ/bit link budget, worked once.
>
> Thermal ceiling. Chronic heating of cortical tissue is held safe below about
> 2 °C of local rise. Translated to a sustainable areal dissipation, that is a
> ceiling near 40 mW/cm², the figure the implanted-BMI thermal literature and the
> neural-dust work both adopt as the design limit.[^thermal][^dust]
>
> Power available to a node. A neural-dust mote is a roughly 100 μm node powered
> ultrasonically at about 2 mm depth. Seo and colleagues estimate about 500 μW
> delivered to such a node at a link efficiency on the order of 7 percent, well
> within the 40 mW/cm² thermal envelope for a sparse population of motes.[^dust]
>
> Bits per joule, the arithmetic. Take the thermal envelope and hand a single node
> its fair share of the area it heats. A node monitoring a patch on the order of 50
> by 50 μm, roughly the tissue holding a handful of neurons, is allotted a power
> share of order 1 μW before it starts pushing that patch past the 2 °C rise.
> Require it to stream telemetry continuously at a target rate near 10⁵ bit/s, and
> the sustainable cost of moving one bit off the node, meaning to sense, encode, and
> transmit it through the tissue at the stated efficiency, lands near 12 pJ/bit.
> This is not a lone estimate. An independent low-power-BMI design study derives the
> same figure from the identical 2 °C and 40 mW/cm² starting point, by exactly this
> power-over-rate route.[^linkbudget] Two derivations from different directions
> converging on one number is the reason it is treated as the spine. It remains an
> order-of-magnitude budget, flagged with a tilde, and every input is exposed so it
> can be revised.
>
> Why it is a wall and not a knob. The waste heat scales with the aggregate bit
> rate, and the aggregate bit rate scales with how much of the brain is being
> interfaced. No one can buy their way past 40 mW/cm² with more electrodes, because
> more electrodes moving more bits is precisely what the ceiling forbids. The only
> free variable is pJ/bit, meaning how cheaply each bit is moved. That is the whole
> game, and §4 asks how much room is left in it.

It helps to fix the scale the wall applies to. The human brain runs roughly 86
billion neurons across on the order of 10¹⁴ synapses.[^herculano] The best
interfaces in clinical hardware today sit six orders of magnitude short of that
neuron count, and even that comparison flatters them, because a channel is not a
neuron. Neuralink's N1 carries 1,024 channels on 64 threads of 16 electrodes
each.[^bci2026] Paradromics' Connexus array reports on the order of 65,000 recording
electrodes.[^bci2026] Against 86 billion neurons those figures are 10⁻⁵ to 10⁻⁶ of
the count, and each channel samples a smear of nearby field potential rather than a
single identified cell.

The consequence is blunt. To interface the brain at whole-neuron density, an
engineer would have to raise channel count by something like a factor of a million
while moving all of the additional waste heat out of a skull that tolerates 2 °C. A
whole-brain-density interface cannot be brute-powered inside living tissue. The race
is not for more electrodes. It is for bits per picojoule per watt of waste heat, and
every rung below is scored on it.

Figure 1. A schematic log-log sketch of interface areal power demand against channel
count. Brute-forcing channel count at fixed pJ/bit drives areal power toward the 40
mW/cm² ceiling long before whole-neuron density near 10¹¹ channels. The only way the
curve stays under the wall at scale is to push pJ/bit down, bending the line rather
than extending it.

## 2. The graveyard

Before any forward claim comes a discipline check, because this field has a long
record of confident timelines that did not survive contact with the calendar. The
pattern is consistent enough to tabulate, with sources, so that the
record is auditable rather than rhetorical.

| Prediction | Made | Promised | Actual |
|---|---|---|---|
| Practical consumer "neural typing" from cortical implants | 2000s hype cycle | within a decade | still investigational; clinical spellers exist but at sub-conversational throughput |
| Whole-brain emulation "achievable by extrapolation of current technology" | Sandberg & Bostrom roadmap, 2008[^wbe2008] | implied decades | a roughly 1 mm³ slab of one mouse cortex mapped, not one whole brain[^brainemu] |
| High-bandwidth consumer BCI as a shipping product | 2010s venture framing | "a few years" | dozen-plus experimental human implants, no consumer device[^bci2026] |
| Mind uploading as a foreseeable clinical option | recurrent futurist claim | within a lifetime | no organism mapped at more than 90 percent of neurons at single-spike resolution[^brainemu] |
| A validated running model of any nervous system | implicit in every roadmap since C. elegans | "the data is the hard part" | none exists, not even for a 302-neuron worm; the bottleneck moved from data to modeling[^brainemu] |

The misses share two roots. The first is optimism about scaling, an assumption that
channel counts, once climbing, would climb to whole-brain coverage on a Moore's-law
curve, when the binding constraint was never lithography but the heat wall of §1.
The second is silence about the connectome. Roadmaps costed the recording hardware
and ignored the far larger problem of knowing what to record from and how the wiring
is arranged. The 2008 Sandberg and Bostrom roadmap is the honest exemplar of the
era's optimism, being careful, explicit about its assumptions, and still framing
whole-brain emulation as reachable "by extrapolations of current technology."[^wbe2008]
Nearly two decades on, the newer accounting is starker in one specific way. The field
now holds terabytes of connectome data and still has no validated running model of
any brain, not even a 302-neuron worm.[^brainemu] The bottleneck moved from
collecting the data to building something that computes from it, which is a harder
and less-funded problem than the roadmaps assumed.

The discipline this record earns is a rule the rest of the paper obeys without
exception, namely no dated milestones. Where a year appears below, it is quoted as
an external projection with its source, never adopted as a claim of this paper.

## 3. The ladder

The path from today's interfaces to substrate independence is a ladder, and the
rungs are placed on two axes at once, biological scale and time horizon. Because the
field's timelines have missed so reliably, the rungs are stated not as dates but as
capability thresholds gated by evidence. Each rung names the thing that must be
demonstrated and survived before the next is attempted. Horizon labels stay soft,
near, mid, and far, and each is pinned to a technical precondition rather than a
year. Every rung answers the same question: what fits under 40 mW/cm²?

| Rung (scale) | Horizon | Proven needed to advance | Where we are / anchor |
|---|---|---|---|
| Region, read-only | near | chronic stability, explant-able, low drift | roughly here, motor decoding at about 1k channels[^bci2026] |
| Region, closed-loop stim | near to mid | bidirectional traffic under the heat budget | early clinical |
| Subsystem hybrid | mid | sustained co-adaptation, no runaway heat | not demonstrated |
| Cortex-scale | far | a bits/pJ breakthrough and a connectome map | mouse whole-brain map projected around 2034; primate 2040s[^brainemu] |
| Whole-brain / migrate | far | the substrate question resolved empirically | no defensible timeline |

Figure 2. The five rungs as a single diagram, each tagged with its horizon, the
evidence gate that must be cleared to leave it, and where the field stands today. The
heat wall is drawn as a band that begins to bind at the subsystem rung and dominates
everything above it.

Region, read-only. This is roughly where the frontier sits. A patch of cortex is
recorded, its population activity decoded, and an external effector driven from the
decode. The gate to climb off this rung is not more channels but chronic
survivability, meaning an array that stays stable for years, drifts little, and can
be explanted without taking tissue with it. That gate is not hypothetical. The
largest retrospective failure-mode study to date, Barrese and colleagues' analysis
of 78 silicon microelectrode arrays implanted in 27 monkeys since 1996, found that
performance degrades over months to a few years, and that the dominant failures are
not electrical but material and biological. Insulation cracks, connectors and
lead-wires fault, and the chronic foreign-body reaction walls electrodes off in
glial scar and drives recording neurons away from the tips.[^barrese] The tissue
treats a rigid probe as a wound it never stops healing. There is at least a credible
path around this, however. Ultra-flexible mesh electronics, injected rather than
inserted, are compliant enough that the brain stops treating them as a wound. Hong,
Lieber, and colleagues report a gliosis-free interface that tracks individual
neurons stably for eight months to a year with minimal chronic immune
response.[^mesh] That does not yet meet the decade-stable, cleanly-explantable bar
this rung demands, but it shows the bar is an engineering target rather than a
biological impossibility. The heat wall is not yet binding here, because the channel
counts are low. It becomes binding two rungs up. Falsifier for this rung: the
read-only base of the ladder would be barred if the foreign-body response were shown
to impose a hard ceiling on chronic yield, with recording sites lost to
encapsulation faster than any biocompatible material or geometry can preserve them.

Figure 3. A schematic recording-yield decay curve of the kind Barrese and colleagues
document, showing viable channels falling over months to years, with the onset of
material failures and of the biological foreign-body response marked separately, and
the flatter trajectory a compliant mesh interface is reported to follow.

Region, closed-loop stimulation. Reading is only half a loop. Writing back, meaning
stimulating the same region in a controlled, information-bearing way while continuing
to read, closes it, and closed loops are where bidirectional traffic begins to press
on the 12 pJ/bit budget. The gate is a demonstrated closed loop that carries useful
bidirectional bandwidth without exceeding 40 mW/cm² across the interfaced area. Early
clinical closed-loop systems exist for narrow indications, but general closed-loop
cortical interfaces at bandwidth do not.

The under-appreciated half of this rung is that writing is the hard direction.
Reading only has to eavesdrop, whereas writing has to inject a signal the cortex will
accept as its own, and the two are not symmetric problems. Intracortical
microstimulation can already evoke crude, localized tactile percepts by injecting
current into somatosensory cortex, so the write channel exists in principle, and the
evoked percepts have proven stable over months.[^write] Doing so at the fidelity,
spatial selectivity, and channel count a full sensory feed demands, while avoiding
the stimulation-induced adaptation, current spread, and seizure risk that all scale
with injected charge, remains unsolved. Every stimulating channel also dissipates
more heat than a recording one for the same information, so the write side hits the
40 mW/cm² wall sooner than the read side does. The sibling feasibility audit grades
this same asymmetry as the dominant unsolved sub-problem of the interface premise,
requiring roughly seven to eight orders of magnitude of channel scaling on the write
side alone (see that paper's §4.4).[^sibling] Falsifier for this rung: every rung
above it would be barred by a proof that stable, high-fidelity write-side stimulation
to large cortical fractions is bounded, thermodynamically or biologically, below the
bandwidth a closed loop needs.

Figure 4. The read and write directions side by side. Reading eavesdrops on fields
the tissue already produces, while writing must inject charge the cortex accepts as
its own, and the schematic contrasts their relative cost in heat, fidelity, and
channel count to show why the write side reaches the wall first.

Subsystem hybrid. Here a functional subsystem, a sensory relay or a memory-adjacent
circuit, is run in sustained partnership with synthetic hardware, the biological and
the artificial co-adapting over time. This rung has not been demonstrated in any
organism. Its gate is sustained co-adaptation with no runaway heat. The hybrid must
hold a stable operating point for a long period under the areal budget, since a
co-adapting loop that slowly drives its own dissipation upward fails the wall even if
it passes on day one. Falsifier for this rung: the hybrid substrate would be barred,
regardless of channel technology, if any co-adapting biological and synthetic loop
were shown to be dynamically unable to settle, its dissipation climbing without bound
as the two sides chase each other.

Cortex-scale. Interfacing an entire cortex at meaningful density requires two things
at once, and neither is in hand. The first is a bits-per-picojoule breakthrough, a
way to move whole-cortex traffic under the same 40 mW/cm² ceiling that today's
pJ/bit figures do not permit at that scale; §4 measures how large that gap actually
is. The second is a connectome map to interface against, and here the gap is stark.
The densest reconstruction to date covers only about a 1 mm³ slab of mouse cortex,
on the order of 120,000 neurons and 523 million synapses densely
reconstructed.[^brainemu] To put that in proportion, the volume is roughly a
millionth of a mouse brain and something like a five-millionth of a human one, and
the cost curve, while falling fast from an estimated $16,500 per reconstructed neuron
in the original C. elegans work to roughly $100 in recent larval-zebrafish efforts,
still multiplies to prohibitive totals at human scale.[^brainemu] No organism has yet
been mapped at more than 90 percent of its neurons with single-spike, simultaneous
resolution. External projections put a mouse whole-brain map around 2034 and a
primate map in the 2040s, with a larval zebrafish full connectome expected
sooner,[^brainemu][^mammalproj] and those are cited as others' estimates, not as this
paper's schedule. Falsifier for this rung: it would be barred as physics rather than
engineering distance by a demonstration that the two gates are jointly unsatisfiable
under the wall, meaning that any interface dense enough to be useful at cortex scale
necessarily exceeds 40 mW/cm² however cheaply its bits are moved.

Whole-brain and migrate. The top rung, interfacing or replacing an entire human
brain so that the mind persists onto a new substrate, has no defensible timeline, and
its gate is not an engineering demonstration at all but the resolution of a
scientific question that is still open. That question is §5. Falsifier for this rung:
there is no engineering falsifier, only a scientific one. Migration would be barred
outright if the substrate question of §5 resolved against gradual replacement, with a
finding that continuity of computation cannot survive any incremental substrate swap.

Each rung's gate has the same shape, survivable and evidenced before the next is
attempted. The ladder does not permit skipping a rung on the strength of a
projection, because the graveyard of §2 is a graveyard of skipped rungs.

## 4. The pJ/bit frontier: how much room is left in the only free variable

Section 1 established that pJ/bit is the whole game, and §3 placed a
bits-per-picojoule breakthrough as the hard gate on the cortex-scale rung. This
section asks the quantitative question those two leave open. How far is the best
demonstrated hardware from the 12 pJ/bit budget, and along which physical routes
might the gap close? The honest answer is that the frontier is close enough to be
tantalizing and far enough to be sobering. The leading approaches sit within a single
order of magnitude of the wall, and none has crossed it at scale.

The obstacle every route shares is that tissue is hostile to the obvious carrier.
Radio-frequency electromagnetic signalling, the default for wearables, is absorbed
strongly by warm saline tissue, so an implant radiating enough RF to be heard outside
the skull spends most of its budget heating the very tissue the wall protects. The
escape routes each swap the carrier for something tissue tolerates better, and each
pays a different transduction tax.

- Ultrasonic, as in neural dust. Acoustic power couples into tissue far more
  efficiently than RF, which is why the neural-dust analysis can deliver about 500 μW
  to a mote and why the 12 pJ/bit budget is derived at ultrasonic scale in the first
  place.[^dust] The open problem is not the physics of a single mote but aggregating
  millions of them without the beamforming and readout electronics breaching the wall
  in aggregate.

- Electro-quasistatic, using dipole coupling. Rather than radiate, this approach
  couples the body itself as a conductor. The biphasic quasistatic
  brain-communication work from Sen's group at Purdue avoids the transduction losses
  of ultrasound, optics, and magneto-electrics by keeping the signal path fully
  electrical, achieving an end-to-end channel loss of only about 60 dB across the
  skull. It reports a measured uplink at roughly 52 pJ/bit.[^qbc] That is the most
  directly comparable real number in the literature, and it is about four times the
  12 pJ/bit budget. The best demonstrated wireless neural link is, in other words,
  still a factor of a few over the wall, at region scale, before whole-cortex
  aggregation is even attempted.

- Optical and magneto-electric. Both offer attractive channels in principle but pay
  large energy-conversion penalties turning electrical signals into photons or
  mechanical strain and back, so they are live research directions rather than
  demonstrated wins against the budget.[^qbc]

Two facts follow, and they set the tone for everything above the subsystem rung.
First, the gap is not astronomical. A fourfold improvement on the best demonstrated
link is a normal decade of device engineering, not a miracle. Second, the gap is real
and it is measured against the friendliest scale, since 52 pJ/bit is a single
region's uplink, and the wall of §1 tightens as coverage grows, because aggregate
heat scales with aggregate bits. Closing that fourfold gap at region scale and then
holding it across a million-fold increase in channels are different problems, and
only the first is within sight. This is the concrete content of the phrase "a
bits-per-picojoule breakthrough": not one number, but a number held as the interface
scales toward the whole cortex.

Figure 5. The pJ/bit landscape on a log scale, from the Landauer floor near 3 × 10⁻²¹
joules per bit, through the 12 pJ/bit thermal budget, to the best demonstrated
quasistatic link at about 52 pJ/bit and legacy implantable CMOS transceivers near 295
pJ/bit. The budget sits far above the physical floor, which is the point of the next
paragraph.

How far the floor actually is. The ultimate bottom of the pJ/bit axis shows that the
wall is an engineering limit and not a physical one.
The thermodynamic floor on erasing a bit is the Landauer bound, about 3 × 10⁻²¹
joules at body temperature, which is kT ln 2 at 310 K.[^landauer] The 12 pJ/bit
budget sits roughly nine orders of magnitude above that floor, and the best
demonstrated neural link near 52 pJ/bit sits higher still. The floor is not even
fixed, since Bennett and others showed that logically reversible computation can in
principle approach zero dissipation per operation, circumventing the Landauer cost
that irreversible erasure must pay, though only in the limit of vanishing
speed.[^bennett] The brain itself is no exemplar of efficiency here. It runs on about
20 W,[^attwell] and its per-signal energy cost, dominated by restoring ion gradients
after each synaptic event and action potential rather than by the Landauer-irreducible
information itself, likewise sits many orders of magnitude above the physical minimum.
The lesson is not that a near-Landauer interface is buildable soon. It is that nothing
in physics forbids driving pJ/bit down by the factor the cortex-scale rung needs. The
wall is real, but it is nowhere near the floor, and the room between them is exactly
the room the ladder is trying to climb into. This is the same
thermodynamics-of-computation lens the sibling audit applies to the accelerated-
simulation and energy-budget premises, where the Landauer bound sets the per-mind
compute cost on the far side of migration (see that paper's §4.6).[^sibling] The same
lens runs outward as well as inward. The OCS corpus's Paper E forward-models a
Landauer-limited waste-heat technosignature at astrophysical scale, the black-hole-scale
counterpart to the interface-scale heat wall of §1, so the two papers bound the
thermodynamics of computation from opposite ends: a single cortex under 40 mW/cm² here,
an engineered intermediate-mass black-hole system dumping the waste heat of computation
there.[^papere]

One further number reframes the budget from the other end. Section 1 fixed the cost
of moving a bit; the traffic itself is smaller than intuition suggests. Zheng and
Meister estimate that the human behavioral throughput, the rate at which a person
actually decides and acts, is only about 10 bits per second, even though the sensory
periphery gathers on the order of 10⁹ bits per second.[^slowness] The interface
problem lives in that gap. An implant that merely rides along with conscious behavior
needs a trivial bit rate, whereas one that reconstructs the full sensory and motor
periphery needs a torrential one, and it is the second figure, not the first, that
the heat wall taxes. This is why the write problem of §3 and the cortex-scale rung
are the expensive ones. They are precisely the parts of the interface that operate at
the 10⁹ end of the range rather than the 10 end.

## 5. The agnostic bet

The top of the ladder forks on a question no experiment has yet settled, and this
paper deliberately declines to pick a side.

On one branch, cognition is substrate-independent. What matters is the computation a
brain performs, not the meat it runs on, and a sufficiently faithful scan emulated on
other hardware would be the same mind. The strongest positive argument for this
branch is Chalmers's fading-qualia thought experiment. Imagine replacing a subject's
neurons one at a time with functionally identical silicon units. If consciousness
were substrate-bound, then somewhere in that replacement the subject's experience
would have to fade, yet by construction the functional organization, and therefore
every behavior and introspective report, is preserved, so the subject keeps insisting
all is normal even as the qualia allegedly drain away. Chalmers argues that a
gradually fading consciousness that consistently reports itself as vivid is so
implausible that we should reject it, concluding that the fully silicon brain is as
conscious as the original, and that functional organization, not biology, fixes
experience.[^chalmers][^fadingqualia] If that holds, then at the cortex-scale rung a
scan-and-emulate migration becomes a coherent engineering target, and the top rung is
reachable in principle by copying rather than rebuilding. The argument is not
unopposed. Recent work by Mogensen and others attacks the step that treats a
subtly-fading-but-self-certain mind as absurd, so the debate is live rather than
closed.[^fadingqualia]

On the other branch, cognition is substrate-entangled. Milinković and Aru, arguing a
biological-computationalism position, hold that neural computation is inseparable from
the brain's physical structure, its energy constraints, and its continuous rather than
discretized dynamics, not an abstract algorithm that a different substrate could simply
rerun.[^aru] If that is right, a static scan throws away exactly the
part that does the computing, and upload-by-scanning is not merely hard but
incoherent, dead on arrival. The only path that preserves the computation is gradual
in-vivo replacement, swapping the substrate piece by piece while the system keeps
running, so the continuous dynamics are never interrupted.

The two branches meet in a way worth pausing on. The same fading-qualia thought
experiment that Chalmers runs in the abstract to argue for substrate independence is,
read as an engineering spec, a description of gradual in-vivo replacement, one unit
at a time, function preserved, the system never halted. The philosophy's cleanest
argument for the permissive branch is, operationally, the conservative branch's only
survivable procedure. That coincidence is the hinge of the bet.

The paper takes no position on which branch is real, because the question is both
unfalsifiable and load-bearing at once, a bad combination to bet on. Instead it notes
which design survives both outcomes, and gradual replacement works either way. If the
substrate is independent, gradual replacement is a valid path to migration and merely
a slower one than scanning. If the substrate is entangled, gradual replacement is the
only path. Scan-and-emulate, by contrast, survives only the first branch and dies on
the second. The ladder therefore favors gradual replacement regardless, not because
the substrate question has been answered but precisely because it has not, and
gradual replacement is the hedge that pays out under either answer. The bet is flagged
here as open, unfalsifiable today, and structurally decisive for everything above the
subsystem rung.

## 6. Harsh realities

Four consequences are commonly foregrounded in the popular treatment of this subject,
and this paper deliberately demotes them. Each is speculative conjecture rather than
a physical result, each is stated in a sentence or two, and each is tied to the rung
where it would bite. They are not the backbone of the argument. The heat wall is the
backbone, and these are what stand at the edges of the ladder.

- Death during early iteration (conjecture, at the subsystem-hybrid rung). The first
  attempts at sustained hybrid substrate will be run on someone, and a co-adaptation
  loop that fails the heat wall fails it in living tissue, which raises, before any of
  it is technical, the question of who consents and who is treated as expendable.

- Access inequality (conjecture, at the whole-brain and migrate rung). If migration
  ever works, it works first for whoever can afford it, and substrate independence
  then becomes the ultimate wealth stratifier, an owning class that can extend and
  multiply its cognition over a biological underclass that cannot.

- Continuity may be a copy (conjecture, at the migrate rung). The upgraded self may
  feel perfectly continuous while the original biological process simply ends, which
  is the ship-of-Theseus worry the §0 footnote parks, unfalsifiable and yet adopted
  the moment anyone chooses to migrate.[^1]

- Simulated worlds as a trap (conjecture, as a post-migrate attractor). A mind cheaply
  hosted in a simulation is a mind that can be cheaply captured, so extended life in
  engineered worlds risks hedonic capture and a quiet, consensual loss of agency long
  before it risks anything dramatic.

## 7. Close

The argument reduces to three claims held under one constraint. The race that matters
is bits per picojoule under the 40 mW/cm² wall, not electrode count, and every rung of
the ladder is scored on it, with the best demonstrated link still a factor of a few
over the budget at region scale and that factor set to tighten as coverage grows. The
ladder is evidence-gated, built from capability thresholds rather than dates, because
the field's record of dated promises is a graveyard and this paper adds no headstones
to it. And the ladder is built to survive either answer to the substrate question by
favoring gradual replacement, the one design that pays out whether cognition turns out
to be substrate-independent or substrate-entangled.

What sits at the top of the ladder, extended life lived in simulated worlds at
whatever subjective rate the substrate permits, is offered here as motivation rather
than prediction. It is the attractor that makes the climb worth attempting. It is not
a place this paper claims anyone will arrive, on any date, by any described means. The
wall is the only thing here stated as fact.

## AI assistance disclosure

Drafting, citation verification, derivation checking, and figure preparation were
performed with substantial assistance from a large language model (Claude, Anthropic),
under the author's direction. The author reviewed and takes full responsibility for
all claims, derivations, and references.

---

[^1]: The continuity-of-self objection, whether a mind migrated onto a new substrate
is the same person or a faithful copy that ends the original, is real and old, and it
is argued elsewhere at length. It is treated here as a footnote rather than a spine
(see §6, "Continuity may be a copy") because it is unfalsifiable and does not change
the engineering. The same ladder is climbed whether or not one believes the person at
the top is numerically identical to the person at the bottom.

[^dust]: Seo, Carmena, Rabaey, Alon, and Maharbiz, "Neural Dust: An Ultrasonic, Low
Power Solution for Chronic Brain-Machine Interfaces," arXiv:1307.2196. Adopts the
roughly 2 °C tissue limit and 40 mW/cm² thermal ceiling, and estimates about 500 μW
delivered to a roughly 100 μm node at about 2 mm depth with roughly 7 percent link
efficiency. <https://arxiv.org/pdf/1307.2196>

[^thermal]: Wolf, P.D., "Thermal Considerations for the Design of an Implanted
Cortical Brain–Machine Interface (BMI)," in *Indwelling Neural Implants* (CRC Press /
NCBI Bookshelf, NBK3932). Chronic device-induced cortical heating held below roughly
1 to 2 °C of local rise, with the implantable-device standard framing the same bound
as a thermal dose of CEM43 at most 2 (cumulative-equivalent-minutes at 43 °C).
<https://www.ncbi.nlm.nih.gov/books/NBK3932/>

[^stujenske]: Stujenske, J.M., Spellman, T., and Gordon, J.A., "Modeling the
Spatiotemporal Dynamics of Light and Heat Propagation for In Vivo Optogenetics,"
*Cell Reports* 12(3), 525–534 (2015). Light delivered for optogenetics warms local
cortex enough to alter single-neuron firing rates below any damage threshold,
evidence that a fraction of a degree already perturbs the signal an interface reads or
writes. doi:10.1016/j.celrep.2015.06.036.
<https://www.cell.com/cell-reports/fulltext/S2211-1247(15)00648-8>

[^linkbudget]: "A low-power communication scheme for wireless, 1000-channel
brain-machine interfaces," bioRxiv 2022.03.11.483996. Derives the same roughly
12 pJ/bit transmission budget for a node monitoring a 50 by 50 μm² patch (about 8
neurons at roughly 1 μW each) from the identical 2 °C and 40 mW/cm² thermal limit, and
notes that prior implantable CMOS transceivers ran near 295 pJ/bit, far above the
target. <https://www.biorxiv.org/content/10.1101/2022.03.11.483996.full.pdf>

[^barrese]: Barrese, J.C., Rao, N., Paroo, K., Triebwasser, C., Vargas-Irwin, C.,
Franquemont, L., and Donoghue, J.P., "Failure mode analysis of silicon-based
intracortical microelectrode arrays in non-human primates," *Journal of Neural
Engineering* 10(6), 066014 (2013). Retrospective analysis of 78 arrays implanted in
27 *Macaca mulatta* since 1996; performance degrades over months to a few years,
dominated by material and mechanical failures (insulation, connectors, leads) and the
chronic biological foreign-body reaction (glial encapsulation, neuronal die-back)
rather than by electronics. doi:10.1088/1741-2560/10/6/066014.
<https://pmc.ncbi.nlm.nih.gov/articles/PMC4868924/>

[^mesh]: Hong, G., Lieber, C.M., and colleagues, "Syringe-injectable mesh electronics
integrate seamlessly with minimal chronic immune response in the brain,"
*Proceedings of the National Academy of Sciences USA* 114(23), 5894–5899 (2017).
Ultra-flexible injected mesh probes form a gliosis-free interface that tracks
individual neurons stably for eight months to a year with minimal chronic immune
response, evidence that the foreign-body limit of the read-only rung is an
engineering target rather than a hard biological ceiling. doi:10.1073/pnas.1705509114.
<https://www.pnas.org/doi/10.1073/pnas.1705509114>

[^write]: Flesher, S.N., Collinger, J.L., Foldes, S.T., Weiss, J.M., Downey, J.E.,
Tyler-Kabara, E.C., Bensmaia, S.J., Schwartz, A.B., Boninger, M.L., and Gaunt, R.A.,
"Intracortical microstimulation of human somatosensory cortex," *Science
Translational Medicine* 8(361), 361ra141 (2016). Microstimulation of hand-area
somatosensory cortex evokes localized, somatotopically organized tactile percepts
with graded, amplitude-dependent intensity, stable over months. Demonstrates that the
write channel exists while underscoring the open problems of fidelity, selectivity,
channel count, and injected-charge limits at full-sensory scale.
doi:10.1126/scitranslmed.aaf8083.
<https://www.science.org/doi/abs/10.1126/scitranslmed.aaf8083>

[^sibling]: Companion audit, *The Science in Cognitive Husbandry: A Feasibility Audit
of a Speculative Scenario* (`cognitive-husbandry-feasibility.html`). Its §4.4 grades
the BCI write problem as the dominant unsolved sub-problem, requiring roughly seven to
eight orders of magnitude of write-side channel scaling; §4.6 prices post-migration
minds at the Landauer floor; §4.5 sets the alpha-band roughly 10 Hz cadence as the
candidate hard ceiling on subjective acceleration. This paper and that one share one
physics, the thermodynamics of computation, approached from the interface side here
and the whole-scenario side there.

[^papere]: Swanson (2026), "Engineered Intermediate-Mass Black Hole Systems:
Infrastructure Constraints, Observable Residue, and a Multi-Messenger Adjudication
Framework," Omega Centauri Society corpus, Paper E. Forward-models a Landauer-limited
waste-heat technosignature at astrophysical scale, the black-hole-scale counterpart to
this paper's interface-scale heat wall; both apply the same thermodynamics-of-computation
lens shared across the corpus (cf. [^sibling], §4.6 of the sibling audit).

[^landauer]: Landauer, R., "Irreversibility and heat generation in the computing
process," *IBM Journal of Research and Development* 5(3), 183–191 (1961).
doi:10.1147/rd.53.0183. The thermodynamic floor on an irreversible bit operation,
kT ln 2, about 3 × 10⁻²¹ J near body temperature. Used here only to fix the distance
between the 12 pJ/bit budget and the physical minimum, about nine orders of
magnitude, showing the wall is an engineering limit rather than a physical one.

[^bennett]: Bennett, C.H., "The Thermodynamics of Computation — a Review,"
*International Journal of Theoretical Physics* 21(12), 905–940 (1982).
doi:10.1007/BF02084158. Logically reversible computation can in principle approach
zero dissipation per operation, circumventing the Landauer erasure cost, though only
in the limit of vanishing speed, which is why the pJ/bit floor is not even fixed.

[^attwell]: Attwell, D. and Laughlin, S.B., "An energy budget for signaling in the
grey matter of the brain," *Journal of Cerebral Blood Flow & Metabolism* 21(10),
1133–1145 (2001). doi:10.1097/00004647-200110000-00001. The neural energy budget
underpinning the roughly 20 W whole-brain figure; most of that energy restores ion
gradients after signaling (action potentials about 47 percent, postsynaptic effects
about 34 percent) rather than paying the Landauer-irreducible cost of the information
moved.

[^slowness]: Zheng, J. and Meister, M., "The unbearable slowness of being: Why do we
live at 10 bits/s?" *Neuron* (2024); arXiv:2408.10234. Human behavioral throughput is
estimated at about 10 bits per second against a sensory intake near 10⁹ bits per
second, a gap that separates the trivial bit rate of a behavior-riding interface from
the torrential rate of one reconstructing the full sensory and motor periphery.
<https://arxiv.org/abs/2408.10234>

[^herculano]: Human brain scale anchors, about 86 billion neurons and roughly 10¹⁴
synapses (Herculano-Houzel and the standard neuroscience consensus).

[^bci2026]: BCI state of the art, 2026: Neuralink N1 at 1,024 channels (64 threads of
16 electrodes) across a dozen-plus experimental human implants; Paradromics Connexus
at roughly 65,000 electrodes; Synchron's Stentrode leading on the safety and
regulatory axis.
<https://www.fiercebiotech.com/medtech/elon-musks-neuralink-kickstart-high-volume-production-brain-computer-interface-devices>

[^qbc]: Chatterjee, Nath, Kumar, Jayant, and Sen, "Biphasic quasistatic brain
communication for energy-efficient wireless neural implants," *Nature Electronics* 6,
686–699 (2023). Electro-quasistatic dipole coupling avoids the transduction losses of
ultrasound, optical, and magneto-electric links, with about 60 dB end-to-end channel
loss at 55 mm and a measured uplink transmitter at roughly 52 pJ/bit, about four times
the 12 pJ/bit budget. <https://www.nature.com/articles/s41928-023-01000-3>

[^brainemu]: State of Brain Emulation report, 2025, arXiv:2510.15745. A roughly 1 mm³
slab of mouse cortex densely reconstructed (about 120k neurons and 523M synapses);
cost per reconstructed neuron falling from about $16,500 (C. elegans) to roughly $100
(larval zebrafish); no organism yet mapped at more than 90 percent of neurons with
single-spike, simultaneous resolution; no validated running model of any nervous
system yet exists, so the bottleneck has shifted from data collection to
model-building; mouse whole-brain connectome projected around 2034, primate 2040s,
larval zebrafish full connectome expected around 2026.
<https://arxiv.org/pdf/2510.15745>

[^wbe2008]: Sandberg, A. and Bostrom, N., "Whole Brain Emulation: A Roadmap,"
Technical Report #2008-3, Future of Humanity Institute, Oxford University (2008). The
careful, explicit exemplar of 2000s roadmap optimism, framing WBE as reachable "by
extrapolations of current technology," and the benchmark the §2 graveyard measures
against. <https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf>

[^mammalproj]: Future projections for mammalian whole-brain simulations based on
technological trends in related fields (mouse cellular-level simulation feasible in
the 2030s, marmoset in the 2040s).
<https://www.sciencedirect.com/science/article/pii/S016801022400138X>

[^chalmers]: Chalmers, "The Singularity: A Philosophical Analysis" (uploading
section), the standard survey of the substrate-independence and scan-and-emulate
position. <https://consc.net/papers/uploading.pdf>

[^fadingqualia]: The fading-qualia argument and its critics. Chalmers, "Absent
Qualia, Fading Qualia, Dancing Qualia" (1995), the gradual neuron-replacement thought
experiment concluding that functional organization fixes conscious experience
(<https://philpapers.org/rec/CHAAQF>); Mogensen, "How to Resist the Fading Qualia
Argument," *Synthese* (2025) and related critiques, which contest the claim that a
subtly-fading-but-self-certain mind is absurd
(<https://www.globalprioritiesinstitute.org/wp-content/uploads/Andreas-Mogensen-How-to-Resist-the-Fading-Qualia-Argument.pdf>).
Read as an engineering spec rather than a philosophical device, the same
one-unit-at-a-time procedure is gradual in-vivo replacement.

[^aru]: Milinković, B. and Aru, J., "On biological and artificial consciousness: A
case for biological computationalism," *Neuroscience & Biobehavioral Reviews* 181,
106524 (2025). doi:10.1016/j.neubiorev.2025.106524. Argues that neural computation is
inseparable from the brain's physical, hybrid, and energy-constrained dynamics rather
than an abstract algorithm running on hardware; if the position holds, upload-by-scanning
is incoherent and only gradual in-vivo replacement preserves the computation.
<https://doi.org/10.1016/j.neubiorev.2025.106524>

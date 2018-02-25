# core papers
- hu et al, 2009
- J Platkiewicz, R Brette, 2010
- Lu, SM Roach, D Song, TW Berger, 2012
- C Koch, Ö Bernander, RJ Douglas, 1995

# to read
- Douglas, 1995
- Jack, Noble, & Tsien, 1975
- Henze, Buzsaki, 2001
- Brette references
- Berger refs
- web of science refs

# basic threshold
- Adrian 1914 - discovers the all-or-none response

# changing threshold
- *C Koch, Ö Bernander, RJ Douglas - Journal of computational …, 1995 - Springer "Do neurons have a voltage or a current threshold for action potential initiation?"*
	- effects of both current and voltage on action potential
	- neural networks operate in "rate" or "pulse/temporal" mode (Hopfield, 1994)
		- in rate mode you can average over the pulses, losing their temporal correlation and be fine
		- these networks generally have continuous output: the rate
		- in pulse/temporal mode, timing is very important
			- lots of different encoding schemes have been proposed
			- require a different single-cell representation
			- most popular is integrate-and-fire (like McCulloch & Pitts, 1943)
			- disagreement as to how biologically accurate this is
	- voltage v. charge threshold(review: Jack, Noble, and Tsien 1975)
	- it has been proposed (Hodgkin and Rushton, 1946; Noble and Stein, 1966; Jack et al., 1975) that the threshold condition for excitation of a cable is that a constant amount of charge be applied. It could be argued for our model cell that for very rapid inputs, the charge delivered by the somatic injection will not have tim to leak away into the dendrites
		- they say this doesn't seem to be the case
		- we say that we concur
- *J Platkiewicz, R Brette - PLoS Comput Biol, 2010 - journals.plos.org "A Threshold Equation for Action Potential Initiation"*
	- "In central neurons, the threshold for spike initiation can depend on the stimulus and varies between cells and between recording sites in a given cell, but it is unclear what mechanisms underlie this variability"
	- also used Hu et al 2009
	- "threshold variability in models depends crucially on the shape of the Na activation function near spike initiation (about 255 mV), while its parameters are adjusted near half-activation voltage (about 230 mV), which might explain why many models exhibit little threshold variability, contrary to experimental observations."
	- background
		- "there is an intense ongoing debate about the origin of threshold variability observed in vivo [8–14]"
		- "numerous experiments have shown that spike initiation does not only depend on the membrane potential but also on complex features of the inputs. For example, it depends on the preceding rate of depolarization [15–21] and on the preceding interspike intervals [12,22]"
		- "Developmental and learning studies have also shown that the threshold adapts to slow changes in input characteristic"
		- There are two additional sources of variability which are artefactual: the fact that the threshold is not measured at the site of spike initiation, and threshold measurement methods. The latter source is difficult to avoid in vivo because only spike onsets can be measured. The former one also seems technically very difficult to avoid in vivo, since spikes are initiated in the axon hillock, which is only a few microns large. Although the soma and AIS are virtually isopotential below threshold, experimentally measured values of threshold differ between the two sites [34] because, as we previously remarked, in vivo measurements correspond to spike onset rather than threshold and therefore take place after spike initiation, when the two sites are not isopotential anymore. This experimental difficulty may introduce artefactual variability in threshold measurements [14]
	- thresh defs
		- in vitro - failure threshold
		- in vivo - spike "initiation"
		- in models - equation
	- According to the threshold equation, most threshold variability was due to Na inactivation
	- threshold equation is correlated but not identical to empirical ‘‘threshold’’ measures, which measure spike onset rather than threshold (those normally overestimate the threshold)
	- compare using 1st deriv method
	- "We have not considered the effect of channel noise, i.e., fluctuations in Na channel gating [42,75–78], which result in random threshold variations. Although dynamical equations of fluctuations in Na channel gating are well set [79,80], they cannot be included in our theoretical framework because we neglected the time constant of Na activation (which leads to the exponential model)"
	- potassium increases threshold "It also results in threshold increase, although it is not additive. This effect also contributes to the neuron refractory period, not only by decreasing the membrane resistance, but also by increasing the spike threshold (see Fig. 5C)."
- *Lu, SM Roach, D Song, TW Berger - IEEE Transactions on …, 2012 - ieeexplore.ieee.org*
	- hippocampal slices from two-week-old male Sprague Dawley
	- "Neuron threshold is the transmembrane voltage level at which any further depolarization will activate a sufficient number of sodium channels to enter a self-generative positive- feedback phase (AP initiation)."
	- measured AP turning points and the actual AP thresholds estimated with varying stimulation intensities
	- background
		- in many neuron models that have an explicit threshold term, e.g., integrate-and-fire models, threshold is often assumed to be a constant [8], [15]–[19]. However, more and more evidence shows that threshold is not constant but rather is influenced by the AP firing history in a nonlinear dynamical manner [10]–[12], [14]
		- The importance of threshold dynamics in affecting spike generation can be recognized in some recently developed neuron models that adopted more realistic spike initiation mechanisms to replace constant voltage threshold and showed significant improvement in spike prediction [13], [20]–[22]
		- Different algorithms have been developed to measure threshold [12], [14], [28]–[33]. Those algorithms aim to find the point at the base of the AP where the membrane potential increases at its fastest rate, referred to as the “AP turning point” in this report. Since this turning point is defined phenomenologically instead of following the physiological definition of threshold, this assumption might be problematic. This study applies various stimulation paradigms to examine the relation between the two.
			- they measure AP turning point as max 3rd deriv
		- This spike-dependent attenuation in neuron excitability has been proposed to work as a noise filter that increases information transfer in nervous systems [14], and a coincidence detector that contributes to the synchronization among neurons [10], [11], [48]. Hence, this attenuation is also proposed to increase the homeostasis of the brain [52].
	- learning Volterra model to predict thresh from input spikes
	- they include a Comparison of Spike Prediction Accuracy Performed by Constant and Dynamical Threshold Models
	- differences
		1. didn't explain it		2. used the mean whereas we would probably use the median / max
		- they titrate intensity instead of duration		- they require "The stimulation intensities of spike trains were adjusted so that approximately 50% of the stimulations induced APs"
	- "Under a certain stimulation intensity, if both nonspiking PSPs and APs coexist, then the average of the maximum peak values of the nonspiking PSPs represents the neuron threshold, which is plotted in each panel of the right column in Fig. 5."
	- Measured threshold versus ISI. It shows that previous spiking activity generally increases the threshold value of the following spikes, while shorter ISI correlates with higher threshold value -> no, threshold depends on intensity of injection, not spike. *they don't see threshold changes w/ intensity, only previous spikes*
	- *Thus, a stronger depolarizing force is needed for the second AP. This is observed in Figs. 3(b) and 6, where higher thresholds correlate with shorter ISIs*

# threshold defs
- failure threshold
	- hu et al, 2009		
- sekerli, 2004 "Estimating Action Potential Thresholds From Neuronal Time-Series: New Metrics and Evaluation of Methodologies"
	- summary from brette: "The first derivative method consists in measuring the membrane potential V when its derivative dV/dt crosses an empirical criterion [8,34] (Fig. 1D). The second and third derivative methods consist in measuring V when respectively d2V/dt2 and d3V/dt3 reach their maximum [12,21]. Sekerli et al. (2004) compared those methods by asking electrophysiologists to identify spike onsets by eye on several membrane potential traces [47]. They found that visual inspection was best matched by the first derivative method, although that method critically relies on the choice of the derivative criterion (Fig. 2 C,D). However, all methods produced the same relative variations of the measured threshold"
	- compare 7 methods to human-selected thresholds
	- One of the most common definitions is the point at which the first temporal derivative of the membrane voltage trace exceeds an ad hoc value (e.g., 50 V/s in [3]; 10 V/s in [4]–[6]). Other definitions used in the literature include the points corresponding to the maximum of the second temporal derivative [7] and the third temporal derivative [8], [9] of the membrane voltage traces. Two additional methods are proposed in [10]. These curvature-based methods define a threshold via either the point of inflection or the maximum curvature of the action potential waveform.
	- note how the derivatives are calculated([17])
	
# ignore stochastic potassium
- G. DE BRUIN, I. GUY, AND R. J. VAN DEN BERG 1984
	- single K+ channel: 1 pS at -45 to -6 pS at +10mV
- Activation is very fast compared to all other relevant time constants (a fraction of ms), in particular the membrane time constant (Baranauskas & Martina, 2006)

# single-channel Na conductance
- 20.7 ± 0.7 pS. from (chatelier, 2010)
- noninactivating channel activity with a single-channel conductance of 15-25 pS carried a Cd2+- and Co2+-insensitive inward current (Distribution of single-channel conductances in cultured rat hippocampal neurons, Leona M. Masukawa, Anker J. Hansen, Gordon Shepherd)
- ~14 pS (Bezanilla, F. R. A. N. C. I. S. C. O. (1987). Single sodium channels from the squid giant axon. Biophysical journal, 52(6), 1087.)
	
# model
- hu et al 2009
	- 1.6s contribute to threshold, 1.2s contribute to somatic threshold	- potassium kv is delayed rectifier channels (Kinetic rates based roughly on Sah et al. and Hamill et al. (1991)) 
		- ka is rapidly inactivating
	- km is slow, noninactivating (muscarinic potassium channel)
	- kca Calcium-dependent potassium channel
	- axon and ais only have kv
	- somatodendritic have the other two potassium channels at .3,.3, compared to kv at 20	- not sure about channel density# threshold importance
- DL Jones, EC Johnson, R Ratnam - Frontiers in computational …, 2015 - ncbi.nlm.nih.gov
	- A stimulus-dependent spike threshold is an optimal neural coder – lots of articles like this
- helps improve accuracy of integrate and fire model

# quantifying energy cost
Quantifying the energetic cost of current fluxesFrom “Metabolic Energy Cost of Action Potential Velocity”“Attwell and Laughlin (2001) estimated that roughly 75% of the total ATP consumed by the gray matter of rodent brain is used for communication and computation. In their Fig. 3A, they show their estimates of how this 75% is divided. The largest share of this ATP is associated with action potentials.At 37°C the minimum free energy extracted from the ATP to adenosine diphosphate (ADP) that powers the Na+/K+ pump in heart is 50 kJ/mol (Jansen et al. 2003), and we used this value for the cost of ionic pumping in the squid axon at 18.5°C. Although the free energy has a different value at this temperature, it changes only the overall normalizations of the energy calculations below, but not the existence and locations of the energy minima; thus it does not alter the major conclusions of this study. Differences in pH can also affect the available free energy from ATP hydrolysis, but this, too, will change only the overall energy normalization.During each cycle of the ionic pump, which consumes a single ATP molecule, three sodium ions are expelled from the neuron whereas two potassium ions are brought in. However, given that an axon always returns to its resting potential, over all time the integrated Na+ and K+ membrane fluxes are nearly equal so long as other fluxes are much less. Because this assumption is consistent with Attwell and Laughlin's conclusion that most energy use goes to communication and computation, we thus assume that the third, i.e., extra Na+ being pumped is used to power other membrane transport phenomena that are metabolically unavoidable. For example, the Na+ gradient will be used to pump Ca2+, glucose, acidic amino acids, and anions. Especially important are CO2 and H2O in the form of HCO3−, whose buildup must be avoided but is the inevitable consequence of metabolism whenever ATP is consumed and regenerated through glucose or lactate. (Such a housekeeping role for the Na+/K+ pump has been pursued, even considered primary, by others, e.g.,Stein 2002.) Thus given the 3:2:1 ratio of Na+/K+/ATP, it is our presumption that the number of ATP molecules required to restore the concentration gradients after an action potential is half of the total number of sodium ions that permeate the membrane during the action potential or, equivalently, half of the potassium ions that leave.The number of ions can, in turn, be calculated by integrating the ionic currents over an appropriate time interval. We choose this interval to be the time from steady-state to the time to threshold. We understand that not everyone agrees with the fate of the third Na+ that is pumped per ATP (e.g., Attwell and Laughlin 2001). Fortunately, alternative formulations do not change the optimization results here. That is, one can rescale the energy consumed by a constant consistent with one's personal theory of the fate of the third Na+.Other sources of energy usage and loss are much smaller. During the HHSFL action potential, for example, the energy of Joule heating arising from the axial current is <3% of the net sodium flux energy and <1% of the total flux energy. We therefore neglect such effects.
Dear Editor and Reviewers,

Thank you for agreeing to accept the article for publication in PeerJ with a
minor revision. We appreciate the thorough feedback and are happy to make the
next revision of the paper that much better. Below we address all of the
comments from the Editor and Reviewers. All of the changes since the version we
first submitted can be viewed here:

https://github.com/csu-hmc/perturbed-data-paper/compare/v0.2...master

and we have also noted the individual Github pull requests that address each
item below.

Editor (Arti Ahluwalia)
=======================

   Please give a context and objective to the work, as noted by Reviewer 1 and
   2. This could stem from the funder driven requirement to share data openly
   (as suggested by R.3), but I am sure the data was generated and analysed for
   one or more specific research questions or hypotheses.

We have expanded the introduction paragraphs to clarify the context and
objective of the work. The research hypotheses we had in mind when designing
the experiments is now described more specifically. We also added a paragraph
explaining our grant's data sharing requirements. The specific changes can be
viewed here:

https://github.com/csu-hmc/perturbed-data-paper/pull/145

   Please address R2 and R3's specific comments to authors.

We have addressed all of the specific comments. Please see below.

Reviewer #1 (Morgan Sangeux)
============================

   The authors of the submission wish to share a comprehensive set of data
   related to the analysis of normal gait. I believe the data will be valuable
   for the gait/biomechanics community and I appreciate the work of the authors
   as well as their willingness to help others.

Thank you, we also believe that this data will be valuable to relevant
communities.

   However, I do not think the proposed manuscript represent a 'unit of
   publication'.

We understand that this manuscript is not a typical submission in this field
because it only focuses on the experimental methods and data description, but
we kindly disagree with your opinion that this does not "represent a 'unit of
publication'". Data papers are not yet widespread in all fields, but also are
not rare. The Wikipedia entry (http://en.wikipedia.org/wiki/Data_paper) gives
some context to the push for recognizing "Data Papers" as a valid "unit of
publication". Also see articles like DOI: 10.1371/journal.pone.0021101 which
discuss current data sharing practices.

Many journals and academic communities do accept these as valid. The validity,
of course, is being discussed and implemented by academic communities,
journals, and granting agencies. For example, the NSF which partially funded
this work now requires submissions to include a "data management plan".  Our
data management plan requires us to share all of the data and software created
during the project. This paper is a partial fulfillment of that grant
requirement. We have now noted this in the paper to be clear. The specific
changes can be viewed here:

https://github.com/csu-hmc/perturbed-data-paper/pull/145

PeerJ does not seem to have an official stance on whether it publishes data
papers, but the editorial office approved the scope of this paper when we
inquired before submitting. We are intentionally not including analyses,
results, and findings from this data in this paper but will be publishing those
in subsequent papers which will cite portions of the dataset herein.

   I suspect these data were collected for a purpose but this purpose is absent
   from the manuscript.

We felt our introduction went into great detail about the two main purposes for
collecting the data:

1. To provide a substantial amount of open and unrestricted data to the public.
2. To collect gait data rich in varied motion so that it may be useful for
   control identification methods.

Nevertheless, we have worked to improve the description of the purpose of
collecting the data and have been more specific about our research questions and
hypotheses. The specific changes can be seen here:

https://github.com/csu-hmc/perturbed-data-paper/pull/145

   As mentioned in basic reporting, there is no research question and therefore
   I do not think it can join the scholarly literature as is. I would strongly
   encourage the authors to re-submit their work/data as part of a paper WITH a
   research question.

See above, we have added more specific research questions.

Reviewer #2 (Paul Lee)
======================

   The submission should be ‘self-contained,’ should represent an appropriate
   ‘unit of publication’, and should include all results relevant to the
   hypothesis. Coherent bodies of work should not be inappropriately subdivided
   merely to increase publication count.
   (I am concern about this point, as this manuscript described an open-source
   data of gait movement, without any data analysis or hypothesis testing.
   Although I agree that the data are useful and worth publication, the authors
   could divide the results of their study for few more papers.)

Thank you for pointing this out. We had not seen this on the PeerJ website.

Before submitting the paper we enquired with the editorial office as to whether
a "data paper" was appropriate for PeerJ and they said that it was, so we
submitted. We are intentionally not including data analysis and hypothesis
testing because we believe the data can be used to test many hypotheses and
support more analyses than we can ever do. We do have some hypotheses of our
own but plan to publish the related results in separate publications. We agree
one should not be allowed to extract the methods section of just any paper and
publish it separately, but we believe that we have gone much further than any
typical methods section in the description of our experiments and the data;
thus this is suitable to stand on its own.

   The submission must describe original primary research within the Scope of
   the journal.
   (The authors mentioned that the objective of this study was to provide a
   rich gait movement data with fluctuations in speed, and I don't believe this
   was a primary research.)
   The submission should clearly define the research question, which must be
   relevant and meaningful.
   (Please see response above)

As mentioned above, PeerJ approved the scope of our paper before we submitted
it. Our work is original and if the `Wikipedia definition`_ of "primary
research" is correct, we believe our paper also meets that.

.. _Wikipedia definition: http://en.wikipedia.org/wiki/Primary_research

   Table 1. Why subject ID 1 trialled 1.2 m/s for three times but did not
   trialled 0.8 m/s and 1.6 m/s?

Subject 1 was a preliminary subject and was used to verify if the protocol
worked and the data collected was satisfactory. We happened to only record data
for one speed, but did three trials. We included this data because the
trials are the only ones that included lateral perturbations and we felt that
the valid kinematic data may be useful to future researchers. Our initial
intentions were to collect data with lateral and longitudinal perturbations for
all of the subjects, but that was thwarted by the equipment issues described in
the paper. We've noted this in the "Data Limitations" section. See:

https://github.com/csu-hmc/perturbed-data-paper/pull/142

   Page 4, line 120. Why the participants were required to wear a baseball cap?

We attached three markers to the subjects' head. For the marker protocol used,
these markers were best suited to locations that are typically covered by the
subject's hair. Ideally, we'd have shaved the subjects' hair and attached the
markers directly to the skin but we felt this was unnecessary because our
research motivations are primarily driven with by the need to discover control
mechanisms. The methods we intended to use for data analyses did not take into
account head orientation. So we decided to collect the head marker data but
sacrifice accuracy and place them on a securely fitting baseball cap. This has
been noted in the paper, see:

https://github.com/csu-hmc/perturbed-data-paper/pull/143

   Page 15, line 374. Why didn't the authors recode the trial numbers from 40
   onwards to 37, 38, ...?

The trial numbers were not recoded because our protocol for raw data is to
leave it as is. That is why it is called "raw" data. The more raw data is
manipulated, the more likely errors are introduced. We wanted to provide the
public as "raw" a view of the data as possible. The trial numbers provided have
not caused us any issues in processing and we do not see it as a major issue.
We have left this as is.

Reviewer #3 (Manoj Srinivasan)
==============================

   This article is an important (if unconventional) addition to the
   biomechanics literature. The article is a wonderful example of attention to
   detail in presenting the protocol and experiment used, in describing
   formatting and reliability of the data, and in providing simple
   computational tools (that do not require any proprietary data) for simple
   processing of the data. I believe that this article will be important in the
   field, and I hope that other researchers will follow Moore et al’s lead in
   sharing and documenting their data — that this is not a one-off but
   something everyone does.

Thank you for the compliment. We agree completely and definitely hope that
others follow suit.

   The authors could refer to new/emerging guidelines by some funding agencies
   (NSF, etc.) and some journals (Royal Society journals) that insist on making
   available all data funded by them or published by them. And your example
   could be a good model for such ‘required’ publication of data.

Thanks for the suggestion, we have now mentioned some of the new requirements
form funders and journals in this regard. See:

https://github.com/csu-hmc/perturbed-data-paper/pull/145

   The citation style seems a bit unorthodox, is this the Peerj recommendation?
   For instance, “David Winter’s published normative gait data, Winter (1990),
   is widely used in biomechanical studies …” could be: “David Winter’s
   published normative gait data (Winter, 1990) is widely used in biomechanical
   studies …”

Thanks for catching that. We were using the incorrect natbib citation style for
some of the citations. It is now fixed. See:

https://github.com/csu-hmc/perturbed-data-paper/pull/138

   “At another website, the CGA Normative Gait Database, Kirtley (2014) shares
   normative gait data from several studies …” Perhaps this sentence could be
   edited to avoid the possible misunderstanding that Kirtley conducted all
   these several studies. Might it be worth also citing the original studies
   from which the data is taken? This might be appropriate and feasible if you
   citations with numbers like [5-10].

PeerJ does not allow the [5-10] citation style and it isn't entirely clear what
the correct citation for each dataset in the database should be so we opted for
simply clarifying that Kirtley is a curator of the data from other
labs/studies. See:

https://github.com/csu-hmc/perturbed-data-paper/pull/139

   Physionet (http://www.physionet.org/), the Carnegie Mellon mocap database (
   http://mocap.cs.cmu.edu/ ), the Ohio State mocap database, the OU-ISIR
   database ( http://www.am.sanken.osaka-u.ac.jp/BiometricDB/GaitTM.html ),
   KIST database ( http://www.me.utexas.edu/~reneu/res/gait_toolbox.html ) are
   some other sources of public data of aspects of human movement, but again,
   all these either suffer from some of the issues that the authors point out,
   or mainly meant for video games, animations, or biometry rather than for
   detailed biomechanical analyses.  Please include some such databases in your
   introductory discussion (ones that seem most relevant).

We were aware of most of these but intentionally left out the graphics and
arbitrary motions datasets/bases because we are more concerned with gait. But
we've added most of these into the introduction be more complete, thanks for
the suggestion. See:

https://github.com/csu-hmc/perturbed-data-paper/pull/148

   Line 110. “Acceleration of treadmill” . Perhaps say “acceleration of
   treadmill base” or something so as to distinguish from the belt
   accelerations?

Fixed.

   page 6. The description of the ‘perturbation signals’ on page 6 does not
   explain what, if any, lateral movements of the treadmill base were imposed.
   Line 151 alludes to the possibility of ‘both’ longitudinal and lateral
   perturbations.

   Are the lateral perturbations used only in trials 6-8? I did not see the
   ‘both’ event for treadmill perturbations in the few other trial YAML files I
   looked at. Perhaps make an explicit note of this.

We have clarified that only one subject's trials included lateral motion and
have given a description of that motion including a graph showing the time
history of the lateral deviation. See:

https://github.com/csu-hmc/perturbed-data-paper/pull/151

   If the perturbations are only in the fore-aft direction, it is possible that
   the data set is insufficiently rich to infer the human walking control
   system; but it is also possible that the data set is rich enough due to
   sufficient coupling of the various degrees of freedom (fore-aft and sideways
   degrees of systems, to be a bit colloquial).

Yes, this data may only be suitable for longitudinal control studies. We had
hoped to have longitudinal and lateral perturbations for the entire study but
were foiled by the unforeseen equipment limitations. But we have added the
stride width comparisons between unperturbed and perturbed data when only
longitudinal perturbations are applied and it turns out there is a relative
increase in stride width. So it may be useful for lateral control studies. See:

https://github.com/csu-hmc/perturbed-data-paper/pull/136

   Line 184-185. “When belt speed is not constant, the inertia of the rollers
   and motor will induce error in the force plate x axis moment, and hence, the
   anterior-posterior coordinate (z axis) of the center of pressure that is
   measured by the instrumentation in the treadmill.” This comment by the
   authors creates doubt in the reader’s mind as to whether the other force
   values are reliable. Perhaps the authors could add an explicit note allaying
   any such doubts.

We've added a bit more explaining how this can be remedied with the cited
paper. See:

https://github.com/csu-hmc/perturbed-data-paper/pull/147

   Line 194. The abbreviation ‘YAML’ is used without previous definition. While
   ASCII is a common-enough word, I’d suggest that YAML is not. Perhaps the
   authors could explain what YAML is in the following sentence, and then refer
   to one of their YAML listings (Listing 1.) in that sentence. Please look for
   other uncommon abbreviations to clarify throughout the paper.

YAML is now defined in a footnote. See:

https://github.com/csu-hmc/perturbed-data-paper/pull/137

   232. TSV (tab separated file). perhaps the expansion in parenthesis.

We defined TSV at the first mention of it, so we did not add any more
definitions.

   Figure 4, caption. Perhaps indicate in your caption what the ‘zero’ for your
   angles correspond to? Alternatively, what does the ‘calibration pose’
   correspond to? I believe that the convention used is different from, for
   instance, David Winter’s data (which is, of course, fine). I believe -90
   degrees ankle corresponds to quite standing in this figure, whereas in
   Winter’s data, 0 degrees ankle is close to quiet standing.

We've added clarification of the nominal configuration, i.e. joint angles = 0.
See:

https://github.com/csu-hmc/perturbed-data-paper/pull/140

   374. Is there a reason why the authors did not re-arrange the trial numbers
   for publication — ignoring accidentally skipped trials, etc?

See the explanation given for reviewer #2's same question.

   Figure 5. Nice figure. It would be interesting to see step width
   distributions as well, comparing perturbed and unperturbed, as it would
   answer my question of whether people’s sideways dynamics were substantially
   affected as well. This is not absolutely necessary for the point that the
   authors wish to make, but could be a quick easy thing for the authors to
   generate from their data (especially given that they have already estimated
   the stride-length, step width is probably only a couple of lines of code!).

We've added the stride width and are happy to report that there is some
increase in stride width given longitudinal perturbations. And yes, it only
took a few more lines of code. See:

https://github.com/csu-hmc/perturbed-data-paper/pull/136

   pages 16-17. I especially liked the ‘Data Limitations’ section. But I would
   suggest that all of these limitations be included as part of the meta data
   in the corresponding YAML files. For instance, in lines 378-381, you state
   that the force measurements should not be trusted in trials 6-15. I checked
   the YAML file for trial 6 and 15 (T006 and T015) to see if its ‘notes’
   contained the same note, and it did not (unless I missed something). I think
   this would be very useful. Of course, I do see that other types of
   limitations or explanations are in the ‘notes’ section of the YAML file.

The only thing that is not included the YAML files are our recommendations to
avoid using the ground reaction loads for trials 6-15. But these are included
in the README file that is included in both of the compressed data files. We
have opted to leave this as is to avoid creating a new version of the dataset.

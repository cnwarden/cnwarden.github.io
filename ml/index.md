---
layout: post_mine
title:  machine learning
---

# CoreNLP

[Stanford Relation Extractor](http://nlp.stanford.edu/software/relationExtractor.html)

Stanford relation extractor is a Java implementation to find relations between two entities. The current relation extraction model is trained on the relation types (except the 'kill' relation) and data from the paper `Roth and Yih, Global inference for entity and relation identification via a linear programming formulation, 2007`, except instead of using the gold NER tags, we used the NER tags predicted by [Stanford NER classifier](http://nlp.stanford.edu/software/CRF-NER.shtml) to improve generalization.

---
layout: post_mine
title:  machine learning
---

# [OpenNLP](http://opennlp.apache.org/)

The Apache OpenNLP library is a machine learning based toolkit for the processing of natural language text.

It supports the most common NLP tasks, such as `tokenization, sentence segmentation, part-of-speech tagging, named entity extraction, chunking, parsing, and coreference resolution`. These tasks are usually required to build more advanced text processing services. OpenNLP also includes `maximum entropy` and `perceptron` based machine learning.

# [CoreNLP](http://nlp.stanford.edu)

[Stanford Relation Extractor](http://nlp.stanford.edu/software/relationExtractor.html)

Stanford relation extractor is a Java implementation to find relations between two entities. The current relation extraction model is trained on the relation types (except the `kill` relation) and data from the paper `Roth and Yih, Global inference for entity and relation identification via a linear programming formulation, 2007`, except instead of using the gold NER tags, we used the NER tags predicted by [Stanford NER classifier](http://nlp.stanford.edu/software/CRF-NER.shtml) to improve generalization.

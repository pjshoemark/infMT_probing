# infMT_probing


## 2nd person pronouns

[/2p_pronouns/MTNT/](https://github.com/pjshoemark/infMT_probing/tree/master/2p_pronouns/MTNT) contains automatically extracted examples from MTNT in which a 2nd person personal pronoun is used in the source text and/or the target text.


### Extracted from aligned data:

In `*.-aligned.tsv`, columns are as follows:

1. Source Text 
2. Target Text
3. Space separated list of identified pronouns and the words they are aligned to. Format: {index}\_{source-token}:{index}\_{aligned-target-token}
5. Are there more 2p pronouns in Source or in Target? {S, T, 0}
6. Are T or V forms used? {0, T, V, Both}

The alignments are the ones Graham obtained using fastalign (original aligned dataset here: http://phontron.com/data/wmt2019-aligned-data.tar.gz)


<hr>

### Extracted from un-aligned data:

In `*.en-fr.tsv` and `*.fr-en.tsv`, columns are as follows:

1. ID  
2. Source Text 
3. Target Text
4. 2p pronouns identified in Source (with counts)
5. 2p pronouns identified in Target (with counts)
6. Are there more 2p pronouns in Source or in Target? {S, T, 0}
7. Are T or V forms used? {0, T, V, Both}

_NB: T forms are more prevalant in French source texts, whereas V forms are more prevalant French reference translations:
ignoring examples where both T and V forms are used, the T/V ratio is 3210/510 for French source texts, vs. 2063/4249 for French reference translations._


 


In `*.en-ja-pronouns.tsv` and `*.ja-en-pronouns.tsv`, the Japanese text has been tokenised using [KyTea](http://www.phontron.com/kytea/), and Japanese personal pronouns (1st, 2nd, and 3rd person) have been marked up such that each pronoun X is surrounded by <<< X >>>_{1,2,3} indicating the person of the pronoun. 
Columns are as follows:

1. ID  
2. Source Text 
3. Target Text
4. 2p pronouns identified in Source (with counts)
5. 2p pronouns identified in Target (with counts)
6. Are there more 2p pronouns in Source or in Target? {S, T, 0}


_NB: In Japanese source texts, 2p pronouns were identified in 70 out of 6506 MTNT training examples (1%), while in Japanese reference translations of English source texts, 2p pronouns were identified in 770 out of 5775 MTNT training examples (13%)._



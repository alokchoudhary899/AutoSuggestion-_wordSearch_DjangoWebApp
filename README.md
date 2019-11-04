# AutoSuggestion-_wordSearch_DjangoWebApp

1. Matches occur anywhere in the string, not just at the beginning. For example, eryx
   matches archaeopteryx (among others).
2. The ranking of results  satisfy the following:
   a. Assume that the user is typing the beginning of the word. Thus, matches at the
      start of a word be ranked higher. For example, for the input pract, the result
      practical  be ranked higher than impractical.
   b. Common words (those with a higher usage count) rank higher than rare
      words.
   c. Short words rank higher than long words. For example, given the input
      environ, the result environment rank higher than environmentalism.
      i. As a corollary to the above, an exact match always be ranked as the
      first result.

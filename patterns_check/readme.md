# patterns_check.py
This series of functions can be used to check patterns in abstracts, such as math, HTML, and URLs.
It was used on abstracts from OpenAlex, but can be used on any string.
Returns a boolean indicating whether the pattern is found in the string.

Works well if using with Pandas to assign a bool value to a new column when vectorizing.
Example usage:
df['has_math'] = df['abstract'].apply(check_math_pattern)

## part of Poppy Riddle's dissertation research.

## todo:
- [ ] unicode block detection for other than Latin
- [ ] arg to use re method for capturing all matches, not just the first match.

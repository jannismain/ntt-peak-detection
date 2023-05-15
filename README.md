# Peak Detection

## Plan

- [x] Research peak detection algorithms
- [ ] Setup project structure
- [ ] Implement and test peak detection algorithm
- [ ] Add FastAPI web interface

## Background

### What is a peak?

A peak (or local maximum) can be defined in many ways depending on the specific use case and algorithm used.

A naive definition could be that a peak is a value that is higher than both of its neighbours

$$ v_{i-1} < v_{i} > v_{i+1} $$

- what about plateus ($v_{i-1} < v_{i} = v_{i+1}$, $v_{i-1} = v_{i} = v_{i+1}$?
- what about first and last values?

If there is a clear separation of regular and peak values, one could also define a peak as a value thats above some threshold

$$ v_{i} > v_{threshold} $$

- how to determine threshold? (minimize false positives and negatives)
- multi-pass processing required? (first pass to calculate threshold, second pass to find peaks)
- single-pass processing with adaptive threshold? what about initial values? look-ahead?

### Data preprocessing

As the requirements state that the data will not include noise, so data preprocessing can initially be disregarded.

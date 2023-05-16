# Peak Detection

## Plan

- [x] Research peak detection algorithms
- [x] Setup project structure
- [x] Implement and test peak detection algorithm
- [x] Add FastAPI web interface

## Getting Started

### Installation

    pip install git+https://github.com/jannismain/ntt-peak-detection.git

### CLI Usage

    ntt_peaks
    ntt_peaks [[CSV_FILE] ..]

### API Usage

Start API Server

    uvicorn ntt_peaks.api:app

Query peak detection algorithm with list of comma-separated values

    $ curl localhost:8000/detect_peaks?v=0,0,5,0,0
    [2]

## Background

### What is a peak?

A peak (or local maximum) can be defined in many ways depending on the specific use case and algorithm used.

A naive definition could be that a peak is a value that is higher than both of its **neighbours**

$$ v_{i-1} < v_{i} > v_{i+1} $$

- what about plateaus ($v_{i-1} < v_{i} = v_{i+1}$, $v_{i-1} = v_{i} = v_{i+1}$?
- what about first and last values?
- what about very low peaks?

If there is a clear separation of regular and peak values, one could also define a peak as a value thats above some **threshold**

$$ v_{i} > v_{threshold} $$

- how to determine threshold? (minimize false positives and negatives)
- multi-pass processing required? (first pass to calculate threshold, second pass to find peaks)
- single-pass processing with adaptive threshold? what about initial values? look-ahead?

Maybe a combined approach (**neighbours + threshold**) could reduce the number of low peaks that neighbours shows while removing the non-peaks that the pure threshold approach shows.

### Data preprocessing

As the requirements state that the data will not include noise, data preprocessing can initially be disregarded.

## Final Thoughts

- interesting problem, as peak detection seems to highly depend on the characteristics of the data trying to detect peaks from
- solution (**neighbours+threshold**) works reasonably well on training data without much hyperparameter optimization
- solution to parsing list of numbers in FastAPI seems too complicated
- requirements not fulfilled completely, as API only works on single list of values, not list of value pairs right now (peak index instead of peak x-value is returned)
  - peak detection algorithms mostly work on y-values only
  - Should have used a Panda dataframe to represent data in more convenient and performant way -> limited prior experience with Python data science libraries
  - Own representation (`Signal(x,y,label)`) surely not the best way

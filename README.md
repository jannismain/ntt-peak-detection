# Peak Detection

![preview](https://github.com/jannismain/ntt-peak-detection/assets/14290527/9610a54c-1d23-46d7-9191-708fb654724e)

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

## Implementation Details

Peak detection algorithms are implemented in the `ntt_peaks.lib` module and picked-up by the cli demo tool (`ntt_peaks.__main__`) automatically. This allows for rapid prototyping of different algorithms and compare them on different data sets.

The FastAPI interface is implemented within `ntt_peaks.api`. It was refactored into a package to separate the (messy) argument parsing from the implementation of the endpoints (or paths).

Data loading is being handled by `ntt_peaks.data`. The package also includes the example data provided with the task description for demonstration purposes. A custom representation of the data `ntt_peaks.Signal` is included to bundle x-values, y-values and its label into a single object.

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

## Plan

- [x] Research peak detection algorithms
- [x] Setup project structure
- [x] Implement and test peak detection algorithm
- [x] Add FastAPI web interface

## Final Thoughts

- interesting problem, as peak detection seems to highly depend on the characteristics of the data trying to detect peaks from
- algorithm (**neighbours+threshold**) works reasonably well on training data without much custom optimization (threshold value is $2*mean$)
  - performance on data with much higher/lower variance likely worse -> different way of determining threshold value
- solution to parsing list of numbers in FastAPI seems too complicated
- requirements not fulfilled completely, as API only works on single list of values, not list of value pairs right now (peak index instead of peak x-value is returned)
  - peak detection algorithms mostly work on y-values only
  - Should have used a Panda dataframe to represent data in more convenient and performant way -> limited prior experience with Python data science libraries
  - Own representation (`Signal(x,y,label)`) surely not the best way

### Next Steps

- extend api to support x- and y-values and return x-values of peaks (not index of y-values)
- if no algorithm works on all data consistently, algorithm selection and parametrization should be included in the api call
- extend test suite to include more corner cases and examples

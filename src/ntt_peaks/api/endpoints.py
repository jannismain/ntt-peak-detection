from fastapi import Query

from ntt_peaks import detect_peaks

from . import CommaSeparatedList, app


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/detect_peaks")
def get_items(v: CommaSeparatedList[int | float] = Query(...)):
    return detect_peaks(v, "neighbours_and_threshold")

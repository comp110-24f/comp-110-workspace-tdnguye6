"""Python Playground"""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    is_good: bool = int(scores[idx]["score"]) >= thresh
    is_last: bool = idx + 1 == len(scores)

    if is_last:
        return is_good
    elif not is_good:
        return is_good
    else:
        return all_good(scores, thresh, idx + 1)


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "8"},
    {"name": "Ada", "score": "8"},
    {"name": "Pip", "score": "10"},
]

print(all_good(scores=pack, thresh=8, idx=0))

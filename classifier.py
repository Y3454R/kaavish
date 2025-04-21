from thaats import THAATS


def classify_thaat(input_notes):
    results = []

    for thaat in THAATS:
        thaat_notes = set(thaat["notes"])
        input_set = set(input_notes)

        matched = thaat_notes.intersection(input_set)
        score = len(matched) / len(thaat_notes)

        match_type = "Exact" if score == 1.0 else "Partial" if score >= 0.6 else "Low"
        if score >= 0.6:
            results.append(
                {
                    "name": thaat["name"],
                    "score": round(score, 2),
                    "match_type": match_type,
                    "matched_notes": sorted(matched),
                    "missing_notes": sorted(thaat_notes - input_set),
                }
            )

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

import pandas as pd

from drugdiscovery.filters.lipinski import apply_lipinski
from drugdiscovery.filters.veber import apply_veber
from drugdiscovery.io.docking_scores import merge_docking_scores
from drugdiscovery.prioritization.scoring import (
    add_ligand_efficiency,
    add_priority_score,
)
from drugdiscovery.validation.descriptors import validate_descriptors_for_ranking


def rank_hits(
    df: pd.DataFrame,
    docking_scores: pd.DataFrame | None = None,
    validate_descriptors: bool = True,
) -> pd.DataFrame:
    """
    Rank compounds using drug-likeness filters, docking scores,
    ligand efficiency, and a weighted priority score.

    Parameters
    ----------
    df:
        Compound library table.

    docking_scores:
        Optional external docking-score table. If supplied, it is merged into
        the compound library using the compound_id column.

    validate_descriptors:
        If True, ranking stops when required descriptor values are missing.
    """
    result = df.copy()

    if docking_scores is not None:
        result = merge_docking_scores(result, docking_scores)

    if validate_descriptors:
        validate_descriptors_for_ranking(result)

    result = apply_lipinski(result)
    result = apply_veber(result)
    result = add_ligand_efficiency(result)
    result = add_priority_score(result)

    result = result.sort_values("priority_score", ascending=False)

    return result

import pandas as pd

from drugdiscovery.filters.lipinski import apply_lipinski
from drugdiscovery.filters.veber import apply_veber
from drugdiscovery.io.docking_scores import merge_docking_scores
from drugdiscovery.prioritization.scoring import (
    add_ligand_efficiency,
    add_priority_score,
)


def rank_hits(
    df: pd.DataFrame,
    docking_scores: pd.DataFrame | None = None,
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
    """
    result = df.copy()

    if docking_scores is not None:
        result = merge_docking_scores(result, docking_scores)

    result = apply_lipinski(result)
    result = apply_veber(result)
    result = add_ligand_efficiency(result)
    result = add_priority_score(result)

    result = result.sort_values("priority_score", ascending=False)

    return result

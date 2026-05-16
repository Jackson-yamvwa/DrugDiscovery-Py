import pandas as pd

from drugdiscovery.filters.lipinski import apply_lipinski
from drugdiscovery.filters.veber import apply_veber
from drugdiscovery.prioritization.scoring import (
    add_ligand_efficiency,
    add_priority_score,
)


def rank_hits(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rank compounds using drug-likeness filters, ligand efficiency, and
    a weighted priority score.
    """
    result = df.copy()

    result = apply_lipinski(result)
    result = apply_veber(result)
    result = add_ligand_efficiency(result)
    result = add_priority_score(result)

    result = result.sort_values("priority_score", ascending=False)

    return result

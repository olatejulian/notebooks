import pandas as pd


def get_pokedex(pokedex_path: str) -> pd.DataFrame:
    df = pd.read_csv(pokedex_path, sep=",", quotechar='"')

    df.set_index("Number", inplace=True)

    return df


def filter_by_location(dataframe: pd.DataFrame, location: str) -> pd.DataFrame:
    local_filter = dataframe["Location"].str.contains(location, na=False)

    return dataframe[local_filter]


def save_to_csv(dataframe: pd.DataFrame, path: str) -> None:
    dataframe.to_csv(path, index=False, sep=";")

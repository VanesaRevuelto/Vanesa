import requests
from typing import List, Optional, Dict, Any



def fetch_data(url: str) -> Optional[Dict[str, Any]]:
    """
    Makes a GET request to the provided URL and returns the JSON data.

    Args:
        url (str): The URL to make the request to.

    Returns:
        Optional[Dict[str, Any]]: The JSON data from the response if successful, or None in case of an error.
    """
    pass

def get_water_type_url() -> Optional[str]:
    """
    Retrieves the URL for the "Water" type Pokémon from the PokeAPI.

    Returns:
        Optional[str]: The URL to fetch Water-type Pokémon, or None if not found or error occurs.
    """
    pass

def fetch_water_pokemons() -> List[str]:
    """
    Fetches the list of all Water-type Pokémon by making an API request.

    Returns:
        List[str]: A list of names of Pokémon that are of Water type.
    """
    pass

def display_pokemons(pokemons: List[str]) -> None:
    """
    Displays the names of all Water-type Pokémon in a readable format.

    Args:
        pokemons (List[str]): A list of Pokémon names to be displayed.
    """
    pass

if __name__ == "__main__":
    """
    Main function to fetch and display Water-type Pokémon.
    """
    pass

def get_city_country(city,country,population=None):
    """返回输入城市和对应的国家"""
    if population:
        return f"{city} - {country} - {population}"
    else:
        return f"{city} - {country}"

def test_get_city_country():
    city_country = get_city_country("shanghai","china")
    assert city_country == "shanghai - china"

def test_get_city_country_population():
    city_country_population = get_city_country("LA","US","500000")
    assert city_country_population == "LA - US - 500000"
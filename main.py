from get_list_of_msoa_lsoa import get_lsoas, get_msoas
from scraper_fns import scrape

BLOCK_SIZE = 200

if __name__ == "__main__":
    get_lsoas()
    get_msoas()
    scrape(BLOCK_SIZE, "all_lsoas_with_coords.csv", "s3://alpha-everyone/travel_time_2/lsoas", "lsoa11cd", "lsoa")
    scrape(BLOCK_SIZE, "all_msoas_with_coords.csv", "s3://alpha-everyone/travel_time_2/msoas", "msoa11cd", "msoa")
# Pawnshop Scrapy Spider 

## Overview

The **Pawnshop Scrapy Spider** is a web scraping tool designed to extract pawnshop details from the "[website](https://www.pawnshops.net/search.php?whatcountry=US&whatstate=)". By automating the process of data extraction, this spider navigates through pages of pawnshop listings, gathering key information such as name, address, locality, region, postal code, and telephone number.

## Features

- **Automated Crawling**: The spider autonomously navigates through multiple pages of pawnshop listings, covering a wide range of data.
- **Data Extraction**: It efficiently extracts relevant details from individual pawnshop pages using carefully crafted CSS selectors.
- **Pagination Handling**: The spider manages pagination to systematically scrape all available listings.

## Getting Started

### Prerequisites

- **Python 3.7 or higher**: Ensure you have a compatible Python version installed.
- **Scrapy Library**: Install the Scrapy library using `pip`:
   `pip install scrapy`


### Installation
**Clone the Repository:** Start by cloning this repository to your local machine:

```git clone https://github.com/eniayejudaniel/Pawn-Shops-In-US-Web-Scraper-with-Scrapy```


**Virtual Environment:** Set up a virtual environment to isolate project dependencies:

```python -m venv venv```
     # On Windows: `venv\Scripts\activate`

**Install Dependencies:** Install the required packages using the provided requirements.txt file:
`pip install -r requirements.txt`

## Usage
Run the Spider: Execute the spider with the following command:
`scrapy crawl pawn_shop -o pawnshop_output.csv`

This command initiates the spider and directs the scraped data to be saved in a CSV file named pawnshop_output.csv.

## Project Structure
. pawnshop.py: The core Scrapy spider code
. pawnshop_output.csv: The CSV file containing the scraped pawnshop details.

## License
This project is licensed under the [MIT License](MIT License). See the LICENSE file for details.

## Acknowledgments
This project was developed as a solution to the need for efficiently collecting pawnshop data for analysis.

Special thanks to the Scrapy community for providing a robust web scraping framework.

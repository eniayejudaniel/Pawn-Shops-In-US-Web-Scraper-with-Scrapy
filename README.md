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

  ```bash
  pip install scrapy

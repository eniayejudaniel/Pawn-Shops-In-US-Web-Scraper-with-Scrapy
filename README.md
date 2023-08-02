# Scrapy Pawnshop Spider 

## Overview

This is a Scrapy spider designed to scrape pawnshop details from the "[website](https://www.pawnshops.net/search.php?whatcountry=US&whatstate=)" The spider navigates through pages of pawnshop listings, extracting relevant information such as name, address, locality, region, postal code, and telephone number.

## Features

- Navigates through multiple pages of pawnshop listings.
- Extracts details from individual pawnshop pages using CSS selectors.
- Handles pagination to scrape all available listings.

## Getting Started

### Prerequisites

- Python 3.7+
- Scrapy library (install with `pip install scrapy`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

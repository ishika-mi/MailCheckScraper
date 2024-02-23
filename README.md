This Scrapy spider scrapes domain names from the website [mailcheck.ai](https://www.mailcheck.ai/) categorized alphabetically.

## Requirements

- Python 3.x
- Scrapy

## Installation
1. Create a virtual environment to isolate the project dependencies. Open a terminal or command prompt and navigate to
   the project directory.

   ```
   python3 -m venv myenv
   ```

2. Activate the virtual environment:

   - For Windows:

      ```
      myenv\Scripts\activate
      ```

   - For Unix or Linux:

     ```
     source myenv/bin/activate
     ```

3. Clone the repository to your local machine.
   ```
   git clone <REPOSITORY URL>
   ```

4. Install the required Python packages using pip:
   ```
   pip install scrapy
   ```
5. Run the scraper
    ```
   cd /MailCheckScraper/mailchimp_scraping/mailchimp_scraping/spiders
   scrapy crawl <spider name>
   scrapy crawl mailcheck
   ```
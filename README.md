## Scraper for cdep.ro

### Setup


1. It's a good idea to set up a virtualenv. It's an even better idea to use
[virtualenvwrapper][].

   ```shell
   $ mkvirtualenv scraper-cdep
   ```

2. Get the code:

   ```shell
   $ git clone https://github.com/mgax/scraper-cdep.git
   $ cd scraper-cdep
```

3. Install dependencies:

   ```shell
   $ pip install -r requirements.txt
   ```

4. Run the scraper; the output will be in `out/people.json`.

   ```shell
   $ ./run scrape-people
   ```

[virtualenvwrapper]: http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvwrapper

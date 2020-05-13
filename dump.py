import os

import biothings, config
biothings.config_for_app(config)
from config import DATA_ARCHIVE_ROOT

import biothings.hub.dataload.dumper


class PdbDumper(bbiothings.hub.dataload.dumper.LastModifiedHTTPDumper):
    SRC_NAME = "covid_pdb_datasets"
    SRC_URLS = [
        "https://cdn.rcsb.org/rcsb-pdb/general_information/news_publications/SARS-Cov-2-LOI/SARS-Cov-2-all-LOI.tsv"
        ]
    # override in subclass accordingly
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)

    __metadata__ = {
        "src_meta": {
            'license_url': 'https://www.rcsb.org/pages/usage-policy',
            'licence': 'CC0 1.0 Universal',
            'url': 'https://www.rcsb.org/news?year=2020&article=5e74d55d2d410731e9944f52&feature=true'
        }
    }

    SCHEDULE = None  # crontab format schedule, if None, won't be scheduled

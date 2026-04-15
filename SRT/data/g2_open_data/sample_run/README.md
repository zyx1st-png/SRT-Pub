# G2 Open-Data Sample Run

This folder contains the first real sample run for the G2 open-data MVP.

Files:

- `pageviews_raw.csv`: raw Wikimedia pageviews pulled for the mapped sample pages
- `rho.csv`: topic-bin density proxy derived from pageviews
- `recentchanges_api.ndjson`: bounded recentchanges sample pulled via the MediaWiki action API
- `j.csv`: topic-bin flow proxy derived from recentchanges
- `trajectories.json`: fused `rho/J` window objects
- `path_summary.csv`: counts and frequencies of the derived path labels

Notes:

- The SSE/EventStreams path was tested but was too sparse/unstable for a short MVP window, so the first usable run uses `fetch-recentchanges-api`.
- The current sample only closes the pipeline once; it is not large enough for any stable `I_{SRT}^*` fit.

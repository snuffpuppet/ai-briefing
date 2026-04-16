# AI Briefing Sources

Two lists. **Primary feeds** are RSS sources the GitHub Action aggregates
into `daily-feed.json` for the daily briefing. **Further reading allowlist**
is the domain list the routine may link to in the "Related Reading" section
at the bottom of each briefing — these are not necessarily RSS-aggregated,
they're searched fresh each run.

Review this file quarterly. Prune dead sources, add new signal sources.
Last reviewed: 2026-04-16.

---

## Primary feeds

### Research labs and builder posts
- https://www.anthropic.com/news/rss.xml
- https://openai.com/blog/rss.xml
- https://bair.berkeley.edu/blog/feed.xml
- https://huggingface.co/blog/feed.xml
- https://deepmind.google/blog/rss.xml

### Production engineering and applied AI
- https://simonwillison.net/atom/everything/
- https://www.latent.space/feed
- https://newsletter.pragmaticengineer.com/feed
- https://www.interconnects.ai/feed
- https://hamel.dev/index.xml

### Software architecture and design
- https://martinfowler.com/feed.atom
- https://www.thoughtworks.com/rss/insights.xml
- https://netflixtechblog.com/feed
- https://engineering.fb.com/feed/

### Research aggregation and analysis
- https://importai.substack.com/feed
- https://thezvi.substack.com/feed
- https://jack-clark.net/feed/

### Journalism
- https://www.technologyreview.com/topic/artificial-intelligence/feed
- https://spectrum.ieee.org/feeds/topic/artificial-intelligence.rss
- https://arstechnica.com/ai/feed/

---

## Further reading allowlist

Domains the routine may link to in "Related Reading". The routine uses
web search constrained to these domains, excludes anything already
surfaced in today's primary briefing, and excludes anything older than
30 days.

### Labs and builders
- anthropic.com
- openai.com
- deepmind.google
- ai.meta.com
- research.google
- microsoft.com/en-us/research
- huggingface.co
- mistral.ai
- cohere.com
- databricks.com/blog

### Engineering and architecture
- martinfowler.com
- thoughtworks.com
- netflixtechblog.com
- engineering.fb.com
- aws.amazon.com/blogs/machine-learning
- cloud.google.com/blog
- stripe.com/blog/engineering
- shopify.engineering

### Independent analysis
- simonwillison.net
- latent.space
- interconnects.ai
- thezvi.substack.com
- hamel.dev
- eugeneyan.com
- newsletter.pragmaticengineer.com
- stratechery.com

### Journalism and research venues
- technologyreview.com
- spectrum.ieee.org
- nature.com
- arxiv.org          # cs.AI, cs.CL, cs.LG only
- paperswithcode.com
- semanticscholar.org

---

## Exclusions

Never suggest from: Medium personal blogs, LinkedIn posts, Twitter/X
threads, VC thought-leadership sites, content-farm aggregators, paywalled
articles the reader cannot access without subscription, and press-release
wire services.

# Structured data verification

Every generated page includes JSON-LD in its HTML. One shared LocalBusiness/Organization entity represents Houston Dumpster Rental at 2812 Center St, Houston, TX 77007, phone +1 346-660-2743. Coordinates matched by the official U.S. Census geocoder: latitude 29.76948834818, longitude -95.38765257458.

WebSite and WebPage/CollectionPage describe the site and its individual pages. BreadcrumbList follows visible navigation. Service entities describe the homepage and five service pages. The eight area guides use the same Houston business entity; no separate branches, addresses or offices are invented. No invented ratings, reviews, hours, prices, certifications or inventory. No deprecated HowTo markup or FAQ rich-result promise.

Run `python3 scripts/check_site.py` after `python3 scripts/build_site.py`. Checks cover 18 canonical pages, unique title/description, one H1 per page, all JSON-LD parseable and references resolved, exact confirmed phone/address, local assets and links, service/area content minimums, no orphan pages, robots and identical 18-URL XML sitemaps. Build is deterministic and uses only the Python standard library.

Browser QA verifies muted video playback, pause/play, no source loading under reduced motion, mobile menu and Escape behavior, header/hero contrast, and no desktop/mobile overflow. Production verification must confirm the deployed commit, all routes, schema, video, poster, source-file exclusion and both sitemaps.

# Website structure

Primary domain: https://houstondumpsterrentalco.shop

| Page | Purpose |
| --- | --- |
| `/` | Houston dumpster rental overview, project selection, planning checklist and FAQs |
| `/residential-dumpster-rental/` | Household cleanout planning, materials, placement, dates and quote considerations |
| `/construction-dumpster-rental/` | Jobsite debris streams, delivery access, weight, scheduling and pickup planning |
| `/dumpster-sizes/` | Volume versus weight, common industry size labels and placement considerations |
| `/site-map/` | Human-readable guide to all content pages |

Every content page has a unique title, description, one H1 and a self-referencing HTTPS canonical. Service guides are linked from the homepage, from each other and from the footer. No fabricated suburb pages, ratings, inventory, rates or credentials.

`sitemap.xml` and the requested `sitemaps.xml` contain the same five canonical URLs. `robots.txt` references the standard sitemap. Both XML files use `sitemap.css` for a styled, responsive presentation without deprecated browser XSLT support; `/site-map/` provides clickable HTML navigation. Last-modified dates reflect actual initial content creation on October 25, 2026. Change those dates only after substantive page changes. No invented priority or update frequency.

Status: deployed at https://houston-dumpster-rental-co.vercel.app with GitHub push-to-production connected. Primary apex/www attached; Spaceship confirms Vercel nameservers saved. Fresh custom DNS/HTTPS propagation pending. All fallback routes passed release checks. Confirm phone/address to add the actual call flow and finish business setup. There is no booking link, per owner request.

# Structured data verification

Implemented directly in HTML as JSON-LD, without client-side injection:

- Organization and WebSite describe the confirmed brand and primary domain.
- WebPage describes each of the five pages.
- Service describes the dumpster rental subject on the homepage and two service guides, with Houston as the confirmed city.
- BreadcrumbList matches visible breadcrumbs on the service guides and size guide, and the Home link and current page on the HTML site map.

LocalBusiness address, phone, opening hours, coordinates, prices, reviews, rating and social profiles are omitted until independently confirmed. Organization is used while those business details are pending. No deprecated HowTo or self-serving review markup. No FAQ rich-result promise.

Local checks passed: valid JSON on all five pages; all entity references resolve within each graph; absolute canonical URLs; unique page URLs; one H1 per page; all local links and assets resolve; five canonical pages exactly match both XML sitemap files. Both XML files parse successfully; CSS presents the five entries without browser XSLT warnings. Residential and construction guides each exceed 800 words of original body content. The size guide is informational, not an inventory list.

Browser checks cover service-page desktop/mobile overflow and sitemap presentation. Production URL status, external schema validator and Search Console indexing remain launch-time checks because this site is not deployed.

References: https://schema.org/Service and https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data

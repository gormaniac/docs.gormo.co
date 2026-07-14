project = "Gormo's Docs"
copyright = "2026, John Gorman"
author = "John Gorman"

extensions = [
    "myst_parser",
]

html_theme = "shibuya"
html_title = project
html_static_path = ["_static"]
html_copy_source = False
html_show_sourcelink = False

myst_enable_extensions = ["colon_fence"]

html_theme_options = {
    "page_layout": "simple",
    "accent_color": "teal",
    "color_mode": "auto",
    "nav_socials": [
        {
            "name": "GitHub",
            "url": "https://url.gormo.co/github",
            "icon": "simple-icons:github",
        },
    ],
        "nav_links": [
        {
            "title": "Python Projects",
            "children": [
                {
                    "title": "StormLib++",
                    "url": "stormlibpp",
                    "summary": "A collection of Python code and Synapse Power-Ups to improve life as a Synapse user/developer.",
                },
                {
                    "title": "CAIC Python",
                    "url": "caic-python",
                    "summary": "Interact with Colorado Avalanche Information Center programmatically.",
                },
                {
                    "title": "PyHatching",
                    "url": "pyhatching",
                    "summary": "A Hatching Triage Sandbox API client.",
                },
                {
                    "title": "stem-http",
                    "url": "stem-http",
                    "summary": "An async HTTP client using the stem library.",
                },
                {
                    "title": "aioipinfo",
                    "url": "aioipinfo",
                    "summary": "An async ipinfo.io client.",
                },
            ],
        },
        {
            "title": "Storm Services",
            "children": [
                {
                    "title": "yarastorm",
                    "url": "yarastorm",
                    "summary": "Yara scanning in Synapse.",
                },
            ],
        },
        {
            "title": "Storm Packages",
            "summary": "The Synapse Rapid Power-Ups I've developed.",
            "children": [
                {
                    "title": "Lookup Storm",
                    "url": "stormlibpp/pkgs/lookup-storm",
                    "summary": "Easily lookup common atomic indicators.",
                },
                {
                    "title": "DNS Storm",
                    "url": "stormlibpp/pkgs/dnsstorm",
                    "summary": "Perform DNS lookups from Synapse.",
                },
                {
                    "title": "Report Ingest",
                    "url": "stormlibpp/pkgs/report-ingest",
                    "summary": "Ingest and scrape TI reports.",
                },
                {
                    "title": "Stix",
                    "url": "stormlibpp/pkgs/stix",
                    "summary": "Improved STIX bundle modeling in Synapse.",
                },
            ],
        },
        {
            "title": "My Homepage",
            "url": "https://gormo.co",
            "external": True,
        },
    ],
}

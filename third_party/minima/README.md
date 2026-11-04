# Minima 2.5.1

Upstream: https://github.com/jekyll/minima/tree/v2.5.1

Pinned commit: `38a84a949f9753c4542e25f422935f59b4913053`

License: MIT; see [LICENSE.txt](LICENSE.txt).

The homepage uses Jekyll and the actual Minima Sass and layout chain. Its styling is compiled by Jekyll from `assets/home.scss`, importing `_sass/minima.scss` and its three upstream partials. These four Sass files are unmodified copies of the pinned release.

`_layouts/minima-home.html` derives from upstream `_layouts/home.html` and `_layouts/minima-default.html` from `_layouts/default.html`. Local adaptations namespace the includes/layout, add accessible main/skip-link behavior, and use the studio's metadata and navigation. Site-specific branding belongs in `assets/home.scss` and `_includes/minima/`, not in upstream Sass.

Minima is scoped to the homepage so existing Cayman subpages and the standalone Mailrise product page retain their own layouts. No posts or publication dates are fabricated. The native Minima post list remains available if real `_posts` are added later.

To update, choose a tagged upstream version, compare layout adaptations, replace the unchanged Sass files, preserve its license, then rebuild and run the homepage acceptance tests against the output.

## Local validation

Install Ruby (3.4 was used for verification) and Bundler, then run from the repository root:

```sh
bundle install
bundle exec jekyll build --config _config.yml,_config.local.yml
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

`_config.local.yml` enables the relevant GitHub Pages plugins locally. Production continues to use GitHub Pages' native Jekyll build and `_config.yml`. For a different build destination, set `SITE_ROOT` to that directory when running the tests.

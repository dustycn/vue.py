# Configuration

Your `vue.py` application can be customized via a `vuepy.yml` file
located in your application folder.

## Stylesheets
If you want to use custom CSS stylsheets, add this section to the configuration file:
```yaml
stylesheets:
  - <path of the stylesheet relative to your application folder>
  - <URL of the stylesheet>
```

## Javascript Libraries
If you want to use custom javascript libraries, add this section to the configuration file:
```yaml
scripts:
  - <path of the script relative to your application folder>
  - <URL of the script>
```
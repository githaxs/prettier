# Prettier

[Prettier](https://prettier.io/) is an opinionated code formatter
created to reduce time spent deliberating over which style conventions
to use.

This task ensures all files are formatted with prettier and allows
you to create globally shared configurations.


### Installation
1. Install the [Githaxs Meta Application](https://github.com/apps/githaxs-meta)

2. Create a repo with the name `githaxs_settings`.

3. Add the following to `ghx.yml` within the repo:

```yaml
# githaxs_settings/ghx.yml

prettier:
  # install on all repos
  org: true
  # install on select repos
  repos:
    - api-microservice
    - websiteservice
  # install on repos with a given topic
  repo_topics:
    - api
    - web
```
### Configuration

|parameter|description|required|
|---|---|---|
|prettier_config|A map of [prettier options](https://prettier.io/docs/en/options.html)| True|

### Example Configurations

To configure global settings:

```yaml
# githaxs_settings/ghx.yml

prettier:
  org: true
  org_settings:
    # Cannot be overriden by repo specific settings
    final:
      prettier_config:
        singleQuote: true
        semi: false
    # Default value if repo specific settings do not exist
    default:
      prettier_config:
        singleQuote: true
        semi: false
   ```

To configure repo specific settings:

```yaml
# <repo name>/ghx.yml

prettier:
  repo_settings:
    singleQuote: true
    semi: false
  ```

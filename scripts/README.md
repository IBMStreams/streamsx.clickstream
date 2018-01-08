# streams-runner

```bash
streamsx-runner --main-composite com.acme.stuff:Main --toolkits <paths to required toolkits>
```

```bash
streamsx-runner --help 
usage: streamsx-runner [-h] (--service-name SERVICE_NAME | --create-bundle)
                       (--topology TOPOLOGY | --main-composite MAIN_COMPOSITE)
                       [--toolkits TOOLKITS [TOOLKITS ...]]

Execute a Streams application using a Streaming Analytics service.

optional arguments:
  -h, --help            show this help message and exit
  --service-name SERVICE_NAME
                        Submit to streaming Analytics service
  --create-bundle       Create a bundle
  --topology TOPOLOGY   Topology to call
  --main-composite MAIN_COMPOSITE
                        SPL Main composite
  --toolkits TOOLKITS [TOOLKITS ...]
                        Additional SPL toolkits
```

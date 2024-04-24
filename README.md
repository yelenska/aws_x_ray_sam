# Demo serverless app with X-Ray tracing

This is a serverless Hello World app which is intended to demonstrate X-Ray tracing in Lambda with using Powertools for
AWS Lambda library

1. Export Poetry dependencies to requirements.txt file in the Lambda root folder:

```shell
$ dependencies.sh
```

2. Build app by using SAM CLI

```shell
$ sam build
```

3. Deploy to AWS using SAM CLI and follow interactive commands

```shell
$ sam deploy --guided
```

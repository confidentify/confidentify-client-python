# How to generate this project

```
openapi-generator generate -g python -i https://api.confidentify.com/openapi?format=yaml --additional-properties=packageName=confidentify_client,generateSourceCodeOnly=true,projectName=confidentify-client-python,packageVersion=1.0.0
rm -Rf confidentify_client/test
rm -Rf confidentify_client/docs
```
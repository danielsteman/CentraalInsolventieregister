# CentraalInsolventieRegister

### Credentials:

[Create an account](https://insolventies.rechtspraak.nl/#!/registratie) and pass environment variables:

```
USERNAME
PASSWORD
```

### Test:

```
poetry shell
poetry install
poetry run pytest -s
```

### Codegen:

```
poetry run xsdata docs/RSpublicWS_InsolvencyRequests.xsd
```

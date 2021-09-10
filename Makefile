webserver:
	BIGQUERY_CREDENTIAL_PATH=./gcp_credential.json python3 -m main
bento-build:
	BIGQUERY_CREDENTIAL_PATH=./gcp_credential.json python3 -m bento
bento-server:

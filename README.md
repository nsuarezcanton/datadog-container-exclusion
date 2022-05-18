# datadog-container-exclusion
1. Create `datadog.env` and `server.env` files, respectively:
  ```
  DD_API_KEY=<your_api_key>
  DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL=true
  DD_LOGS_ENABLED=true
  DD_CONTAINER_EXCLUDE=image:datadog*
  ```
  and 
  ```
  DD_AGENT_HOST=agent
  DD_AGENT_PORT=8126
  DD_ENV=dev
  DD_SERVICE=dev-server
  DD_VERSION=0.0.1
  ```
2. Run `docker compose up`.

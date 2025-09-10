# Security & Privacy Guidance

- This is a demo prototype. Do NOT upload any real PII or production telemetry.
- Data anonymization guidance:
  - Remove or hash VINs, driver IDs, device identifiers before sharing.
  - Use K-anonymity: ensure no small groups (<5) can be re-identified.
  - Redact precise GPS to coarse geohash or tile (e.g., 1km grid) for shared datasets.
- Responsible disclosure: report vulnerabilities to security@fleetpulse.com.
- Production recommendations: TLS for all ingress, mTLS between services, OAuth2/JWT for API auth, IAM roles for cloud resources.

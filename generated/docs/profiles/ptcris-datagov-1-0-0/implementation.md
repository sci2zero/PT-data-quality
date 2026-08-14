# Implementation outputs — PTCRIS-DATAGOV-1.0.0

## PT Master runtime JSON

The generator creates `generated/implementation/pt-master/PTCRIS-DATAGOV-1.0.0/1.0.0.json` in the legacy-compatible format and `runtime-config.json` with explicit traceability metadata.

## SHACL

- Bound validation targets: **0**
- Emitted SHACL Core constraints: **0**
- Unbound active targets: **163**

SHACL is emitted only when the XLSX contains `RDF_SHACL` bindings in the `Implementation Bindings` sheet. This avoids inventing RDF classes or properties.

## Schematron

- Bound validation targets: **0**
- Emitted Schematron assertions: **0**
- Unbound active targets: **163**

Schematron is emitted only when the XLSX contains `XML_SCHEMATRON` bindings with an XML context and value selector.

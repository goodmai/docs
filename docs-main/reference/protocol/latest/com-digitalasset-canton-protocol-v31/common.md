---
title: "common.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v31 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v31/common.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v31/common.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31)
- Package set: [com.digitalasset.canton.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30) | `com.digitalasset.canton.protocol.v31` | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v31/common.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v31/common.proto)

## Related sections in this package

- _No sibling sections in this package._

## Types in this section

- [com.digitalasset.canton.protocol.v31.ContractAuthenticationData](#type-com-digitalasset-canton-protocol-v31-contractauthenticationdata)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v31-contractauthenticationdata"></a>
**Message `com.digitalasset.canton.protocol.v31.ContractAuthenticationData`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v31/common.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v31/common.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| contract_salt | `bytes` | optional |  |
| creating_transaction_id | `bytes` | optional |  |
| relative_argument_suffixes | `bytes` | repeated |  |

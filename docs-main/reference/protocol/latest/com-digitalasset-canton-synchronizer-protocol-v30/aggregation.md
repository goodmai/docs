---
title: "aggregation.proto"
description: "Markdown extract for com.digitalasset.canton.synchronizer.protocol.v30 / community/synchronizer/src/main/protobuf/com/digitalasset/canton/synchronizer/protocol/v30/aggregation.proto."
---

# `community/synchronizer/src/main/protobuf/com/digitalasset/canton/synchronizer/protocol/v30/aggregation.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Package set: [com.digitalasset.canton.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30) | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | `com.digitalasset.canton.synchronizer.protocol.v30`
- Source file: [community/synchronizer/src/main/protobuf/com/digitalasset/canton/synchronizer/protocol/v30/aggregation.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/synchronizer/src/main/protobuf/com/digitalasset/canton/synchronizer/protocol/v30/aggregation.proto)

## Related sections in this package

- _No sibling sections in this package._

## Types in this section

- [com.digitalasset.canton.synchronizer.protocol.v30.AggregatedSignaturesOfSender](#type-com-digitalasset-canton-synchronizer-protocol-v30-aggregatedsignaturesofsender)
- [com.digitalasset.canton.synchronizer.protocol.v30.AggregatedSignaturesOfSender.SignaturesForEnvelope](#type-com-digitalasset-canton-synchronizer-protocol-v30-aggregatedsignaturesofsender-signaturesforenvelope)

## Extracted reference

<a id="type-com-digitalasset-canton-synchronizer-protocol-v30-aggregatedsignaturesofsender"></a>
**Message `com.digitalasset.canton.synchronizer.protocol.v30.AggregatedSignaturesOfSender`**

- Source: [community/synchronizer/src/main/protobuf/com/digitalasset/canton/synchronizer/protocol/v30/aggregation.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/synchronizer/src/main/protobuf/com/digitalasset/canton/synchronizer/protocol/v30/aggregation.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| signatures_by_envelope | [`com.digitalasset.canton.synchronizer.protocol.v30.AggregatedSignaturesOfSender.SignaturesForEnvelope`](#type-com-digitalasset-canton-synchronizer-protocol-v30-aggregatedsignaturesofsender-signaturesforenvelope) | repeated |  |

<a id="type-com-digitalasset-canton-synchronizer-protocol-v30-aggregatedsignaturesofsender-signaturesforenvelope"></a>
**Message `com.digitalasset.canton.synchronizer.protocol.v30.AggregatedSignaturesOfSender.SignaturesForEnvelope`**

- Source: [community/synchronizer/src/main/protobuf/com/digitalasset/canton/synchronizer/protocol/v30/aggregation.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/synchronizer/src/main/protobuf/com/digitalasset/canton/synchronizer/protocol/v30/aggregation.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| signatures | [`com.digitalasset.canton.crypto.v30.Signature`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signature) | repeated |  |

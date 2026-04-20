---
title: "confirmation_response.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/mediator)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/ordering_request.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/ordering-request)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-reassignment)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-transaction)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/quorum.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/quorum)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/signed_content.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/signed-content)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/storage.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/storage)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronization)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronizer-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/topology)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/traffic-control-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/versioned_google_rpc_status.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/versioned-google-rpc-status)

## Types in this section

- [com.digitalasset.canton.protocol.v30.ConfirmationResponse](#type-com-digitalasset-canton-protocol-v30-confirmationresponse)
- [com.digitalasset.canton.protocol.v30.ConfirmationResponses](#type-com-digitalasset-canton-protocol-v30-confirmationresponses)
- [com.digitalasset.canton.protocol.v30.LocalVerdict](#type-com-digitalasset-canton-protocol-v30-localverdict)
- [com.digitalasset.canton.protocol.v30.LocalVerdict.VerdictCode](#type-com-digitalasset-canton-protocol-v30-localverdict-verdictcode)
- [com.digitalasset.canton.protocol.v30.MerkleSeqIndex](#type-com-digitalasset-canton-protocol-v30-merkleseqindex)
- [com.digitalasset.canton.protocol.v30.ViewPosition](#type-com-digitalasset-canton-protocol-v30-viewposition)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-confirmationresponse"></a>
**Message `com.digitalasset.canton.protocol.v30.ConfirmationResponse`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| local_verdict | [`com.digitalasset.canton.protocol.v30.LocalVerdict`](#type-com-digitalasset-canton-protocol-v30-localverdict) | optional |  |
| confirming_parties | `string` | repeated |  |
| view_position | [`com.digitalasset.canton.protocol.v30.ViewPosition`](#type-com-digitalasset-canton-protocol-v30-viewposition) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-confirmationresponses"></a>
**Message `com.digitalasset.canton.protocol.v30.ConfirmationResponses`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto)
- Fields: 5

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| request_id | `int64` | optional |  |
| root_hash | `bytes` | optional |  |
| physical_synchronizer_id | `string` | optional |  |
| sender | `string` | optional |  |
| responses | [`com.digitalasset.canton.protocol.v30.ConfirmationResponse`](#type-com-digitalasset-canton-protocol-v30-confirmationresponse) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-localverdict"></a>
**Message `com.digitalasset.canton.protocol.v30.LocalVerdict`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| code | [`com.digitalasset.canton.protocol.v30.LocalVerdict.VerdictCode`](#type-com-digitalasset-canton-protocol-v30-localverdict-verdictcode) | optional |  |
| reason | `google.rpc.Status` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-localverdict-verdictcode"></a>
**Enum `com.digitalasset.canton.protocol.v30.LocalVerdict.VerdictCode`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto)

_No description._

| Name | Number |
| --- | --- |
| VERDICT_CODE_UNSPECIFIED | `0` |
| VERDICT_CODE_LOCAL_APPROVE | `1` |
| VERDICT_CODE_LOCAL_REJECT | `2` |
| VERDICT_CODE_LOCAL_MALFORMED | `3` |
| VERDICT_CODE_LOCAL_ABSTAIN | `4` |

<a id="type-com-digitalasset-canton-protocol-v30-merkleseqindex"></a>
**Message `com.digitalasset.canton.protocol.v30.MerkleSeqIndex`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| is_right | `bool` | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-viewposition"></a>
**Message `com.digitalasset.canton.protocol.v30.ViewPosition`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| position | [`com.digitalasset.canton.protocol.v30.MerkleSeqIndex`](#type-com-digitalasset-canton-protocol-v30-merkleseqindex) | repeated |  |

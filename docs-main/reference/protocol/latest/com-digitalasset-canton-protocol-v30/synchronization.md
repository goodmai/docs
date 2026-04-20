---
title: "synchronization.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/confirmation-response)
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
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronizer-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/topology)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/traffic-control-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/versioned_google_rpc_status.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/versioned-google-rpc-status)

## Types in this section

- [com.digitalasset.canton.protocol.v30.EnvelopeContent](#type-com-digitalasset-canton-protocol-v30-envelopecontent)
- [com.digitalasset.canton.protocol.v30.SignedProtocolMessage](#type-com-digitalasset-canton-protocol-v30-signedprotocolmessage)
- [com.digitalasset.canton.protocol.v30.TypedSignedProtocolMessageContent](#type-com-digitalasset-canton-protocol-v30-typedsignedprotocolmessagecontent)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-envelopecontent"></a>
**Message `com.digitalasset.canton.protocol.v30.EnvelopeContent`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto)
- Fields: 6

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| informee_message | [`com.digitalasset.canton.protocol.v30.InformeeMessage`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-transaction#type-com-digitalasset-canton-protocol-v30-informeemessage) | optional |  |
| encrypted_view_message | [`com.digitalasset.canton.protocol.v30.EncryptedViewMessage`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-transaction#type-com-digitalasset-canton-protocol-v30-encryptedviewmessage) | optional |  |
| unassignment_mediator_message | [`com.digitalasset.canton.protocol.v30.UnassignmentMediatorMessage`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-reassignment#type-com-digitalasset-canton-protocol-v30-unassignmentmediatormessage) | optional |  |
| assignment_mediator_message | [`com.digitalasset.canton.protocol.v30.AssignmentMediatorMessage`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-reassignment#type-com-digitalasset-canton-protocol-v30-assignmentmediatormessage) | optional |  |
| root_hash_message | [`com.digitalasset.canton.protocol.v30.RootHashMessage`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-transaction#type-com-digitalasset-canton-protocol-v30-roothashmessage) | optional |  |
| topology_transactions_broadcast | [`com.digitalasset.canton.protocol.v30.TopologyTransactionsBroadcast`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/topology#type-com-digitalasset-canton-protocol-v30-topologytransactionsbroadcast) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-signedprotocolmessage"></a>
**Message `com.digitalasset.canton.protocol.v30.SignedProtocolMessage`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| signature | [`com.digitalasset.canton.crypto.v30.Signature`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signature) | repeated |  |
| typed_signed_protocol_message_content | `bytes` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-typedsignedprotocolmessagecontent"></a>
**Message `com.digitalasset.canton.protocol.v30.TypedSignedProtocolMessageContent`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| confirmation_responses | `bytes` | optional |  |
| confirmation_result | `bytes` | optional |  |
| acs_commitment | `bytes` | optional |  |
| set_traffic_purchased | `bytes` | optional |  |

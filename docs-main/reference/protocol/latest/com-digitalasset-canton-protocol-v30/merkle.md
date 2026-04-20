---
title: "merkle.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/confirmation-response)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/mediator)
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

- [com.digitalasset.canton.protocol.v30.BlindableNode](#type-com-digitalasset-canton-protocol-v30-blindablenode)
- [com.digitalasset.canton.protocol.v30.GenTransactionTree](#type-com-digitalasset-canton-protocol-v30-gentransactiontree)
- [com.digitalasset.canton.protocol.v30.MerkleSeq](#type-com-digitalasset-canton-protocol-v30-merkleseq)
- [com.digitalasset.canton.protocol.v30.MerkleSeqElement](#type-com-digitalasset-canton-protocol-v30-merkleseqelement)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-blindablenode"></a>
**Message `com.digitalasset.canton.protocol.v30.BlindableNode`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| unblinded | `bytes` | optional |  |
| blinded_hash | `bytes` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-gentransactiontree"></a>
**Message `com.digitalasset.canton.protocol.v30.GenTransactionTree`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| submitter_metadata | [`com.digitalasset.canton.protocol.v30.BlindableNode`](#type-com-digitalasset-canton-protocol-v30-blindablenode) | optional |  |
| common_metadata | [`com.digitalasset.canton.protocol.v30.BlindableNode`](#type-com-digitalasset-canton-protocol-v30-blindablenode) | optional |  |
| participant_metadata | [`com.digitalasset.canton.protocol.v30.BlindableNode`](#type-com-digitalasset-canton-protocol-v30-blindablenode) | optional |  |
| root_views | [`com.digitalasset.canton.protocol.v30.MerkleSeq`](#type-com-digitalasset-canton-protocol-v30-merkleseq) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-merkleseq"></a>
**Message `com.digitalasset.canton.protocol.v30.MerkleSeq`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| root_or_empty | [`com.digitalasset.canton.protocol.v30.BlindableNode`](#type-com-digitalasset-canton-protocol-v30-blindablenode) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-merkleseqelement"></a>
**Message `com.digitalasset.canton.protocol.v30.MerkleSeqElement`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| first | [`com.digitalasset.canton.protocol.v30.BlindableNode`](#type-com-digitalasset-canton-protocol-v30-blindablenode) | optional |  |
| second | [`com.digitalasset.canton.protocol.v30.BlindableNode`](#type-com-digitalasset-canton-protocol-v30-blindablenode) | optional |  |
| data | [`com.digitalasset.canton.protocol.v30.BlindableNode`](#type-com-digitalasset-canton-protocol-v30-blindablenode) | optional |  |
